import random
import csv
import io

# --- CONFIGURATION ---
TARGET_FOUND = 5  # Stop after finding this many cases
NUM_CANDIDATES = 7  # 4 makes it easier to have 3 diff winners than 3
NUM_BALLOTS = 3  # Kept small for readability
SCORE_RANGE = [0, 1, 2, 3, 4, 5]
# ---------------------


def get_condorcet_winner(ballots, candidates):
    """Returns CW or None."""
    for cand in candidates:
        beaten_all = True
        for opp in candidates:
            if cand == opp:
                continue

            # Head-to-Head
            c_wins = 0
            o_wins = 0
            for b in ballots:
                if b[cand] > b[opp]:
                    c_wins += 1
                elif b[opp] > b[cand]:
                    o_wins += 1

            if c_wins <= o_wins:  # Must strictly win
                beaten_all = False
                break
        if beaten_all:
            return cand
    return None


def get_score_winner(ballots, candidates):
    """Returns the candidate with highest total score."""
    totals = {c: 0 for c in candidates}
    for b in ballots:
        for c in candidates:
            totals[c] += b[c]

    # Sort by score descending
    sorted_cands = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    # Return top. Note: This simple version ignores ties for simplicity in search.
    return sorted_cands[0][0], totals


def get_star_winner(ballots, candidates, totals):
    """Returns STAR winner (Top 2 Score -> Runoff)."""
    # 1. Scoring Round (Reuse totals from Score Step)
    sorted_cands = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    finalist_a = sorted_cands[0][0]
    finalist_b = sorted_cands[1][0]

    # 2. Runoff Round
    a_votes = 0
    b_votes = 0
    for b in ballots:
        if b[finalist_a] > b[finalist_b]:
            a_votes += 1
        elif b[finalist_b] > b[finalist_a]:
            b_votes += 1

    if a_votes > b_votes:
        return finalist_a
    elif b_votes > a_votes:
        return finalist_b
    else:
        return None  # Tie in runoff


def generate_random_scenario():
    cands = [chr(65 + i) for i in range(NUM_CANDIDATES)]  # A, B, C, D
    ballots = []
    for _ in range(NUM_BALLOTS):
        b = {c: random.choice(SCORE_RANGE) for c in cands}
        ballots.append(b)
    return ballots, cands


def format_csv(ballots, cands):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(cands)
    for b in ballots:
        writer.writerow([b[c] for c in cands])
    return output.getvalue().strip()


def main():
    print(f"🔎 Searching for {TARGET_FOUND} scenarios with 3 DIFFERENT winners...")
    print("   (Condorcet != Score != STAR)\n")

    found_count = 0
    attempts = 0

    while found_count < TARGET_FOUND:
        attempts += 1
        ballots, cands = generate_random_scenario()

        # 1. Find Condorcet
        cw = get_condorcet_winner(ballots, cands)
        if not cw:
            continue  # Skip cycles

        # 2. Find Score Winner
        sw, totals = get_score_winner(ballots, cands)
        if sw == cw:
            continue  # We want divergence

        # 3. Find STAR Winner
        star = get_star_winner(ballots, cands, totals)
        if not star:
            continue

        # 4. Check for Total Divergence
        # We want: CW, SW, and STAR to be three UNIQUE candidates
        if (sw != star) and (star != cw):
            found_count += 1
            print(f"🚨 SCENARIO #{found_count} FOUND (Attempt {attempts:,})")
            print(f"   Condorcet: {cw}")
            print(f"   Score:     {sw}")
            print(f"   STAR:      {star}")
            print("\n--- Ballot CSV ---")
            print("```csv")
            print(format_csv(ballots, cands))
            print("```")
            print("-" * 40 + "\n")

    print("✅ Search Complete.")


if __name__ == "__main__":
    main()
