#!/usr/bin/env python3
"""
RCV / IRV tabulation engine wrapper.

Mirrors the role of ``starvote_larry_hastings.py``: it reads the same YAML
election format (score ballots, 0..5) and tabulates a single-winner
Instant-Runoff Voting (IRV) election using the vendored ``pyrankvote``
library (MIT licensed, see ./pyrankvote/LICENSE.txt).

Because the YAML ballots are *scores* but IRV needs *ranks*, this wrapper
converts each score ballot into a ranked ballot. See score_ballot_to_ranking()
for the conversion rules.

Usage:
    python rcv_irv_tabulation.py path/to/election.yaml
"""

import os
import re
import sys

# Make the vendored packages importable no matter where we're launched from.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import pyrankvote  # noqa: E402  (vendored)
from pyrankvote import Ballot, Candidate  # noqa: E402

try:
    import yaml  # PyYAML
except ImportError:  # pragma: no cover
    yaml = None


# Marker characters that all count as "no support" (mirrors the STAR engine).
MARKERS = set("~&^?%-")


# --------------------------------------------------------------------------- #
# YAML loading
# --------------------------------------------------------------------------- #
def load_ballots_block(path):
    """Return (title, ballots_text) from a STAR/IRV-style YAML file."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if yaml is None:
        raise RuntimeError("PyYAML is required to read .yaml election files.")
    data = yaml.safe_load(text)

    # Accept either a flat mapping (voting_method/ballots at top level) or a
    # nested race_* / election wrapper; grab the first mapping that has ballots.
    def find_ballots(d):
        if isinstance(d, dict):
            if "ballots" in d:
                return d
            for v in d.values():
                found = find_ballots(v)
                if found:
                    return found
        elif isinstance(d, list):               # e.g. election: races: [ {...} ]
            for v in d:
                found = find_ballots(v)
                if found:
                    return found
        return None

    race = find_ballots(data) or {}
    ballots_text = race.get("ballots", "")
    title = race.get("election_title") or race.get("title")
    num_winners = race.get("num_winners", race.get("seats", 1))
    try:
        num_winners = max(1, int(num_winners))
    except (TypeError, ValueError):
        num_winners = 1
    return title, ballots_text, num_winners


# --------------------------------------------------------------------------- #
# Score-ballot parsing (subset of the STAR engine's parser)
# --------------------------------------------------------------------------- #
def parse_score_ballots(ballot_string):
    """
    Parse the score-grid format into (candidates, ballots).

    ballots is a list of (weight, {candidate: score}) tuples.

    Supports:
      * header row of candidate names; a leading "Count:" label is stripped
      * per-row weight via the colon/x prefix, e.g. "30:5,4,0" or "30 x 5,4,0"
      * blank cells and marker characters count as score 0
    """
    lines = []
    for raw in ballot_string.strip().splitlines():
        line = raw.split("#")[0].strip()
        if line:
            lines.append(line)
    if not lines:
        return [], []

    headers = [h.strip() for h in re.split(r"[,\t]+", lines[0]) if h.strip()]
    if headers and re.match(r"(?i)^count\s*:", headers[0]):
        headers[0] = headers[0].split(":", 1)[1].strip()

    ballots = []
    for line in lines[1:]:
        weight = 1
        parts = re.split(r"[,\t]", line)
        wmatch = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", parts[0])
        if wmatch:
            weight = int(wmatch.group(1))
            parts[0] = wmatch.group(2)
        cells = [p.strip() for p in parts]
        if len(cells) != len(headers):
            continue  # skip malformed rows

        def to_score(c):
            c = c.strip()
            if c == "" or c in MARKERS:
                return 0
            try:
                return int(c)
            except ValueError:
                return 0

        scores = {h: to_score(c) for h, c in zip(headers, cells)}
        ballots.append((weight, scores))
    return headers, ballots


# --------------------------------------------------------------------------- #
# Score -> rank conversion
# --------------------------------------------------------------------------- #
def score_ballot_to_ranking(scores, candidate_order):
    """
    Convert one score ballot {candidate: score} into an ordered list of
    candidate names (most-preferred first).

    Rules:
      * Higher score  -> more preferred.
      * Score 0 (or blank/marker) -> UNRANKED; the candidate is left off the
        ballot entirely (matches STAR's "0 = no support" semantics, and means
        the ballot becomes exhausted rather than transferring to a 0-score).
      * Equal NON-zero scores -> a tie. IRV needs a strict order, so ties are
        broken deterministically by candidate column order (the order the
        candidates appear in the ballot header). This is a documented
        simplification; equal-rank IRV is not represented.
    """
    ranked = [c for c in candidate_order if scores.get(c, 0) > 0]
    col_index = {c: i for i, c in enumerate(candidate_order)}
    ranked.sort(key=lambda c: (-scores[c], col_index[c]))
    return ranked


# --------------------------------------------------------------------------- #
# Ranked-ballot parsing (native RCV format, e.g. "40:A>C>B")
# --------------------------------------------------------------------------- #
def parse_ranked_ballots(ballot_string):
    """
    Parse native ranked ballots into (candidates, ballots).

    Each line is an optional weight prefix plus a '>'-separated preference
    order, most-preferred first:  "40:A>C>B"  or  "A > C > B".

    Equal ranks ("A=B") are not representable in IRV, so tied candidates are
    listed in left-to-right order (a documented simplification). Candidates that
    don't appear on a ballot are simply unranked (the ballot can exhaust).
    """
    ballots = []
    candidates = []  # first-appearance order
    for raw in ballot_string.strip().splitlines():
        line = raw.split("#")[0].strip()
        if not line:
            continue
        weight = 1
        m = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", line)
        if m:
            weight = int(m.group(1))
            line = m.group(2).strip()
        ranking = []
        for group in line.split(">"):
            for name in group.split("="):  # equal ranks -> listed order
                name = name.strip()
                if name:
                    ranking.append(name)
                    if name not in candidates:
                        candidates.append(name)
        if ranking:
            ballots.append((weight, ranking))
    return candidates, ballots


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def run(path):
    # pyrankvote breaks elimination ties with random.choice(). Unseeded, the
    # SAME ballots can elect DIFFERENT winners run to run — unacceptable for a
    # library whose counts must be reproducible (cf. the STAR engine's
    # deterministic lot order). Seed the RNG so tie resolution is arbitrary
    # but stable. (A true tie is still a tie — the report shows the tied
    # tallies; this only pins which candidate the coin flip picks.)
    import random
    random.seed(0)
    title, ballots_text, num_winners = load_ballots_block(path)
    seats = max(1, int(num_winners or 1))

    # Auto-detect: '>' means native ranked ballots; otherwise score ballots.
    # Strip per-line comments first, so a rank annotation in a score-ballot
    # comment (e.g. "14:4,3,5,2,1  # Carmen base (C > A > B)") doesn't get
    # misread as a real ranked ballot. (Mirrors the STAR engine.)
    _detect = "\n".join(line.split("#")[0] for line in ballots_text.splitlines())
    ranked_mode = ">" in _detect
    if ranked_mode:
        candidates_names, parsed = parse_ranked_ballots(ballots_text)
    else:
        candidates_names, parsed = parse_score_ballots(ballots_text)
    if not parsed:
        print("Error: no valid ballots found.")
        sys.exit(1)                             # an error must not exit 0

    cand_objs = {name: Candidate(name) for name in candidates_names}
    pv_ballots = []
    total = 0
    for weight, payload in parsed:
        if ranked_mode:
            ranking = payload  # already an ordered list of names
        else:
            ranking = score_ballot_to_ranking(payload, candidates_names)
        ranked_objs = [cand_objs[n] for n in ranking]
        for _ in range(weight):
            pv_ballots.append(Ballot(ranked_candidates=ranked_objs))
        total += weight

    if seats > 1:
        label = f"STV / Single Transferable Vote (multi-winner — {seats} seats)"
    else:
        label = "RCV / Instant-Runoff Voting (single winner)"

    print(f"\n--- {label} ---")
    if title:
        print(f"  {title}")
    source = ("ranked ballots" if ranked_mode
              else "converted from score ballots; 0 = unranked")
    print(f" Tabulating {total} ballots ({source}).")
    if seats > 1:
        # Droop quota = floor(valid_votes / (seats + 1)) + 1
        droop = total // (seats + 1) + 1
        print(f" {seats} seats; Droop quota = {droop} "
              f"({droop / total * 100:.1f}% of {total}).")
    print()

    if seats > 1:
        result = pyrankvote.single_transferable_vote(
            list(cand_objs.values()), pv_ballots, number_of_seats=seats
        )
    else:
        result = pyrankvote.instant_runoff_voting(
            list(cand_objs.values()), pv_ballots
        )
    print(result)

    winners = result.get_winners()
    print(f"\nWinner(s) — {label}")
    if winners:
        for w in winners:
            print(f"  {w.name}")
    else:
        print("  (no winner)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    run(sys.argv[1])
