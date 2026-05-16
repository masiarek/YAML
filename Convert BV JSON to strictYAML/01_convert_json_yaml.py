import json
import yaml
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


def convert_election_data(input_json_path, output_yaml_path):
    with open(input_json_path, 'r') as file:
        data = json.load(file)

    election = data.get("Election", {})
    raw_ballots = data.get("Ballots", [])

    original_description = election.get("description") or ""
    election_id = election.get("election_id") or ""
    new_description = f"{original_description} BV id - {election_id}".strip()

    minimal_data = {
        "election": {
            "election_title": election.get("title", ""),
            "election_description": new_description,
            "races": []
        }
    }

    for race in election.get("races", []):
        race_id = race.get("race_id")
        num_winners = race.get("num_winners", 1)
        voting_method = race.get("voting_method", "")

        # Standardize election method terminology
        if num_winners > 1 and voting_method == "STAR":
            voting_method = "Bloc STAR"
        elif voting_method == "RankedRobin":
            voting_method = "RCV-RR"

        candidates = race.get("candidates", [])
        cand_ids = []
        formatted_candidates = []
        uuid_to_cand_id = {}

        for index, c in enumerate(candidates):
            old_uuid = c.get("candidate_id")
            new_cand_id = get_cand_id(index)
            name = c.get("candidate_name", "")

            uuid_to_cand_id[old_uuid] = new_cand_id
            cand_ids.append(new_cand_id)

            formatted_candidates.append(FlowDict({
                "cand_id": new_cand_id,
                "candidate_name": name
            }))

        race_ballots = []
        for b in raw_ballots:
            vote_for_race = next((v for v in b.get("votes", []) if v.get("race_id") == race_id), None)

            if vote_for_race:
                # Safely handle null/None scores by converting them to "-"
                score_map = {}
                for s in vote_for_race.get("scores", []):
                    raw_score = s.get("score")
                    score_map[s.get("candidate_id")] = str(raw_score) if raw_score is not None else "-"

                # Extract scores, using "-" as the ultimate fallback for completely missing candidates
                score_list = [score_map.get(c.get("candidate_id"), "-") for c in candidates]
                race_ballots.append(",".join(score_list))

        if race_ballots:
            header = ",".join(cand_ids)
            csv_string = header + "\n" + "\n".join(race_ballots)
        else:
            csv_string = ",".join(cand_ids) + "\n"

        formatted_ballots = LiteralString(csv_string)

        minimal_race = {
            "race_title": race.get("title", ""),
            "race_description": race.get("description") or "",
            "num_winners": num_winners,
            "voting_method": voting_method,
            "candidates": formatted_candidates,
            "ballots": formatted_ballots
        }
        minimal_data["election"]["races"].append(minimal_race)

    with open(output_yaml_path, 'w') as file:
        yaml.dump(minimal_data, file, default_flow_style=False, sort_keys=False)

    print(f"Successfully converted '{input_json_path}' to '{output_yaml_path}'")


if __name__ == "__main__":
    # Get the directory where this Python script is physically located
    script_dir = Path(__file__).resolve().parent

    # Find all JSON files in the same directory
    input_files = list(script_dir.glob("*.json"))

    if not input_files:
        print(f"No JSON files found in {script_dir}")
    else:
        for input_file in input_files:
            # Generate the corresponding output filename by swapping the extension to .yaml
            output_file = input_file.with_suffix(".yaml")

            # Execute conversion
            convert_election_data(str(input_file), str(output_file))