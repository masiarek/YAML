import re
import string

def convert_ballots_interleaved(input_str):
    # Split input into lines and filter out empty ones
    lines = [line.strip() for line in input_str.strip().splitlines() if line.strip()]

    for line in lines:
        # 1. Print Separator
        print("-" * 20)

        # 2. Print Original Tuples
        print("Scores as Tuples:")
        print(line)

        # 3. Process CSV
        matches = re.findall(r'\(([^)]+)\)', line)

        if matches:
            print("Scores CSV:")

            # Generate Header (A,B,C...)
            first_ballot_parts = matches[0].split(',')
            num_candidates = len(first_ballot_parts)
            header = ",".join(string.ascii_uppercase[:num_candidates])
            print(header)

            # Print Rows
            for match in matches:
                cleaned_row = ",".join(num.strip() for num in match.split(','))
                print(cleaned_row)

# --- Usage ---
input_data = '''
(0,0,0) (0,0,1) (0,0,1) (0,3,0)
(0,0,5) (0,0,1) (0,0,1) (0,4,0)
'''

convert_ballots_interleaved(input_data)