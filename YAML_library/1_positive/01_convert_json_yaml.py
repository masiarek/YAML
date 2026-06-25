import json
import yaml
import re
import sys
import io
from contextlib import redirect_stdout
from pathlib import Path

try:
    import starvote
except ImportError:
    starvote = None


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


# 2b. Custom list class to force inline YAML (flow style), e.g. [E, C, F, B, D, A]
class FlowList(list):
    pass


def flow_list_representer(dumper, data):
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)


yaml.add_representer(FlowList, flow_list_representer)


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


def extract_lot_order(result, uuid_to_cid):
    """Translate a BetterVoting Results entry's official tie-break order into a
    list of cand_ids in priority order (index 0 = highest priority, wins ties).

    Prefers the explicit `perm` array; falls back to sorting the result's
    candidates by their `tieBreakOrder` (ascending = higher priority). Returns
    [] when no order is available (older exports without the sequence).
    """
    if not isinstance(result, dict):
        return []

    ordered_uuids = []
    perm = result.get("perm")
    if isinstance(perm, list) and perm:
        ordered_uuids = perm
    else:
        # Fallback: gather candidates from summaryData/elected/other and sort by
        # tieBreakOrder ascending.
        cands = []
        sd = result.get("summaryData")
        if isinstance(sd, dict) and isinstance(sd.get("candidates"), list):
            cands = sd["candidates"]
        else:
            cands = (result.get("elected") or []) + (result.get("other") or [])
        cands = [c for c in cands if isinstance(c, dict) and c.get("tieBreakOrder") is not None]
        ordered_uuids = [c.get("id") for c in sorted(cands, key=lambda c: c.get("tieBreakOrder"))]

    # Map UUIDs -> cand_ids, dropping any that don't resolve.
    lot = [uuid_to_cid[u] for u in ordered_uuids if u in uuid_to_cid]
    return lot


def convert_election_data(input_json_path, engine_module):
    with open(input_json_path, 'r') as file:
        data = json.load(file)

    election = data.get("Election", {})
    raw_ballots = data.get("Ballots", [])
    raw_results = data.get("Results", [])
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
    all_race_descs = []

    # Pre-index ballots by race_id to avoid O(n²) lookup in the race loop
    ballots_by_race = {}
    for b in raw_ballots:
        for v in b.get("votes", []):
            ballots_by_race.setdefault(v.get("race_id"), []).append((b, v))

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
        all_race_descs.append(orig_race_desc)
        clean_race_desc, race_cats = extract_categories_and_clean(orig_race_desc)

        candidates = race.get("candidates", [])
        cand_ids = []
        formatted_candidates = []
        used_ids = set()
        # Map each source candidate UUID -> the new cand_id. Needed to translate
        # the provider's tie-break order (which references UUIDs) into the
        # cand_ids the ballots/engine actually use.
        uuid_to_cid = {}

        for index, c in enumerate(candidates):
            old_uuid = c.get("candidate_id")
            name = c.get("candidate_name", "").strip()

            # cand_id is the candidate's REAL NAME, verbatim (e.g. "Chocolate",
            # "Chocolate Chip"). A single-letter name naturally stays itself
            # ("A" -> "A"), so abstract A/B/C elections still read cleanly.
            # Sequential letter codes (A, B, C, ...) are now only a FALLBACK,
            # used when a candidate has no name at all.
            if name:
                base_id = name
            elif isinstance(old_uuid, str) and old_uuid.strip():
                base_id = old_uuid.strip()
            else:
                base_id = get_cand_id(index)

            # cand_ids become the CSV ballot header (comma-separated) and the
            # lot_numbers list, so a literal comma would corrupt the columns.
            # Names don't normally contain commas; replace defensively if one
            # slips through (candidate_name below keeps the original text).
            base_id = base_id.replace(",", " ").strip()

            # Guarantee uniqueness. BetterVoting normally enforces distinct
            # candidate names already; this only disambiguates an accidental
            # collision (e.g. two "Chocolate" -> "Chocolate", "Chocolate (2)").
            new_cand_id = base_id
            dup = 2
            while new_cand_id in used_ids:
                new_cand_id = f"{base_id} ({dup})"
                dup += 1

            used_ids.add(new_cand_id)
            cand_ids.append(new_cand_id)
            if old_uuid is not None:
                uuid_to_cid[old_uuid] = new_cand_id

            formatted_candidates.append(FlowDict({
                "cand_id": new_cand_id,
                "candidate_name": name
            }))

        # Per-ballot score strings in candidate (column) order. A missing score
        # is shown as "-" (blank marker); the engine reads that as 0.
        score_rows = []
        for _b, vote_for_race in ballots_by_race.get(race_id, []):
            score_map = {}
            for s in vote_for_race.get("scores", []):
                raw_score = s.get("score")
                score_map[s.get("candidate_id")] = str(raw_score) if raw_score is not None else "-"
            score_rows.append([score_map.get(c.get("candidate_id"), "-") for c in candidates])

        # Align each column so every score sits directly under its candidate
        # header. The engine strips whitespace around every cell, so this padding
        # is purely cosmetic and parses identically (header and rows share the
        # same ", " separator, keeping columns lined up).
        grid = [cand_ids] + score_rows
        col_w = [max(len(row[i]) for row in grid) for i in range(len(cand_ids))]

        def _fmt_row(cells, _w=col_w):
            return ", ".join(cell.rjust(_w[i]) for i, cell in enumerate(cells))

        if score_rows:
            csv_string = "\n".join(_fmt_row(r) for r in grid)
        else:
            csv_string = _fmt_row(cand_ids) + "\n"

        formatted_ballots = LiteralString(csv_string)

        # Engine-input copy: blanks/markers -> "0" PER CELL (not a blanket string
        # replace), so a candidate name containing '-' is never corrupted.
        tab_rows = [[(c if c.isdigit() else "0") for c in row] for row in score_rows]
        if tab_rows:
            tabulation_csv = "\n".join(_fmt_row(r) for r in ([cand_ids] + tab_rows))
        else:
            tabulation_csv = _fmt_row(cand_ids) + "\n"

        # --- Official tie-break lot order (from the provider's Results) ---
        # Results entries align with races by index; translate the UUID-based
        # order into cand_ids so the engine reproduces the provider's tiebreak.
        race_result = raw_results[idx] if idx < len(raw_results) else {}
        lot_list = extract_lot_order(race_result, uuid_to_cid)

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

        # Persist the official lot order (inline list) so re-tabulation by the
        # engine reproduces the provider's exact tiebreak. Omitted when absent.
        if lot_list:
            minimal_race["lot_numbers"] = FlowList(lot_list)

        # --- Generate Expected Results using add_extra_expl ---
        expected_winners = []
        analysis_log = ""

        if engine_module and starvote and "STAR" in voting_method:
            try:
                # tabulation_csv (built above) is the engine-input copy with
                # blanks/markers already mapped to "0" per cell.

                # 1. Run silently for clean array of winners using exact number of seats
                # (parse_ballots_from_string returns (candidates, ballots, display_rows))
                _, parsed_ballots, _ = engine_module.parse_ballots_from_string(tabulation_csv)
                if parsed_ballots:
                    tb = engine_module.LotNumberTiebreaker(lot_numbers=lot_list, silent=True)
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
                        csv_input=tabulation_csv,
                        lot_numbers=lot_list,
                        show_matrix=True
                    )
                # Filter out potential ANSI color codes for clean YAML
                raw_log = log_capture.getvalue()
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                analysis_log = ansi_escape.sub('', raw_log).strip()

            except Exception as e:
                analysis_log = f"Error generating expected results: {e}"

        minimal_race["expected_results"] = {
            "winners": expected_winners,
            "report": format_description(analysis_log)  # Changed from analysis_log to report
        }
        # ----------------------------------------------------

        minimal_data["election"]["races"].append(minimal_race)

    # --- Filename Generation ---
    tie_code = "T" if "tie" in (elec_cats + " ".join(all_race_descs)).lower() else "N"
    clean_title_alpha = re.sub(r'[^a-zA-Z0-9\s]', '', clean_title).strip()
    pascal_title = "".join(word.capitalize() for word in clean_title_alpha.split()) or "Election"

    bv_part = f"{bv_prefix}_" if bv_prefix else ""
    base_filename = f"{primary_method_code}_W{primary_num_winners}_{tie_code}_{bv_part}{pascal_title}_{election_id}"

    yaml_filename = f"{base_filename}.yaml"
    json_filename = f"{base_filename}.json"

    # Write generated YAML into a "_generated/" staging subfolder so it can never
    # overwrite hand-refined test-case YAML living alongside the JSON sources.
    out_dir = Path(input_json_path).parent / "_generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    output_yaml_path = out_dir / yaml_filename

    with open(output_yaml_path, 'w') as file:
        # allow_unicode=True is required so non-ASCII characters in the report
        # (e.g. the em-dash in "Winner — STAR…") are written literally. Without
        # it PyYAML must escape them, which forces the whole `report` scalar into
        # an ugly escaped double-quoted blob instead of a clean `|-` block.
        yaml.dump(minimal_data, file, default_flow_style=False, sort_keys=False,
                  allow_unicode=True)

    print(f"Generated: _generated/{yaml_filename}")

    original_json_path = Path(input_json_path)
    new_json_path = original_json_path.parent / json_filename

    if original_json_path.name != json_filename:
        # Use replace() instead of rename() to overwrite existing files on Windows
        original_json_path.replace(new_json_path)
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
            import starvote_larry_hastings as engine_module
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