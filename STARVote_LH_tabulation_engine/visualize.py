import csv
import itertools
import datetime
import string

def generate_all_unique_ballots(num_candidates, max_score):
    """
    Generates every possible permutation of scores for the given candidates.
    (The Cartesian Product).
    """
    # 1. Setup Candidates (Columns)
    if num_candidates <= 26:
        candidates = list(string.ascii_uppercase[:num_candidates])
    else:
        candidates = [f"C{i+1}" for i in range(num_candidates)]

    # 2. Setup Score Range (0 to Max)
    scores = range(max_score + 1)

    # 3. Generate all permutations (The "Menu")
    # This creates every possible combination: (0,0), (0,1), (1,0), (1,1)...
    ballot_permutations = list(itertools.product(scores, repeat=num_candidates))

    return candidates, ballot_permutations

def save_to_csv(candidates, ballots, max_score):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    # naming it "menu" because it lists the distinct options
    filename = f"ballot_menu_C{len(candidates)}_S{max_score}_{timestamp}.csv"

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write Header: A, B
            writer.writerow(candidates)

            # Write Rows: 0,0 etc.
            writer.writerows(ballots)

        print(f"✅ Generated {len(ballots)} unique ballot types.")
        print(f"📁 Saved to: {filename}")

    except IOError as e:
        print(f"❌ Error writing file: {e}")

if __name__ == "__main__":
    # --- Configuration ---
    NUM_CANDIDATES = 5
    SCORE_RANGE = 4
    # ---------------------

    print("Generating all possible unique ballots...")
    headers, rows = generate_all_unique_ballots(NUM_CANDIDATES, SCORE_RANGE)

    # Preview
    print("\nPreview:")
    print(",".join(headers))
    for r in rows:
        print(",".join(map(str, r)))
    print("")

    save_to_csv(headers, rows, SCORE_RANGE)