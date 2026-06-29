"""
pref_voting_tabulation.py — independent referee for the LH engine.

Cross-checks the LH `starvote_larry_hastings` engine against Eric Pacuit's
`pref_voting` library (https://github.com/voting-tools/pref_voting) on the
ranked-ballot methods both can compute: **Plurality, RCV-IRV, Condorcet**, plus
**Copeland (= Ranked Robin)** and **Borda** as bonus columns pref_voting provides.

Why: pref_voting is a mature, peer-reviewed social-choice library, so it's an
independent witness that the LH engine's IRV / Condorcet / pairwise machinery is
correct. (pref_voting has **no STAR**, so STAR's runoff itself is *not* cross-checked
here — that's what the STAR positive tests are for. This validates the surrounding
ranked machinery.)

Usage (CLI):
    python pref_voting_tabulation_engine/pref_voting_tabulation.py FILE.yaml [...]
    python pref_voting_tabulation_engine/pref_voting_tabulation.py --all   # whole repo

Programmatic:
    from pref_voting_tabulation import crosscheck
    result = crosscheck("path/to/election.yaml")   # dict: method -> (lh, pv, status)

Requires: pip install pref_voting  (optional dependency; importers should guard).
"""
import os
import re
import sys
import glob

# This engine lives at <repo>/pref_voting_tabulation_engine/. The LH engine it
# cross-checks against is the sibling <repo>/STARVote_LH_tabulation_engine/.
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_REPO, "STARVote_LH_tabulation_engine"))
import yaml  # noqa: E402
import starvote_larry_hastings as LH  # noqa: E402

# pref_voting is optional; callers (e.g. the pytest) should skip if absent.
try:
    from pref_voting.profiles import Profile
    from pref_voting.profiles_with_ties import ProfileWithTies
    from pref_voting.iterative_methods import instant_runoff
    from pref_voting.scoring_methods import plurality, borda
    from pref_voting.c1_methods import copeland
    PREF_VOTING_AVAILABLE = True
except Exception:  # pragma: no cover
    PREF_VOTING_AVAILABLE = False

# Methods we skip (pref_voting's ranked methods are meaningless on these).
_SKIP_METHODS = {"approval", "bloc", "sss", "rrv", "allocated", "stv"}


# --------------------------------------------------------------------------- #
# Parsing: one YAML -> (candidates, per-voter score dicts, optional strict
# rankings, tiebreak priority, has_ties flag, voting_method).
# --------------------------------------------------------------------------- #
def _load_race(path):
    d = yaml.safe_load(open(path))
    if isinstance(d, dict) and "election" in d:
        race = d["election"]["races"][0]
    else:
        race = d
    return (race.get("ballots", ""),
            str(race.get("voting_method", "STAR")),
            race.get("lot_numbers"))


def parse_election(path):
    ballots_txt, vm, lot = _load_race(path)
    # Detect ranked ballots by a '>' in *non-comment* content.
    clean = "\n".join(l.split("#")[0] for l in ballots_txt.splitlines())
    if ">" in clean:                                  # ranked ballots
        voters, cset = [], []
        for ln in ballots_txt.splitlines():
            ln = ln.split("#")[0].strip()
            if not ln:
                continue
            m = re.match(r"(\d+)\s*[:xX×]\s*(.+)", ln)
            if m:
                w, order = int(m.group(1)), [c.strip() for c in m.group(2).split(">")]
            else:
                w, order = 1, [c.strip() for c in ln.split(">")]
            for c in order:
                if c not in cset:
                    cset.append(c)
            voters += [order] * w
        cands = sorted(cset)
        dicts = [{c: (len(o) - i if c in o else 0) for i, c in enumerate(o)}
                 for o in voters]
        return cands, dicts, voters, (lot or cands), False, vm
    # score ballots
    cands, dicts, _ = LH.parse_ballots_from_string(ballots_txt)
    has_ties = any(
        len([s for s in b.values() if s > 0]) != len({s for s in b.values() if s > 0})
        for b in dicts)
    return cands, dicts, None, (lot or cands), has_ties, vm


# --------------------------------------------------------------------------- #
# The two engines
# --------------------------------------------------------------------------- #
def lh_results(cands, dicts, priority):
    from collections import Counter
    cw = LH.condorcet_winner(cands, dicts)
    irv = LH.compute_irv_winner(cands, dicts, priority)[0]
    fc = Counter()
    for b in dicts:
        mx = max(b.values()) if b else 0
        if mx > 0:
            tops = sorted([c for c in cands if b.get(c, 0) == mx],
                          key=lambda c: priority.index(c) if c in priority else 1e9)
            fc[tops[0]] += 1
    plur = (max(fc, key=lambda c: (fc[c], -(priority.index(c) if c in priority else 1e9)))
            if fc else None)
    return {"Condorcet": cw, "IRV": irv, "Plurality": plur}


def _pv_irv(cands, dicts, priority):
    """Truncated profile for IRV/Plurality: rank only the candidates a ballot
    actually scores (> 0), breaking equal positive scores by `priority`. Score-0
    candidates are left **unranked** — so they're treated as *exhausted* in IRV,
    exactly as the LH engine (pyrankvote) does. (Filling them in would invent
    phantom transfers and break on bullet/truncated votes.)"""
    I = {c: i for i, c in enumerate(cands)}
    rankings = []
    for b in dicts:
        ranked = sorted([c for c in cands if b.get(c, 0) > 0],
                        key=lambda c: (-b[c], priority.index(c) if c in priority else 1e9))
        rankings.append({I[c]: pos for pos, c in enumerate(ranked)})
    return ProfileWithTies(rankings, candidates=list(range(len(cands))))


def _pv_ties(cands, dicts):
    I = {c: i for i, c in enumerate(cands)}
    rmaps = []
    for b in dicts:
        uniq = sorted({b.get(c, 0) for c in cands}, reverse=True)
        rank = {s: i for i, s in enumerate(uniq)}
        rmaps.append({I[c]: rank[b.get(c, 0)] for c in cands})
    return ProfileWithTies(rmaps, candidates=list(range(len(cands))))


def pv_results(cands, dicts, ranks, priority):
    """Each method maps to a *set* of co-winners (pref_voting returns all winners
    that tie under the method, so a set of size > 1 means a genuine tie).

    Everything is derived from the per-voter score dicts (ranked ballots were
    already converted to descending-score dicts upstream, with unranked = 0).
    This handles truncated ballots and equal-rank/equal-score indifference
    uniformly: a strict profile (ties broken by `priority`) for IRV/Plurality,
    and a weak-order profile (indifference preserved) for Condorcet/Copeland/Borda.
    """
    inv = {i: c for i, c in enumerate(cands)}
    irv_prof = _pv_irv(cands, dicts, priority)    # IRV / Plurality (truncation kept)
    ties = _pv_ties(cands, dicts)                 # Condorcet / Copeland / Borda
    names = lambda xs: [inv[x] for x in xs] if xs else []
    cw = ties.condorcet_winner()
    return {
        "Condorcet": ([inv[cw]] if cw is not None else []),
        "IRV": names(instant_runoff(irv_prof)),
        "Plurality": names(plurality(irv_prof)),
        "Copeland": names(copeland(ties)),   # = Ranked Robin
        "Borda": names(borda(ties)),
    }


# --------------------------------------------------------------------------- #
# Public API
# --------------------------------------------------------------------------- #
def crosscheck(path):
    """Return {method: (lh_winner, pv_winner, status)} for one election.

    status: 'ok' (agree) | 'mismatch' | 'report' (tie present: not asserted) |
            'pv-only' (Copeland/Borda; LH doesn't compute it).
    """
    cands, dicts, ranks, priority, has_ties, vm = parse_election(path)
    lh = lh_results(cands, dicts, priority)
    pv = pv_results(cands, dicts, ranks, priority)   # method -> [co-winners]
    out = {}
    for m in ("Condorcet", "IRV", "Plurality"):
        lh_w, pv_set = lh[m], pv[m]
        if len(pv_set) > 1:
            # pref_voting reports a tie (>1 co-winner). Cross-engine tiebreaks
            # legitimately differ, so we only require LH's pick to be *among*
            # the tied co-winners; not a hard assertion of one name.
            status = "ok-tie" if (lh_w in pv_set) else "mismatch"
        elif not pv_set:                       # pref_voting: no winner (e.g. cycle)
            status = "ok" if lh_w is None else "mismatch"
        else:
            status = "ok" if (lh_w == pv_set[0]) else "mismatch"
        out[m] = (lh_w, pv_set, status)
    for m in ("Copeland", "Borda"):
        out[m] = (None, pv[m], "pv-only")
    return out


def is_crosscheckable(path):
    name = os.path.basename(path).lower()
    if any(t in name for t in ("temp", "trash", "scratch", "tmp")):
        return False                       # scratch files, not real elections
    try:
        d = yaml.safe_load(open(path))
        race = d["election"]["races"][0] if "election" in d else d
        if str(race.get("voting_method", "STAR")).strip().lower() in _SKIP_METHODS:
            return False
        if int(race.get("num_winners", 1) or 1) != 1:
            return False
        if not race.get("ballots"):
            return False
        # Must parse to a real >=2-candidate election (skips malformed files).
        cands, dicts, *_ = parse_election(path)
        return len(cands) >= 2 and len(dicts) >= 1
    except Exception:
        return False


def discover(dirs):
    files = []
    for d in dirs:
        for p in sorted(glob.glob(os.path.join(d, "*.yaml"))):
            if "_tabulated" in p:
                continue
            if is_crosscheckable(p):
                files.append(p)
    return files


def _print_table(path):
    base = os.path.basename(path)
    print(f"\n=== {base} ===")
    res = crosscheck(path)
    mark = {"ok": "✓", "ok-tie": "✓ (tie — LH picks among co-winners)",
            "mismatch": "✗ MISMATCH", "pv-only": "(pref_voting only)"}
    for m, (lh, pv, st) in res.items():
        lh_s = "-" if st == "pv-only" else str(lh)
        pv_s = pv[0] if len(pv) == 1 else (str(pv) if pv else "None")
        print(f"  {m:10} LH={lh_s:11} pref_voting={str(pv_s):14} {mark[st]}")
    return res


if __name__ == "__main__":
    if not PREF_VOTING_AVAILABLE:
        sys.exit("pref_voting not installed:  pip install pref_voting")
    args = sys.argv[1:]
    REPO = _REPO
    if args == ["--all"]:
        dirs = [os.path.join(REPO, "01_Single_winner"),
                os.path.join(REPO, "01_Single_winner", "runoff_overturns_leader"),
                os.path.join(REPO, "01_Single_winner", "paradoxes_and_whoops"),
                os.path.join(REPO, "01_Single_winner", "Flat_scores_ties"),
                os.path.join(REPO, "01_Single_winner", "summability_demo"),
                os.path.join(REPO, "split_voting"),
                os.path.join(REPO, "YAML_library", "1_positive")]
        args = discover(dirs)
    mism = 0
    for f in args:
        res = _print_table(f)
        mism += sum(1 for _, _, st in res.values() if st == "mismatch")
    print(f"\n{len(args)} file(s) cross-checked; {mism} mismatch(es).")
    sys.exit(1 if mism else 0)
