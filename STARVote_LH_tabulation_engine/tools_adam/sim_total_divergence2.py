"""
Combined Script:
1. Engine: Random Search (Target: Condorcet != Score != STAR)
2. Output: Exact Legacy CSV Format (24 Columns)
"""

import sys
import csv
import io
import contextlib
import re
import random
import starvote
from starvote import Tiebreaker

# --- CONFIGURATION ---
NUM_CANDIDATES = 4
NUM_BALLOTS = 7
SCORE_RANGE = [0, 1, 2, 3, 4, 5]
TARGET_FOUND = 5  # Stop after finding this many cases
OUTPUT_FILENAME = "divergence_detailed_results.csv"
# ---------------------


class SilentSequenceTiebreaker(Tiebreaker):
    def __init__(self, mode="left"):
        self.mode = mode

    def __call__(self, options, tie, desired, exception):
        ranked = sorted(list(tie))
        return ranked[:desired]


# --- SEARCH HELPERS (FAST) ---


def get_condorcet_winner(ballots, candidates):
    for cand in candidates:
        beaten_all = True
        for opp in candidates:
            if cand == opp:
                continue
            c_wins = 0
            o_wins = 0
            for b in ballots:
                if b[cand] > b[opp]:
                    c_wins += 1
                elif b[opp] > b[cand]:
                    o_wins += 1
            if not (c_wins > o_wins):
                beaten_all = False
                break
        if beaten_all:
            return cand
    return None


def get_score_winner(ballots, candidates):
    totals = {c: sum(b[c] for b in ballots) for c in candidates}
    sorted_cands = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_cands[0][0], totals


def get_star_winner_quick(ballots, candidates, totals):
    sorted_cands = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    f1, f2 = sorted_cands[0][0], sorted_cands[1][0]
    votes_f1 = sum(1 for b in ballots if b[f1] > b[f2])
    votes_f2 = sum(1 for b in ballots if b[f2] > b[f1])
    if votes_f1 > votes_f2:
        return f1
    elif votes_f2 > votes_f1:
        return f2
    return None


# --- LEGACY PARSING LOGIC (EXACT COPY) ---


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


# --- MAIN EXECUTION ---


def main():
    print(f"🔎 Random Search: {NUM_CANDIDATES} Candidates, {NUM_BALLOTS} Ballots")
    print(f"🎯 Target: {TARGET_FOUND} Triple Divergence Cases")

    candidates = [chr(65 + i) for i in range(NUM_CANDIDATES)]
    max_score_setting = max(SCORE_RANGE)

    # 24 Exact Columns from original script
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

    with open(OUTPUT_FILENAME, mode="w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_columns)

        found_count = 0
        attempts = 0

        while found_count < TARGET_FOUND:
            attempts += 1
            if attempts % 10000 == 0:
                print(
                    f"   ...checked {attempts:,} scenarios...",
                    end="\r",
                    file=sys.stderr,
                )

            # 1. Generate Random
            ballots_dicts = [
                {c: random.choice(SCORE_RANGE) for c in candidates}
                for _ in range(NUM_BALLOTS)
            ]

            # 2. Check for Triple Divergence (CW != Score != STAR)
            cw = get_condorcet_winner(ballots_dicts, candidates)
            if not cw:
                continue

            sw, totals = get_score_winner(ballots_dicts, candidates)
            if sw == cw:
                continue

            star_quick = get_star_winner_quick(ballots_dicts, candidates, totals)
            if not star_quick:
                continue

            if (sw != star_quick) and (star_quick != cw):
                found_count += 1

                # 3. Generate Full Data for CSV
                ballot_strs = [
                    "".join(str(b[c]) for c in candidates) for b in ballots_dicts
                ]
                ballot_display = "_".join(sorted(ballot_strs))

                # Run FULL Analysis (Parsing logs etc)
                data = solve_star_election_with_full_blocks(
                    ballots_dicts, candidates, max_score_setting, "0"
                )

                # Divergence Flag Formatting
                max_score_val = max(totals.values())
                score_leaders = sorted(
                    [c for c, s in totals.items() if s == max_score_val]
                )
                div_flag = f"Y: {''.join(score_leaders)}=>{data['winner']}"

                # 4. Write Exact Legacy Row
                row = [
                    found_count,
                    ballot_display,
                    data["winner"],
                    cw,
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
                csvfile.flush()
                print(
                    f"✅ Found #{found_count}: CW={cw} / Score={sw} / STAR={data['winner']}"
                )

    print(f"\n🎉 Done! Saved to {OUTPUT_FILENAME}")


if __name__ == "__main__":
    main()
