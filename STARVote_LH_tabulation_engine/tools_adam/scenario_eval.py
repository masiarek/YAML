#!/usr/bin/env python3
"""
scenario_eval.py
================
Shared helper: tabulate an election file and return its winners + seat count,
using the same method/seats/tiebreaker logic as the main wrapper but WITHOUT
any printing. Used by both the test suite and the expected-winners generator,
so they always agree.
"""

import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))

import starvote  # noqa: E402
import starvote_larry_hastings as wrapper  # noqa: E402


def scenario_winners(path):
    """Return (winners, seats) for an election file.

    winners is a list[str] in the order the engine elected them. Ties are
    resolved deterministically with the same fallback the wrapper uses
    (LotNumberTiebreaker over CSV column order), so results are reproducible.
    """
    el = wrapper.load_election(str(path))
    candidates, ballots, _ = wrapper.parse_ballots_from_string(el["ballots"])
    method = el["method"] or starvote.star
    seats = el["seats"] or 1
    tiebreaker = wrapper.LotNumberTiebreaker(lot_numbers=[], silent=True)
    # NOTE: run at verbosity=1 to MIRROR the wrapper exactly. The engine's SSS
    # method can return different winners at verbosity=0 vs 1 (an upstream bug);
    # the wrapper runs verbose, so the tests must too, to match what users see.
    result = starvote.election(
        method,
        ballots,
        seats=seats,
        maximum_score=5,
        tiebreaker=tiebreaker,
        verbosity=1,
        print=lambda *a, **k: None,
    )
    winners = result if isinstance(result, (list, tuple)) else [result]
    return [str(w) for w in winners], seats


def scenario_counts(path):
    """Return (num_candidates, num_ballots) for an election file.

    num_ballots is the total number of ballots the engine tabulates — i.e.
    weighted rows like '42: ...' are expanded, matching the engine's
    'Tabulating N ballots.' line.
    """
    el = wrapper.load_election(str(path))
    candidates, ballots, _ = wrapper.parse_ballots_from_string(el["ballots"])
    return len(candidates), len(ballots)
