#!/usr/bin/env python3
"""
fbc_simulation.py — measure how often STAR (vs RCV-IRV) actually satisfies the
Favorite Betrayal Criterion, by brute force over many random elections.

WHY THIS EXISTS
---------------
The debate doc claimed STAR is "~98% favorite-betrayal-proof." That number had no
clean source (Equal Vote's chart is binary pass/fail; the ~91-98% figure floating
around is *Voter Satisfaction Efficiency* — accuracy, a different thing). So rather
than cite a number we can't defend, we MEASURE one — and, crucially, we report the
modelling assumptions, because the result swings hugely with them.

WHAT WE MEASURE
---------------
1. FBC-compliance frequency.
   For each random election we compute the honest STAR winner W. Then, for every
   voter, we ask: holding everyone else's honest ballot fixed, is there ANY ballot
   this voter could cast in which they do NOT keep their true favorite (co-)top —
   i.e. an actual favorite *betrayal* — that yields a winner they sincerely prefer
   to W? If even one voter has such a profitable betrayal, the election FAILS FBC.
   The fraction of elections with NO such voter is the empirical FBC rate.
   The favorite-betrayal ballot search is EXHAUSTIVE (every 0-5 ballot for STAR,
   every ranking for IRV), so this is a true best-response test, not a heuristic.

2. Works : backfires ratio (the "honesty" stat Equal Vote actually publishes,
   ~1:1 STAR vs ~3:1 IRV). Over every (voter, favorite-betrayal ballot) pair across
   all elections, we count how many strictly HELP the voter vs strictly HURT them
   (by their sincere utilities). The ratio help:hurt is reported per method.
   NOTE: this counts *all possible* betrayals, so it is a superset of the realistic
   strategies a faction would actually attempt; read it as "if you betray your
   favorite blindly, how often does it pay off vs cost you," not as Quinn's exact
   strategic-faction pipeline.

ELECTORATE MODELS
-----------------
- spatial    : voters and candidates are points in `--dims`-D issue space; sincere
               utility = -distance. This is the realistic model (what VSE uses).
- impartial  : each voter's utility for each candidate is uniform[0,1], independent.
               An adversarial stress test that manufactures far more paradoxes; treat
               its FBC rate as a rough lower bound.

Sincere ballots are derived deterministically from utilities: STAR scores are the
per-voter min-max scaling of utilities onto 0..5 (rounded); IRV rankings sort the
candidates by utility, descending.

TIE-BREAKS (fixed, for reproducibility)
---------------------------------------
- STAR finalists: top two score totals, ties broken toward the lower candidate index.
- STAR runoff tie (equal preference counts): the higher-scoring finalist wins.
- IRV elimination tie (equal fewest first-choices): the lower candidate index is
  eliminated. IRV majority check is > half of continuing ballots.

Everything is seeded; pass --seed to reproduce a run exactly.

USAGE
-----
    python3 fbc_simulation.py                  # default sweep, both models
    python3 fbc_simulation.py --elections 3000 --voters 21 --candidates 3
    python3 fbc_simulation.py --selftest       # just run the known-answer checks
"""

import argparse
import itertools
from collections import Counter

import numpy as np


# --------------------------------------------------------------------------- #
# Tabulators (minimal, fast — built for millions of calls).                    #
# --------------------------------------------------------------------------- #
def star_winner(scores):
    """scores: (V, C) int array of 0..5. Returns winning candidate index."""
    totals = scores.sum(axis=0)
    # finalists = two highest totals; tie -> lower index.
    order = sorted(range(len(totals)), key=lambda c: (-int(totals[c]), c))
    a, b = order[0], order[1]
    col_a = scores[:, a]
    col_b = scores[:, b]
    pa = int((col_a > col_b).sum())
    pb = int((col_b > col_a).sum())
    if pa > pb:
        return a
    if pb > pa:
        return b
    return a  # runoff tie -> higher-total finalist (a, by construction)


def irv_winner(rankings, C):
    """rankings: list of full candidate orderings (best first). Returns winner."""
    remaining = set(range(C))
    while len(remaining) > 1:
        counts = Counter()
        for r in rankings:
            for c in r:
                if c in remaining:
                    counts[c] += 1
                    break
        total = sum(counts.values())
        top = max(remaining, key=lambda c: (counts.get(c, 0), -c))
        if total and counts.get(top, 0) * 2 > total:
            return top
        # eliminate fewest first-choices; tie -> lower index.
        low = min(remaining, key=lambda c: (counts.get(c, 0), c))
        remaining.discard(low)
    return next(iter(remaining))


# --------------------------------------------------------------------------- #
# Sincere ballots from utilities.                                             #
# --------------------------------------------------------------------------- #
def honest_scores(U):
    """U: (V, C) float utilities -> (V, C) int STAR scores in 0..5."""
    mn = U.min(axis=1, keepdims=True)
    mx = U.max(axis=1, keepdims=True)
    rng = np.where(mx > mn, mx - mn, 1.0)
    s = np.rint((U - mn) / rng * 5).astype(int)
    return np.clip(s, 0, 5)


def honest_rankings(U):
    """U: (V, C) -> list of sincere full rankings (best first; ties by index)."""
    V = U.shape[0]
    return [list(np.argsort(-U[v], kind="stable")) for v in range(V)]


# --------------------------------------------------------------------------- #
# Electorate models.                                                          #
# --------------------------------------------------------------------------- #
def sample_utilities(rng, V, C, model, dims):
    if model == "spatial":
        vp = rng.normal(size=(V, dims))
        cp = rng.normal(size=(C, dims))
        d = np.linalg.norm(vp[:, None, :] - cp[None, :, :], axis=2)
        return -d
    if model == "impartial":
        return rng.random((V, C))
    raise ValueError(f"unknown model: {model}")


# --------------------------------------------------------------------------- #
# FBC test + works:backfires accumulation, per election.                      #
# --------------------------------------------------------------------------- #
def analyze_star(U):
    """Exhaustive favorite-betrayal best-response, done with incremental totals so
    the inner loop is pure-Python int math (no per-ballot numpy call)."""
    V, C = U.shape
    S = honest_scores(U)
    W = star_winner(S)

    Slist = S.tolist()
    Ulist = U.tolist()
    totals_all = [int(S[:, c].sum()) for c in range(C)]
    # P[a][b] = # voters scoring a strictly above b (sincere electorate).
    P = [[0] * C for _ in range(C)]
    for a in range(C):
        for b in range(C):
            if a != b:
                P[a][b] = int((S[:, a] > S[:, b]).sum())

    clean = True
    help_ = hurt = 0
    cand_ballots = list(itertools.product(range(6), repeat=C))
    for v in range(V):
        srow = Slist[v]
        uv = Ulist[v]
        f = max(range(C), key=lambda c: uv[c])
        uW = uv[W]
        # totals / pairwise counts for everyone EXCEPT voter v.
        tot_oth = [totals_all[c] - srow[c] for c in range(C)]
        P_oth = [[P[a][b] - (1 if srow[a] > srow[b] else 0) for b in range(C)]
                 for a in range(C)]
        for ballot in cand_ballots:
            bf = ballot[f]
            if not any(ballot[c] > bf for c in range(C) if c != f):
                continue  # favorite still (co-)top -> not a betrayal
            nt = [tot_oth[c] + ballot[c] for c in range(C)]
            order = sorted(range(C), key=lambda c: (-nt[c], c))
            a, b = order[0], order[1]
            pa = P_oth[a][b] + (1 if ballot[a] > ballot[b] else 0)
            pb = P_oth[b][a] + (1 if ballot[b] > ballot[a] else 0)
            Wp = a if pa >= pb else b   # runoff tie -> higher-total finalist (a)
            uWp = uv[Wp]
            if uWp > uW:
                help_ += 1
                clean = False
            elif uWp < uW:
                hurt += 1
    return clean, help_, hurt


def analyze_irv(U):
    V, C = U.shape
    R = honest_rankings(U)
    W = irv_winner(R, C)
    clean = True
    help_ = hurt = 0
    perms = list(itertools.permutations(range(C)))
    for v in range(V):
        f = int(np.argmax(U[v]))
        uW = U[v, W]
        sincere = R[v]
        for p in perms:
            if p[0] == f:           # favorite still first -> not a betrayal
                continue
            R[v] = list(p)
            Wp = irv_winner(R, C)
            uWp = U[v, Wp]
            if uWp > uW:
                help_ += 1
                clean = False
            elif uWp < uW:
                hurt += 1
        R[v] = sincere
    return clean, help_, hurt


# --------------------------------------------------------------------------- #
# Driver.                                                                      #
# --------------------------------------------------------------------------- #
def run_model(rng, model, elections, V, C, dims):
    res = {
        "star": {"clean": 0, "help": 0, "hurt": 0},
        "irv": {"clean": 0, "help": 0, "hurt": 0},
    }
    for _ in range(elections):
        U = sample_utilities(rng, V, C, model, dims)
        c_s, h_s, x_s = analyze_star(U)
        c_i, h_i, x_i = analyze_irv(U)
        res["star"]["clean"] += c_s
        res["star"]["help"] += h_s
        res["star"]["hurt"] += x_s
        res["irv"]["clean"] += c_i
        res["irv"]["help"] += h_i
        res["irv"]["hurt"] += x_i
    return res


def fmt_ratio(help_, hurt):
    if hurt == 0:
        return f"{help_}:0 (no backfires)"
    return f"{help_/hurt:.2f} : 1  ({help_} help / {hurt} hurt)"


def report(model, res, elections):
    print(f"\n=== model: {model}   ({elections} elections) ===")
    print(f"{'method':<10}{'FBC-compliant elections':<28}{'betrayal works:backfires'}")
    for m, label in (("star", "STAR"), ("irv", "RCV-IRV")):
        d = res[m]
        pct = 100.0 * d["clean"] / elections
        print(f"{label:<10}{d['clean']}/{elections} = {pct:5.1f}%        "
              f"   {fmt_ratio(d['help'], d['hurt'])}")


# --------------------------------------------------------------------------- #
# Known-answer self-tests (verification step).                                #
# --------------------------------------------------------------------------- #
def selftest():
    ok = True

    # STAR: clear score winner who also wins runoff.
    s = np.array([[5, 2, 0],
                  [5, 1, 0],
                  [4, 0, 1],
                  [0, 5, 3]])
    w = star_winner(s)
    ok &= (w == 0)
    print(f"[selftest] STAR clear winner -> {w} (expect 0) {'OK' if w == 0 else 'FAIL'}")

    # Center-squeeze: IRV eliminates the center, STAR elects it.
    # 3 candidates: 0=Left, 1=Center, 2=Right.
    #   40 voters Left > Center > Right
    #   35 voters Right > Center > Left
    #   25 voters Center > (Left=Right)
    rankings = ([[0, 1, 2]] * 40) + ([[2, 1, 0]] * 35) + ([[1, 0, 2]] * 25)
    iw = irv_winner(rankings, 3)
    ok &= (iw != 1)  # IRV squeezes the center out
    print(f"[selftest] IRV center-squeeze -> winner {iw} (expect NOT 1 / not Center) "
          f"{'OK' if iw != 1 else 'FAIL'}")

    # Same electorate as STAR scores: Center reaches runoff on broad support & wins.
    scores = (([[5, 4, 0]] * 40) + ([[0, 4, 5]] * 35) + ([[0, 5, 0]] * 25))
    sw = star_winner(np.array(scores))
    ok &= (sw == 1)
    print(f"[selftest] STAR center-squeeze -> winner {sw} (expect 1 / Center) "
          f"{'OK' if sw == 1 else 'FAIL'}")

    print(f"[selftest] {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--elections", type=int, default=1500)
    ap.add_argument("--voters", type=int, default=15)
    ap.add_argument("--candidates", type=int, default=3)
    ap.add_argument("--dims", type=int, default=2, help="issue-space dimensions (spatial)")
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--models", nargs="+", default=["spatial", "impartial"],
                    choices=["spatial", "impartial"])
    ap.add_argument("--selftest", action="store_true", help="run known-answer checks only")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(0 if selftest() else 1)

    print("Favorite-Betrayal simulation")
    print(f"  candidates={args.candidates}  voters={args.voters}  "
          f"elections/model={args.elections}  dims={args.dims}  seed={args.seed}")
    print("  FBC-compliant = NO voter has a profitable favorite-betrayal ballot "
          "(exhaustive best-response).")
    if not selftest():
        raise SystemExit("self-tests failed; aborting.")

    for model in args.models:
        rng = np.random.default_rng(args.seed)  # same seed per model -> comparable
        res = run_model(rng, model, args.elections, args.voters,
                        args.candidates, args.dims)
        report(model, res, args.elections)

    print("\nReminder: the FBC % is model-dependent. Report the model alongside the "
          "number, or it is meaningless.")


if __name__ == "__main__":
    main()
