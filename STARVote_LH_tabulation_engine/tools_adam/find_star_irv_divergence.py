"""
find_star_irv_divergence.py

Enumerate every 3-candidate STAR election (up to NUM_BALLOTS ballots) and report
all GENUINE cases where the STAR winner and the RCV/IRV winner differ.

"Genuine" (per design decision) = STRICT BALLOTS ONLY: we only consider ballots
whose non-zero scores are all distinct, so converting scores -> ranks is
unambiguous and the divergence cannot be an artifact of score->rank
tie-breaking. (Score 0 = unranked.) Profiles where STAR or IRV would need an
arbitrary tiebreak to pick a winner are skipped as ambiguous.

Reuses the enumeration approach from sim_total_divergence3_both.py
(itertools.product menu + combinations_with_replacement), but pre-filters the
menu to strict ballot types and adds an IRV winner.

Config below; NUM_BALLOTS can also be passed on the command line:
    python find_star_irv_divergence.py 5
"""

import csv
import datetime
import itertools
import sys
from collections import Counter

# --- CONFIGURATION ---
NUM_CANDIDATES = 3
NUM_BALLOTS = 5                       # override with argv[1]
VALID_SCORES = [0, 2, 3, 4, 5]
WRITE_CSV = True
DEDUPE_BY_SYMMETRY = True            # collapse candidate-relabel duplicates
# ---------------------

CANDS = [chr(65 + i) for i in range(NUM_CANDIDATES)]  # A, B, C


# --------------------------------------------------------------------------- #
# Ballot helpers
# --------------------------------------------------------------------------- #
def is_strict(ballot_tuple):
    """True if the non-zero scores are all distinct (unambiguous ranking)."""
    nz = [s for s in ballot_tuple if s > 0]
    return len(nz) == len(set(nz))


def ranking(scores):
    """Ordered candidate list, most-preferred first, 0 = unranked. Strict input."""
    ranked = [c for c in CANDS if scores[c] > 0]
    ranked.sort(key=lambda c: -scores[c])
    return ranked


# --------------------------------------------------------------------------- #
# STAR (returns winner name, or None if an arbitrary tiebreak would be needed)
# --------------------------------------------------------------------------- #
def star_winner(ballots):
    totals = {c: 0 for c in CANDS}
    for b in ballots:
        for c in CANDS:
            totals[c] += b[c]
    order = sorted(CANDS, key=lambda c: -totals[c])
    a, b2, c3 = order
    # First two advance. Ambiguity only at the 2nd/3rd score boundary.
    if totals[b2] == totals[c3]:
        # Official rule: break by head-to-head between the tied pair.
        h2 = sum(1 for bal in ballots if bal[b2] > bal[c3])
        h3 = sum(1 for bal in ballots if bal[c3] > bal[b2])
        if h3 > h2:
            b2 = c3
        elif h3 == h2:
            return None  # unresolved -> ambiguous, skip
    # Also ambiguous if the top score is a 3-way tie (who are the finalists?).
    if totals[a] == totals[b2] == totals[c3]:
        return None
    # Runoff between finalists a and b2.
    v1 = sum(1 for bal in ballots if bal[a] > bal[b2])
    v2 = sum(1 for bal in ballots if bal[b2] > bal[a])
    if v1 > v2:
        return a
    if v2 > v1:
        return b2
    return None  # runoff tie -> ambiguous


# --------------------------------------------------------------------------- #
# IRV (returns winner name, or None on an elimination/runoff tie)
# --------------------------------------------------------------------------- #
def irv_winner(ballots):
    active = list(CANDS)
    while len(active) > 1:
        counts = {c: 0 for c in active}
        continuing = 0
        for b in ballots:
            ranked = [c for c in active if b[c] > 0]
            if not ranked:
                continue
            top = max(ranked, key=lambda c: b[c])  # strict -> unique
            counts[top] += 1
            continuing += 1
        best = max(active, key=lambda c: counts[c])
        if counts[best] * 2 > continuing:
            return best
        low = min(counts[c] for c in active)
        losers = [c for c in active if counts[c] == low]
        if len(losers) > 1:
            return None  # elimination / final tie -> ambiguous
        active.remove(losers[0])
    return active[0] if active else None


# --------------------------------------------------------------------------- #
# Canonical key for symmetry de-duplication (relabel candidates)
# --------------------------------------------------------------------------- #
def canonical_key(ballot_set):
    """
    Smallest representation of this profile over all relabelings of candidates,
    so e.g. "A beats via split" and its B/C mirror collapse to one pattern.
    """
    best = None
    for perm in itertools.permutations(range(NUM_CANDIDATES)):
        relabel = tuple(
            sorted(tuple(b[p] for p in perm) for b in ballot_set)
        )
        if best is None or relabel < best:
            best = relabel
    return best


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    global NUM_BALLOTS
    if len(sys.argv) > 1:
        NUM_BALLOTS = int(sys.argv[1])

    strict_menu = [b for b in itertools.product(VALID_SCORES, repeat=NUM_CANDIDATES)
                   if is_strict(b)]
    total = 0
    divergences = []
    seen_keys = set()

    for ballot_set in itertools.combinations_with_replacement(strict_menu, NUM_BALLOTS):
        total += 1
        ballots = [{CANDS[i]: v for i, v in enumerate(b)} for b in ballot_set]
        sw = star_winner(ballots)
        if sw is None:
            continue
        iw = irv_winner(ballots)
        if iw is None or iw == sw:
            continue
        # Genuine STAR != IRV divergence.
        if DEDUPE_BY_SYMMETRY:
            key = canonical_key(ballot_set)
            if key in seen_keys:
                continue
            seen_keys.add(key)
        divergences.append((ballot_set, sw, iw))

    print(f"Config: C={NUM_CANDIDATES}, B={NUM_BALLOTS}, scores={VALID_SCORES}")
    print(f"Strict ballot types: {len(strict_menu)}  |  profiles scanned: {total:,}")
    label = "distinct patterns" if DEDUPE_BY_SYMMETRY else "profiles"
    print(f"Genuine STAR != IRV divergences ({label}): {len(divergences):,}\n")

    for ballot_set, sw, iw in divergences[:40]:
        b_str = "  ".join("".join(str(s) for s in b) for b in ballot_set)
        print(f"  STAR={sw}  IRV={iw}   ballots(ABC): {b_str}")
    if len(divergences) > 40:
        print(f"  ... and {len(divergences) - 40:,} more (see CSV).")

    if WRITE_CSV and divergences:
        fn = (f"star_irv_divergence_C{NUM_CANDIDATES}_B{NUM_BALLOTS}_"
              f"{datetime.datetime.now():%Y%m%d-%H%M%S}.csv")
        with open(fn, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, lineterminator="\n")  # LF, not csv's default CRLF
            w.writerow(["star_winner", "irv_winner", "ballots_ABC"])
            for ballot_set, sw, iw in divergences:
                w.writerow([sw, iw,
                            "_".join("".join(str(s) for s in b) for b in ballot_set)])
        print(f"\nWrote {len(divergences):,} rows to {fn}")


if __name__ == "__main__":
    main()
