"""
Script: starvote_larry_hastings.py
Description: Runs a STAR Voting election with detailed tiebreaker analysis and matrix visualization.
"""

import re
import sys
from collections import defaultdict

import starvote
from starvote import Tiebreaker

# --- ANSI Color Codes ---
# Disabled automatically when output is not a TTY (e.g. piped to a file),
# so redirected output doesn't get littered with escape sequences.
if sys.stdout.isatty():
    COLOR_GREEN = "\033[92m"
    COLOR_RED = "\033[91m"
    COLOR_BLUE = "\033[94m"
    COLOR_RESET = "\033[0m"
else:
    COLOR_GREEN = COLOR_RED = COLOR_BLUE = COLOR_RESET = ""


# ---
# 1. TIEBREAKER CLASS
# ---
class LotNumberTiebreaker(Tiebreaker):
    def __init__(self, lot_numbers=None, silent=False):
        self.lot_numbers = lot_numbers or []
        self.silent = silent
        self.order_map = {}
        self.info_printed = False
        self.expl = ""

    def initialize(self, options, ballots):
        # Determine candidate order from the first ballot keys
        first_ballot = next(iter(ballots))
        cands_in_csv_order = list(first_ballot.keys())

        # Check if the user provided lot numbers
        if not self.lot_numbers:
            # DEV MODE: Auto-generate a fallback sequence from CSV column order
            self.lot_numbers = cands_in_csv_order
            self.expl = "*** No official Tie-breaking Lot Numbers were provided \n- hence the Ties are resolved using fallback sequence - CSV column order."
        else:
            # PRODUCTION MODE: Use the provided numbers
            self.expl = "*(Ties are resolved by selecting the tied candidate with the highest priority official Lot Number).*"

        # Create an O(1) lookup map: {Candidate: Priority_Index}
        self.order_map = {c: i for i, c in enumerate(self.lot_numbers)}

    def __call__(self, options, tie, desired, exception):
        # We only enter this function if an actual tie has occurred.

        # Print the explanation if this is the first tie we've encountered
        if not self.info_printed and not self.silent:
            print(f"\n{self.expl}")
            print(f"Tiebreaker: LOT NUMBERS - priority sequence: {self.lot_numbers}")
            self.info_printed = True

        # Sort tied candidates by their assigned lot number priority
        ranked = sorted(tie, key=lambda c: self.order_map.get(c, float("inf")))
        winners = ranked[:desired]

        if not self.silent:
            print("\n[Tiebreaker: Lot Number Priority]")
            print(f"  Tie detected among: {tie}")
            print(f"  Result: {winners} selected based on lot numbers.")

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


def get_top_two_finalists(ballots, order_map=None):
    """Top two by total score; score ties broken by lot-number priority
    (same rule as LotNumberTiebreaker) so the matrix '*' markers match
    the finalists starvote actually selects."""
    if order_map is None:
        order_map = {}
    scores = defaultdict(int)
    for b in ballots:
        for c, s in b.items():
            scores[c] += s
    ranked = sorted(
        scores.items(), key=lambda x: (-x[1], order_map.get(x[0], float("inf")))
    )
    return [c for c, _ in ranked[:2]]


def print_matrix(candidates, matrix, finalists=None, star_winner=None):
    if not candidates or not matrix:
        return
    if finalists is None:
        finalists = []
    print("\n--- Runoff (Preference) Matrix ---")
    print(
        f"Legend: {COLOR_GREEN}For{COLOR_RESET} - {COLOR_BLUE}Equal Preference{COLOR_RESET} - {COLOR_RED}Against{COLOR_RESET}"
    )
    print("        * indicates Top 2 Finalist")

    col_width = max((len(c) + 2 for c in candidates), default=10)
    max_data_str = "0 - 0 - 0"
    if matrix:
        max_data_str = max(
            (
                f"{matrix[c1][c2][0]} - {matrix[c1][c2][2]} - {matrix[c1][c2][1]}"
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
                raw_str = f"{for_val} - {no_pref_val} - {against_val}"
                padding = col_width - len(raw_str)
                l_pad = padding // 2
                colored_tuple = (
                    f"{COLOR_GREEN}{for_val}{COLOR_RESET} - "
                    f"{COLOR_BLUE}{no_pref_val}{COLOR_RESET} - "
                    f"{COLOR_RED}{against_val}{COLOR_RESET}"
                )
                row_str += f"{' ' * l_pad}{colored_tuple}{' ' * (padding - l_pad)} |"
        print(row_str)

    print("\n[Condorcet Winner]")
    print(f"  {analyze_condorcet(candidates, matrix, star_winner, finalists)}")


def _star_comparison(cw, star_winner, finalists):
    """Annotate how the Condorcet winner relates to the STAR result."""
    if star_winner is None:
        return ""
    if cw == star_winner:
        return " — matches the STAR winner"
    note = f" — STAR elected {star_winner} instead"
    if finalists and cw not in finalists:
        note += f" ({cw} was eliminated in the scoring round)"
    return note


def analyze_condorcet(candidates, matrix, star_winner=None, finalists=None):
    """Classify the pairwise outcome instead of conflating ties with cycles.

    1. Strict winner: beats every other candidate head-to-head.
    2. Unique weak winner: unbeaten, but ties at least one matchup.
    3. Multiple unbeaten candidates: pairwise ties, no cycle among them.
    4. Genuine cycle: every candidate loses at least one matchup.
    """
    beats = {c: set() for c in candidates}
    losses = {c: 0 for c in candidates}
    for c1 in candidates:
        for c2 in candidates:
            if c1 == c2:
                continue
            for_c1, against_c1, _ = matrix[c1][c2]
            if for_c1 > against_c1:
                beats[c1].add(c2)
            elif against_c1 > for_c1:
                losses[c1] += 1

    n_others = len(candidates) - 1
    unbeaten = [c for c in candidates if losses[c] == 0]

    # Case 1: strict Condorcet winner
    for c in candidates:
        if len(beats[c]) == n_others:
            return f"Condorcet Winner: {c}" + _star_comparison(
                c, star_winner, finalists
            )

    # Case 2: unique weak winner (unbeaten, but ties some matchups)
    if len(unbeaten) == 1:
        return (
            f"No strict Condorcet winner; weak Condorcet winner: {unbeaten[0]}"
            + _star_comparison(unbeaten[0], star_winner, finalists)
        )

    # Case 3: multiple unbeaten candidates (indifference, not intransitivity)
    if len(unbeaten) > 1:
        return (
            f"No strict Condorcet winner; "
            f"unbeaten candidates: {', '.join(unbeaten)} (pairwise ties)"
        )

    # Case 4: everyone loses at least once -> a majority cycle must exist
    cycle = _find_beats_cycle(candidates, beats)
    if cycle:
        return f"No Condorcet winner (majority cycle: {' > '.join(cycle)})"
    return "No Condorcet winner (every candidate loses at least one matchup)"


def _find_beats_cycle(candidates, beats):
    """DFS for a directed cycle in the 'beats' graph.
    Returns the cycle as a list like ['A', 'B', 'C', 'A'], or None."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {c: WHITE for c in candidates}
    stack = []

    def dfs(c):
        color[c] = GRAY
        stack.append(c)
        for nxt in beats[c]:
            if color[nxt] == GRAY:
                i = stack.index(nxt)
                return stack[i:] + [nxt]
            if color[nxt] == WHITE:
                found = dfs(nxt)
                if found:
                    return found
        stack.pop()
        color[c] = BLACK
        return None

    for c in candidates:
        if color[c] == WHITE:
            found = dfs(c)
            if found:
                return found
    return None


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
        # A Reversal HAPPENED (Runoff winner is NOT the score winner)
        score_winners_str = ", ".join(top_scorers)
        print(
            "\nMajority Preference Enforcement Principle:\n"
            f" - Score Round Winner(s) = ({score_winners_str})\n"
            f"  - Runoff Round Winner = ({runoff_winner_name})"
        )
        print(
            f"  Candidate {score_winners_str} earned the highest total score,\n"
            f"  but Candidate {runoff_winner_name} won the automatic runoff by "
            "being the head-to-head majority favorite.\n"
        )


# ---
# 3. EXECUTION LOGIC
# ---
def run_election(
    csv_input, lot_numbers, show_matrix=True, brief=False, seats=1, method=None
):
    if method is None:
        method = starvote.star

    # Parse once, return both headers and parsed ballots
    candidates, ballots = parse_ballots_from_string(csv_input)

    if not ballots:
        print("Error: No valid ballots found in input.")
        return

    # Generate matrix from the already-parsed data
    matrix = calculate_preference_matrix(candidates, ballots)

    # Same priority rule the tiebreaker uses (falls back to CSV column order)
    priority = lot_numbers or candidates
    order_map = {c: i for i, c in enumerate(priority)}
    finalists = get_top_two_finalists(ballots, order_map)

    # Initialize the new deterministic tiebreakers
    tiebreaker_obj = LotNumberTiebreaker(lot_numbers=lot_numbers, silent=False)
    tiebreaker_silent = LotNumberTiebreaker(lot_numbers=lot_numbers, silent=True)

    # Run silent election for analysis
    if winners_silent := starvote.election(
        method=starvote.star,
        ballots=ballots,
        seats=1,
        tiebreaker=tiebreaker_silent,
        verbosity=0,
        maximum_score=5,
    ):
        # (The normalized ballot CSV is printed by custom_print, right after
        # the engine's "Tabulating N ballots." line.)

        # CONFIGURED MATRIX OUTPUT
        if show_matrix:
            # seats=1: election() returns a single winner or a list
            star_winner = (
                winners_silent[0]
                if isinstance(winners_silent, list)
                else winners_silent
            )
            print_matrix(candidates, matrix, finalists, star_winner)

        print_extended_analysis(ballots, winners_silent)

    # Reject method/seats mismatches before tabulating — the intent is
    # ambiguous, so make the user correct it rather than silently guessing.
    method_name = getattr(method, "name", str(method))
    single_winner = method is starvote.star
    if single_winner and seats > 1:
        print(
            f"{COLOR_RED}Error:{COLOR_RESET} {method_name} elects a single winner,\n"
            f"  but got seats={seats}.\n"
            f"  Fix: set seats=1,\n"
            f"       or choose a multi-winner method to elect {seats} winners:\n"
            f"       starvote.bloc, starvote.sss,\n"
            f"       starvote.rrv, starvote.allocated."
        )
        sys.exit(1)
    if not single_winner and seats == 1:
        print(
            f"{COLOR_RED}Error:{COLOR_RESET} {method_name} elects multiple winners,\n"
            f"  but got seats=1 (requires seats >= 2).\n"
            f"  Fix: set seats to the number of winners you want,\n"
            f"       or use method=starvote.star for a single winner."
        )
        sys.exit(1)

    # Header banner naming the actual method + seat count.
    if seats > 1:
        print(f"\n--- {method_name} — {seats} seats — Larry Hastings engine ---")
    else:
        print(f"\n--- {method_name} — Larry Hastings engine ---")

    # Intercept the engine's print() to fix grammar and relabel the
    # "No Preference" bucket, re-aligning score columns so the longer
    # label doesn't shove the " -- " separator out of column.
    EQUAL_LABEL = "Equal Preference"
    EQUAL_NOTE = "(Equal Support or Equal Opposition)"
    row_re = re.compile(r"^(\s*)(\S.*?)\s+--\s+(.*)$")

    def custom_print(*args, **kwargs):
        if args and isinstance(args[0], str):
            text = args[0]

            # The engine bakes the trailing newline into the string and calls
            # us with end='' — preserve it so rows don't run together.
            trailing = "\n" if text.endswith("\n") else ""
            if trailing:
                text = text[:-1]

            # 0. BRIEF mode: collapse the repetitive engine section headers.
            #    "[STAR Voting]"               -> dropped entirely
            #    "[STAR Voting: Scoring Round]" -> "Scoring Round"
            #    (also works for "[Bloc STAR: Round 1: ...]")
            stripped = text.strip()
            if brief and stripped.startswith("[") and stripped.endswith("]"):
                inner = stripped[1:-1]
                if ":" in inner:
                    text = inner.split(":", 1)[1].strip()
                    args = (text + trailing,) + args[1:]
                    print(*args, **kwargs)
                else:
                    # Bare top-level method header -> suppress.
                    pass
                return

            # 1. Fix the singular/plural grammar.
            text = text.replace("Tabulating 1 ballots.", "Tabulating 1 ballot.")

            # 1b. After the "Tabulating N ballot(s)." line, list the
            #     normalized ballots as Standard CSV.
            if text.lstrip().startswith("Tabulating ") and "ballot" in text:
                csv_rows = [",".join(candidates)] + [
                    ",".join(str(b.get(c, 0)) for c in candidates) for b in ballots
                ]
                text = text + "\n" + "\n".join(csv_rows) + "\n"

            # 2. Relabel the no-preference bucket.
            relabeled = "No Preference" in text
            text = text.replace("No Preference", EQUAL_LABEL)

            # 3. Re-align score rows ("   <label> -- <value>"), skipping
            #    section headers like "[STAR Voting: ...]".
            m = row_re.match(text)
            if m and not text.lstrip().startswith("["):
                indent, label, rest = m.groups()
                if relabeled and EQUAL_NOTE not in rest:
                    rest = f"{rest} {EQUAL_NOTE}"
                text = f"{indent}{label:<{len(EQUAL_LABEL)}} -- {rest}"

            args = (text + trailing,) + args[1:]
        print(*args, **kwargs)

    winners = starvote.election(
        method=method,
        ballots=ballots,
        seats=seats,
        tiebreaker=tiebreaker_obj,
        verbosity=1,
        maximum_score=5,
        print=custom_print,  # Inject the custom print function here
    )

    return winners


if __name__ == "__main__":
    # Code is available at: "https://github.com/larryhastings/starvote"

    csv_input = """
Ann,Bob,Cal,Dave,Eno,Fox
1,2,3,4,5,5
1,2,3,4,5,5
"""

    # TIEBREAKER SETTING
    # Provide a list like ["B", "A", "C"] for production ties.
    # Leave empty [] to auto-generate based on CSV columns for quick testing.
    LOT_NUMBERS = []

    # FLAG: Set to False to hide the Preference Matrix and Condorcet output
    SHOW_MATRIX = False

    # FLAG: Set to True for shorter output (collapses repetitive [STAR Voting: ...]
    # section headers into plain sub-headings and drops the bare "[STAR Voting]").
    BRIEF = True

    # METHOD + SEATS.
    #   starvote.star  -> single-winner STAR (use SEATS = 1)
    #   starvote.bloc  -> Bloc STAR, multi-winner (use SEATS >= 2)
    # A mismatch (star with SEATS>1, or bloc with SEATS=1) is rejected with an
    # error and exits, so you must correct the combination.
    METHOD = starvote.star
    SEATS = 2

    run_election(
        csv_input, LOT_NUMBERS, SHOW_MATRIX, brief=BRIEF, seats=SEATS, method=METHOD
    )
