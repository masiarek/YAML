#!/usr/bin/env python3
"""
build_divergence_index.py
=========================
Cross-method divergence ledger for the *curated* single-winner STAR library.

For every real single-winner STAR election in the repo it re-tabulates the
SAME ballots under the other methods and records where they disagree with STAR:

    STAR  vs  RCV-IRV  vs  Ranked Robin (RCV-RR / Copeland)  vs  Approval

The point is NOT to hunt for divergence in random ballots (that's what
tools_adam/find_*divergence.py do, and that's the cherry-picking trap). This
walks only Adam's hand-built teaching elections, reports a base rate
("D of N diverged"), and groups the hits by a decision tree so the genuinely
teachable cases float to the top and tie-break artifacts are flagged, not
promoted.

Score -> rank is the tricky bit, so we record BOTH conversions (house decision):
  * STRICT : equal non-zero scores broken by lot/priority order -> a full
             strict ranking (the engine's canonical `score_ballot_to_ranking`).
  * WEAK   : equal scores stay equal (no head-to-head preference between them) —
             the natural reading of a score ballot.
RCV-RR and Condorcet are computed under BOTH (they genuinely differ when a
ballot has tied scores). RCV-IRV cannot represent equal ranks (pyrankvote needs
a strict order), so "weak IRV" does not exist; instead IRV is run STRICT and we
add a fragility probe (re-run under REVERSED priority) plus the engine's own
tied-ballot count, so a tie-break-driven IRV result is flagged rather than sold
as a deep method difference.

Outputs (generated — safe to delete and rebuild):
  divergence_review/INDEX.md       human review surface, grouped by bucket
  divergence_review/divergence.csv  one row per election, all winners + flags

Run from the repo root:   python3 scripts/build_divergence_index.py
"""

from __future__ import annotations

import csv
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENGINE = REPO / "STARVote_LH_tabulation_engine"
RCV = REPO / "RCV_IRV_tabulation_engine"
for p in (ENGINE, RCV):
    sys.path.insert(0, str(p))

import starvote  # noqa: E402
import starvote_larry_hastings as w  # noqa: E402

# Folders that hold real, curated single-winner STAR elections (per CLAUDE.md).
SCAN_DIRS = ["01_Single_winner", "split_voting", "YAML_library/1_positive"]

OUT_DIR = REPO / "divergence_review"


# --------------------------------------------------------------------------- #
# Method helpers (reuse the engine's own functions wherever possible)
# --------------------------------------------------------------------------- #
def _priority_order(candidates, lot_numbers):
    order = [c for c in (lot_numbers or candidates) if c in candidates]
    for c in candidates:
        if c not in order:
            order.append(c)
    return order


def star_winner(path):
    """STAR winner via the same path scenario_eval/the CLI use (no printing)."""
    el = w.load_election(str(path))
    candidates, ballots, _ = w.parse_ballots_from_string(el["ballots"])
    tb = w.LotNumberTiebreaker(lot_numbers=el.get("lot_numbers") or [], silent=True)
    res = starvote.election(
        el["method"] or starvote.star, ballots, seats=1, maximum_score=5,
        tiebreaker=tb, verbosity=1, print=lambda *a, **k: None,
    )
    winners = res if isinstance(res, (list, tuple)) else [res]
    return str(winners[0]) if winners else None


def _copeland_winner(candidates, score_ballots, order):
    """Ranked Robin (Copeland) winner from {cand: value} ballots.

    Mirrors run_ranked_robin's tally: most pairwise wins, then total margin,
    then lot/priority order. Returns (winner, is_cycle)."""
    matrix = w.calculate_preference_matrix(candidates, score_ballots)
    if not matrix:
        return None, False
    wins = {c: 0 for c in candidates}
    margin = {c: 0 for c in candidates}
    for i, a in enumerate(candidates):
        for b in candidates[i + 1:]:
            fa, ag, _ = matrix[a][b]
            margin[a] += fa - ag
            margin[b] += ag - fa
            if fa > ag:
                wins[a] += 1
            elif ag > fa:
                wins[b] += 1
    ranked = sorted(candidates, key=lambda c: (-wins[c], -margin[c], order.index(c)))
    top = wins[ranked[0]]
    leaders = [c for c in candidates if wins[c] == top]
    # A cycle: nobody wins all their matchups yet several share the top win count.
    is_cycle = len(leaders) > 1 and top < len(candidates) - 1
    return ranked[0], is_cycle


def _irv_stable(candidates, ballots, order, samples=9):
    """compute_irv_winner via pyrankvote is nondeterministic on a PERFECT tie
    (it returns whichever tied candidate the internal set yields). For a
    committed artifact we need a stable answer, so sample a few times: if the
    winner is unanimous it's real; if it wobbles, the election is a genuine IRV
    tie — resolve it by the SAME priority order STAR uses and mark it fragile.
    Returns (winner, unstable, tie_ballots, total)."""
    seen, tb, tot = [], 0, 0
    for _ in range(samples):
        irv, tb, tot = w.compute_irv_winner(candidates, ballots, order)
        seen.append(irv)
    uniq = list(dict.fromkeys(seen))
    if len(uniq) == 1:
        return uniq[0], False, tb, tot
    rep = next((c for c in order if c in uniq), uniq[0])   # priority tiebreak
    return rep, True, tb, tot


def _strict_pseudo_scores(score_ballots, order):
    """Convert each score ballot to a STRICT ranking (ties -> priority order),
    then re-express it as descending pseudo-scores so the pairwise matrix sees a
    strict order with no equal-preference cells."""
    out = []
    for b in score_ballots:
        ranking = w._score_to_rank(b, order)  # 0-scores dropped, ties by order
        n = len(ranking)
        out.append({c: (n - i) for i, c in enumerate(ranking)})
    return out


def analyze(path):
    """Return a dict of winners/flags for one single-winner STAR election, or
    None if the file isn't an eligible STAR/score/single-winner election."""
    el = w.load_election(str(path))
    method_name = (el.get("method_name") or "").strip().lower()
    if method_name not in ("", "star"):
        return None                       # skip Approval/RR/RCV/bloc/sss/etc.
    if (el.get("seats") or 1) != 1:
        return None                       # single-winner only
    ballots_text = el["ballots"]
    detect = "\n".join(ln.split("#")[0] for ln in ballots_text.splitlines())
    if ">" in detect:
        return None                       # native ranked ballots, not a score race
    candidates, ballots, _ = w.parse_ballots_from_string(ballots_text)
    if not candidates or not ballots:
        return None
    order = _priority_order(candidates, el.get("lot_numbers"))
    rev = list(reversed(order))

    star = star_winner(path)

    irv, irv_unstable, tie_ballots, total = _irv_stable(candidates, ballots, order)
    irv_rev, rev_unstable, _, _ = _irv_stable(candidates, ballots, rev)
    irv_fragile = (irv_unstable or rev_unstable
                   or (irv is not None and irv_rev is not None and irv != irv_rev))

    strict = _strict_pseudo_scores(ballots, order)
    rr_weak, cyc_weak = _copeland_winner(candidates, ballots, order)
    rr_strict, cyc_strict = _copeland_winner(candidates, strict, order)
    cond_weak = w.condorcet_winner(candidates, ballots)
    cond_strict = w.condorcet_winner(candidates, strict)

    approval = w.approval_winner(candidates, ballots, order)

    rr_conv_sensitive = rr_weak != rr_strict

    return {
        "file": str(path.relative_to(REPO)),
        "candidates": len(candidates),
        "ballots": len(ballots),
        "STAR": star,
        "IRV": irv,
        "IRV_rev": irv_rev,
        "RR_weak": rr_weak,
        "RR_strict": rr_strict,
        "Approval": approval,
        "Condorcet_weak": cond_weak,
        "Condorcet_strict": cond_strict,
        "tie_ballots": tie_ballots,
        "irv_fragile": irv_fragile,
        "rr_conv_sensitive": rr_conv_sensitive,
        "cycle": cyc_weak or cyc_strict or cond_weak is None,
    }


# --------------------------------------------------------------------------- #
# Classification — the decision tree (anti-cherry-pick discipline)
# --------------------------------------------------------------------------- #
BUCKETS = [
    ("IRV_OUTLIER_RR_WITH_STAR",
     "RCV-IRV is the outlier — Ranked Robin AGREES with STAR (strongest teachable: the center-squeeze story, two methods against one)"),
    ("STAR_OUTLIER_RR_WITH_IRV",
     "STAR is the outlier — Ranked Robin sides with RCV-IRV (show it anyway, for evenhandedness: STAR isn't always the Condorcet pick)"),
    ("IRV_DIFFERS_ARTIFACT",
     "RCV-IRV differs but it's a score->rank tie-break artifact (tied ballots and/or flips under reversed priority) — log, do NOT bark on IRV"),
    ("CYCLE_OR_THREE_WAY",
     "Condorcet cycle / three-way split — genuinely hard case, no clean villain"),
    ("APPROVAL_OR_MINOR",
     "Only Approval (or a minor method) differs — usually a threshold story, not an IRV one"),
]


def classify(r):
    if r["STAR"] is None:
        return "APPROVAL_OR_MINOR"
    irv_diff = r["IRV"] is not None and r["IRV"] != r["STAR"]
    rr = r["RR_weak"]
    rr_diff = rr is not None and rr != r["STAR"]
    appr_diff = r["Approval"] is not None and r["Approval"] != r["STAR"]

    if irv_diff and (r["tie_ballots"] or r["irv_fragile"]):
        return "IRV_DIFFERS_ARTIFACT"          # tie-break artifact, not a cycle
    if r["cycle"] and (irv_diff or rr_diff):
        return "CYCLE_OR_THREE_WAY"
    if irv_diff and not rr_diff:
        return "IRV_OUTLIER_RR_WITH_STAR"          # RR agrees with STAR
    if irv_diff and rr_diff and rr == r["IRV"]:
        return "STAR_OUTLIER_RR_WITH_IRV"          # RR sides with IRV
    if irv_diff or rr_diff:
        return "CYCLE_OR_THREE_WAY"
    if appr_diff:
        return "APPROVAL_OR_MINOR"
    return "AGREE"


# --------------------------------------------------------------------------- #
# Per-case teaching .md generation
# --------------------------------------------------------------------------- #
BUCKET_TITLE = {
    "IRV_OUTLIER_RR_WITH_STAR": "RCV-IRV is the outlier (center squeeze)",
    "STAR_OUTLIER_RR_WITH_IRV": "STAR is the outlier",
    "IRV_DIFFERS_ARTIFACT": "RCV-IRV differs — tie-break artifact",
    "CYCLE_OR_THREE_WAY": "Cycle / three-way split",
    "APPROVAL_OR_MINOR": "Only Approval differs",
}


def _load_case(path):
    """(candidates, ballots, ballots_text, order, title) for one election file."""
    el = w.load_election(str(path))
    candidates, ballots, _ = w.parse_ballots_from_string(el["ballots"])
    order = _priority_order(candidates, el.get("lot_numbers"))
    title = el.get("title") or el.get("name") or Path(path).stem
    return candidates, ballots, el["ballots"], order, title


def _ballot_table(candidates, ballots):
    """Markdown table of ballots, collapsing identical score rows into counts."""
    seen, counts = [], {}
    for b in ballots:
        key = tuple(b.get(c, 0) for c in candidates)
        if key not in counts:
            counts[key] = 0
            seen.append(key)
        counts[key] += 1
    head = "| Count | " + " | ".join(candidates) + " |"
    sep = "|---:|" + "|".join([":--:"] * len(candidates)) + "|"
    rows = [f"| {counts[k]} | " + " | ".join(str(v) for v in k) + " |"
            for k in seen]
    return "\n".join([head, sep] + rows)


def _star_summary(candidates, ballots, order):
    """STAR result text: score totals, the two finalists, and the automatic
    runoff between them — recomputed from the ballots (matches the engine)."""
    rank = {c: i for i, c in enumerate(order)}
    totals = {c: sum(b.get(c, 0) for b in ballots) for c in candidates}
    finalists = sorted(candidates, key=lambda c: (-totals[c], rank[c]))[:2]
    a, b2 = finalists
    pa = sum(1 for bl in ballots if bl.get(a, 0) > bl.get(b2, 0))
    pb = sum(1 for bl in ballots if bl.get(b2, 0) > bl.get(a, 0))
    eq = len(ballots) - pa - pb
    win = a if (pa, -rank[a]) >= (pb, -rank[b2]) else b2
    tot_line = ", ".join(f"{c} {totals[c]}"
                         for c in sorted(candidates, key=lambda c: -totals[c]))
    lines = [
        "**Scoring round (sum of scores):** " + tot_line,
        f"**Finalists (top two):** {a} and {b2}",
        f"**Automatic runoff:** {a} {pa} vs {b2} {pb}"
        + (f"  ({eq} equal/no-preference)" if eq else ""),
        f"**STAR winner: {win}**",
    ]
    return "\n\n".join(lines)


def _irv_text(candidates, ballots, order):
    return w.build_irv_report(candidates, ballots, order) or "(RCV-IRV engine unavailable)"


def _rr_text(ballots_text, order):
    """Full Ranked Robin round-robin report text (reuse the engine, no print)."""
    tmp = Path(tempfile.gettempdir()) / "._rr_case.txt"
    try:
        w.run_ranked_robin(ballots_text, file_path="x.yaml", lot_numbers=order,
                           silent=True, out_path=tmp)
        return tmp.read_text(encoding="utf-8").strip()
    except Exception:
        return "(Ranked Robin report unavailable)"
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass


def _explanation(r):
    S, I, RR, A, C = (r["STAR"], r["IRV"], r["RR_weak"], r["Approval"],
                      r["Condorcet_weak"] or None)
    b = r["bucket"]
    if b == "IRV_OUTLIER_RR_WITH_STAR":
        return (
            f"STAR elects **{S}** — and so do Ranked Robin and Condorcet, because "
            f"**{S} is the head-to-head (pairwise) winner**, beating every rival "
            f"one-on-one. RCV-IRV instead elects **{I}**: {S} collects fewer top "
            f"(first-choice) votes, so IRV eliminates {S} early, and those ballots "
            f"transfer to {I}. This is the classic **center squeeze** — the broadly "
            f"acceptable candidate is knocked out by round-by-round elimination even "
            f"though a majority prefers them in a direct matchup. Two methods (STAR + "
            f"RR) against one (RCV-IRV): IRV is the outlier.")
    if b == "STAR_OUTLIER_RR_WITH_IRV":
        return (
            f"RCV-IRV and Ranked Robin both elect **{I}**, the Condorcet (pairwise) "
            f"winner. STAR instead elects **{S}**, because its score-then-automatic-"
            f"runoff can reward a candidate with broad, intense *scored* support even "
            f"when a different candidate wins every head-to-head. Here **STAR is the "
            f"outlier** — an honest reminder that STAR does not always elect the "
            f"Condorcet candidate.")
    if b == "IRV_DIFFERS_ARTIFACT":
        detail = []
        if r["tie_ballots"]:
            detail.append(f"{r['tie_ballots']} of {r['ballots']} ballots have tied "
                          f"non-zero scores, so their ranks are set by an arbitrary "
                          f"candidate-priority order")
        if r["irv_fragile"]:
            detail.append("the RCV-IRV winner flips when that priority order is reversed")
        why = "; ".join(detail) or "the score→rank conversion is ambiguous here"
        return (
            f"On these ballots RCV-IRV reports **{I}** rather than STAR's **{S}**, but "
            f"this is an **artifact of score→rank conversion**, not a robust method "
            f"difference: {why}. Ranked Robin and Condorcet agree with STAR (**{S}**). "
            f"**Do not use this case to criticize RCV-IRV** — the disagreement is a "
            f"coin-flip created by equal scores and would vanish under a different "
            f"(equally arbitrary) tie-break.")
    if b == "CYCLE_OR_THREE_WAY":
        if not C:
            return (
                f"There is **no Condorcet winner** — the head-to-head results form a "
                f"cycle (X beats Y beats Z beats X). With no pairwise anchor the methods "
                f"split: STAR={S}, RCV-IRV={I}, Ranked Robin={RR} (RR breaks the cycle "
                f"by total margin). No rule is clearly 'right'; a genuinely hard "
                f"election, not an indictment of any one method.")
        return (
            f"The methods split: STAR={S}, RCV-IRV={I}, Ranked Robin={RR}; the Condorcet "
            f"(pairwise) winner is {C}. A genuinely hard, divided electorate — useful for "
            f"showing that the choice of method matters most exactly when voters are split.")
    return (
        f"STAR, RCV-IRV and Ranked Robin all agree on **{S}**. Only **Approval** differs, "
        f"electing **{A}**: Approval counts every score of 3–5 as one equal 'approve' and "
        f"ignores intensity, rewarding {A}'s *breadth* of acceptability over {S}'s stronger "
        f"but more concentrated support. A **threshold story about Approval**, not a "
        f"STAR-vs-IRV teaching case.")


def _flag_line(r):
    flags = []
    if r["tie_ballots"]:
        flags.append(f"{r['tie_ballots']} tied-score ballot(s)")
    if r["irv_fragile"]:
        flags.append("IRV winner flips under reversed priority (fragile tie)")
    if r["rr_conv_sensitive"]:
        flags.append(f"RR conversion-sensitive (weak={r['RR_weak']}, strict={r['RR_strict']})")
    return "; ".join(flags) if flags else "none"


def case_md(r, dupes):
    """Full teaching markdown for one diverging election."""
    src = REPO / r["file"]
    candidates, ballots, ballots_text, order, title = _load_case(src)
    tab = w.tabulated_output_path(src)
    try:
        tab_rel = "../../" + str(tab.relative_to(REPO))
    except ValueError:
        tab_rel = str(tab)
    src_rel = "../../" + r["file"]

    M = []
    M.append(f"# {title}\n")
    M.append(f"**Bucket — {r['bucket']}:** {BUCKET_TITLE.get(r['bucket'], '')}\n")
    M.append(f"_Generated by `scripts/build_divergence_index.py` — rebuilt from the "
             f"election file; do not hand-edit._\n")
    M.append("## What happens\n")
    M.append(_explanation(r) + "\n")
    M.append("## Winners by method\n")
    M.append("| Method | Winner |")
    M.append("|---|---|")
    M.append(f"| STAR | **{r['STAR']}** |")
    M.append(f"| RCV-IRV | {r['IRV']} |")
    M.append(f"| Ranked Robin (RCV-RR) | {r['RR_weak']} |")
    M.append(f"| Approval | {r['Approval']} |")
    M.append(f"| Condorcet | {r['Condorcet_weak'] or 'none (cycle)'} |")
    M.append("")
    M.append(f"**Flags:** {_flag_line(r)}\n")
    M.append(f"**Source election:** [`{r['file']}`]({src_rel})  ·  "
             f"**STAR tabulated mirror:** [`{tab.name}`]({tab_rel})")
    if dupes:
        M.append("\n_Also present (identical ballots) at: "
                 + ", ".join(f"`{d}`" for d in dupes) + "._")
    M.append(f"\n_{r['candidates']} candidates, {r['ballots']} ballots._\n")

    M.append("## The ballots\n")
    M.append("Each row is a group of identical score ballots (0 = no support, "
             "5 = max).\n")
    M.append(_ballot_table(candidates, ballots) + "\n")

    M.append("## STAR result (official)\n")
    M.append(_star_summary(candidates, ballots, order) + "\n")

    M.append("## RCV-IRV — round by round\n")
    if r["irv_fragile"]:
        M.append("> ⚠️ This election has a **fragile IRV tie** (equal scores force an "
                 "arbitrary tie-break). The round table below is only *one* realization; "
                 "a different tie-break can change the winner. See the flag above.\n")
    M.append("```text\n" + _irv_text(candidates, ballots, order) + "\n```\n")

    M.append("## Ranked Robin (RCV-RR) — every pair, head-to-head\n")
    M.append("```text\n" + _rr_text(ballots_text, order) + "\n```\n")

    return "\n".join(M)


def _dedupe(diverged):
    """Group identical elections (same candidates + ballots). Returns a list of
    (primary_row, [duplicate_file_paths]); primary prefers the non-YAML_library
    copy so the teaching doc lives with the curated example."""
    groups = {}
    for r in diverged:
        src = REPO / r["file"]
        try:
            cands, ballots, _, _, _ = _load_case(src)
            key = (tuple(cands),
                   tuple(tuple(b.get(c, 0) for c in cands) for b in ballots))
        except Exception:
            key = (r["file"],)
        groups.setdefault(key, []).append(r)
    out = []
    for members in groups.values():
        members.sort(key=lambda r: ("YAML_library" in r["file"], r["file"]))
        primary = members[0]
        dupes = [m["file"] for m in members[1:]]
        out.append((primary, dupes))
    return out


def _case_filename(r):
    return Path(r["file"]).stem + ".md"


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def main():
    files = []
    for d in SCAN_DIRS:
        base = REPO / d
        if base.exists():
            files += [p for p in sorted(base.rglob("*.y*ml"))
                      if "_tabulated" not in p.parts]

    rows, skipped = [], 0
    for f in files:
        try:
            r = analyze(f)
        except Exception as e:                       # keep going, note the file
            print(f"  ! {f.relative_to(REPO)}: {e}", file=sys.stderr)
            skipped += 1
            continue
        if r is None:
            skipped += 1
            continue
        r["bucket"] = classify(r)
        rows.append(r)

    n = len(rows)
    diverged = [r for r in rows if r["bucket"] != "AGREE"]
    OUT_DIR.mkdir(exist_ok=True)

    # --- CSV (machine-readable) ---
    cols = ["bucket", "file", "candidates", "ballots", "STAR", "IRV", "IRV_rev",
            "RR_weak", "RR_strict", "Approval", "Condorcet_weak",
            "Condorcet_strict", "tie_ballots", "irv_fragile",
            "rr_conv_sensitive", "cycle"]
    with (OUT_DIR / "divergence.csv").open("w", newline="") as fh:
        wri = csv.DictWriter(fh, fieldnames=cols)
        wri.writeheader()
        for r in sorted(rows, key=lambda x: (x["bucket"], x["file"])):
            wri.writerow({k: r.get(k, "") for k in cols})

    # --- INDEX.md (human review surface) ---
    L = []
    L.append("# Cross-method divergence review\n")
    L.append(f"_Generated {datetime.now():%Y-%m-%d %H:%M} by "
             "`scripts/build_divergence_index.py` — do not hand-edit; rebuild._\n")
    L.append("Re-tabulates every **curated single-winner STAR** election under "
             "RCV-IRV, Ranked Robin (RCV-RR / Copeland) and Approval, and flags "
             "where they disagree with STAR. Only hand-built library elections "
             "are scanned (never random ballots), and the base rate is reported, "
             "so the collection stays honest rather than cherry-picked.\n")

    by_pct = (100 * len(diverged) / n) if n else 0
    L.append("## Base rate\n")
    L.append(f"- Scanned **{n}** single-winner STAR elections "
             f"(skipped {skipped} non-eligible files: multi-winner / Approval / "
             "RR / RCV / ranked-ballot / unparseable).")
    L.append(f"- **{len(diverged)}** ({by_pct:.0f}%) diverge from STAR under at "
             "least one method; **{0}** agree across the board.\n"
             .format(n - len(diverged)))

    by_bucket = {}
    for r in diverged:
        by_bucket.setdefault(r["bucket"], []).append(r)

    # --- Per-case teaching .md files (one per DISTINCT election, deduped) ---
    cases_dir = OUT_DIR / "cases"
    if cases_dir.exists():
        shutil.rmtree(cases_dir)            # rebuild clean, no stale cases
    deduped = _dedupe(diverged)
    case_link = {}                          # primary file -> md link from INDEX
    primaries_by_bucket = {}
    for primary, dupes in deduped:
        bucket = primary["bucket"]
        bdir = cases_dir / bucket
        bdir.mkdir(parents=True, exist_ok=True)
        fn = _case_filename(primary)
        (bdir / fn).write_text(case_md(primary, dupes), encoding="utf-8")
        case_link[primary["file"]] = f"cases/{bucket}/{fn}"
        primaries_by_bucket.setdefault(bucket, []).append((primary, dupes))
    n_cases = sum(len(v) for v in primaries_by_bucket.values())

    L.append("| Bucket | Count |")
    L.append("|---|---:|")
    for key, _desc in BUCKETS:
        L.append(f"| {key} | {len(by_bucket.get(key, []))} |")
    L.append("")

    L.append("## Score→rank conversion (recorded both ways)\n")
    L.append("- **STRICT** — equal non-zero scores broken by lot/priority order "
             "(`score_ballot_to_ranking`). Feeds RCV-IRV and the `RR_strict` / "
             "`Condorcet_strict` columns.\n"
             "- **WEAK** — equal scores stay equal (no preference). Feeds "
             "`RR_weak` / `Condorcet_weak` (the natural reading of a score ballot).\n"
             "- **`rr_conv_sensitive`** = RR_weak ≠ RR_strict → the RR result "
             "depends on how ties are read; treat with care.\n"
             "- RCV-IRV can't represent equal ranks, so there is no weak IRV. "
             "`tie_ballots` (ballots with tied non-zero scores) and `irv_fragile` "
             "(winner flips under reversed priority) flag a tie-break artifact.\n")

    def _row(r, dupes):
        flags = []
        if r["tie_ballots"]:
            flags.append(f"{r['tie_ballots']} tied-score ballot(s)")
        if r["irv_fragile"]:
            flags.append("IRV flips on reversed priority")
        if r["rr_conv_sensitive"]:
            flags.append(f"RR conv-sensitive (weak={r['RR_weak']}, strict={r['RR_strict']})")
        flagtxt = ("  \n    _flags: " + "; ".join(flags) + "_") if flags else ""
        duptxt = (f"  \n    _also at: {', '.join('`'+d+'`' for d in dupes)}_"
                  if dupes else "")
        link = case_link.get(r["file"], "")
        return (f"- **[{Path(r['file']).stem}]({link})** — `{r['file']}` "
                f"({r['candidates']}c/{r['ballots']}b)  \n"
                f"    STAR=**{r['STAR']}** · IRV={r['IRV']} · "
                f"RR={r['RR_weak']} · Approval={r['Approval']} · "
                f"Condorcet={r['Condorcet_weak'] or 'none'}{flagtxt}{duptxt}")

    L.append("## Cases by bucket\n")
    L.append("Review order is the teaching value of each bucket. Each case links to "
             "a full teaching `.md` (ballots + every method's report + a plain-English "
             "explanation) under `cases/`. Listing is **deduped** to one entry per "
             f"distinct election ({n_cases} cases; identical library copies merged).\n")
    for key, desc in BUCKETS:
        cases = primaries_by_bucket.get(key, [])
        L.append(f"### {key} — {len(cases)}\n")
        L.append(f"_{desc}_\n")
        if cases:
            L += [_row(r, dupes)
                  for r, dupes in sorted(cases, key=lambda x: x[0]["file"])]
        else:
            L.append("_(none)_")
        L.append("")

    L.append("## Full table\n")
    L.append("See `divergence.csv` for the machine-readable version "
             "(all columns, including the strict/weak split).\n")

    (OUT_DIR / "INDEX.md").write_text("\n".join(L) + "\n")

    print(f"Scanned {n} STAR single-winner elections, {len(diverged)} diverge "
          f"({n_cases} distinct cases after dedupe).")
    print(f"Wrote {OUT_DIR/'INDEX.md'}, {OUT_DIR/'divergence.csv'}, "
          f"and {n_cases} case files under {cases_dir}/")


if __name__ == "__main__":
    main()
