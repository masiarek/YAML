"""
Unified STAR Voting Script:
1. Deterministic Generator (First/Last Chunks)
2. Triple Divergence Hunter (Appends rare anomalies at the end)
"""

import csv
import itertools
import datetime
import io
import contextlib
import re
import math
import random
import time
import starvote
from starvote import Tiebreaker

# --- CONFIGURATION ---
NUM_CANDIDATES = 3
NUM_BALLOTS = 5
VALID_SCORES = [0, 2, 3, 4, 5]

# Chunking Config
ROWS_PER_FILE = 3000
SAVE_FIRST_CHUNKS = 2
SAVE_LAST_CHUNKS = 2

# Hunter Config (The new feature)
SEARCH_TIME_LIMIT = 10  # Seconds to hunt for anomalies at the end
# ---------------------


class SilentSequenceTiebreaker(Tiebreaker):
    def __init__(self, mode="left"):
        self.mode = mode

    def __call__(self, options, tie, desired, exception):
        ranked = sorted(list(tie))
        return ranked[:desired]


# --- FAST CHECKS FOR HUNTER ---
def get_condorcet_winner(ballots, candidates):
    for cand in candidates:
        beaten_all = True
        for opp in candidates:
            if cand == opp:
                continue
            c_wins = sum(1 for b in ballots if b.get(cand, 0) > b.get(opp, 0))
            o_wins = sum(1 for b in ballots if b.get(opp, 0) > b.get(cand, 0))
            if not (c_wins > o_wins):
                beaten_all = False
                break
        if beaten_all:
            return cand
    return None


def get_score_winner(ballots, candidates):
    totals = {c: sum(b.get(c, 0) for b in ballots) for c in candidates}
    # Sort for deterministic stability on ties
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_totals[0][0], totals


def get_star_winner_quick(ballots, candidates, totals):
    """
    Calculates STAR winner with correct Scoring Round Tiebreaker logic.
    """
    # 1. Scoring Round
    sorted_cands = sorted(totals.items(), key=lambda x: x[1], reverse=True)

    # Needs at least 2 candidates
    if len(sorted_cands) < 2:
        return sorted_cands[0][0]

    finalist_a = sorted_cands[0][0]
    finalist_b = sorted_cands[1][0]

    # --- TIEBREAKER CHECK (Crucial Fix) ---
    # If 2nd and 3rd place are tied in score, use Head-to-Head to decide finalist_b
    if len(sorted_cands) > 2:
        score_2nd = sorted_cands[1][1]
        score_3rd = sorted_cands[2][1]

        if score_2nd == score_3rd:
            cand_2 = finalist_b
            cand_3 = sorted_cands[2][0]

            # Check preferences
            votes_for_2 = 0
            votes_for_3 = 0
            for b in ballots:
                if b.get(cand_2, 0) > b.get(cand_3, 0):
                    votes_for_2 += 1
                elif b.get(cand_3, 0) > b.get(cand_2, 0):
                    votes_for_3 += 1

            # If 3rd place wins H2H, they become the finalist
            if votes_for_3 > votes_for_2:
                finalist_b = cand_3

    # 2. Runoff Round
    v1 = sum(1 for b in ballots if b.get(finalist_a, 0) > b.get(finalist_b, 0))
    v2 = sum(1 for b in ballots if b.get(finalist_b, 0) > b.get(finalist_a, 0))

    if v1 > v2:
        return finalist_a
    elif v2 > v1:
        return finalist_b
    return None  # Tie in runoff


# --- PARSING & LOGGING ---
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
    formatted = [f"{c[0]}={c[1]}" for c in candidates_list]
    return formatted, no_pref_val


def extract_tie_message(text_block):
    if not text_block:
        return ""
    m = re.search(
        r"There.*?(two|three|four|five|six)-way tie for (first|second)",
        text_block,
        re.IGNORECASE,
    )
    if m:
        num_map = {"two": "2", "three": "3", "four": "4", "five": "5", "six": "6"}
        return f"{num_map.get(m.group(1).lower(), '?')}-way tie ({'1st' if 'first' in m.group(2).lower() else '2nd'})"
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

    def j(c):
        return ", ".join(c)

    sc, _ = parse_candidates_and_nopref(logs["log_scoring_main"])
    stats["sc_1st"] = j(sc)
    stats["sc_tie_type"] = extract_tie_message(logs["log_scoring_main"])

    if logs["log_scoring_break1"]:
        c, np = parse_candidates_and_nopref(logs["log_scoring_break1"])
        stats["sc_br1_1st"], stats["sc_br1_no_pref"] = j(c), np
        stats["sc_br1_tie_type"] = extract_tie_message(logs["log_scoring_break1"])

    ro, _ = parse_candidates_and_nopref(logs["log_runoff"])
    stats["ro_1st"] = j(ro)
    stats["ro_tie_type"] = extract_tie_message(logs["log_runoff"])
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

    log_sc_br1 = extract_section(
        full_log, headers["scoring_br1"], all_markers
    ) or extract_section(full_log, headers["scoring_br1_alt"], all_markers)
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
    return {**logs, **parse_granularity_consolidated(logs, manual_no_pref)}


# --- MAIN ENGINE ---
def generate_and_analyze():
    # 1. Setup
    n_types = len(VALID_SCORES) ** NUM_CANDIDATES
    total_combinations = math.comb(n_types + NUM_BALLOTS - 1, NUM_BALLOTS)
    total_chunks = math.ceil(total_combinations / ROWS_PER_FILE)

    param_block = (
        f"⚠️ CONFIG: C={NUM_CANDIDATES}, B={NUM_BALLOTS}, S={VALID_SCORES}\n"
        f"Total Permutations: {total_combinations:,}"
    )
    print(param_block)

    candidates = [chr(65 + i) for i in range(NUM_CANDIDATES)]
    menu = list(itertools.product(VALID_SCORES, repeat=NUM_CANDIDATES))
    profiles_iter = itertools.combinations_with_replacement(menu, NUM_BALLOTS)
    max_score_setting = max(VALID_SCORES)

    base_filename = f"sim_star_combined_C{NUM_CANDIDATES}_B{NUM_BALLOTS}_{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

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

    last_filename = None
    active_chunk = -1

    # Trackers
    triple_divergence_found = False

    # --- PHASE 1: DETERMINISTIC LOOP ---
    try:
        current_file = None
        writer = None

        for i, ballot_set in enumerate(profiles_iter):
            chunk_index = i // ROWS_PER_FILE
            is_start = chunk_index < SAVE_FIRST_CHUNKS
            is_end = chunk_index >= (total_chunks - SAVE_LAST_CHUNKS)

            if not (is_start or is_end):
                if i % 500_000 == 0:
                    print(f"⏩ Skipping {i:,} (Middle)...", end="\r")
                continue

            if chunk_index != active_chunk:
                if current_file:
                    current_file.close()
                last_filename = f"{base_filename}_part{chunk_index:05d}.csv"
                current_file = open(
                    last_filename, mode="w", newline="", encoding="utf-8-sig"
                )
                writer = csv.writer(current_file)
                writer.writerow(csv_columns)
                print(f"\n📂 Writing chunk {chunk_index}: {last_filename}")
                active_chunk = chunk_index

            # Prepare Data
            b_dicts = [
                {candidates[j]: val for j, val in enumerate(b)} for b in ballot_set
            ]
            b_str = "_".join(["".join(map(str, b)) for b in ballot_set])

            # Solve
            data = solve_star_election_with_full_blocks(
                b_dicts, candidates, max_score_setting, "0"
            )

            # Divergence Check
            totals = {c: sum(b[c] for b in b_dicts) for c in candidates}
            mx = max(totals.values())
            leaders = "".join(sorted([c for c, s in totals.items() if s == mx]))

            div_flag = "N"
            if data["winner"] not in leaders:
                div_flag = f"Y: {leaders}=>{data['winner']}"

            cw = get_condorcet_winner(b_dicts, candidates)
            cw_str = cw if cw else "Cycle"

            # Check Triple Divergence (CW != Score != STAR)
            sw, _ = get_score_winner(b_dicts, candidates)
            # Must ensure all three are different
            if cw and (cw != sw) and (sw != data["winner"]) and (cw != data["winner"]):
                triple_divergence_found = True
                div_flag = "Y: TRIPLE_DIV"

            row = [
                i + 1,
                b_str,
                data["winner"],
                cw_str,
                div_flag,
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
                print(f"✍️  Row {i:,}...", end="\r")

    except KeyboardInterrupt:
        print("\n🛑 Interrupted.")
    finally:
        if current_file:
            current_file.close()

    # --- PHASE 2: THE HUNTER ---
    print("\n\n🔎 Phase 1 Complete. Initiating Hunter Protocol...")

    if last_filename:
        with open(last_filename, mode="a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([])  # Spacer
            writer.writerow(
                ["---", "HUNTER PHASE START", "Searching for Triple Divergence", "---"]
            )

            start_time = time.time()
            found_in_hunter = False
            scenarios_checked = 0

            # Loop until time runs out
            while (time.time() - start_time) < SEARCH_TIME_LIMIT:
                scenarios_checked += 1
                # Generate Random Ballot set
                b_dicts = [
                    {c: random.choice(VALID_SCORES) for c in candidates}
                    for _ in range(NUM_BALLOTS)
                ]

                cw = get_condorcet_winner(b_dicts, candidates)
                if not cw:
                    continue  # Skip cycles

                sw, totals = get_score_winner(b_dicts, candidates)

                # If CW == SW, it cannot be a triple divergence
                if cw == sw:
                    continue

                # Get Fast STAR Winner
                star = get_star_winner_quick(b_dicts, candidates, totals)
                if not star:
                    continue

                # --- CHECK TRIPLE DIVERGENCE ---
                # We need: CW != SW != STAR != CW
                if (sw != star) and (star != cw) and (sw != cw):

                    # Verify with full engine to be safe
                    data = solve_star_election_with_full_blocks(
                        b_dicts, candidates, max_score_setting, "0"
                    )

                    # Double check result matches verification
                    if data["winner"] != star:
                        # This happens if our quick check is still slightly off or tiebreaker differs
                        continue

                    b_str = "_".join(
                        sorted(
                            ["".join(str(b[c]) for c in candidates) for b in b_dicts]
                        )
                    )

                    row = [
                        f"HUNTER_{scenarios_checked}",
                        b_str,
                        data["winner"],
                        cw,
                        "Y: TRIPLE_DIV",
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
                    print(f"🚨 Hunter found anomaly! Appended to {last_filename}")
                    found_in_hunter = True
                    break  # Remove break if you want to find multiple

            if not found_in_hunter:
                msg = f"No triple divergence (CW!=Score!=STAR) found in {SEARCH_TIME_LIMIT}s."
                writer.writerow(["RESULT", msg])
                print(f"🤷 Hunter timed out: {msg}")


if __name__ == "__main__":
    generate_and_analyze()