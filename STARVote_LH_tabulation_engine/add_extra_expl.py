"""
Script: add_extra_expl.py
Description: Runs a STAR Voting election with detailed tiebreaker analysis and matrix visualization.

UPDATES (Current Version):
-------------------------------------------------------------------------------
1. HYBRID PARSING SUPPORT:
   The script now supports two distinct formats for defining ballots in the `csv_input` variable.

   Format A: Standard CSV
   ----------------------
   Standard comma-separated values. Supports 'Weight:Score' prefix.
   Example:
     A,B,C
     0,5,2
     3:5,5,0   <-- (Weighted ballot: 3 voters voted 5,5,0)

   Format B: Compact Underscore (New)
   ----------------------------------
   Useful for quick data entry. Ballots are defined as underscore-separated digit groups.
   Each digit corresponds to a candidate in the Header order.
   Constraint: Scores must be single digits (0-9).

   Example:
     A,B,C
     052_225_323

   Interpretation:
     - 052 -> A=0, B=5, C=2
     - 225 -> A=2, B=2, C=5
     - 323 -> A=3, B=2, C=3

2. VALIDATION:
   The script now performs a plausibility check on compact segments.
   If you provide '052' (3 digits) for 4 candidates, it will print a warning and ignore that segment.

3. STANDARDIZED OUTPUT:
   The "Input Ballot Data" section now always prints as normalized Standard CSV
   to verify correct parsing.
-------------------------------------------------------------------------------
"""

import starvote
import re
import random
from collections import defaultdict
from starvote import Tiebreaker

# --- ANSI Color Codes ---
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"


# ---
# 1. TIEBREAKER CLASS
# ---
class SequenceTiebreaker(Tiebreaker):
    def __init__(self, mode="last", manual_order=None, silent=False):
        self.mode = mode.lower()
        self.manual_order = manual_order or []
        self.silent = silent
        self.order_map = {}
        self.info_printed = False

    def initialize(self, options, ballots):
        # Determine candidate order from the first ballot keys
        first_ballot = next(iter(ballots))
        cands_in_csv_order = list(first_ballot.keys())

        if self.mode == "manual" and self.manual_order:
            self.preferred_order = self.manual_order
        elif self.mode in ("first", "left"):
            self.preferred_order = cands_in_csv_order
        else:
            # Default to 'right' / 'last' / 'reversed'
            self.preferred_order = list(reversed(cands_in_csv_order))

        # Create a mapping for O(1) lookups: {Candidate: Index}
        self.order_map = {c: i for i, c in enumerate(self.preferred_order)}

        if not self.info_printed and not self.silent:
            direction = "Left/First" if self.mode in ("first", "left") else "Right/Last"
            print(
                f'Tiebreaker: "{self.mode.upper()}" ({direction}) - priority order: {self.preferred_order}'
            )
            self.info_printed = True

    def __call__(self, options, tie, desired, exception):
        # Sort tied candidates by their index in the preferred_order list
        ranked = sorted(tie, key=lambda c: self.order_map.get(c, 999))
        winners = ranked[:desired]

        if not self.silent:
            print("\n[Tiebreaker: Sequence Priority]")
            print(f"  Tie detected among: {tie}")
            print(f"  Priority order: {self.preferred_order}")
            print(f"  Result: {winners} selected based on sequence priority.")

        return winners


# ---
# 2. HELPER FUNCTIONS
# ---
def parse_ballots_from_string(ballot_string):
    """
    Parses ballot data. Supports two formats per line:
    1. Standard CSV: 0,5,2
    2. Compact Underscore: 052_225_323

    Includes validation to warn on length mismatches.
    """
    lines = []
    for line in ballot_string.strip().split("\n"):
        line = line.strip()
        if line.startswith("#,"):
            clean_line = line
        else:
            clean_line = line.split("#")[0].strip()
        if clean_line:
            lines.append(clean_line)

    if not lines:
        return [], []

    # Parse Headers
    headers = [name.strip() for name in re.split(r"[,\t]+", lines[0]) if name.strip()]
    if headers and headers[0] == "#":
        headers.pop(0)

    ballots = []

    for line_num, line in enumerate(lines[1:], start=2):
        # 1. Attempt Standard CSV Parse first
        parts = re.split(r"[,\t]+", line)
        weight = 1

        # Handle "Weight:Score" format
        if ":" in parts[0]:
            try:
                w_str, s_str = parts[0].split(":", 1)
                weight = int(w_str)
                parts[0] = s_str
            except ValueError:
                pass

        clean_parts = [p.strip() for p in parts if p.strip()]

        # Check if this matches Standard CSV (Score count == Header count)
        if len(clean_parts) == len(headers):
            try:
                scores = [int(p) for p in clean_parts]
                ballot = {h: s for h, s in zip(headers, scores)}
                for _ in range(weight):
                    ballots.append(ballot)
                continue  # Successfully parsed as CSV
            except ValueError:
                pass  # Fall through

        # 2. Attempt Compact Underscore Format
        segments = line.split("_")
        for seg in segments:
            seg = seg.strip()
            if not seg:
                continue

            # PLAUSIBILITY CHECK
            if seg.isdigit():
                if len(seg) == len(headers):
                    scores = [int(char) for char in seg]
                    ballot = {h: s for h, s in zip(headers, scores)}
                    ballots.append(ballot)
                else:
                    # Found a digit-only chunk with wrong length -> WARN USER
                    print(
                        f"{COLOR_RED}Warning (Line {line_num}):{COLOR_RESET} "
                        f"Segment '{seg}' has {len(seg)} digits, but expected {len(headers)} "
                        f"for candidates {headers}. Ignored."
                    )

    return headers, ballots


def calculate_preference_matrix(candidates, ballots):
    """
    Generates the pairwise preference matrix from already-parsed ballots.
    """
    if not ballots or not candidates:
        return None

    num_ballots = len(ballots)
    matrix = defaultdict(lambda: defaultdict(tuple))

    for c_i in candidates:
        for c_j in candidates:
            if c_i == c_j:
                matrix[c_i][c_j] = (0, 0, num_ballots)
                continue

            for_i = 0
            against_i = 0
            no_pref = 0

            for ballot in ballots:
                s_i = ballot.get(c_i, 0)
                s_j = ballot.get(c_j, 0)

                if s_i > s_j:
                    for_i += 1
                elif s_j > s_i:
                    against_i += 1
                else:
                    no_pref += 1

            matrix[c_i][c_j] = (for_i, against_i, no_pref)

    return matrix


def get_top_two_finalists(ballots):
    scores = defaultdict(int)
    for b in ballots:
        for c, s in b.items():
            scores[c] += s
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    finalists = []
    if len(ranked) >= 1:
        finalists.append(ranked[0][0])
    if len(ranked) >= 2:
        finalists.append(ranked[1][0])
    return finalists


def print_matrix(candidates, matrix, finalists=None):
    if not candidates or not matrix:
        return
    if finalists is None:
        finalists = []
    print("\n--- Runoff (Preference) Matrix ---")
    print(
        f"Legend: {COLOR_GREEN}For{COLOR_RESET} - {COLOR_RED}Against{COLOR_RESET} - No Preference"
    )
    print("        * indicates Top 2 Finalist")

    col_width = max((len(c) + 2 for c in candidates), default=10)
    max_data_str = "0 - 0 - 0"
    if matrix:
        max_data_str = max(
            (
                f"{matrix[c1][c2][0]} - {matrix[c1][c2][1]} - {matrix[c1][c2][2]}"
                for c1 in candidates
                for c2 in candidates
                if c1 != c2
            ),
            key=len,
            default=max_data_str,
        )
    col_width = max(col_width, len(max_data_str), 10)
    row_label_width = col_width + 4
    header = " " * row_label_width + " | "

    for cand in candidates:
        display_name = f"* {cand}" if cand in finalists else f"  {cand}"
        header += f"{display_name:^{col_width}} |"
    print(header)
    print("-" * len(header))

    for cand_i in candidates:
        prefix = "* " if cand_i in finalists else "  "
        row_label = f"{prefix}{cand_i} >"
        row_str = f"{row_label:>{row_label_width}} | "
        for cand_j in candidates:
            if cand_i == cand_j:
                row_str += f"{'---':^{col_width}} |"
            else:
                for_val, against_val, no_pref_val = matrix[cand_i][cand_j]
                raw_str = f"{for_val} - {against_val} - {no_pref_val}"
                padding = col_width - len(raw_str)
                l_pad = padding // 2
                colored_tuple = (
                    f"{COLOR_GREEN}{for_val}{COLOR_RESET} - "
                    f"{COLOR_RED}{against_val}{COLOR_RESET} - "
                    f"{no_pref_val}"
                )
                row_str += f"{' ' * l_pad}{colored_tuple}{' ' * (padding - l_pad)} |"
        print(row_str)

    print("\n[Condorcet Winner]")
    condorcet_winner = None
    for c1 in candidates:
        is_winner = True
        for c2 in candidates:
            if c1 == c2:
                continue
            for_c1, against_c1, _ = matrix[c1][c2]
            if for_c1 <= against_c1:
                is_winner = False
                break
        if is_winner:
            condorcet_winner = c1
            break
    print(
        f"  {condorcet_winner if condorcet_winner else 'No Condorcet Winner (cycle detected)'}"
    )


def print_extended_analysis(ballots, winners):
    if not winners:
        return
    runoff_winner_name = list(winners)[0]
    scores = defaultdict(int)
    for b in ballots:
        for c, s in b.items():
            scores[c] += s
    max_score = max(scores.values()) if scores else 0
    top_scorers = [c for c, s in scores.items() if s == max_score]

    if runoff_winner_name not in top_scorers:
        ranked_by_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        score_winner_name = ranked_by_score[0][0]
        print(f"\n{'  NOTE: SCORING / RUNOFF DIVERGENCE DETECTED  ':^60}")
        print(
            f"Score Winner ({score_winner_name}) != Runoff Winner ({runoff_winner_name})"
        )
    else:
        print(
            f"\n[Analysis] Winner '{runoff_winner_name}' had the highest score ({max_score}). No divergence."
        )


# ---
# 3. EXECUTION LOGIC
# ---
def run_election(csv_input, mode, manual_list, seed):
    # Parse once, return both headers and parsed ballots
    candidates, ballots = parse_ballots_from_string(csv_input)

    if not ballots:
        print("Error: No valid ballots found in input.")
        return

    # Generate matrix from the already-parsed data
    matrix = calculate_preference_matrix(candidates, ballots)
    finalists = get_top_two_finalists(ballots)

    if mode.lower() == "random":
        tiebreaker_obj = lambda options, tie, desired, exception: random.sample(
            list(tie), desired
        )
        tiebreaker_silent = tiebreaker_obj
        random.seed(seed)
    else:
        tiebreaker_obj = SequenceTiebreaker(
            mode=mode, manual_order=manual_list, silent=False
        )
        tiebreaker_silent = SequenceTiebreaker(
            mode=mode, manual_order=manual_list, silent=True
        )

    # Run silent election for analysis
    if winners_silent := starvote.election(
        method=starvote.star,
        ballots=ballots,
        seats=1,
        tiebreaker=tiebreaker_silent,
        verbosity=0,
    ):
        # STANDARDIZED OUTPUT: Print parsed data as Standard CSV
        print("--- Input Ballot Data ---")
        print(",".join(candidates))
        for b in ballots:
            # Reconstruct row from dict
            print(",".join(str(b[c]) for c in candidates))

        print_matrix(candidates, matrix, finalists)
        print_extended_analysis(ballots, winners_silent)

    print("\n--- STARVOTE results ---")
    if mode.lower() == "random":
        random.seed(seed)
        print(f"Tiebreaker: RANDOM Mode (Seed: {seed})")

    winners = starvote.election(
        method=starvote.star,
        ballots=ballots,
        seats=1,
        tiebreaker=tiebreaker_obj,
        verbosity=1,
        maximum_score=5,
    )


if __name__ == "__main__":
    # Compact Format Input with intentional error for testing:
    # '052' (3 digits) vs 'A,B,C,D' (4 candidates) -> Should warn

    csv_input = """
A,B,C,D,E
5,0,4,4,1
"""
    # TIEBREAKER SETTINGS
    # Options: 'left', 'right', 'random', 'manual'
    TIEBREAKER_MODE = "left"
    MANUAL_ORDER = ["B", "A", "C"]
    RANDOM_SEED = 42

    run_election(csv_input, TIEBREAKER_MODE, MANUAL_ORDER, RANDOM_SEED)
