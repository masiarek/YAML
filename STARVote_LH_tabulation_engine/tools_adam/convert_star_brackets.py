import io
import csv
from collections import defaultdict

def convert_and_display(csv_data):
    clean_csv = csv_data.strip()

    # --- Parse Data ---
    f = io.StringIO(clean_csv)
    reader = csv.reader(f)

    try:
        header = next(reader)
    except StopIteration:
        print("Error: Empty input")
        return

    # Aggregate counts
    aggregated_data = defaultdict(int)

    for row in reader:
        # Handle "Count:Score" input syntax
        first_val = row[0]
        if ':' in first_val:
            qty_str, score_str = first_val.split(':', 1)
            qty = int(qty_str)
            row[0] = score_str
        else:
            qty = 1

        score_tuple = tuple(row)
        aggregated_data[score_tuple] += qty

    # --- Determine if we need to show weights ---
    show_weights = any(count > 1 for count in aggregated_data.values())

    # --- Output 1: CSV Data ---
    print("--- Scores - CSV Data ---")

    if show_weights:
        # Add "#:" prefix to header
        print("#:" + ",".join(header))
    else:
        # Standard CSV header
        print(",".join(header))

    for scores, qty in aggregated_data.items():
        csv_line = ",".join(scores)
        if show_weights:
            print(f"{qty}:{csv_line}")
        else:
            print(csv_line)

    # --- Output 2: Brackets Notation ---
    print("--- Scores - Brackets Notation ---")

    for scores, qty in aggregated_data.items():
        entries = [f"{cand}[{score}]" for cand, score in zip(header, scores)]
        bracket_str = ", ".join(entries)

        if show_weights:
            print(f"{qty}:{bracket_str}")
        else:
            print(bracket_str)

# --- Test Data (Weighted) ---
input_csv = """
A,B,C
3:1,1,1
9:2,2,2
"""

# --- Execution ---
convert_and_display(input_csv)