"""
find_four_way_divergence.py

Long-running search for elections where STAR, RCV-IRV, Approval, and Condorcet
all elect DIFFERENT winners (a "four-way divergence"), and more generally for
the maximum number of distinct winners these four methods can produce.

Designed to be left running overnight: it sweeps configurations in increasing
size (candidates, then ballots), enumerates exhaustively when the space is
small enough and otherwise samples randomly within a per-config time budget,
and appends any hit to a results file immediately (so a Ctrl-C never loses
progress).

GENUINE / STRICT BALLOTS ONLY: every ballot's non-zero scores must be distinct,
so the score->rank conversion is unambiguous; profiles where STAR or IRV would
need an arbitrary tiebreak to pick a winner are skipped. This means every hit
is a real method disagreement, not a tie-breaking artifact.

Fast direct winner functions are used for speed; run with --validate first to
confirm they match the real starvote / pyrankvote engines.

Usage:
    python find_four_way_divergence.py --validate         # sanity-check engines
    python find_four_way_divergence.py                    # overnight sweep
    python find_four_way_divergence.py --max-cands 8 --max-ballots 31
"""

import argparse
import csv
import itertools
import os
import random
import sys
import time
from datetime import datetime

# --- defaults (override on the command line) ---
SCORES = [0, 1, 2, 3, 4, 5]
EXHAUSTIVE_CAP = 8_000_000     # enumerate fully below this many profiles, else sample
PER_CONFIG_SECONDS = 120       # time budget per (C, B) when sampling
TARGET_DISTINCT = 4            # stop early if we hit this many distinct winners
HITS_FILE = "four_way_hits.csv"
LOG_FILE = "four_way_log.txt"


# --------------------------------------------------------------------------- #
# Ballot helpers
# --------------------------------------------------------------------------- #
def is_strict(b):
    nz = [s for s in b if s > 0]
    return len(nz) == len(set(nz))


def totals_of(cands, ballots):
    t = {c: 0 for c in cands}
    for b in ballots:
        for c in cands:
            t[c] += b[c]
    return t


# --------------------------------------------------------------------------- #
# Fast winner functions (return None when an arbitrary tiebreak would be needed)
# --------------------------------------------------------------------------- #
def star_winner(cands, ballots, totals):
    order = sorted(cands, key=lambda c: -totals[c])
    a = order[0]
    # Top must be unique (else who is finalist #1 is ambiguous).
    if totals[order[0]] == totals[order[1]] and len(cands) > 1:
        # a tie at the very top: both could be finalists only if exactly 2 tie
        # AND no third ties; otherwise ambiguous.
        top = totals[order[0]]
        tied_top = [c for c in cands if totals[c] == top]
        if len(tied_top) != 2:
            return None
        a, b = tied_top  # both advance
    else:
        b = order[1]
        # 2nd/3rd boundary tie -> resolve by head-to-head, else ambiguous.
        if len(order) > 2 and totals[order[1]] == totals[order[2]]:
            tied = [c for c in order[1:] if totals[c] == totals[order[1]]]
            if len(tied) != 2:
                return None
            x, y = tied
            hx = sum(1 for bal in ballots if bal[x] > bal[y])
            hy = sum(1 for bal in ballots if bal[y] > bal[x])
            if hx > hy:
                b = x
            elif hy > hx:
                b = y
            else:
                return None
    v1 = sum(1 for bal in ballots if bal[a] > bal[b])
    v2 = sum(1 for bal in ballots if bal[b] > bal[a])
    if v1 > v2:
        return a
    if v2 > v1:
        return b
    return None


def irv_winner(cands, ballots):
    active = list(cands)
    while len(active) > 1:
        counts = {c: 0 for c in active}
        continuing = 0
        for b in ballots:
            ranked = [c for c in active if b[c] > 0]
            if not ranked:
                continue
            counts[max(ranked, key=lambda c: b[c])] += 1  # strict -> unique
            continuing += 1
        best = max(active, key=lambda c: counts[c])
        if counts[best] * 2 > continuing:
            return best
        low = min(counts[c] for c in active)
        losers = [c for c in active if counts[c] == low]
        if len(losers) > 1:
            return None  # elimination tie -> ambiguous
        active.remove(losers[0])
    return active[0] if active else None


def approval_winner(cands, ballots, totals_unused=None):
    appr = {c: sum(1 for b in ballots if b[c] >= 3) for c in cands}
    top = max(appr.values())
    tied = [c for c in cands if appr[c] == top]
    return tied[0] if len(tied) == 1 else None  # require a clean single winner


def condorcet_winner(cands, ballots):
    for c in cands:
        ok = True
        for o in cands:
            if c == o:
                continue
            fc = sum(1 for b in ballots if b[c] > b[o])
            ac = sum(1 for b in ballots if b[o] > b[c])
            if not (fc > ac):
                ok = False
                break
        if ok:
            return c
    return None


def four_winners(cands, ballots):
    """
    FAST PRE-FILTER. Return (star, irv, approval, condorcet) or None if any is
    ambiguous. The fast IRV is standard single-elimination and may disagree with
    pyrankvote in rare near-tie cases, so any promising result is re-checked by
    verify_with_engine() before it is logged as a hit.
    """
    totals = totals_of(cands, ballots)
    sw = star_winner(cands, ballots, totals)
    if sw is None:
        return None
    iw = irv_winner(cands, ballots)
    if iw is None:
        return None
    aw = approval_winner(cands, ballots)
    if aw is None:
        return None
    cw = condorcet_winner(cands, ballots)
    if cw is None:
        return None
    return sw, iw, aw, cw


# Lazily-initialised engine handles (the real STAR + RCV-IRV used by the
# tabulation block), so logged hits are guaranteed to reproduce there.
_ENGINE = {}


def _init_engine():
    if _ENGINE:
        return
    import io
    import contextlib
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here + "/..")
    sys.path.insert(0, here + "/../../RCV_IRV_tabulation_engine")
    import starvote
    from starvote import Tiebreaker
    from starvote_larry_hastings import (
        compute_irv_winner, approval_winner as eng_approval,
        condorcet_winner as eng_condorcet,
    )

    class TB(Tiebreaker):
        def __call__(self, options, tie, desired, exception):
            return sorted(list(tie))[:desired]

    def eng_star(cands, ballots):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            w = starvote.election(method=starvote.star, ballots=ballots, seats=1,
                                  tiebreaker=TB(), verbosity=0, maximum_score=5)
        return w[0] if isinstance(w, list) else w

    _ENGINE.update(star=eng_star, irv=compute_irv_winner,
                   approval=eng_approval, condorcet=eng_condorcet)


def verify_with_engine(cands, ballots):
    """
    Re-tabulate with the real engine (matching the tabulation block exactly).
    Returns (star, irv, approval, condorcet) or None if anything is undefined.
    """
    _init_engine()
    sw = _ENGINE["star"](cands, ballots)
    iw, _, _ = _ENGINE["irv"](cands, ballots, cands)  # priority = column order
    aw = _ENGINE["approval"](cands, ballots, cands)
    cw = _ENGINE["condorcet"](cands, ballots)
    if None in (sw, iw, aw, cw):
        return None
    return sw, iw, aw, cw


# --------------------------------------------------------------------------- #
# Validation against the real engines
# --------------------------------------------------------------------------- #
def validate():
    import io
    import contextlib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../../RCV_IRV_tabulation_engine")
    import starvote
    from starvote import Tiebreaker
    import pyrankvote
    from pyrankvote import Ballot, Candidate

    class TB(Tiebreaker):
        def __call__(self, options, tie, desired, exception):
            return sorted(list(tie))[:desired]

    def eng_star(cands, ballots):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            w = starvote.election(method=starvote.star, ballots=ballots, seats=1,
                                  tiebreaker=TB(), verbosity=0, maximum_score=5)
        return w[0] if isinstance(w, list) else w

    def eng_irv(cands, ballots):
        objs = {c: Candidate(c) for c in cands}
        pv = []
        for b in ballots:
            r = sorted([c for c in cands if b[c] > 0], key=lambda c: -b[c])
            pv.append(Ballot([objs[c] for c in r]))
        res = pyrankvote.instant_runoff_voting(list(objs.values()), pv)
        w = res.get_winners()
        return w[0].name if w else None

    random.seed(0)
    ms = mi = checked = 0
    for C in (4, 5, 6):
        cands = [chr(65 + i) for i in range(C)]
        for _ in range(2000):
            nb = random.randint(C, 15)
            ballots = []
            for _ in range(nb):
                while True:
                    b = {c: random.choice(SCORES) for c in cands}
                    if is_strict(tuple(b[c] for c in cands)):
                        break
                ballots.append(b)
            totals = totals_of(cands, ballots)
            fs = star_winner(cands, ballots, totals)
            fi = irv_winner(cands, ballots)
            if fs is not None:
                checked += 1
                if fs != eng_star(cands, ballots):
                    ms += 1
            if fi is not None:
                if fi != eng_irv(cands, ballots):
                    mi += 1
    print(f"validation: checked={checked}  STAR mismatches={ms}  IRV mismatches={mi}")
    if ms == 0 and mi == 0:
        print("OK — fast functions match the engines exactly.")
    elif ms == 0:
        print(f"STAR exact. {mi} rare fast-IRV near-tie disagreement(s) with "
              f"pyrankvote — harmless: every hit is re-verified by the real "
              f"engine before logging, so these only cost a little recall.")
    else:
        print("STAR mismatch — investigate before trusting the pre-filter.")


# --------------------------------------------------------------------------- #
# Search
# --------------------------------------------------------------------------- #
def log(msg):
    line = f"[{datetime.now():%H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def record_hit(writer, fh, C, B, ballots, cands, winners, n_distinct):
    b_str = "_".join("".join(str(b[c]) for c in cands) for b in ballots)
    sw, iw, aw, cw = winners
    writer.writerow([datetime.now().isoformat(timespec="seconds"),
                     C, B, n_distinct, sw, iw, aw, cw, b_str])
    fh.flush()


def evaluate(cands, ballots, C, B, best_seen, writer, fh):
    res = four_winners(cands, ballots)  # fast pre-filter
    if res is None:
        return 0
    n = len(set(res))
    if n > best_seen[0]:
        best_seen[0] = n
        log(f"  C={C} B={B}: new best (fast) = {n} distinct "
            f"(STAR={res[0]} IRV={res[1]} Approval={res[2]} Condorcet={res[3]})")
    if n >= TARGET_DISTINCT:
        # Confirm with the real engine before trusting/logging.
        ver = verify_with_engine(cands, ballots)
        if ver is not None and len(set(ver)) >= TARGET_DISTINCT:
            log(f"  *** VERIFIED {len(set(ver))}-way: C={C} B={B} "
                f"STAR={ver[0]} IRV={ver[1]} Approval={ver[2]} Condorcet={ver[3]}")
            record_hit(writer, fh, C, B, ballots, cands, ver, len(set(ver)))
            return len(set(ver))
        return 0  # fast pre-filter false positive; keep searching
    return n


def search(max_cands, max_ballots):
    log(f"START sweep: cands 4..{max_cands}, ballots up to {max_ballots}, "
        f"scores={SCORES}, target={TARGET_DISTINCT} distinct")
    hits_exist = os.path.exists(HITS_FILE)
    fh = open(HITS_FILE, "a", newline="", encoding="utf-8")
    writer = csv.writer(fh, lineterminator="\n")  # LF, not csv's default CRLF
    if not hits_exist:
        writer.writerow(["found_at", "candidates", "ballots", "n_distinct",
                         "STAR", "RCV_IRV", "Approval", "Condorcet", "ballots_ABC"])
        fh.flush()

    best_seen = [0]
    try:
        for C in range(4, max_cands + 1):
            cands = [chr(65 + i) for i in range(C)]
            strict_menu = [b for b in itertools.product(SCORES, repeat=C)
                           if is_strict(b)]
            for B in range(C, max_ballots + 1):
                # number of strict profiles = C(len(menu)+B-1, B)
                import math
                n_profiles = math.comb(len(strict_menu) + B - 1, B)
                if n_profiles <= EXHAUSTIVE_CAP:
                    log(f"C={C} B={B}: EXHAUSTIVE over {n_profiles:,} profiles "
                        f"(menu={len(strict_menu)})")
                    found_target = False
                    for combo in itertools.combinations_with_replacement(strict_menu, B):
                        ballots = [{cands[i]: v for i, v in enumerate(t)} for t in combo]
                        if evaluate(cands, ballots, C, B, best_seen, writer, fh) >= TARGET_DISTINCT:
                            found_target = True
                    if found_target:
                        log(f"C={C} B={B}: TARGET reached — see {HITS_FILE}")
                else:
                    log(f"C={C} B={B}: SAMPLING {PER_CONFIG_SECONDS}s "
                        f"({n_profiles:,} profiles too many to enumerate)")
                    t0 = time.time()
                    tries = 0
                    while time.time() - t0 < PER_CONFIG_SECONDS:
                        tries += 1
                        ballots = []
                        for _ in range(B):
                            while True:
                                t = tuple(random.choice(SCORES) for _ in range(C))
                                if is_strict(t):
                                    break
                            ballots.append({cands[i]: v for i, v in enumerate(t)})
                        if evaluate(cands, ballots, C, B, best_seen, writer, fh) >= TARGET_DISTINCT:
                            log(f"C={C} B={B}: TARGET hit after {tries:,} samples")
                            break
    except KeyboardInterrupt:
        log("interrupted by user — progress saved.")
    finally:
        fh.close()
    log(f"DONE. Best distinct-winner count seen: {best_seen[0]}. Hits in {HITS_FILE}")


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true",
                    help="check fast functions against starvote/pyrankvote and exit")
    ap.add_argument("--max-cands", type=int, default=7)
    ap.add_argument("--max-ballots", type=int, default=25)
    args = ap.parse_args()
    if args.validate:
        validate()
        return
    search(args.max_cands, args.max_ballots)


if __name__ == "__main__":
    main()
