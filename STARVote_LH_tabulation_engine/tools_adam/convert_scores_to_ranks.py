import csv
import io

def convert_star_to_rcv_strict(csv_data):
    # Parse the CSV data
    f = io.StringIO(csv_data.strip())
    reader = csv.reader(f)

    # 1. Get Candidates (Header) and preserve their original indices (0, 1, 2...)
    candidates = next(reader)

    # We will store the results here to print them in separate blocks later
    strict_results = []
    weak_results = []

    for row in reader:
        # Convert string scores to integers
        scores = [int(s) for s in row]

        # 2. Create a list of tuples: (score, original_index, candidate_name)
        candidate_data = []
        for i, score in enumerate(scores):
            candidate_data.append((score, i, candidates[i]))

        # 3. Sort the data
        # Primary key: Score (Descending) -> -x[0]
        # Secondary key: Index (Ascending/Left-to-Right) -> x[1]
        sorted_candidates = sorted(candidate_data, key=lambda x: (-x[0], x[1]))

        # --- STRICT LOGIC (Your original logic) ---
        strict_names = [c[2] for c in sorted_candidates]
        strict_results.append(">".join(strict_names))

        # --- WEAK LOGIC (New logic) ---
        weak_line = ""
        for i, (score, idx, name) in enumerate(sorted_candidates):
            if i == 0:
                # First candidate always starts the string
                weak_line += name
            else:
                # Compare current score with the previous candidate's score
                prev_score = sorted_candidates[i-1][0]

                if score == prev_score:
                    # Equal preference
                    weak_line += "=" + name
                else:
                    # Strict preference
                    weak_line += ">" + name
        weak_results.append(weak_line)

    # 4. Output Block 1: Strict Rankings
    print("--- Converted RCV-IRV Ballots (Strict Rankings) ---")
    for line in strict_results:
        print(line)

    # 5. Output Block 2: Weak Rankings
    print("\n--- Converted to RCV-RR - Ranked Robin  (weak, equal ranks allowed) ---")
    for line in weak_results:
        print(line)

# --- Test Data (8 Candidates) ---
# Using quotes since one name contains a space, just to be safe with CSV parsing
raw_csv_input = """
A,B
5,0 
5,0 
0,1 
0,1 
0,1 
"""

print ('--- STAR Voting Scores (5 is Max Score) ---', raw_csv_input)
# Run the conversion
convert_star_to_rcv_strict(raw_csv_input)