"""
find_star_irv_sweep.py

Simple progressive search for elections where STAR and RCV-IRV elect DIFFERENT
winners. Grows the search by candidates, then ballots, sampling each size for a
time budget and appending verified divergences to a CSV.

Companion to find_four_way_divergence.py (which compares all four methods);
this one compares only STAR vs RCV-IRV. It reuses that script's validated fast
winner functions and real-engine verification, so every logged hit reproduces
in the tabulation block.

GENUINE / STRICT BALLOTS ONLY: each ballot's non-zero scores are distinct, so
the score-to-rank conversion is unambiguous and a divergence is a real method
difference, not a tie-breaking artifact.

Usage:
    python find_star_irv_sweep.py                         # default sweep
    python find_star_irv_sweep.py --min-cands 3 --max-cands 7 --max-ballots 31
    python find_star_irv_sweep.py --per-config 60
"""

import argparse
import csv
import itertools
import math
import os
import random
import time
from datetime import datetime

import find_four_way_divergence as base  # shared fast funcs + engine verify

SCORES = base.SCORES
EXHAUSTIVE_CAP = 5_000_000
HITS_FILE = "star_irv_hits.csv"
LOG_FILE = "star_irv_log.txt"


def log(msg):
    line = f"[{datetime.now():%H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def star_vs_irv(cands, ballots):
    """Fast pre-filter: return (star, irv) if both unambiguous and differ."""
    totals = base.totals_of(cands, ballots)
    sw = base.star_winner(cands, ballots, totals)
    if sw is None:
        return None
    iw = base.irv_winner(cands, ballots)
    if iw is None or iw == sw:
        return None
    return sw, iw


def verify(cands, ballots):
    """Confirm STAR != RCV-IRV with the real engine; return (star, irv) or None."""
    base._init_engine()
    sw = base._ENGINE["star"](cands, ballots)
    iw, _, _ = base._ENGINE["irv"](cands, ballots, cands)
    if sw is None or iw is None or sw == iw:
        return None
    return sw, iw


def record(writer, fh, C, B, cands, ballots, sw, iw):
    b_str = "_".join("".join(str(b[c]) for c in cands) for b in ballots)
    writer.writerow([datetime.now().isoformat(timespec="seconds"),
                     C, B, sw, iw, b_str])
    fh.flush()


def sweep(min_cands, max_cands, max_ballots, per_config, stop_on_first):
    log(f"START STAR-vs-RCV-IRV sweep: cands {min_cands}..{max_cands}, "
        f"ballots up to {max_ballots}, scores={SCORES}")
    new_file = not os.path.exists(HITS_FILE)
    fh = open(HITS_FILE, "a", newline="", encoding="utf-8")
    writer = csv.writer(fh, lineterminator="\n")  # LF, not csv's default CRLF
    if new_file:
        writer.writerow(["found_at", "candidates", "ballots",
                         "STAR", "RCV_IRV", "ballots_ABC"])
        fh.flush()

    try:
        for C in range(min_cands, max_cands + 1):
            cands = [chr(65 + i) for i in range(C)]
            menu = [b for b in itertools.product(SCORES, repeat=C) if base.is_strict(b)]
            for B in range(C, max_ballots + 1):
                n_profiles = math.comb(len(menu) + B - 1, B)
                hits_here = 0

                def handle(ballots):
                    nonlocal hits_here
                    pre = star_vs_irv(cands, ballots)
                    if pre is None:
                        return False
                    ver = verify(cands, ballots)
                    if ver is None:
                        return False
                    record(writer, fh, C, B, cands, ballots, ver[0], ver[1])
                    hits_here += 1
                    return True

                if n_profiles <= EXHAUSTIVE_CAP:
                    log(f"C={C} B={B}: EXHAUSTIVE over {n_profiles:,} profiles")
                    for combo in itertools.combinations_with_replacement(menu, B):
                        ballots = [{cands[i]: v for i, v in enumerate(t)}
                                   for t in combo]
                        if handle(ballots) and stop_on_first:
                            break
                else:
                    log(f"C={C} B={B}: SAMPLING {per_config}s "
                        f"({n_profiles:,} profiles)")
                    t0 = time.time()
                    while time.time() - t0 < per_config:
                        ballots = []
                        for _ in range(B):
                            while True:
                                t = tuple(random.choice(SCORES) for _ in range(C))
                                if base.is_strict(t):
                                    break
                            ballots.append({cands[i]: v for i, v in enumerate(t)})
                        if handle(ballots) and stop_on_first:
                            break

                if hits_here:
                    log(f"C={C} B={B}: {hits_here} STAR!=RCV-IRV divergence(s) "
                        f"-> {HITS_FILE}")
    except KeyboardInterrupt:
        log("interrupted by user — progress saved.")
    finally:
        fh.close()
    log(f"DONE. Hits in {HITS_FILE}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-cands", type=int, default=3)
    ap.add_argument("--max-cands", type=int, default=7)
    ap.add_argument("--max-ballots", type=int, default=25)
    ap.add_argument("--per-config", type=int, default=60,
                    help="seconds to sample each size when too large to enumerate")
    ap.add_argument("--stop-on-first", action="store_true",
                    help="move to the next size as soon as one divergence is found")
    args = ap.parse_args()
    sweep(args.min_cands, args.max_cands, args.max_ballots,
          args.per_config, args.stop_on_first)


if __name__ == "__main__":
    main()
