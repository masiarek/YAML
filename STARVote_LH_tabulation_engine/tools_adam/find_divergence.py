#!/usr/bin/env python3
"""
find_divergence.py
==================
Generate random score ballots and search for a profile where **Bloc STAR**
(majoritarian) and a **proportional STAR** method elect a different SET of
winners.

Why these methods can disagree
------------------------------
Bloc STAR just runs STAR once per seat with no reweighting, so a cohesive
majority can sweep every seat. The proportional methods reweight or "spend"
ballots after each seat is filled, so a cohesive minority can earn a seat.
That structural difference is exactly what this script hunts for.

Proportional methods available (pass with --method):
    allocated   Allocated Score Voting  -- the OFFICIAL "Proportional STAR"
                method endorsed on starvoting.org / electowiki. Good default.
    sss         Sequentially Spent Score -- a newer proportional-score method
                with nice monotonicity behaviour; a strong modern alternative.
    rrv         Reweighted Range Voting  -- older, score-based PR. NOT part of
                STAR's score-then-runoff family and has weaker proportionality
                guarantees, but included for comparison.
    all         Stop at the first profile that beats ANY of the three, and
                report which method disagreed.

Recommendation: if you just want one "the best" proportional STAR method to
compare against, use the default `allocated` (Allocated Score). It is the
canonical Proportional STAR method.

Tie handling / robustness
--------------------------
With very few ballots, ties are common and an apparent "divergence" can be an
artifact of how ties are broken. By default (--robust) every candidate profile
is re-tabulated under several independent tiebreaker seeds, and is accepted
ONLY if BOTH methods give a stable, tie-free result and those results differ.
That guarantees the disagreement is a genuine method difference, not noise.

Examples
--------
    # default: 4 candidates, 2 seats, auto-find the minimal ballot count
    python find_divergence.py

    # fixed 50 ballots, 5 candidates, 3 seats, compare vs SSS, write YAML
    python find_divergence.py -c 5 -s 3 -b 50 -m sss --yaml out.yaml

    # reproducible, compare against any proportional method
    python find_divergence.py --seed 1234 -m all
"""

import argparse
import functools
import random
import sys
from pathlib import Path


# --------------------------------------------------------------------------- #
# Make `starvote` importable even when this file lives outside the engine repo.
# --------------------------------------------------------------------------- #
def _bootstrap_starvote():
    try:
        import starvote  # noqa: F401

        return
    except ImportError:
        pass
    # Walk up from CWD and from this file looking for the engine package.
    seeds = [Path.cwd(), Path(__file__).resolve().parent]
    for base in seeds:
        for p in [base, *base.parents]:
            for cand in (p, p / "STARVote_LH_tabulation_engine"):
                if (cand / "starvote" / "__init__.py").exists():
                    sys.path.insert(0, str(cand))
                    return
    sys.exit(
        "ERROR: could not import `starvote`. Run this from inside the\n"
        "STARVote_LH_tabulation_engine/ directory, or add it to PYTHONPATH."
    )


_bootstrap_starvote()
import starvote  # noqa: E402


PROP_METHODS = {
    "allocated": ("Allocated Score Voting", starvote.Allocated_Score_Voting),
    "sss": ("Sequentially Spent Score", starvote.Sequentially_Spent_Score),
    "rrv": ("Reweighted Range Voting", starvote.Reweighted_Range_Voting),
}
BLOC = ("Bloc STAR Voting", starvote.Bloc_STAR_Voting)


def candidate_names(n):
    """A, B, ... Z, AA, AB, ... for arbitrary n."""
    names = []
    for i in range(n):
        s, x = "", i
        while True:
            s = chr(ord("A") + x % 26) + s
            x = x // 26 - 1
            if x < 0:
                break
        names.append(s)
    return names


def _tiebreaker(seed):
    return functools.partial(
        starvote.on_demand_random_tiebreaker, random=random.Random(seed)
    )


def winners(method_fn, ballots, seats, max_score, tb_seed=0):
    """Return frozenset of winners, or None if the election can't resolve."""
    try:
        w = starvote.election(
            method_fn,
            ballots,
            seats=seats,
            maximum_score=max_score,
            tiebreaker=_tiebreaker(tb_seed),
        )
        return frozenset(w)
    except starvote.UnbreakableTieError, starvote.ElectionError:
        return None


def stable_winners(method_fn, ballots, seats, max_score, tb_seeds):
    """
    Tabulate under several tiebreaker seeds. Return the winner set if it is
    identical (i.e. tie-free / robust) across all seeds, else None.
    """
    result = None
    for s in tb_seeds:
        w = winners(method_fn, ballots, seats, max_score, tb_seed=s)
        if w is None:
            return None
        if result is None:
            result = w
        elif w != result:
            return None  # outcome depends on tiebreak -> not robust
    return result


def random_ballots(rng, names, n_ballots, max_score):
    return [{c: rng.randint(0, max_score) for c in names} for _ in range(n_ballots)]


def search_at_count(rng, names, seats, n_ballots, max_score, prop_keys, trials, robust):
    """
    Try up to `trials` random profiles with exactly `n_ballots` ballots.
    Return a result dict on the first qualifying divergence, else None.
    """
    tb_seeds = (101, 202, 303, 404, 505) if robust else (0,)
    for t in range(trials):
        ballots = random_ballots(rng, names, n_ballots, max_score)

        bloc_set = stable_winners(BLOC[1], ballots, seats, max_score, tb_seeds)
        if bloc_set is None:
            continue  # bloc itself tie-dependent; skip for a clean example

        for key in prop_keys:
            label, fn = PROP_METHODS[key]
            prop_set = stable_winners(fn, ballots, seats, max_score, tb_seeds)
            if prop_set is None or prop_set == bloc_set:
                continue
            return {
                "trial": t,
                "n_ballots": n_ballots,
                "ballots": ballots,
                "bloc_winners": bloc_set,
                "prop_key": key,
                "prop_label": label,
                "prop_winners": prop_set,
            }
    return None


def find(
    names, seats, n_ballots, max_score, prop_keys, trials, robust, max_ballots, seed
):
    """
    If n_ballots is given, search at that count. Otherwise escalate from a
    small count upward and return the smallest count that yields a divergence.
    """
    rng = random.Random(seed)
    if n_ballots is not None:
        res = search_at_count(
            rng, names, seats, n_ballots, max_score, prop_keys, trials, robust
        )
        if res:
            res["minimal"] = False
        return res

    start = max(2, seats + 1)
    for n in range(start, max_ballots + 1):
        res = search_at_count(
            rng, names, seats, n, max_score, prop_keys, trials, robust
        )
        if res:
            res["minimal"] = True
            return res
    return None


# --------------------------------------------------------------------------- #
# Output helpers
# --------------------------------------------------------------------------- #
def ballot_table(ballots, names):
    rows = [",".join(names)]
    for b in ballots:
        rows.append(",".join(str(b[c]) for c in names))
    return rows


def print_result(res, names, seats, max_score, prop_choice):
    b = res["ballots"]
    totals = {c: sum(x[c] for x in b) for c in names}
    print("=" * 64)
    if res.get("minimal"):
        print(f"DIVERGENCE FOUND  (minimal ballot count = {res['n_ballots']})")
    else:
        print(f"DIVERGENCE FOUND  ({res['n_ballots']} ballots)")
    print("=" * 64)
    print(f"candidates : {names}")
    print(f"seats      : {seats}    max score : {max_score}")
    print(f"found at   : trial #{res['trial']}")
    print()
    print("Ballots:")
    for line in ballot_table(b, names):
        print("   " + line)
    print()
    print(f"Score totals: {totals}")
    print()
    print(f"  {BLOC[0]:26s} -> {sorted(res['bloc_winners'])}")
    print(f"  {res['prop_label']:26s} -> {sorted(res['prop_winners'])}")
    print("=" * 64)


def write_yaml(path, res, names, seats):
    b = res["ballots"]
    totals = {c: sum(x[c] for x in b) for c in names}
    lines = [
        "# Auto-generated by find_divergence.py",
        f"# Same ballots, {seats} seats -> different winners:",
        f"#   bloc            (Bloc STAR)          -> {sorted(res['bloc_winners'])}",
        f"#   {res['prop_key']:<15s} ({res['prop_label']}) -> {sorted(res['prop_winners'])}",
        f"# Score totals: {totals}",
        f"num_winners: {seats}",
        "voting_method: bloc",
        "ballots: |-",
    ]
    for line in ballot_table(b, names):
        lines.append("  " + line)
    Path(path).write_text("\n".join(lines) + "\n")
    print(f"\nWrote YAML to {path}")


# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Find random ballots where Bloc STAR and a proportional "
        "STAR method elect different winners.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument(
        "-c",
        "--candidates",
        type=int,
        default=4,
        help="number of candidates (named A, B, C, ...)",
    )
    ap.add_argument("-s", "--seats", type=int, default=2, help="number of winners")
    ap.add_argument(
        "-b",
        "--ballots",
        type=int,
        default=None,
        help="number of ballots; omit to auto-find the minimal count",
    )
    ap.add_argument(
        "-m",
        "--method",
        default="allocated",
        choices=[*PROP_METHODS.keys(), "all"],
        help="proportional method to compare against (or 'all')",
    )
    ap.add_argument(
        "--max-score", type=int, default=5, help="maximum ballot score (0..max)"
    )
    ap.add_argument(
        "-t",
        "--trials",
        type=int,
        default=20000,
        help="random profiles to try per ballot count",
    )
    ap.add_argument(
        "--max-ballots",
        type=int,
        default=60,
        help="upper bound when auto-finding the minimal count",
    )
    ap.add_argument(
        "--seed", type=int, default=None, help="RNG seed for reproducible searches"
    )
    ap.add_argument(
        "--robust",
        dest="robust",
        action="store_true",
        default=True,
        help="require the divergence to be tie-free (default on)",
    )
    ap.add_argument(
        "--no-robust",
        dest="robust",
        action="store_false",
        help="accept divergences even if they depend on tiebreaking",
    )
    ap.add_argument(
        "--yaml",
        metavar="PATH",
        default=None,
        help="write the found profile to a YAML file",
    )
    args = ap.parse_args(argv)

    if args.candidates <= args.seats:
        ap.error("need more candidates than seats for a meaningful race")

    names = candidate_names(args.candidates)
    prop_keys = list(PROP_METHODS) if args.method == "all" else [args.method]

    res = find(
        names=names,
        seats=args.seats,
        n_ballots=args.ballots,
        max_score=args.max_score,
        prop_keys=prop_keys,
        trials=args.trials,
        robust=args.robust,
        max_ballots=args.max_ballots,
        seed=args.seed,
    )

    if res is None:
        scope = (
            f"{args.ballots} ballots"
            if args.ballots
            else f"up to {args.max_ballots} ballots"
        )
        print(
            f"No divergence found ({scope}, {args.trials} trials each). "
            "Try more trials, more ballots, or --no-robust."
        )
        return 1

    print_result(res, names, args.seats, args.max_score, args.method)
    if args.yaml:
        write_yaml(args.yaml, res, names, args.seats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
