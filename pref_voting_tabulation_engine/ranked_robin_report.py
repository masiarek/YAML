#!/usr/bin/env python3
"""
ranked_robin_report.py — a friendly Ranked Robin (RCV-RR / Copeland) tabulation.

Why this exists: the STAR engine (`starvote_larry_hastings.py`) has **no Ranked
Robin tabulator**, so when it's handed ranked ballots it dispatches them to
**RCV-IRV** — its echo shows elimination rounds, not the round-robin. This tool
prints the *Ranked Robin* view instead: the ballots, the full pairwise
(round-robin) table, each candidate's win–loss record, and the winner — the way
Ranked Robin actually decides (most head-to-head wins).

Dependency-light: uses only the LH engine's pairwise-matrix helper (no
`pref_voting` needed). If `pref_voting` is installed, the winner is also
cross-checked against its Copeland implementation.

Usage:
    python ranked_robin_report.py FILE.yaml
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
# parse_election (handles nested/flat YAML, ranked + score) needs no pref_voting.
from pref_voting_tabulation import parse_election  # noqa: E402
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "STARVote_LH_tabulation_engine"))
import starvote_larry_hastings as LH  # noqa: E402


def _ballot_lines(cands, dicts, ranks):
    """Collapse ballots to 'count × A > B > C' (ranked) or 'count × 5,3,0' (score)."""
    rows = []
    if ranks is not None:
        for order in ranks:
            rows.append(" > ".join(order))
    else:
        for b in dicts:
            rows.append(", ".join(str(b.get(c, 0)) for c in cands))
    counts = Counter(rows)
    # preserve first-seen order
    seen = []
    for r in rows:
        if r not in seen:
            seen.append(r)
    return [(counts[r], r) for r in seen]


def report(path):
    cands, dicts, ranks, priority, has_ties, vm = parse_election(path)
    n = len(dicts)
    matrix = LH.calculate_preference_matrix(cands, dicts)

    out = []
    out.append("=== Ranked Robin (RCV-RR / Copeland) — single winner ===")
    kind = "ranked" if ranks is not None else "score"
    out.append(f" Tabulating {n} {kind} ballots, {len(cands)} candidates.\n")

    out.append("Ballots:")
    for cnt, r in _ballot_lines(cands, dicts, ranks):
        out.append(f"   {cnt:>3} × {r}")
    out.append("")

    # Each unordered pair, head-to-head.
    out.append('Round-robin — every pair, head-to-head (votes For – Against):')
    wins = {c: [] for c in cands}
    losses = {c: [] for c in cands}
    ties = {c: [] for c in cands}
    margin = {c: 0 for c in cands}
    for i, a in enumerate(cands):
        for b in cands[i + 1:]:
            fa, aa, _ = matrix[a][b]      # a-For, a-Against
            margin[a] += fa - aa
            margin[b] += aa - fa
            if fa > aa:
                wins[a].append(b); losses[b].append(a)
                out.append(f"   {a} beats {b}   {fa} – {aa}")
            elif aa > fa:
                wins[b].append(a); losses[a].append(b)
                out.append(f"   {b} beats {a}   {aa} – {fa}")
            else:
                ties[a].append(b); ties[b].append(a)
                out.append(f"   {a} ties {b}    {fa} – {aa}")
    out.append("")

    # Win–loss record; Ranked Robin = most wins, then highest total margin.
    out.append("Win–loss record (most head-to-head wins wins; ties broken by total margin):")
    ranked = sorted(cands, key=lambda c: (-len(wins[c]), -margin[c],
                                          priority.index(c) if c in priority else 1e9))
    for c in ranked:
        w, l, t = len(wins[c]), len(losses[c]), len(ties[c])
        rec = f"{w}–{l}" + (f"–{t}t" if t else "")
        beat = f"   (beats: {', '.join(wins[c])})" if wins[c] else ""
        out.append(f"   {c:<8} {rec:<6} margin {margin[c]:+d}{beat}")
    out.append("")

    # Winner + why.
    top_wins = len(wins[ranked[0]])
    leaders = [c for c in cands if len(wins[c]) == top_wins]
    winner = ranked[0]
    if len(leaders) == 1:
        if len(losses[winner]) == 0:
            why = "beats every opponent head-to-head — the Condorcet winner."
        else:
            why = f"the most head-to-head wins ({top_wins})."
        out.append(f"Winner — Ranked Robin: {winner}\n   {why}")
    else:
        out.append(f"Winner — Ranked Robin: {winner}")
        out.append(f"   ⚠️  {len(leaders)} candidates tie on wins ({', '.join(leaders)}) — "
                   "a cycle. Broken by total margin, then lot order. "
                   "(This is where Minimax / Ranked Pairs / Schulze differ — see "
                   "cycle_resolution.md.)")

    # Optional cross-check.
    try:
        from pref_voting.profiles import Profile
        from pref_voting.c1_methods import copeland
        I = {c: i for i, c in enumerate(cands)}
        if ranks is not None:
            prof = Profile([[I[c] for c in o] for o in ranks])
            cope = [cands[x] for x in copeland(prof)]
            out.append(f"\n (pref_voting Copeland cross-check: {', '.join(cope)})")
    except Exception:
        pass
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python ranked_robin_report.py FILE.yaml [FILE2.yaml ...]")
    for p in sys.argv[1:]:
        print(report(p))
        print()
