import json
import yaml
from pathlib import Path


def convert_election_data(input_json_path, output_yaml_path):
    # 1. Open and read the local JSON file
    with open(input_json_path, 'r') as file:
        data = json.load(file)

    election = data.get("Election", {})
    raw_ballots = data.get("Ballots", [])

    # 2. Append election_id to the description (safely handling nulls)
    original_description = election.get("description") or ""
    election_id = election.get("election_id") or ""
    new_description = f"{original_description} {election_id}".strip()

    # 3. Build the minimal structure
    minimal_data = {
        "Election": {
            "title": election.get("title", ""),
            "description": new_description,
            "races": []
        }
    }

    # Extract required fields for each race and candidate
    for race in election.get("races", []):
        race_id = race.get("race_id")
        num_winners = race.get("num_winners", 1)
        voting_method = race.get("voting_method", "")

        # Transform STAR to Bloc STAR for multi-winner races
        if num_winners > 1 and voting_method == "STAR":
            voting_method = "Bloc STAR"

        # Preserve candidate order to correctly map ballot scores
        candidate_ids = [c.get("candidate_id") for c in race.get("candidates", [])]

        # 4. Extract ballots specific to this race
        race_ballots = []
        for b in raw_ballots:
            # Find the vote object that matches this race
            vote_for_race = next((v for v in b.get("votes", []) if v.get("race_id") == race_id), None)

            if vote_for_race:
                # Map the given scores by candidate_id
                score_map = {s.get("candidate_id"): s.get("score") for s in vote_for_race.get("scores", [])}

                # Build the comma-separated score string (A,B,C), defaulting to 0 if a score is missing
                score_list = [str(score_map.get(cid, 0)) for cid in candidate_ids]
                race_ballots.append(",".join(score_list))

        # 5. Assemble the final race object
        minimal_race = {
            "title": race.get("title", ""),
            "description": race.get("description") or "",
            "num_winners": num_winners,
            "voting_method": voting_method,
            "candidates": [
                {"candidate_name": c.get("candidate_name", "")}
                for c in race.get("candidates", [])
            ],
            "ballots": race_ballots
        }
        minimal_data["Election"]["races"].append(minimal_race)

    # 6. Write the strict YAML to a local file
    with open(output_yaml_path, 'w') as file:
        yaml.dump(minimal_data, file, default_flow_style=False, sort_keys=False)

    print(f"Successfully converted '{input_json_path}' to '{output_yaml_path}'")


if __name__ == "__main__":
    INPUT_FILE = "03_d8mgtv.json"

    # Automatically swap the .json extension for .yaml
    OUTPUT_FILE = str(Path(INPUT_FILE).with_suffix(".yaml"))

    convert_election_data(INPUT_FILE, OUTPUT_FILE)