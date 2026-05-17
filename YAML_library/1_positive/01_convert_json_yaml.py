import json
import yaml
import re
import sys
import io
from contextlib import redirect_stdout
from pathlib import Path


# 1. Custom string class to force the YAML block scalar (|) style
class LiteralString(str):
    pass


def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')


yaml.add_representer(LiteralString, literal_str_representer)


# 2. Custom dict class to force inline YAML (flow style)
class FlowDict(dict):
    pass


def flow_dict_representer(dumper, data):
    # flow_style=True forces the {key: value, key: value} format
    return dumper.represent_mapping('tag:yaml.org,2002:map', data, flow_style=True)


yaml.add_representer(FlowDict, flow_dict_representer)


def get_cand_id(index):
    """Generates sequential IDs: A-Z, then a-z, then C53+ as a fallback."""
    if index < 26:
        return chr(65 + index)  # 0-25 -> A, B, C ... Z
    elif index < 52:
        return chr(97 + index - 26)  # 26-51 -> a, b, c ... z
    else:
        return f"C{index + 1}"  # 52+ -> C53, C54 (Safe fallback)


def extract_categories_and_clean(desc):
    """
    Looks for 'cat:' or 'Cat:' in the description.
    Returns a tuple: (cleaned_description, categories_string)
    """
    if not desc:
        return "", ""

    # Case-insensitive split on 'cat:'
    parts = re.split(r'(?i)cat:\s*', desc, maxsplit=1)

    if len(parts) > 1:
        clean_desc = parts[0].strip()
        # Remove trailing punctuation (like a period or comma) left before 'cat:'
        clean_desc = re.sub(r'[,.\s]+$', '', clean_desc)
        cats = parts[1].strip()
        return clean_desc, cats

    return desc.strip(), ""


def format_description(text):
    """
    Cleans up text to force PyYAML to use block style (|).
    Strips trailing spaces from individual lines which cause PyYAML to fallback to quotes.
    """
    if not text:
        return LiteralString("")
    # In case the JSON loaded literal '\n' instead of actual newlines
    text = text.replace('\\n', '\n')
    # Strip trailing whitespace from each line, but keep the newlines
    clean_lines = [line.rstrip() for line in text.splitlines()]
    # Rejoin and wrap in LiteralString
    return LiteralString("\n".join(clean_lines))


def convert_election_data(input_json_path, engine_module):
    with open(input_json_path, 'r') as file:
        data = json.load(file)

    election = data.get("Election", {})
    raw_ballots = data.get("Ballots", [])
    election_id = election.get("election_id", "noid")
    raw_title = election.get("title", "").strip()

    # Extract BV prefix from title (e.g., "BV10a best book" -> "BV10a", "best book")
    bv_prefix = ""
    clean_title = raw_title
    bv_match = re.match(r'(?i)^(BV[a-zA-Z0-9]{2,4})[\s_-]*(.*)', raw_title)
    if bv_match:
        bv_prefix = bv_match.group(1)
        clean_title = bv_match.group(2).strip()

    # Extract categories and clean description at the Election level
    orig_election_desc = election.get("description") or ""
    clean_elec_desc, elec_cats = extract_categories_and_clean(orig_election_desc)

    new_elec_desc = clean_elec_desc
    if election_id:
        new_elec_desc = f"{clean_elec_desc} BV id - {election_id}" if clean_elec_desc else f"BV id - {election_id}"

    minimal_data = {
        "election": {
            "election_title": raw_title,
            "election_description": format_description(new_elec_desc.strip(" -")),
            "races": []
        }
    }

    # If categories were found at the root election level, add them
    if elec_cats:
        minimal_data["election"]["categories"] = elec_cats

    # Variables for filename generation (derived from the primary/first race)
    primary_method_code = "U"
    primary_num_winners = 1

    for idx, race in enumerate(election.get("races", [])):
        race_id = race.get("race_id")
        num_winners = race.get("num_winners", 1)
        raw_method = race.get("voting_method", "")

        # Standardize voting method terminology
        voting_method = raw_method
        if num_winners > 1:
            if raw_method == "STAR":
                voting_method = "Bloc STAR"
            elif raw_method == "Approval":
                voting_method = "Approval Multiwinner"
        elif raw_method == "RankedRobin":
            voting_method = "RCV-RR"

        # Map to filename codes
        method_map = {
            "STAR": "S", "Approval": "A", "RCV-RR": "R", "RCV-IRV": "I", "Plurality": "P",
            "Approval Multiwinner": "AM", "Bloc STAR": "B",
            "Allocated Score Voting (ASV)": "AS", "Reweighted Range Voting (RRV)": "RR",
            "Sequentially Spent Score (SSS)": "SS"
        }
        method_code = method_map.get(voting_method, "U")

        # Capture primary race details for the filename
        if idx == 0:
            primary_method_code = method_code
            primary_num_winners = num_winners

        # Extract categories and clean description at the Race level
        orig_race_desc = race.get("description") or ""
        clean_race_desc, race_cats = extract_categories_and_clean(orig_race_desc)

        candidates = race.get("candidates", [])
        cand_ids = []
        formatted_candidates = []
        uuid_to_cand_id = {}
        used_ids = set()

        for index, c in enumerate(candidates):
            old_uuid = c.get("candidate_id")
            name = c.get("candidate_name", "").strip()

            # Determine candidate ID:
            if len(name) == 1 and name.isalpha():
                new_cand_id = name
            elif isinstance(old_uuid, str) and len(old_uuid.strip()) == 1 and old_uuid.strip().isalpha():
                new_cand_id = old_uuid.strip()
            else:
                fallback_idx = index
                new_cand_id = get_cand_id(fallback_idx)
                while new_cand_id in used_ids:
                    fallback_idx += 1
                    new_cand_id = get_cand_id(fallback_idx)

            used_ids.add(new_cand_id)
            uuid_to_cand_id[old_uuid] = new_cand_id
            cand_ids.append(new_cand_id)

            formatted_candidates.append(FlowDict({
                "cand_id": new_cand_id,
                "candidate_name": name or c.get("candidate_name", "")
            }))

        race_ballots = []
        for b in raw_ballots:
            vote_for_race = next((v for v in b.get("votes", []) if v.get("race_id") == race_id), None)

            if vote_for_race:
                score_map = {}
                for s in vote_for_race.get("scores", []):
                    raw_score = s.get("score")
                    score_map[s.get("candidate_id")] = str(raw_score) if raw_score is not None else "-"

                score_list = [score_map.get(c.get("candidate_id"), "-") for c in candidates]

                # Append raw scores directly (No 1: prefix)
                race_ballots.append(",".join(score_list))

        if race_ballots:
            header = ",".join(cand_ids)
            csv_string = header + "\n" + "\n".join(race_ballots)
        else:
            csv_string = ",".join(cand_ids) + "\n"

        formatted_ballots = LiteralString(csv_string)

        # --- Build the race dictionary dynamically ---
        minimal_race = {}

        if race_id is not None:
            minimal_race["race_id"] = race_id

        race_title_val = race.get("title", "").strip()
        if race_title_val and race_title_val != clean_title and race_title_val != raw_title:
            minimal_race["race_title"] = race_title_val

        minimal_race["race_description"] = format_description(clean_race_desc)

        if race_cats:
            minimal_race["categories"] = race_cats

        minimal_race.update({
            "num_winners": num_winners,
            "voting_method": voting_method,
            "candidates": formatted_candidates,
            "ballots": formatted_ballots
        })

        # --- Generate Expected Results using add_extra_expl ---
        expected_winners = []
        analysis_log = ""

        if engine_module and "STAR" in voting_method:
            try:
                import starvote
                # 1. Run silently for clean array of winners using exact number of seats
                _, parsed_ballots = engine_module.parse_ballots_from_string(csv_string)
                if parsed_ballots:
                    tb = engine_module.SequenceTiebreaker(mode='left', silent=True)
                    winners_set = starvote.election(
                        method=starvote.star,
                        ballots=parsed_ballots,
                        seats=num_winners,
                        tiebreaker=tb,
                        verbosity=0,
                        maximum_score=5
                    )
                    expected_winners = list(winners_set) if winners_set else []

                # 2. Capture rich matrices & analysis output by redirecting stdout
                log_capture = io.StringIO()
                with redirect_stdout(log_capture):
                    engine_module.run_election(
                        csv_input=csv_string,
                        mode="left",
                        manual_list=[],
                        seed=42
                    )
                # Filter out potential ANSI color codes for clean YAML
                raw_log = log_capture.getvalue()
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                analysis_log = ansi_escape.sub('', raw_log).strip()

            except Exception as e:
                analysis_log = f"Error generating expected results: {e}"

        minimal_race["expected_results"] = {
            "winners": expected_winners,
            "analysis_log": format_description(analysis_log)
        }
        # ----------------------------------------------------

        minimal_data["election"]["races"].append(minimal_race)

    # --- Filename Generation ---
    tie_code = "T" if "tie" in (elec_cats + orig_race_desc).lower() else "N"
    clean_title_alpha = re.sub(r'[^a-zA-Z0-9\s]', '', clean_title).strip()
    pascal_title = "".join(word.capitalize() for word in clean_title_alpha.split()) or "Election"

    bv_part = f"{bv_prefix}_" if bv_prefix else ""
    base_filename = f"{primary_method_code}W{primary_num_winners}_{tie_code}_{bv_part}{pascal_title}_{election_id}"

    yaml_filename = f"{base_filename}.yaml"
    json_filename = f"{base_filename}.json"

    output_yaml_path = Path(input_json_path).parent / yaml_filename

    with open(output_yaml_path, 'w') as file:
        yaml.dump(minimal_data, file, default_flow_style=False, sort_keys=False)

    print(f"Generated: {yaml_filename}")

    original_json_path = Path(input_json_path)
    new_json_path = original_json_path.parent / json_filename

    if original_json_path.name != json_filename:
        original_json_path.rename(new_json_path)
        print(f"Renamed original JSON to: {json_filename}\n")


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent

    # Locate STARVote_LH_tabulation_engine by traversing up the tree
    project_root = script_dir.parent.parent
    engine_dir = project_root / "STARVote_LH_tabulation_engine"

    engine_module = None
    if engine_dir.exists():
        if str(engine_dir) not in sys.path:
            sys.path.append(str(engine_dir))
        try:
            import add_extra_expl as engine_module
        except ImportError as e:
            print(f"Warning: Could not import add_extra_expl. Expected results will be skipped. ({e})")
    else:
        print(f"Warning: Engine directory not found at {engine_dir}")

    input_files = list(script_dir.glob("*.json"))

    if not input_files:
        print(f"No JSON files found in {script_dir}")
    else:
        for input_file in input_files:
            convert_election_data(str(input_file), engine_module)