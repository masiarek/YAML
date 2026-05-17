"""
See documentation at: https://docs.google.com/document/d/17WO3OrhCS2EuRNy1v1UbnH_ekYnwBRo8aW-nP5G9o44/edit?tab=t.0
"""

import csv
import itertools
import datetime
import io
import contextlib
import re
import math
import starvote
from starvote import Tiebreaker

# --- Configuration ---
NUM_CANDIDATES = 3
NUM_BALLOTS = 5
VALID_SCORES = [0,2,3,4,5]

# Chunking Config
ROWS_PER_FILE = 3000  # Rows per CSV file
SAVE_FIRST_CHUNKS = 4  # Save the first 2 files
SAVE_LAST_CHUNKS = 2  # Save the last 2 files
# ---------------------


class SilentSequenceTiebreaker(Tiebreaker):
    def __init__(self, mode="left"):
        self.mode = mode

    def __call__(self, options, tie, desired, exception):
        ranked = sorted(list(tie))
        return ranked[:desired]


def get_condorcet_winner(ballots, candidates):
    """
    Returns the name of the Condorcet Winner if one exists, else None.
    """
    for cand in candidates:
        beaten_all = True
        for opponent in candidates:
            if cand == opponent:
                continue
            cand_wins = 0
            opp_wins = 0
            for b in ballots:
                s_cand = b.get(cand, 0)
                s_opp = b.get(opponent, 0)
                if s_cand > s_opp:
                    cand_wins += 1
                elif s_opp > s_cand:
                    opp_wins += 1
            if not (cand_wins > opp_wins):
                beaten_all = False
                break
        if beaten_all:
            return cand
    return None


def extract_section(full_text, start_marker, stop_markers):
    if start_marker not in full_text:
        return ""
    start_idx = full_text.find(start_marker)
    search_start = start_idx + len(start_marker)
    end_idx = len(full_text)
    for marker in stop_markers:
        marker_idx = full_text.find(marker, search_start)
        if marker_idx != -1 and marker_idx < end_idx:
            end_idx = marker_idx
    return full_text[start_idx:end_idx].strip()


def parse_candidates_and_nopref(text_block):
    pattern = r"^\s*([A-Za-z0-9\s]+?)\s+--\s+(\d+)"
    matches = re.findall(pattern, text_block, re.MULTILINE)
    candidates_list = []
    no_pref_val = ""
    for name, score_str in matches:
        name = name.strip()
        score = int(score_str)
        if "No Preference" in name:
            no_pref_val = str(score)
        else:
            candidates_list.append((name, score))
    candidates_list.sort(key=lambda x: (-x[1], x[0]))
    formatted_cands = [f"{c[0]}={c[1]}" for c in candidates_list]
    return formatted_cands, no_pref_val


def extract_tie_message(text_block):
    if not text_block:
        return ""
    match_1st = re.search(
        r"There.*?(two|three|four|five|six)-way tie for first",
        text_block,
        re.IGNORECASE,
    )
    if match_1st:
        num_map = {"two": "2", "three": "3", "four": "4", "five": "5", "six": "6"}
        return f"{num_map.get(match_1st.group(1).lower(), '?')}-way tie (1st)"
    match_2nd = re.search(
        r"There.*?(two|three|four|five|six)-way tie for second",
        text_block,
        re.IGNORECASE,
    )
    if match_2nd:
        num_map = {"two": "2", "three": "3", "four": "4", "five": "5", "six": "6"}
        return f"{num_map.get(match_2nd.group(1).lower(), '?')}-way tie (2nd)"
    return ""


def parse_granularity_consolidated(logs, manual_no_pref):
    stats = {
        "sc_1st": "",
        "sc_tie_type": "",
        "sc_br1_1st": "",
        "sc_br1_no_pref": "",
        "sc_br1_tie_type": "",
        "sc_br2_1st": "",
        "sc_br2_no_pref": "",
        "sc_br2_tie_type": "",
        "ro_1st": "",
        "ro_no_pref": str(manual_no_pref),
        "ro_tie_type": "",
        "br1_1st": "",
        "br2_1st": "",
    }

    def join_cands(c_list):
        return ", ".join(c_list)

    sc_cands, _ = parse_candidates_and_nopref(logs["log_scoring_main"])
    stats["sc_1st"] = join_cands(sc_cands)
    stats["sc_tie_type"] = extract_tie_message(logs["log_scoring_main"])
    if logs["log_scoring_break1"]:
        c, np = parse_candidates_and_nopref(logs["log_scoring_break1"])
        stats["sc_br1_1st"] = join_cands(c)
        stats["sc_br1_no_pref"] = np
        stats["sc_br1_tie_type"] = extract_tie_message(logs["log_scoring_break1"])
    if logs["log_scoring_break2"]:
        c, np = parse_candidates_and_nopref(logs["log_scoring_break2"])
        stats["sc_br2_1st"] = join_cands(c)
        stats["sc_br2_no_pref"] = np
        stats["sc_br2_tie_type"] = extract_tie_message(logs["log_scoring_break2"])
    ro_cands, _ = parse_candidates_and_nopref(logs["log_runoff"])
    stats["ro_1st"] = join_cands(ro_cands)
    stats["ro_tie_type"] = extract_tie_message(logs["log_runoff"])
    if logs["log_break1"]:
        c, _ = parse_candidates_and_nopref(logs["log_break1"])
        stats["br1_1st"] = join_cands(c)
    if logs["log_break2"]:
        c, _ = parse_candidates_and_nopref(logs["log_break2"])
        stats["br2_1st"] = join_cands(c)
    return stats


def solve_star_election_with_full_blocks(
    ballots, candidates, max_score_val, manual_no_pref
):
    output_buffer = io.StringIO()
    tiebreaker = SilentSequenceTiebreaker(mode="left")
    with contextlib.redirect_stdout(output_buffer):
        starvote.election(
            method=starvote.star,
            ballots=ballots,
            seats=1,
            tiebreaker=tiebreaker,
            verbosity=1,
            maximum_score=max_score_val,
        )
    full_log = output_buffer.getvalue()
    headers = {
        "scoring_main": "[STAR Voting: Scoring Round]",
        "scoring_br1": "[STAR Voting: Scoring Round: Tiebreaker]",
        "scoring_br1_alt": "[STAR Voting: Scoring Round: First tiebreaker]",
        "scoring_br2": "[STAR Voting: Scoring Round: Second tiebreaker]",
        "runoff": "[STAR Voting: Automatic Runoff Round]",
        "break1": "[STAR Voting: Automatic Runoff Round: First tiebreaker]",
        "break2": "[STAR Voting: Automatic Runoff Round: Second tiebreaker]",
        "winner": "[STAR Voting: Winner]",
    }
    all_markers = list(headers.values()) + [
        "[Tiebreaker: Sequence Priority]",
        headers["scoring_br1_alt"],
    ]
    log_sc_br1 = extract_section(full_log, headers["scoring_br1"], all_markers)
    if not log_sc_br1:
        log_sc_br1 = extract_section(full_log, headers["scoring_br1_alt"], all_markers)
    logs = {
        "log_scoring_main": extract_section(
            full_log, headers["scoring_main"], all_markers
        ),
        "log_scoring_break1": log_sc_br1,
        "log_scoring_break2": extract_section(
            full_log, headers["scoring_br2"], all_markers
        ),
        "log_runoff": extract_section(full_log, headers["runoff"], all_markers),
        "log_break1": extract_section(full_log, headers["break1"], all_markers),
        "log_break2": extract_section(full_log, headers["break2"], all_markers),
        "winner": extract_section(full_log, headers["winner"], all_markers)
        .replace(headers["winner"], "")
        .strip(),
    }
    granular_stats = parse_granularity_consolidated(logs, manual_no_pref)
    return {**logs, **granular_stats}


def generate_and_analyze():
    # --- PRE-CALCULATIONS ---
    unique_ballot_types = len(VALID_SCORES) ** NUM_CANDIDATES
    n = unique_ballot_types
    k = NUM_BALLOTS
    total_combinations = math.comb(n + k - 1, k)
    total_chunks = math.ceil(total_combinations / ROWS_PER_FILE)

    # 1. Prepare Parameter Block
    param_block = (
        f"⚠️ AUDIT CONFIG ⚠️\n"
        f"Candidates: {NUM_CANDIDATES}\n"
        f"Ballots: {NUM_BALLOTS}\n"
        f"Scores: {VALID_SCORES}\n"
        f"Total Permutations: {total_combinations:,}\n"
        f"Strategy: First {SAVE_FIRST_CHUNKS} & Last {SAVE_LAST_CHUNKS} chunks\n"
        f"----------------------------------\n"
    )
    print(param_block)

    candidates = [chr(65 + i) for i in range(NUM_CANDIDATES)]
    menu = list(itertools.product(VALID_SCORES, repeat=NUM_CANDIDATES))
    profiles_iter = itertools.combinations_with_replacement(menu, NUM_BALLOTS)

    max_score_setting = max(VALID_SCORES)

    # 2. Filename Logic
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    scores_str = "".join(map(str, VALID_SCORES))
    base_filename = f"sim_star_crunch_C{NUM_CANDIDATES}_B{NUM_BALLOTS}_Scores_{scores_str}_{timestamp}"

    # 3. Headers
    csv_columns = [
        "row_nr",
        "ballot",
        "Winner",
        "CW",
        "Div?",
        "log_scoring_main",
        "sc_tie_type",
        "sc_1st",
        "log_scoring_break1",
        "sc_br1_tie_type",
        "sc_br1_1st",
        "sc_br1_no_pref",
        "log_scoring_break2",
        "sc_br2_tie_type",
        "sc_br2_1st",
        "sc_br2_no_pref",
        "log_runoff",
        "ro_tie_type",
        "ro_1st",
        "ro_no_pref",
        "log_break1",
        "br1_1st",
        "log_break2",
        "br2_1st",
    ]

    current_file = None
    writer = None
    active_chunk_index = -1
    first_row_written = False

    try:
        for i, ballot_set in enumerate(profiles_iter):
            chunk_index = i // ROWS_PER_FILE
            is_start_block = chunk_index < SAVE_FIRST_CHUNKS
            is_end_block = chunk_index >= (total_chunks - SAVE_LAST_CHUNKS)

            if not (is_start_block or is_end_block):
                if i % 1_000_000 == 0:
                    print(f"⏩ Skipping row {i:,} (Middle Zone)...", end="\r")
                continue

            if chunk_index != active_chunk_index:
                if current_file:
                    current_file.close()

                part_filename = f"{base_filename}_part{chunk_index:05d}.csv"
                current_file = open(
                    part_filename, mode="w", newline="", encoding="utf-8-sig"
                )

                writer = csv.writer(current_file)
                writer.writerow(csv_columns)

                print(f"\n📂 Creating/Writing chunk {chunk_index}: {part_filename}")
                active_chunk_index = chunk_index

            ballot_strs = ["".join(map(str, b)) for b in ballot_set]
            ballot_display = "_".join(ballot_strs)
            ballot_dicts = []

            # --- Calculate Total Scores for Divergence Check ---
            total_scores = {c: 0 for c in candidates}

            for b_tuple in ballot_set:
                b_dict = {candidates[j]: val for j, val in enumerate(b_tuple)}
                ballot_dicts.append(b_dict)
                for c, s in b_dict.items():
                    total_scores[c] += s

            # Solve Election
            data = solve_star_election_with_full_blocks(
                ballot_dicts, candidates, max_score_setting, "0"
            )

            if not first_row_written:
                data["log_scoring_main"] = param_block + data["log_scoring_main"]
                first_row_written = True

            # --- Score vs Runoff Divergence Logic ---
            # 1. Who got the most points?
            max_score_val = max(total_scores.values())
            score_leaders = sorted([c for c, s in total_scores.items() if s == max_score_val])

            # 2. Is the winner one of the score leaders?
            star_winner = data["winner"]
            divergence_flag = "N"

            if star_winner not in score_leaders:
                # Format: Y: {ScoreLeaders}=>{Winner}
                # e.g., "Y: AC=>B" or "Y: A=>B"
                leaders_str = "".join(score_leaders)
                divergence_flag = f"Y: {leaders_str}=>{star_winner}"

            # 3. Calculate CW (Just for display)
            cw = get_condorcet_winner(ballot_dicts, candidates)
            cw_str = cw if cw else "Cycle"

            row = [
                i + 1,
                ballot_display,
                data["winner"],
                cw_str,
                divergence_flag,
                data["log_scoring_main"],
                data["sc_tie_type"],
                data["sc_1st"],
                data["log_scoring_break1"],
                data["sc_br1_tie_type"],
                data["sc_br1_1st"],
                data["sc_br1_no_pref"],
                data["log_scoring_break2"],
                data["sc_br2_tie_type"],
                data["sc_br2_1st"],
                data["sc_br2_no_pref"],
                data["log_runoff"],
                data["ro_tie_type"],
                data["ro_1st"],
                data["ro_no_pref"],
                data["log_break1"],
                data["br1_1st"],
                data["log_break2"],
                data["br2_1st"],
            ]
            writer.writerow(row)

            if i % 1000 == 0:
                print(f"✍️  Processed {i:,} rows...", end="\r")

    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user.")
    finally:
        if current_file:
            current_file.close()
        print(
            f"\n✅ Done. Checked start and end of {total_combinations:,} combinations."
        )


if __name__ == "__main__":
    generate_and_analyze()