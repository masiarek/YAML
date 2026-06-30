#!/usr/bin/env python3
"""
random_star_divergence.py
=========================
Generate RANDOM single-winner STAR elections and flag any where another voting
method disagrees with STAR. Defaults: 6 candidates, 5 ballots, scores 0-5.

For each random election it tabulates — using the SAME engine the repo ships —
    STAR  vs  RCV-IRV (Hare)  vs  Ranked Robin (RCV-RR/Copeland)
              vs  Approval  vs  Choose-One (Plurality)  vs  Condorcet
and, whenever at least one of those differs from the STAR winner, writes the
ballots + every winner to a CSV so the case is reproducible.

Usage:
    python3 random_star_divergence.py [--candidates 6] [--ballots 5]
        [--trials 1000] [--seed 0] [--out <path>] [--max-rows N] [--examples 3]

Note: RCV-IRV ties are broken nondeterministically by pyrankvote on a *perfect*
tie; this script samples IRV a few times and flags `irv_fragile` when it wobbles,
resolving it by candidate (priority) order so the CSV is reproducible.
"""
import argparse
import csv
import os
import random
import sys
import tempfile
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))
import starvote                       # noqa: E402
import starvote_larry_hastings as w   # noqa: E402


def star_winner(ballots, tb):
    res = starvote.election(starvote.star, ballots, seats=1, maximum_score=5,
                            tiebreaker=tb, verbosity=1, print=lambda *a, **k: None)
    winners = res if isinstance(res, (list, tuple)) else [res]
    return str(winners[0]) if winners else None


def irv_winner(candidates, ballots, order, samples=7):
    """Sample IRV; return (winner, fragile). Perfect ties resolved by priority."""
    seen = []
    for _ in range(samples):
        irv, _, _ = w.compute_irv_winner(candidates, ballots, order)
        seen.append(irv)
    uniq = list(dict.fromkeys(seen))
    if len(uniq) == 1:
        return uniq[0], False
    rep = next((c for c in order if c in uniq), uniq[0])
    return rep, True


def plurality_winner(candidates, ballots, order):
    fc, _ = w.first_choice_counts(candidates, ballots, order)
    if not any(v > 0 for v in fc.values()):
        return None
    rank = {c: i for i, c in enumerate(order)}
    return min(candidates, key=lambda c: (-fc[c], rank[c]))


def tabulate_all(candidates, ballots, tb):
    order = list(candidates)
    star = star_winner(ballots, tb)
    irv, fragile = irv_winner(candidates, ballots, order)
    rr = w.copeland_winner(candidates, ballots, order)
    appr = w.approval_winner(candidates, ballots, order)
    plur = plurality_winner(candidates, ballots, order)
    cond = w.condorcet_winner(candidates, ballots)
    methods = {"RCV-IRV": irv, "RankedRobin": rr, "Approval": appr,
               "Plurality": plur, "Condorcet": cond}
    differ = [m for m, win in methods.items()
              if win is not None and win != star]
    return star, methods, differ, fragile


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", type=int, default=6)
    ap.add_argument("--ballots", type=int, default=5)
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--max-rows", type=int, default=500,
                    help="cap divergent rows written to the CSV")
    ap.add_argument("--examples", type=int, default=3,
                    help="how many divergent elections to print in detail")
    ap.add_argument("--out", default=None,
                    help="CSV path (default: a temp file)")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    candidates = [chr(ord("A") + i) for i in range(args.candidates)]
    tb = w.LotNumberTiebreaker(lot_numbers=[], silent=True)
    out = args.out or os.path.join(
        tempfile.gettempdir(),
        f"star_divergence_c{args.candidates}_b{args.ballots}.csv")

    cols = (["trial", "STAR", "RCV-IRV", "RankedRobin", "Approval",
             "Plurality", "Condorcet", "differ_from_STAR", "irv_fragile"]
            + [f"ballot{i+1}({''.join(candidates)})" for i in range(args.ballots)])

    n_div = 0
    per_method = {m: 0 for m in ["RCV-IRV", "RankedRobin", "Approval",
                                 "Plurality", "Condorcet"]}
    examples = []
    rows = []
    for t in range(args.trials):
        ballots = [{c: rng.randint(0, 5) for c in candidates}
                   for _ in range(args.ballots)]
        star, methods, differ, fragile = tabulate_all(candidates, ballots, tb)
        if not differ:
            continue
        n_div += 1
        for m in differ:
            per_method[m] += 1
        if len(rows) < args.max_rows:
            enc = [",".join(str(b[c]) for c in candidates) for b in ballots]
            rows.append([t, star, methods["RCV-IRV"], methods["RankedRobin"],
                         methods["Approval"], methods["Plurality"],
                         methods["Condorcet"], "|".join(differ),
                         "yes" if fragile else "", *enc])
        if len(examples) < args.examples:
            examples.append((t, ballots, star, methods, differ, fragile))

    with open(out, "w", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow(cols)
        wr.writerows(rows)

    # ---- report ----
    print(f"Swept {args.trials} random elections "
          f"({args.candidates} candidates, {args.ballots} ballots, scores 0-5, "
          f"seed {args.seed}).")
    pct = 100 * n_div / args.trials if args.trials else 0
    print(f"Divergent (some method != STAR): {n_div} ({pct:.0f}%).")
    print("How often each method disagreed with STAR:")
    for m, n in sorted(per_method.items(), key=lambda kv: -kv[1]):
        print(f"   {m:<12} {n:>5} ({100*n/args.trials:.0f}%)")
    print(f"\nWrote {min(len(rows), args.max_rows)} divergent cases -> {out}")

    for t, ballots, star, methods, differ, fragile in examples:
        print(f"\n=== Example (trial {t}) — STAR winner: {star} ===")
        print("  Ballots (scores 0-5):  " + "  ".join(candidates))
        for i, b in enumerate(ballots, 1):
            print(f"    #{i}: " + " ".join(f"{b[c]}" for c in candidates))
        for m, win in methods.items():
            tag = "  <-- differs from STAR" if (win is not None and win != star) else ""
            extra = " (fragile IRV tie)" if (m == "RCV-IRV" and fragile) else ""
            print(f"    {m:<12} = {win}{tag}{extra}")


if __name__ == "__main__":
    main()
