#!/usr/bin/env python3
"""
runoff_reversal_simulation.py — how often does a STAR Runoff Reversal happen?

A "Runoff Reversal" is the STAR outcome where the candidate who LEADS the Scoring
Round (most total stars) LOSES the Automatic Runoff to the other finalist. This
script measures how often that occurs over many random elections — and, crucially,
it reports the result *by model*, because the answer swings enormously with the
modelling assumptions.

The 301 takeaway is not a single percentage. It is this: a simulation number is
meaningless until you state (1) the electorate model, (2) the electorate size, and
(3) how ties were handled. This script makes all three explicit.

Two electorate models (both run by default):
  - impartial : every score uniform 0..5, independent per candidate. "White noise"
                (Impartial Culture). Adversarial stress test — manufactures far more
                reversals than real life; treat its rate as a loose upper bound.
  - spatial   : voters & candidates are points in issue space; a voter's sincere
                STAR ballot comes from min-max scaling utility = -distance onto 0..5.
                The realistic model (correlated ballots), where reversals are rarer.

Ties are NOT swept under an arbitrary tiebreaker. Each election lands in exactly one
of four buckets, so you can see how much of a raw "divergence" count is genuine
versus a tie an arbitrary rule happened to break:
  - reversal           : score leader is unambiguous AND strictly loses the runoff
  - runoff_tie         : the two finalists tie in the runoff (a tiebreaker decides)
  - finalist_score_tie : the top-two-by-score are tied (who "leads" is ambiguous)
  - no_reversal        : score leader also wins the runoff

Everything is seeded. No external dependencies beyond numpy.

Usage:
    python3 runoff_reversal_simulation.py                  # default sweep
    python3 runoff_reversal_simulation.py --selftest       # known-answer checks
    python3 runoff_reversal_simulation.py --elections 1000000 --voters 10 --candidates 5
"""

import argparse
import numpy as np

MAX_SCORE = 5


# --- core: classify many elections at once -----------------------------------
def classify(scores):
    """scores: int array (E, V, C). Returns dict of bucket -> boolean mask (E,)."""
    E, V, C = scores.shape
    totals = scores.sum(axis=1)                     # (E, C) total stars per candidate
    order = np.argsort(-totals, axis=1)             # finalists = order[:,0], order[:,1]
    e = np.arange(E)
    t1, t2 = order[:, 0], order[:, 1]
    t1tot, t2tot = totals[e, t1], totals[e, t2]
    t3tot = totals[e, order[:, 2]] if C >= 3 else np.full(E, -1)

    # the top-two-by-score are ambiguous if 1st ties 2nd, or 2nd ties 3rd (who is the
    # second finalist?). Either way "the score leader / finalists" isn't well defined.
    finalist_score_tie = (t1tot == t2tot) | (t2tot == t3tot)

    # runoff between the two finalists: each ballot prefers whichever it scored higher
    s1 = scores[e, :, t1]                            # (E, V) finalist-1 scores
    s2 = scores[e, :, t2]
    prefer1 = (s1 > s2).sum(axis=1)
    prefer2 = (s2 > s1).sum(axis=1)
    runoff_tie = (prefer1 == prefer2)
    leader_loses = prefer2 > prefer1                 # score-2nd beats score-1st

    # clean 4-way partition (priority: score-tie > runoff-tie > reversal > none)
    b_score_tie = finalist_score_tie
    b_runoff_tie = ~b_score_tie & runoff_tie
    b_reversal = ~b_score_tie & ~runoff_tie & leader_loses
    b_none = ~b_score_tie & ~b_runoff_tie & ~b_reversal
    return {
        "reversal": b_reversal,
        "runoff_tie": b_runoff_tie,
        "finalist_score_tie": b_score_tie,
        "no_reversal": b_none,
    }


# --- electorate models -------------------------------------------------------
def impartial(E, V, C, rng):
    """Impartial Culture: every score uniform 0..MAX_SCORE, independent."""
    return rng.integers(0, MAX_SCORE + 1, size=(E, V, C))


def spatial(E, V, C, rng, dims=2):
    """Spatial model: utility = -distance in [0,1]^dims, scaled per-voter to 0..5."""
    cand = rng.random((E, 1, C, dims))              # candidate positions
    vote = rng.random((E, V, 1, dims))              # voter positions
    util = -np.sqrt(((vote - cand) ** 2).sum(axis=3))   # (E, V, C), higher = closer
    lo = util.min(axis=2, keepdims=True)
    hi = util.max(axis=2, keepdims=True)
    span = np.where(hi > lo, hi - lo, 1.0)
    scaled = (util - lo) / span * MAX_SCORE         # min-max onto 0..5 per voter
    return np.rint(scaled).astype(int)


# --- runner ------------------------------------------------------------------
def run(model_fn, E, V, C, rng, chunk=200_000):
    """Run E elections in memory-safe chunks; return bucket percentages."""
    counts = {"reversal": 0, "runoff_tie": 0, "finalist_score_tie": 0, "no_reversal": 0}
    done = 0
    while done < E:
        n = min(chunk, E - done)
        scores = model_fn(n, V, C, rng)
        for k, mask in classify(scores).items():
            counts[k] += int(mask.sum())
        done += n
    return {k: 100.0 * v / E for k, v in counts.items()}


def fmt(pcts):
    return (f"reversal {pcts['reversal']:5.1f}% | runoff_tie {pcts['runoff_tie']:5.1f}% "
            f"| finalist_score_tie {pcts['finalist_score_tie']:5.1f}% "
            f"| no_reversal {pcts['no_reversal']:5.1f}%")


def selftest():
    """Known-answer checks on hand-built elections (E=1)."""
    # Case A — a clean reversal: A leads on score (13) but B wins the runoff 2-1.
    A = np.array([[[5, 1, 2], [4, 5, 0], [4, 5, 0]]])   # (1,3,3)  cols A,B,C
    assert classify(A)["reversal"][0], "expected a clean reversal"
    # Case B — no reversal: B leads on score AND wins the runoff.
    B = np.array([[[2, 5, 1], [2, 5, 0], [5, 4, 0]]])
    assert classify(B)["no_reversal"][0], "expected no reversal"
    # Case C — a runoff tie between the two finalists.
    Cc = np.array([[[5, 5, 0], [5, 0, 0], [0, 5, 0]]])  # A,B tie on score and runoff
    cls = classify(Cc)
    assert cls["finalist_score_tie"][0] or cls["runoff_tie"][0], "expected a tie bucket"
    print("selftest: OK (clean reversal, no-reversal, and tie cases classify correctly)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--elections", type=int, default=300_000)
    ap.add_argument("--voters", type=int, default=21)
    ap.add_argument("--candidates", type=int, default=5)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        selftest()
        return

    rng = np.random.default_rng(args.seed)
    print(f"Runoff Reversal frequency — {args.elections:,} elections, "
          f"{args.candidates} candidates, {args.voters} voters, seed {args.seed}")
    print("(A 'reversal' = the Scoring-Round leader loses the Automatic Runoff.)")
    print("-" * 78)
    for name, fn in (("impartial", impartial), ("spatial  ", spatial)):
        pcts = run(fn, args.elections, args.voters, args.candidates, rng)
        print(f"  {name}: {fmt(pcts)}")
    print("-" * 78)
    print("Read the model + size + tie split alongside the number — never the % alone.")


if __name__ == "__main__":
    main()
