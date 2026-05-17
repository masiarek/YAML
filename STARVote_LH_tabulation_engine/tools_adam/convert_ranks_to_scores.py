import re
import textwrap
from collections import Counter
from typing import List, Dict, Tuple, Optional

class StarVoteConverter:
    def __init__(self, strict_mode: bool = True, equal_ranks_rule: str = 'High', compressed_output: bool = False):
        """
        Initialize the converter with rules.

        Args:
            strict_mode (bool): If True, '=' ties are forbidden.
            equal_ranks_rule (str): 'High' (optimistic/ceiling) or 'Low' (pessimistic/floor).
            compressed_output (bool): If True, aggregates identical ranks/scores in output.
        """
        self.strict_mode = strict_mode
        self.equal_ranks_rule = equal_ranks_rule.capitalize()
        self.compressed_output = compressed_output

        if self.equal_ranks_rule not in ['High', 'Low']:
            raise ValueError("equal_ranks_rule must be 'High' or 'Low'")

        self.ballots: List[List[List[str]]] = [] # List of ballots. Each ballot is a list of rank groups (lists of candidate IDs).
        self.all_candidates: Dict[str, str] = {} # Map canonical_id -> Display Name

    def normalize_name(self, name: str) -> Tuple[str, str]:
        """
        Normalizes a candidate name.
        Returns (canonical_id, display_name).
        """
        clean_name = name.strip()
        return clean_name.lower(), clean_name.title()

    def parse_line(self, line: str, line_num: int) -> Optional[List[List[str]]]:
        """
        Parses a single line of input.
        Returns a list of rank groups (e.g., [['a'], ['b', 'c']]) or None if empty/comment.
        """
        # 1. Strip Comments
        if '#' in line:
            line = line.split('#')[0]
        line = line.strip()

        if not line:
            return None

        # 2. Extract Multiplier
        multiplier = 1
        rank_content = line

        # Check for multiplier pattern "N:" at start
        match = re.match(r'^(\d+):(.*)', line)
        if match:
            count_str, content = match.groups()
            try:
                multiplier = int(count_str)
            except ValueError:
                raise ValueError(f"Line {line_num}: Invalid Multiplier. Must be an integer.")

            if multiplier < 1:
                raise ValueError(f"Line {line_num}: Invalid Multiplier. Must be a positive integer > 0.")
            rank_content = content.strip()

        # 3. Validate Characters
        # Allowed: Alphanumeric, spaces, >, =
        if not re.match(r'^[A-Za-z0-9\s>=]+$', rank_content):
            # Find the invalid char for the error message
            invalid_chars = re.findall(r'[^A-Za-z0-9\s>=]', rank_content)
            unique_invalid = sorted(list(set(invalid_chars)))
            raise ValueError(f"Line {line_num}: Invalid Syntax. Illegal character(s) '{', '.join(unique_invalid)}' found. Valid characters are letters, numbers, '>', and '='.")

        # 4. Strict Mode Check
        if self.strict_mode and '=' in rank_content:
            raise ValueError(f"Line {line_num}: Strict ranking enforced. Ties ('=') are not allowed.")

        # 5. Parse Candidates & Check Empty Slots
        # Split by '>' first to get ranks
        raw_ranks = rank_content.split('>')

        parsed_ballot = []
        candidates_in_ballot = set()

        for rank_str in raw_ranks:
            rank_str = rank_str.strip()

            # Check for empty slots (e.g., A >> B or trailing >)
            if not rank_str:
                raise ValueError(f"Line {line_num}: Syntax Error: Found empty ranking slot. Check for double delimiters (>>) or trailing symbols.")

            # Handle Ties (=)
            if '=' in rank_str:
                # Split ties
                tied_names = rank_str.split('=')
                group = []
                for name in tied_names:
                    name = name.strip()
                    if not name:
                        raise ValueError(f"Line {line_num}: Syntax Error: Found empty ranking slot in tie (==).")

                    cid, display = self.normalize_name(name)

                    # 6. Check Duplicates (Validation 5.2)
                    if cid in candidates_in_ballot:
                        raise ValueError(f"Line {line_num}: Error: Candidate '{display}' appears twice in the same ballot. A candidate may only be ranked once.")

                    candidates_in_ballot.add(cid)
                    self.all_candidates[cid] = display # Store display name
                    group.append(cid)
                parsed_ballot.append(group)
            else:
                # Single candidate
                cid, display = self.normalize_name(rank_str)

                # 6. Check Duplicates
                if cid in candidates_in_ballot:
                    raise ValueError(f"Line {line_num}: Error: Candidate '{display}' appears twice in the same ballot.")

                candidates_in_ballot.add(cid)
                self.all_candidates[cid] = display
                parsed_ballot.append([cid])

        # Return the ballot repeated by multiplier
        return [parsed_ballot for _ in range(multiplier)]

    def process_input(self, input_text: str):
        """
        Main processing loop.
        """
        # Clean input: Dedent removes common leading whitespace from docstrings
        clean_text = textwrap.dedent(input_text).strip()

        # Reset state
        self.ballots = []
        self.all_candidates = {}

        lines = clean_text.split('\n')

        # Parse Logic
        for i, line in enumerate(lines):
            try:
                # Line numbers usually 1-indexed for humans
                result = self.parse_line(line, i + 1)
                if result:
                    self.ballots.extend(result)
            except ValueError as e:
                # Print raw input for context if there's an error, then the error
                print("Ranks (Preview before Error):")
                print(clean_text)
                print(f"\nValidation Error: {e}")
                return

        # Print Ranks (Processed)
        print("Ranks:")
        if self.compressed_output:
            self.print_compressed_ranks()
        else:
            print(clean_text)
        print() # Newline

        # 6. Global Check: Insufficient Candidates
        if len(self.all_candidates) < 2:
            print("Election Error: Less than 2 unique candidates found. A valid election requires at least 2 candidates.")
            return

        self.calculate_scores()

    def reconstruct_ballot_string(self, ballot: List[List[str]]) -> str:
        """Helper to turn internal ballot structure back into 'A > B = C' string."""
        group_strings = []
        for group in ballot:
            # Convert CIDs back to Display Names
            display_names = [self.all_candidates[cid] for cid in group]
            # Join ties with '='
            group_strings.append("=".join(display_names))
        # Join groups with '>'
        return ">".join(group_strings)

    def print_compressed_ranks(self):
        """Reconstructs ballots from data, counts duplicates, and prints."""
        if not self.ballots:
            return

        # Convert all ballots to string representations
        ballot_strings = [self.reconstruct_ballot_string(b) for b in self.ballots]

        # Count them
        # Note: We use a simple Counter. The order of output depends on insertion order in Python 3.7+ dicts
        counts = Counter(ballot_strings)

        for b_str, count in counts.items():
            if count > 1:
                print(f"{count}:{b_str}")
            else:
                print(b_str)

    def calculate_scores(self):
        """
        Calculates scores based on Top-Anchored logic and Equal Ranks Rule.
        """
        # Prepare score accumulator
        # Map canonical_id -> list of scores (one per ballot)
        candidate_scores = {cid: [] for cid in self.all_candidates}

        # Sort candidates alphabetically for consistent output column order
        sorted_cids = sorted(self.all_candidates.keys(), key=lambda x: self.all_candidates[x])

        for ballot in self.ballots:
            # Track which candidates have been scored in this ballot
            scored_candidates = set()

            # Slot tracking
            current_slot = 0

            for rank_group in ballot:
                group_size = len(rank_group)

                # Determine slots consumed by this group
                # e.g. if current_slot is 0 and group_size is 2 (A=B), they consume slots 0 and 1.
                consumed_slots = range(current_slot, current_slot + group_size)

                # Calculate Base Scores for these slots
                # Top-Anchored Formula: Score = max(5 - slot_index, 0)
                slot_scores = [max(5 - idx, 0) for idx in consumed_slots]

                # Apply Equal Ranks Rule
                final_score = 0
                if group_size == 1:
                    final_score = slot_scores[0]
                else:
                    if self.equal_ranks_rule == 'High':
                        final_score = max(slot_scores)
                    else: # Low
                        final_score = min(slot_scores)

                # Assign score to all in group
                for cid in rank_group:
                    candidate_scores[cid].append(final_score)
                    scored_candidates.add(cid)

                # Advance slot counter
                current_slot += group_size

            # Assign 0 to unranked candidates
            for cid in self.all_candidates:
                if cid not in scored_candidates:
                    candidate_scores[cid].append(0)

        # Output Generation
        self.print_results(candidate_scores, sorted_cids)

    def print_results(self, scores: Dict[str, List[int]], sorted_cids: List[str]):
        """
        Prints the results in CSV format.
        """
        print("Scores:")
        # Header
        headers = [self.all_candidates[cid] for cid in sorted_cids]
        print(",".join(headers))

        # Rows
        num_ballots = len(scores[sorted_cids[0]])
        rows = []

        for i in range(num_ballots):
            row_items = [str(scores[cid][i]) for cid in sorted_cids]
            rows.append(",".join(row_items))

        if self.compressed_output:
            counts = Counter(rows)
            for row_str, count in counts.items():
                if count > 1:
                    print(f"{count}:{row_str}")
                else:
                    print(row_str)
        else:
            for row_str in rows:
                print(row_str)

# --- Example Usage / Test Cases ---

def run_example(name, raw_input, strict=True, rule='High', compressed=False):
    print(f"\n--- {name} (Strict={strict}, Rule={rule}, Compressed={compressed}) ---")
    converter = StarVoteConverter(strict_mode=strict, equal_ranks_rule=rule, compressed_output=compressed)
    converter.process_input(raw_input)

if __name__ == "__main__":
    # Example 1: Basic
    ex1 = """
14:A>B>C
20:B>A>C

    """
run_example("add title", ex1, strict=False, rule='High', compressed=True)
