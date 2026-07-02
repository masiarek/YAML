#!/usr/bin/env python3
"""
build_yaml_pages.py — generate a browsable, EDUCATIONAL Markdown page for every
election YAML, the same way `_tabulated` mirrors and the YAML index are
generated. One page per YAML, written to `<folder>/<folder>_pages/<stem>.md`
(nested beside the source, like the `_tabulated` mirrors).

Each page carries: title · method (linked to its concept docs) · the file's own
scenario description · the ballots (with a how-to-read line and a marker legend
when markers appear) · the expected winner · the full engine report (pulled
from the `_tabulated` mirror — machine-specific file:// lines stripped) · and
auto cross-references: the folder README, topic hubs matched from the content,
the divergence-review case when methods disagree on this election, sibling
cases in the same set, the glossary, and the by-method index.

Pages are GENERATED — do not edit by hand. `tests/test_yaml_pages_current.py`
fails if a page drifts from its YAML/mirror. Regenerate with:

    python scripts/build_yaml_pages.py
"""
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOTS = ["01_STAR", "02_STAR_Bloc", "03_STAR_PR", "04_Approval",
         "05_Ranked_Robin", "method_comparisons", "other_methods"]

GENERATED_SUFFIXES = ("_tabulated", "_generated", "_pages")

# --- method → (display name, concept-docs path relative to repo root) --------
METHOD_DOCS = {
    "star":        ("STAR (single winner)", "00_start_here/STAR_Voting"),
    "approval":    ("Approval Voting", "00_start_here/Approval_Voting"),
    "rankedrobin": ("Ranked Robin (RCV-RR / Copeland)", "00_start_here/RCV_Ranked_Robin"),
    "rcv_irv":     ("RCV-IRV (Instant Runoff)", "00_start_here/RCV_IRV"),
    "bloc":        ("Bloc STAR (multi-winner, majoritarian)", "00_start_here/proportional_representation"),
    "sss":         ("Sequentially Spent Score (proportional STAR)", "00_start_here/proportional_representation"),
    "rrv":         ("Reweighted Range Voting (proportional STAR)", "00_start_here/proportional_representation"),
    "allocated":   ("Allocated Score (proportional STAR)", "00_start_here/proportional_representation"),
    "stv":         ("STV (proportional, ranked ballots)", "00_start_here/proportional_representation"),
}
METHOD_ALIASES = {
    "rcv_rr": "rankedrobin", "copeland": "rankedrobin", "consensus": "rankedrobin",
    "rr": "rankedrobin", "rcv": "rcv_irv", "irv": "rcv_irv",
    "approve": "approval", "av": "approval", "approval_voting": "approval",
    "approval_single_winner": "approval", "approval_multi_winner": "approval",
}

# --- keyword → topic hub / concept page (relative to repo root) --------------
TOPIC_LINKS = [
    (r"center[ _-]?squeeze", "Center squeeze (topic hub)", "00_start_here/topics/center_squeeze/README_center_squeeze.md"),
    (r"monotonic",           "Monotonicity (topic hub)", "00_start_here/topics/monotonicity/README_monotonicity.md"),
    (r"summab",              "Summability (topic hub)", "00_start_here/topics/summability/README_summability.md"),
    (r"condorcet|cycle",     "Condorcet efficiency (topic hub)", "00_start_here/topics/condorcet/README_condorcet.md"),
    (r"\btie|lot[ _]order|lot[ _]number|dead[ _]rung|tiebreak", "Ties & tie-breaking (topic hub)", "00_start_here/topics/ties/README_ties.md"),
    (r"tie[ _-]?break|dead[ _]rung", "The tie-breaking ladder (full chain)", "00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md"),
    (r"quorum",              "Quorum", "00_start_here/quorum.md"),
    (r"split|spoiler",       "Vote splitting (worked set)", "method_comparisons/split_voting/README_split_voting.md"),
    (r"runoff",              "Runoff reversal (worked set)", "01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md"),
    (r"abstention|marker|blank|spoiled", "Ballot & terminology basics", "00_start_here/ballot_and_terminology_basics.md"),
    (r"black[ _]curtain",    "The Black Curtain (worked set)", "method_comparisons/black_curtain/README_black_curtain.md"),
    (r"exhaust",             "Exhausted ballots (conversation)", "interviews_conversations/exhausted_ballots_301.md"),
]

GLOSSARY = "00_start_here/GLOSSARY.md"
INDEX = "00_start_here/YAML_test_case_index/README_YAML_test_case_index.md"

MARKER_LEGEND = ("`-` blank · `~` race abstention · `&` candidate abstention · "
                 "`?` spoiled · `%` spoiled+reissued — all tabulate as 0 "
                 "(reported honestly)")


# --------------------------------------------------------------------------- #
# Extraction helpers (schema-tolerant: flat files and nested BV imports)
# --------------------------------------------------------------------------- #
def _find_first(node, keys):
    """Depth-first search for the first value under any of `keys`."""
    if isinstance(node, dict):
        for k in keys:
            if k in node and node[k] is not None:
                return node[k]
        for v in node.values():
            found = _find_first(v, keys)
            if found is not None:
                return found
    elif isinstance(node, list):
        for v in node:
            found = _find_first(v, keys)
            if found is not None:
                return found
    return None


def _norm_method(raw):
    m = re.split(r"[#\s]", str(raw or "STAR").strip())[0].strip().lower()
    return METHOD_ALIASES.get(m, m)


def _ballot_kind(ballots_text, method):
    clean = "\n".join(ln.split("#")[0] for ln in str(ballots_text).splitlines())
    if ">" in clean:
        return "ranked"
    if method == "approval":
        return "approval"
    return "score"

HOW_TO_READ = {
    "score":    "Row 1 = candidate names; each later row is one voter's 0–5 scores "
                "(a `N ×` prefix = N identical ballots).",
    "approval": "Row 1 = candidate names; each later row is one voter's approvals "
                "(`1` = approve, `0`/blank = not approved).",
    "ranked":   "Each row is one voter's ranking, most-preferred first "
                "(`N:` prefix = N identical ballots).",
}


def _mirror_path(yaml_path):
    d = os.path.dirname(yaml_path)
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    return os.path.join(d, os.path.basename(d) + "_tabulated", stem + "_tabulated.txt")


def _mirror_report(yaml_path):
    """The engine report from the _tabulated mirror: the section after the
    TABULATION RESULTS divider (composed mirrors) or the whole file (plain
    mirrors). Machine-specific file:// lines are stripped."""
    mp = _mirror_path(yaml_path)
    if not os.path.exists(mp):
        return None
    text = open(mp, encoding="utf-8").read()
    if "TABULATION RESULTS" in text:
        text = text.split("TABULATION RESULTS", 1)[1]
        text = text.split("\n", 2)[2] if text.count("\n") >= 2 else text
    lines = [ln for ln in text.splitlines() if "file:///" not in ln]
    # The full render opens with the title banner and the (indented) scenario
    # description — the page already shows both, so trim that echo: drop the
    # leading "=== title ===" line plus any indented/blank lines that follow.
    out, started = [], False
    for i, ln in enumerate(lines):
        if not started:
            if re.match(r"^=== .* ===\s*$", ln):
                continue
            if not ln.strip() or ln.startswith("  "):
                continue
            started = True
        out.append(ln)
    return "\n".join(out).strip("\n")


def _rel(target_repo_relative, page_dir):
    return os.path.relpath(os.path.join(REPO, target_repo_relative),
                           page_dir).replace(os.sep, "/")


def _folder_readme(folder):
    for fn in sorted(os.listdir(folder)):
        if fn.lower().startswith("readme") and fn.lower().endswith(".md"):
            return fn
    return None


def _divergence_case(stem):
    root = os.path.join(REPO, "divergence_review", "cases")
    if not os.path.isdir(root):
        return None
    for dirpath, _dirs, files in os.walk(root):
        if stem + ".md" in files:
            return os.path.relpath(os.path.join(dirpath, stem + ".md"), REPO)
    return None


# --------------------------------------------------------------------------- #
# Page rendering
# --------------------------------------------------------------------------- #
def render(yaml_path, siblings):
    rel_src = os.path.relpath(yaml_path, REPO).replace(os.sep, "/")
    folder = os.path.dirname(yaml_path)
    stem = os.path.splitext(os.path.basename(yaml_path))[0]
    page_dir = os.path.join(folder, os.path.basename(folder) + "_pages")

    data = yaml.safe_load(open(yaml_path, encoding="utf-8").read())
    if not isinstance(data, (dict, list)):
        return None
    ballots = _find_first(data, ["ballots"])
    if ballots is None:
        return None
    title = _find_first(data, ["election_title", "title"]) or stem
    desc = _find_first(data, ["scenario_description", "election_description",
                              "race_description"])
    method = _norm_method(_find_first(data, ["voting_method"]))
    seats = _find_first(data, ["num_winners", "seats"]) or 1
    winners = None
    ew = data.get("expected_winners") if isinstance(data, dict) else None
    if isinstance(ew, list) and ew:
        winners = [str(w) for w in ew]
    else:
        er = _find_first(data, ["expected_results"])
        w = _find_first(er, ["winners", "elected"]) if er is not None else None
        if isinstance(w, list) and w:
            winners = [str(x) for x in w]
    lot = data.get("lot_numbers") if isinstance(data, dict) else None

    disp, docs = METHOD_DOCS.get(method, (str(method), "00_start_here"))
    kind = _ballot_kind(ballots, method)
    ballots_text = str(ballots).rstrip("\n")
    has_markers = bool(re.search(r"[~&?%]|(^|,)\s*-\s*(,|$)", ballots_text, re.M))

    L = []
    L.append(f"# {title}")
    L.append("")
    L.append(f"*Generated from [`{os.path.basename(yaml_path)}`](../{os.path.basename(yaml_path)}) "
             f"— do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*")
    L.append("")
    seat_txt = "1 seat" if str(seats) == "1" else f"{seats} seats"
    L.append(f"**Method:** [{disp}]({_rel(docs, page_dir)}) · **{seat_txt}**"
             + (f" · **Expected winner{'s' if winners and len(winners) > 1 else ''}:** "
                + ", ".join(winners) if winners else ""))
    if lot:
        L.append("")
        L.append(f"**Official tie-break (lot) order:** {' > '.join(str(c) for c in lot)} "
                 f"— consulted only if every deterministic tiebreaker stays tied "
                 f"([how the ladder works]({_rel('00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md', page_dir)})).")
    L.append("")
    if desc:
        L.append("## Scenario")
        L.append("")
        L.append(str(desc).strip())
        L.append("")
    L.append("## Ballots")
    L.append("")
    L.append(HOW_TO_READ[kind])
    if has_markers:
        L.append("")
        L.append(f"Markers on these ballots: {MARKER_LEGEND}.")
    L.append("")
    L.append("```text")
    L.append(ballots_text)
    L.append("```")
    L.append("")
    report = _mirror_report(yaml_path)
    L.append("## What the engine says")
    L.append("")
    if report:
        mirror_rel = os.path.relpath(_mirror_path(yaml_path), page_dir).replace(os.sep, "/")
        L.append(f"Full report from the [`_tabulated` mirror]({mirror_rel}) "
                 f"(regenerated on every run; every analysis forced on):")
        L.append("")
        L.append("```text")
        L.append(report)
        L.append("```")
    else:
        L.append("*(No `_tabulated` mirror found — run the file once to generate it.)*")
    L.append("")
    L.append("Run it yourself:")
    L.append("")
    L.append("```bash")
    L.append(f"python STARVote_LH_tabulation_engine/starvote_larry_hastings.py {rel_src}")
    L.append("```")
    L.append("")

    # --- cross-references ---------------------------------------------------
    refs = []
    readme = _folder_readme(folder)
    if readme:
        refs.append(f"[This set's lesson (README)](../{readme}) — the hand-written "
                    f"teaching context for every case in this folder")
    div = _divergence_case(stem)
    if div:
        refs.append(f"[Methods disagree on this election]({_rel(div, page_dir)}) — "
                    f"its entry in the divergence review ledger")
    hay = " ".join([stem, str(title), str(desc or "")]).lower()
    seen = set()
    for pat, label, target in TOPIC_LINKS:
        if re.search(pat, hay) and target not in seen and os.path.exists(os.path.join(REPO, target)):
            seen.add(target)
            refs.append(f"[{label}]({_rel(target, page_dir)})")
    refs.append(f"[Glossary]({_rel(GLOSSARY, page_dir)}) · "
                f"[all cases by method]({_rel(INDEX, page_dir)})")
    L.append("## See also")
    L.append("")
    for r in refs:
        L.append(f"- {r}")
    others = [s for s in siblings if s != os.path.basename(yaml_path)]
    if others:
        L.append("")
        L.append("More cases in this set: "
                 + " · ".join(f"[{os.path.splitext(s)[0]}]({os.path.splitext(s)[0]}.md)"
                              for s in others))
    L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def expected_pages():
    """Return {absolute page path: content} for every election YAML."""
    pages = {}
    for root in ROOTS:
        base = os.path.join(REPO, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames
                           if not d.endswith(GENERATED_SUFFIXES) and d != "img"]
            ymls = sorted(f for f in filenames if f.endswith((".yaml", ".yml")))
            for fn in ymls:
                path = os.path.join(dirpath, fn)
                try:
                    content = render(path, ymls)
                except Exception as e:      # unparsable file: skip, warn
                    print(f"  ! skipped {os.path.relpath(path, REPO)}: {e}")
                    continue
                if content is None:
                    continue
                page_dir = os.path.join(dirpath, os.path.basename(dirpath) + "_pages")
                pages[os.path.join(page_dir, os.path.splitext(fn)[0] + ".md")] = content
    return pages


def existing_pages():
    found = {}
    for root in ROOTS:
        base = os.path.join(REPO, root)
        for dirpath, _dirs, filenames in os.walk(base):
            if os.path.basename(dirpath).endswith("_pages"):
                for fn in filenames:
                    if fn.endswith(".md"):
                        p = os.path.join(dirpath, fn)
                        found[p] = open(p, encoding="utf-8").read()
    return found


def check():
    """Return (stale_or_missing, orphans) page paths."""
    want, have = expected_pages(), existing_pages()
    stale = [p for p, c in want.items() if have.get(p) != c]
    orphans = [p for p in have if p not in want]
    return stale, orphans


def main():
    want = expected_pages()
    written = 0
    for p, content in sorted(want.items()):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if not os.path.exists(p) or open(p, encoding="utf-8").read() != content:
            open(p, "w", encoding="utf-8").write(content)
            written += 1
    removed = 0
    for p in existing_pages():
        if p not in want:
            os.remove(p)
            removed += 1
    print(f"yaml-pages: {len(want)} pages ({written} written/updated, {removed} orphan(s) removed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
