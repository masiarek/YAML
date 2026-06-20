"""
Script: starvote_larry_hastings.py
Description: Runs a STAR Voting election with detailed tiebreaker analysis and matrix visualization.
"""

import math
import os
import re
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import starvote
from starvote import Tiebreaker

# Optional cross-check against RCV-IRV. The sibling engine vendors pyrankvote
# and the score->rank conversion. If it isn't present, IRV comparison is simply
# skipped and STAR tabulation is unaffected.
try:
    _IRV_ENGINE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "RCV_IRV_tabulation_engine",
    )
    if _IRV_ENGINE not in sys.path:
        sys.path.insert(0, _IRV_ENGINE)
    import pyrankvote as _pyrankvote
    from pyrankvote import Ballot as _IRVBallot, Candidate as _IRVCandidate
    from rcv_irv_tabulation import score_ballot_to_ranking as _score_to_rank
    _IRV_AVAILABLE = True
except Exception:  # pragma: no cover - IRV cross-check is optional
    _IRV_AVAILABLE = False

# --- ANSI Color Codes ---
# Enabled for a real terminal AND for PyCharm's run console (which sets
# PYCHARM_HOSTED and renders ANSI). Disabled when piped to a plain file, so
# redirected output doesn't get littered with escape sequences. Set NO_COLOR
# to force plain output anywhere.
_USE_COLOR = os.environ.get("NO_COLOR") is None and (
    sys.stdout.isatty() or os.environ.get("PYCHARM_HOSTED") == "1"
)
if _USE_COLOR:
    COLOR_GREEN = "\033[92m"
    COLOR_RED = "\033[91m"
    COLOR_BLUE = "\033[94m"
    COLOR_RESET = "\033[0m"
    # Section-header palette (bold). Distinct color per phase.
    COLOR_HEADER = "\033[1;95m"  # bold magenta — banner / fallback
    COLOR_SCORING = "\033[1;96m"  # bold cyan   — Scoring Round (+ its tiebreakers)
    COLOR_RUNOFF = "\033[1;93m"  # bold yellow — Automatic Runoff (+ its tiebreakers)
    COLOR_WINNER = "\033[1;92m"  # bold green  — Winner / Winners
    COLOR_DIM = "\033[2;90m"  # faint gray  — round-separator rule
else:
    COLOR_GREEN = COLOR_RED = COLOR_BLUE = COLOR_RESET = ""
    COLOR_HEADER = COLOR_SCORING = COLOR_RUNOFF = COLOR_WINNER = ""
    COLOR_DIM = ""


def header_color(label):
    """Pick a section-header color by phase, so tiebreaker sub-headers inherit
    the color of their parent round."""
    low = label.lower()
    if "runoff" in low:
        return COLOR_RUNOFF
    if "winner" in low:
        return COLOR_WINNER
    if "scoring" in low:
        return COLOR_SCORING
    return COLOR_HEADER


# --- Ballot marker characters ---
# Any of these (and an empty cell) tabulate as 0; every ballot still counts.
# A legend is printed listing only the markers that actually appear in the data.
MARKER_MEANINGS = {
    "-": "Blank — no score / voter left the candidate blank",
    "~": "Race-level abstention — voter abstained from the entire race",
    "&": "Candidate-level abstention — explicitly abstained for this candidate",
    "?": "Spoiled / voided ballot — overvote, protest mark, or invalid format",
    "%": "Spoiled & re-issued — ballot voided and a replacement was issued",
}

# Ballot-level markers apply to the WHOLE ballot, so they may not be mixed with
# scores — a valid row is the marker in every column (e.g. "~,~,~,~").
BALLOT_LEVEL_MARKERS = {"~", "?", "%"}
# The rest (-, &, ^, empty) are per-candidate and may be mixed freely.


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
            self.expl = (
                "*** No official tie-breaking lot numbers were provided.\n"
                "    Ties are resolved using a fallback order: CSV column order."
            )
        else:
            # PRODUCTION MODE: Use the provided numbers
            self.expl = (
                "*(Ties are resolved by choosing the tied candidate with the "
                "highest-priority official lot number.)*"
            )

        # Create an O(1) lookup map: {Candidate: Priority_Index}
        self.order_map = {c: i for i, c in enumerate(self.lot_numbers)}

    def __call__(self, options, tie, desired, exception):
        # We only enter this function if an actual tie has occurred.

        # Print the explanation if this is the first tie we've encountered
        if not self.info_printed and not self.silent:
            print(f"\n{self.expl}")
            print(f"    Lot-number priority order: {self.lot_numbers}")
            self.info_printed = True

        # Sort tied candidates by their assigned lot number priority
        ranked = sorted(tie, key=lambda c: self.order_map.get(c, float("inf")))
        winners = ranked[:desired]

        if not self.silent:
            print("\n[Tiebreaker: Lot Number Priority]")
            print(f"  Tie among: {tie}")
            print(f"  Resolved: {winners} (selected by lot-number priority).")

        return winners


# ---
# 2. HELPER FUNCTIONS
# ---
# Map a YAML "voting_method" string to a starvote method object.
METHOD_BY_NAME = {
    "star": starvote.star,
    "bloc": starvote.bloc,
    "bloc star": starvote.bloc,
    "sss": starvote.sss,
    "sequentially spent score": starvote.sss,
    "rrv": starvote.rrv,
    "reweighted range voting": starvote.rrv,
    "allocated": starvote.allocated,
    "allocated score voting": starvote.allocated,
}


def _find_race(data, race_index=0):
    """Locate the race-like mapping that holds `ballots`, tolerating both the
    full schema and flattened forms:
      - election.races[i]          (full schema)
      - election.{ballots,...}     (single race under election, no races list)
      - races[i]                   (races list at top level)
      - {ballots,...}              (fully flat, top level)
    """
    if isinstance(data, dict):
        if isinstance(data.get("election"), dict):
            el = data["election"]
            return el["races"][race_index] if "races" in el else el
        if "races" in data:
            return data["races"][race_index]
        if "ballots" in data:
            return data
    raise KeyError("could not find a 'ballots' block in the YAML file")


# Output-control options a YAML file may set (under `options:` or top level).
OPTION_KEYS = (
    "show_matrix",
    "show_condorcet",
    "show_score_counts",
    "brief",
    "collapse_ballots",
    "count_separator",
    "show_irv",
)


def _yaml_lite(text):
    """Extract just the fields we need from the STAR election schema, without
    requiring PyYAML: the first race's `ballots` block (a YAML `|` block
    scalar), `num_winners`, `voting_method`, and any output `options`.
    Returns (ballots_text, seats, method_name, options)."""
    lines = text.splitlines()

    seats = None
    method_name = None
    options = {}
    for ln in lines:
        m = re.match(r"\s*num_winners:\s*(\d+)", ln)
        if m and seats is None:
            seats = int(m.group(1))
        m = re.match(r"\s*voting_method:\s*(\S.*?)\s*$", ln)
        if m and method_name is None:
            method_name = m.group(1).strip().strip("\"'")
        m = re.match(r"\s*([a-z_]+):\s*(\S.*?)\s*$", ln)
        if m and m.group(1) in OPTION_KEYS and m.group(1) not in options:
            options[m.group(1)] = m.group(2).strip().strip("\"'")

    ballots_text = None
    for idx, ln in enumerate(lines):
        key = re.match(r"(\s*)ballots:\s*\|", ln)
        if not key:
            continue
        base = len(key.group(1))
        block = []
        for nxt in lines[idx + 1 :]:
            if nxt.strip() == "":
                block.append("")
                continue
            if len(nxt) - len(nxt.lstrip()) <= base:
                break  # dedent -> end of block
            block.append(nxt)
        nonempty = [b for b in block if b.strip()]
        if nonempty:
            cut = min(len(b) - len(b.lstrip()) for b in nonempty)
            ballots_text = "\n".join(b[cut:] if b.strip() else "" for b in block).strip(
                "\n"
            )
        break
    return ballots_text, seats, method_name, options


def load_election(path, race_index=0):
    """Load an election from a file. Returns a dict:
        {"ballots": str, "seats": int|None, "method": obj|None, "options": dict}

    - .yaml / .yml : reads the race; pulls the `ballots` block, `num_winners`
      -> seats, `voting_method` -> method, and any output `options`. Uses
      PyYAML when available, else a built-in extractor (no install needed).
    - anything else : raw text as ballots; seats/method/options empty.
    """
    p = Path(path)
    if not p.is_absolute() and not p.exists():
        # Resolve relative to this script, so it works regardless of cwd.
        p = Path(__file__).resolve().parent / path
    text = p.read_text(encoding="utf-8")

    if not str(path).lower().endswith((".yaml", ".yml")):
        return {
            "ballots": text,
            "seats": None,
            "method": None,
            "options": {},
            "title": None,
            "description": None,
        }

    title = description = None
    try:
        import yaml  # use PyYAML when present (most robust)

        data = yaml.safe_load(text)
        race = _find_race(data, race_index)
        ballots_text = race["ballots"]
        seats = int(race["num_winners"]) if "num_winners" in race else None
        method_name = race.get("voting_method")
        options = {}
        if isinstance(data, dict) and isinstance(data.get("options"), dict):
            options.update(data["options"])
        if isinstance(race.get("options"), dict):
            options.update(race["options"])

        # Optional human-readable context, looked up on the race first, then the
        # top-level mapping (and an `election:` wrapper if present).
        top = data if isinstance(data, dict) else {}
        el = top.get("election") if isinstance(top.get("election"), dict) else {}

        def _pick(*keys):
            for src in (race, el, top):
                if isinstance(src, dict):
                    for k in keys:
                        v = src.get(k)
                        if v:
                            return str(v).strip()
            return None

        title = _pick("election_title", "title")
        description = _pick(
            "scenario_description", "race_description", "election_description"
        )

        def _num(*keys):
            for src in (race, el, top):
                if isinstance(src, dict):
                    for k in keys:
                        if src.get(k) is not None:
                            return src.get(k)
            return None

        eligible_voters = _num("eligible_voters", "electorate", "registered_voters")
        if eligible_voters is not None:
            eligible_voters = int(eligible_voters)
        quorum = _num("quorum", "minimum_quorum")
    except ImportError:
        ballots_text, seats, method_name, options = _yaml_lite(text)
        eligible_voters = quorum = None

    method = (
        METHOD_BY_NAME.get(str(method_name).strip().lower()) if method_name else None
    )
    return {
        "ballots": ballots_text,
        "seats": seats,
        "method": method,
        "method_name": method_name,
        "options": options,
        "title": title,
        "description": description,
        "eligible_voters": eligible_voters,
        "quorum": quorum,
    }


_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def strip_ansi(s):
    """Remove ANSI color escape sequences (for saving plain text)."""
    return _ANSI_RE.sub("", s)


def save_results_to_file(path, winners, report):
    """Append (or replace) a top-level `expected_results:` block in the file,
    holding the winners and the plain-text tabulation report. Comments and
    formatting elsewhere in the file are preserved (only this block is rewritten).
    """
    p = Path(path)
    if not p.is_absolute() and not p.exists():
        p = Path(__file__).resolve().parent / path
    text = p.read_text(encoding="utf-8")

    # Drop any previous top-level expected_results block (to end of file).
    text = re.sub(r"\n*^expected_results:.*\Z", "", text, flags=re.S | re.M).rstrip(
        "\n"
    )

    winner_lines = "\n".join(f"  - {w}" for w in winners) or "  []"
    report_body = "\n".join(
        ("    " + ln).rstrip() for ln in strip_ansi(report).splitlines()
    )
    block = (
        "\n\nexpected_results:\n"
        f"  winners:\n{winner_lines}\n"
        "  report: |-\n"
        f"{report_body}\n"
    )
    p.write_text(text + "\n" + block, encoding="utf-8")


def tabulated_output_path(src_path):
    """Where to write the plain-text tabulation for an election file.

    The copy goes into a sibling folder whose name is the source folder + the
    '_tabulated' suffix, and the file itself also gets a '_tabulated' suffix.
    Example:
        .../elections_illustrations/02_Multi_winner/foo.yaml
        -> .../elections_illustrations/Multi_winner_tabulated/foo_tabulated.txt
        .../elections_illustrations/bar.yaml
        -> .../elections_illustrations_tabulated/bar_tabulated.txt
    """
    p = Path(src_path).resolve()
    out_dir = p.parent.parent / (p.parent.name + "_tabulated")
    return out_dir / (p.stem + "_tabulated.txt")


def ensure_filename_comment(path):
    """Make sure a YAML election file ends with a '# file: <name>' comment that
    matches its CURRENT name. Rewrites only when missing/stale, so a normal run
    (already correct) changes nothing — no needless edits or editor reloads.
    """
    p = Path(path)
    if p.suffix.lower() not in (".yaml", ".yml"):
        return
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return
    lines = text.splitlines()
    # Drop trailing blanks and any existing '# file:' trailer.
    while lines and (not lines[-1].strip() or lines[-1].lstrip().startswith("# file:")):
        lines.pop()
    desired = "\n".join(lines).rstrip() + f"\n\n# file: {p.name}\n"
    if desired != text:
        try:
            p.write_text(desired, encoding="utf-8")
        except OSError:
            pass  # read-only / locked file: skip silently, don't break the run


def write_tabulated_copy(src_path, output_text):
    """Write the (ANSI-stripped) tabulation text next to its source, under the
    '<folder>_tabulated' mirror folder. Returns the path written."""
    out_path = tabulated_output_path(src_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(strip_ansi(output_text), encoding="utf-8")
    return out_path


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
        return [], [], []

    # Parse Headers
    headers = [name.strip() for name in re.split(r"[,\t]+", lines[0]) if name.strip()]
    if headers and headers[0] == "#":
        headers.pop(0)

    # The first column may carry a "Count" label documenting the colon-weight
    # prefix (e.g. "Count:Chocolate"). It's not part of the candidate name.
    if headers and re.match(r"(?i)^count\s*:", headers[0]):
        headers[0] = headers[0].split(":", 1)[1].strip()

    ballots = []
    display_rows = []  # parallel to ballots; keeps blanks visible as "-"

    def cell_to_score(cell):
        # An empty cell or any marker character counts as 0 (no support),
        # same as an explicit 0. (Markers: see MARKER_MEANINGS.)
        cell = cell.strip()
        if cell == "" or cell in MARKER_MEANINGS:
            return 0
        return int(cell)  # may raise ValueError -> caller falls through

    def display_cell(cell, score):
        # Keep the original marker visible in the echo; blank empty cell -> "-".
        cell = cell.strip()
        if cell == "":
            return "-"
        if cell in MARKER_MEANINGS:
            return cell
        return str(score)

    for line_num, line in enumerate(lines[1:], start=2):
        # 1. Attempt Standard CSV Parse first. Use a single-delimiter split so
        #    blank cells keep their position (e.g. "5,5,,0" or "5,5,4,-").
        parts = re.split(r"[,\t]", line)
        weight = 1

        # Handle "Weight x Score" repetition, e.g. "9:5", "9x5", "9 × 5".
        # Accepted separators: ":", "x"/"X", "×".
        wmatch = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", parts[0])
        if wmatch:
            weight = int(wmatch.group(1))
            parts[0] = wmatch.group(2)

        cells = [p.strip() for p in parts]

        # Whole-ballot markers (~, ?, %) apply to the entire race. They may only
        # appear as a full row of one marker (e.g. "~,~,~,~") or a lone token
        # ("~"); mixing with scores is an error.
        present_ballot_markers = {c for c in cells if c in BALLOT_LEVEL_MARKERS}
        if present_ballot_markers:
            marker = next(iter(present_ballot_markers))
            non_blank = [c for c in cells if c != ""]
            is_whole_ballot = len(present_ballot_markers) == 1 and all(
                c == marker for c in non_blank
            )
            if not is_whole_ballot:
                full_row = ",".join([marker] * len(headers))
                print(
                    f"{COLOR_RED}Error (Line {line_num}):{COLOR_RESET} "
                    f"'{marker}' is a whole-ballot marker "
                    f"({MARKER_MEANINGS[marker].split(' — ')[0]}),\n"
                    f"  so it cannot be mixed with scores.\n"
                    f"  Got:  {line}\n"
                    f"  Fix:  use a full row '{full_row}', or remove '{marker}'."
                )
                sys.exit(1)
            # Valid whole-ballot row: every candidate scores 0, ballot counts.
            ballot = {h: 0 for h in headers}
            display = ",".join([marker] * len(headers))
            for _ in range(weight):
                ballots.append(ballot)
                display_rows.append(display)
            continue

        # Check if this matches Standard CSV (Score count == Header count)
        if len(cells) == len(headers):
            try:
                scores = [cell_to_score(p) for p in cells]
                ballot = {h: s for h, s in zip(headers, scores)}
                # Display keeps the original markers visible (source stays
                # faithful) even though they tabulate as 0.
                display = ",".join(display_cell(c, s) for c, s in zip(cells, scores))
                for _ in range(weight):
                    ballots.append(ballot)
                    display_rows.append(display)
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
                    display_rows.append(",".join(str(s) for s in scores))
                else:
                    # Found a digit-only chunk with wrong length -> WARN USER
                    print(
                        f"{COLOR_RED}Warning (Line {line_num}):{COLOR_RESET} "
                        f"Segment '{seg}' has {len(seg)} digits, but expected {len(headers)} "
                        f"for candidates {headers}. Ignored."
                    )

    return headers, ballots, display_rows


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


def print_matrix(
    candidates, matrix, finalists=None, star_winner=None, finalists_only=False
):
    if not candidates or not matrix:
        return
    if finalists is None:
        finalists = []
    # Optionally restrict the grid to just the two finalists — the decisive
    # head-to-head that determines the STAR runoff.
    if finalists_only and finalists:
        candidates = [c for c in candidates if c in finalists]
    print("\n--- Runoff (Preference) Matrix ---")
    print("Head-to-head / pairwise comparison")
    print(
        f"Legend: {COLOR_GREEN}For{COLOR_RESET} - {COLOR_BLUE}Equal Preference{COLOR_RESET} - {COLOR_RED}Against{COLOR_RESET}"
    )
    print("        * indicates Top 2 Finalist")

    # +4 = 2 for the "* "/"  " finalist prefix + 2 for an even left/right margin,
    # so the longest name still centers instead of sitting flush to the divider.
    col_width = max((len(c) + 4 for c in candidates), default=10)
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


def print_condorcet(candidates, matrix, star_winner=None, finalists=None):
    """Print the Condorcet analysis line on its own (independent of the matrix)."""
    if not candidates or not matrix:
        return
    print("\n[Condorcet Winner]")
    print(f"  {analyze_condorcet(candidates, matrix, star_winner, finalists)}")


def compute_irv_winner(candidates, ballots, priority):
    """
    Tabulate the same election under RCV-IRV and return the winner's name
    (or None if unavailable / no winner).

    The STAR ballots are *scores*; IRV needs *ranks*. Conversion (see
    rcv_irv_tabulation.score_ballot_to_ranking): higher score = higher
    preference, score 0 = unranked. IRV cannot represent equal ranks, so ties
    between equal non-zero scores are broken by `priority` order — the same
    left-to-right candidate priority STAR uses for its tiebreaks. This keeps the
    two methods' tiebreak philosophy aligned (documented for the comparison).
    """
    if not _IRV_AVAILABLE or not candidates or not ballots:
        return None, 0, 0
    order = [c for c in (priority or candidates) if c in candidates]
    for c in candidates:  # include any candidate missing from priority
        if c not in order:
            order.append(c)

    cand_objs = {c: _IRVCandidate(c) for c in candidates}
    pv_ballots = []
    tie_ballots = 0  # ballots whose score->rank order depended on the tiebreak
    for b in ballots:
        # A consequential tie = two ranked (non-zero) candidates share a score,
        # so their relative rank is decided by candidate priority order.
        nonzero = [b[c] for c in candidates if b.get(c, 0) > 0]
        if len(nonzero) != len(set(nonzero)):
            tie_ballots += 1
        ranking = _score_to_rank(b, order)
        pv_ballots.append(_IRVBallot(ranked_candidates=[cand_objs[n] for n in ranking]))

    try:
        result = _pyrankvote.instant_runoff_voting(
            list(cand_objs.values()), pv_ballots
        )
        winners = result.get_winners()
        winner = winners[0].name if winners else None
        return winner, tie_ballots, len(ballots)
    except Exception:  # pragma: no cover
        return None, 0, 0


def approval_winner(candidates, ballots, priority):
    """
    Approval winner (single): a candidate is approved on a ballot for every
    score of 3, 4, or 5 (stars). The candidate with the most approvals wins;
    a tie is broken by `priority` order (left-to-right CSV column sequence) —
    the same tiebreak STAR uses — so a single winner is returned.
    """
    approvals = {
        c: sum(1 for b in ballots if b.get(c, 0) >= 3) for c in candidates
    }
    if not approvals:
        return None
    top = max(approvals.values())
    order = [c for c in (priority or candidates) if c in candidates]
    for c in candidates:  # any candidate missing from priority falls in last
        if c not in order:
            order.append(c)
    tied = [c for c in candidates if approvals[c] == top]
    tied.sort(key=lambda c: order.index(c))
    return tied[0]


def _approval_raw_problems(ballots_text):
    """
    Validate Approval ballots against the RAW source rows (not the parsed
    ballots, which silently drop malformed rows). Returns (headers, problems)
    where each problem is (row_number, raw_line, reason). Catches non-numeric
    cells (e.g. 'a'), out-of-range values (not 0/1), and wrong column counts.
    """
    lines = []
    for raw in ballots_text.strip().splitlines():
        line = raw if raw.strip().startswith("#,") else raw.split("#")[0]
        line = line.strip()
        if line:
            lines.append(line)
    if len(lines) < 2:
        return [], []

    headers = [h.strip() for h in re.split(r"[,\t]+", lines[0]) if h.strip()]
    if headers and headers[0] == "#":
        headers.pop(0)
    if headers and re.match(r"(?i)^count\s*:", headers[0]):
        headers[0] = headers[0].split(":", 1)[1].strip()
    count_col = bool(headers) and headers[0].lower() == "count"
    if count_col:
        headers.pop(0)

    problems = []
    for i, line in enumerate(lines[1:], 1):
        parts = re.split(r"[,\t]", line)
        m = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", parts[0])  # weight prefix
        if m:
            parts = [m.group(2)] + parts[1:]
        cells = [p.strip() for p in parts]
        if count_col and cells:
            cells = cells[1:]
        if len(cells) != len(headers):
            problems.append((i, line,
                             f"has {len(cells)} value(s), expected {len(headers)}"))
            continue
        # Valid Approval cell: "1" = approved; "0", blank, or a recognized
        # marker (e.g. "-") = not approved. Anything else is an error.
        bad = [f"{h}={c}" for h, c in zip(headers, cells)
               if not (c in ("0", "1", "") or c in MARKER_MEANINGS)]
        if bad:
            problems.append((i, line, "invalid: " + ", ".join(bad)))
    return headers, problems


def tabulate_approval(ballots_text, seats=1, priority=None):
    """
    Tabulate an Approval Voting election. Ballots are approvals, so ANY non-zero
    score counts as one approval (unlike the 3+ stars threshold the STAR
    comparison block uses on 0..5 score ballots).

    Single-winner: the most-approved candidate wins. Multi-winner (seats >= 2)
    uses block/at-large approval: the `seats` most-approved candidates win.
    Ties are broken by candidate priority order (left-to-right CSV columns).
    """
    # Validate raw rows first, so malformed ballots error instead of being
    # silently dropped by the shared parser.
    header_names, problems = _approval_raw_problems(ballots_text)
    if problems:
        print(
            f"{COLOR_RED}Error: Approval ballots may only use scores {{0, 1}} "
            f"(0 = not approved, 1 = approved).{COLOR_RESET}\n"
            f"  Offending ballot(s)  [{','.join(header_names)}]:"
        )
        for i, line, reason in problems:
            print(f"    ballot {i}: {line}   ({reason})")
        print(f"  Accepted marks: 1 (approved), 0 / blank / a marker "
              f"({', '.join(MARKER_MEANINGS)}) = not approved.")
        print("  Fix or remove these rows. If they are 0..5 score ballots, set "
              "voting_method to STAR.")
        return

    candidates, ballots, _ = parse_ballots_from_string(ballots_text)
    if not ballots:
        print("Error: No valid ballots found in input.")
        return

    counts = {c: sum(1 for b in ballots if b.get(c, 0) > 0) for c in candidates}
    order = [c for c in (priority or candidates) if c in candidates]
    for c in candidates:
        if c not in order:
            order.append(c)
    ranked = sorted(candidates, key=lambda c: (-counts[c], order.index(c)))

    seats = max(1, min(int(seats), len(candidates)))
    winners = ranked[:seats]
    label = "single winner" if seats == 1 else f"{seats} winners"

    total = len(ballots)
    abstentions = sum(1 for b in ballots
                      if all(b.get(c, 0) == 0 for c in candidates))

    print(f"\n{COLOR_HEADER}--- Approval Voting ({label}) ---{COLOR_RESET}")
    print(f" Tabulating {total} ballots (any non-zero score = approval).")
    if abstentions:
        cast = total - abstentions
        print(f" Abstentions: {abstentions} of {total} ballots approved no one "
              f"({cast} ballot{'' if cast == 1 else 's'} cast an approval).")
    name_w = max(len(c) for c in candidates)
    for i, c in enumerate(ranked):
        tag = " -- Elected" if i < seats else ""
        print(f"   {c.ljust(name_w)} -- {counts[c]}{tag}")

    # Flag a tie straddling the cut and spell out exactly how it was resolved.
    if seats < len(candidates) and counts[ranked[seats - 1]] == counts[ranked[seats]]:
        cutoff = counts[ranked[seats - 1]]
        tied = sorted((c for c in candidates if counts[c] == cutoff),
                      key=lambda c: order.index(c))
        above = sum(1 for c in candidates if counts[c] > cutoff)
        remaining_seats = seats - above           # seats the tied group splits
        elected_tied = [c for c in tied if c in winners]
        missed_tied = [c for c in tied if c not in winners]
        seat_word = "seat" if remaining_seats == 1 else "seats"
        prio = " > ".join(tied)                    # their left-to-right priority
        print(
            f"  Note: {', '.join(tied)} each have {cutoff} approval"
            f"{'' if cutoff == 1 else 's'} and tie for the last {remaining_seats} "
            f"{seat_word}."
        )
        print(
            f"        Candidate priority order ({prio}) broke the tie: "
            f"{', '.join(elected_tied)} elected, {', '.join(missed_tied)} not elected."
        )

    word = "Winner" if seats == 1 else "Winners"
    print(f"\n{COLOR_WINNER}{word} — Approval Voting ({label}){COLOR_RESET}")
    print(f"  {', '.join(winners)}")


def condorcet_winner(candidates, ballots):
    """
    Condorcet winner: the candidate who wins every head-to-head pairwise
    matchup by strict majority. Returns the name, or None if none exists.
    """
    for c in candidates:
        wins_all = True
        for o in candidates:
            if c == o:
                continue
            for_c = sum(1 for b in ballots if b.get(c, 0) > b.get(o, 0))
            against_c = sum(1 for b in ballots if b.get(o, 0) > b.get(c, 0))
            if not (for_c > against_c):
                wins_all = False
                break
        if wins_all:
            return c
    return None


def print_method_comparison(candidates, ballots, star_winner, priority):
    """
    Use STAR as the baseline and only surface the comparison when it is
    interesting: if RCV-IRV, Approval, or Condorcet elects a DIFFERENT winner
    than STAR, print the block; if every method agrees with STAR, print nothing.

    A method "differs" when:
      * RCV-IRV  : its winner != the STAR winner
      * Approval : its (single) winner != the STAR winner
      * Condorcet: a Condorcet winner exists and != the STAR winner
        (no Condorcet winner / a cycle is not treated as a disagreement)
    """
    irv, tie_ballots, total = compute_irv_winner(candidates, ballots, priority)
    approval = approval_winner(candidates, ballots, priority)
    condorcet = condorcet_winner(candidates, ballots)

    irv_diff = irv is not None and irv != star_winner
    approval_diff = approval is not None and approval != star_winner
    condorcet_diff = condorcet is not None and condorcet != star_winner

    if not (irv_diff or approval_diff or condorcet_diff):
        return  # every method agrees with STAR — nothing to learn here

    def line(label, value, differs, width):
        tag = "   (differs from STAR)" if differs else ""
        return f"  {label.ljust(width)} = {value}{tag}"

    # "Condorcet" (9) is the widest label whenever it is shown.
    width = 9 if condorcet is not None else 8

    print("\n[Divergence from STAR]")
    print(line("STAR", star_winner if star_winner else "(tie)", False, width))
    print(line("RCV-IRV", irv if irv else "(none)", irv_diff, width))
    print(line("Approval", approval if approval else "(none)",
               approval_diff, width))
    if condorcet is not None:
        print(line("Condorcet", condorcet, condorcet_diff, width))

    # Smart note: when RCV-IRV differs, say whether the score->rank tiebreak
    # could be responsible (an artifact) or not (a genuine method difference).
    def _note(text):
        # Wrap to a readable width with a hanging indent under "Note: ".
        print(textwrap.fill(text, width=76, initial_indent="  ",
                            subsequent_indent="        "))

    if irv_diff:
        if tie_ballots:
            pct = (100 * tie_ballots / total) if total else 0
            _note(
                f"Note: {tie_ballots} of {total} ballots ({pct:.0f}%) had equal "
                f"non-zero scores, so their ranks were decided by candidate "
                f"priority order. The RCV-IRV result may be an artifact of "
                f"score-to-rank tie-breaking rather than a deep difference."
            )
        else:
            _note(
                f"Note: no ballots had tied scores, so RCV-IRV vs STAR here is a "
                f"genuine method difference, not a tie-breaking artifact."
            )


def markers_used(display_rows):
    """Return the marker characters that actually appear, in MARKER_MEANINGS order."""
    seen = set()
    for row in display_rows:
        for cell in row.split(","):
            cell = cell.strip()
            if cell in MARKER_MEANINGS:
                seen.add(cell)
    return [m for m in MARKER_MEANINGS if m in seen]


def classify_ballot(display_row, candidates=None):
    """
    Label "special" ballot rows for the echo, or return None for a normal
    fully-scored preference ballot. Buckets:
      * abstention — whole race : explicit race-abstention mark (e.g. "~,~,~")
      * abstention — left blank : every candidate blank, no score ("-,-,-")
      * spoiled ballot          : full row of a spoiled marker ("?" / "%")
      * cast, no support        : has scores, but none above 0 ("0,0,0", "-,-,-,0")
      * cast, equal support (no preference) : every candidate the same score > 0
      * partial — left blank    : some candidates scored, others left blank
                                  ("-,-,1,1"); the blanks count as 0
    """
    cells = [c.strip() for c in display_row.split(",")]
    digits = [c for c in cells if c.isdigit()]
    nonblank = [c for c in cells if c != ""]

    if not digits:  # no numeric score at all -> an abstention of some kind
        if nonblank and all(c == "~" for c in nonblank):
            return "abstention — whole race"
        if nonblank and all(c in ("?", "%") for c in nonblank) \
                and len(set(nonblank)) == 1:
            return "spoiled ballot"
        return "abstention — left blank"

    blank_idx = [i for i, c in enumerate(cells) if not c.isdigit()]

    def _blanks():
        if candidates and len(candidates) == len(cells):
            return ", ".join(candidates[i] for i in blank_idx)
        return "some candidates"

    if all(int(c) == 0 for c in digits):
        # Supports no one; still note any left-blank candidates so the label is
        # consistent with the partial case below.
        if blank_idx:
            return f"cast, no support — {_blanks()} left blank"
        return "cast, no support"

    # Every candidate scored the same value > 0 (no blanks): a real vote with
    # no preference between candidates.
    if len(digits) == len(cells) and len(set(digits)) == 1 and int(digits[0]) > 0:
        return "cast, equal support (no preference)"

    # Partial: some candidates scored above 0, others left blank (a marker, not
    # an explicit 0). The blanks count as 0.
    if blank_idx:
        return f"partial — {_blanks()} left blank (counts as 0)"

    return None


def _append_ballot_flags(body_rows):
    """
    body_rows: list of (row_text, label_or_None). Append an aligned trailing
    "# label" comment to flagged rows; leave normal rows untouched. The comments
    are '#' comments, so the echo still round-trips as valid input.
    """
    if not any(label for _, label in body_rows):
        return [t for t, _ in body_rows]
    pad = max(len(t) for t, _ in body_rows)
    out = []
    for t, label in body_rows:
        out.append(f"{t.ljust(pad)}   # {label}" if label else t)
    return out


def print_marker_legend(used):
    """Print a legend explaining only the markers present in the data."""
    if not used:
        return
    print("\n[Legend] (these all count as score 0)")
    for m in used:
        print(f"  {m}  {MARKER_MEANINGS[m]}")


def print_score_counts(candidates, ballots, max_score=5):
    """Per-candidate score distribution: how many ballots gave each score value,
    plus the total and average. Shows how each candidate's total is composed."""
    if not candidates or not ballots:
        return

    counts = {c: defaultdict(int) for c in candidates}
    totals = {c: 0 for c in candidates}
    for b in ballots:
        for c in candidates:
            s = b.get(c, 0)
            counts[c][s] += 1
            totals[c] += s

    scores = list(range(max_score, -1, -1))  # high to low, e.g. 5..0
    n = len(ballots)
    name_w = max((len(c) for c in candidates), default=4)

    print("\n[Score Distribution] (number of ballots giving each score)")
    header = f"{'':<{name_w}}  " + "  ".join(f"{s:>2}" for s in scores)
    print(f"{header}  | Total   Avg")
    for c in candidates:
        cells = "  ".join(f"{counts[c][s]:>2}" for s in scores)
        avg = totals[c] / n if n else 0.0
        print(f"{c:<{name_w}}  {cells}  | {totals[c]:>5}  {avg:>4.1f}")


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
def evaluate_quorum(participation, total_cast, eligible_voters, quorum_spec):
    """
    Decide whether an election meets quorum.

    participation : ballots counting toward quorum (abstentions INCLUDED, since a
                    cast abstention is still participation).
    total_cast    : total ballots cast (for messaging).
    eligible_voters: size of the electorate, or None if unknown.
    quorum_spec   : None  -> default = majority (>50%) of eligible voters
                    "50%" / 0.5 -> a fraction of eligible voters
                    integer >= 1 -> an absolute minimum number of ballots

    Returns (met, message):
      met = True / False / None  (None = cannot be assessed)
    """
    # Interpret the spec into either a fraction (of eligible) or absolute count.
    fraction = None
    absolute = None
    default_used = quorum_spec is None
    if quorum_spec is None:
        fraction = 0.5  # majority of eligible voters
    elif isinstance(quorum_spec, str) and quorum_spec.strip().endswith("%"):
        fraction = float(quorum_spec.strip().rstrip("%")) / 100.0
    else:
        v = float(quorum_spec)
        if 0 < v <= 1:
            fraction = v
        else:
            absolute = int(round(v))

    if absolute is not None:
        met = participation >= absolute
        msg = (f"Quorum: {participation} of {total_cast} ballots count toward "
               f"quorum; requires at least {absolute}. "
               f"{'MET' if met else 'NOT MET'}.")
        return met, msg

    # Fraction of eligible voters — needs the electorate size.
    if not eligible_voters:
        how = "default majority (>50%)" if default_used else f"{fraction:.0%}"
        return None, (
            f"Quorum not assessed: a turnout quorum ({how} of eligible voters) "
            f"needs an 'eligible_voters:' field, which is not set. "
            f"({total_cast} ballots cast.)"
        )
    required = math.floor(fraction * eligible_voters) + 1  # strictly more than
    met = participation >= required
    turnout = participation / eligible_voters * 100
    msg = (f"Quorum: {participation} of {eligible_voters} eligible voters "
           f"participated ({turnout:.0f}% turnout); requires more than "
           f"{fraction:.0%} (>= {required}). {'MET' if met else 'NOT MET'}.")
    return met, msg


def validate_star_rows(ballots_text, max_score=5):
    """
    Validate STAR score rows against the RAW source (so malformed rows error
    instead of being silently dropped by the parser). Only standard comma/tab
    grids are checked; the compact underscore format (e.g. "052_225") is left to
    the parser. A cell is valid if it is an int 0..max_score, blank, or a
    recognized marker. Returns (headers, problems) with (row_number, raw, reason).
    """
    lines = []
    for raw in ballots_text.strip().splitlines():
        line = raw if raw.strip().startswith("#,") else raw.split("#")[0]
        line = line.strip()
        if line:
            lines.append(line)
    if len(lines) < 2:
        return [], []

    headers = [h.strip() for h in re.split(r"[,\t]+", lines[0]) if h.strip()]
    if headers and headers[0] == "#":
        headers.pop(0)
    if headers and re.match(r"(?i)^count\s*:", headers[0]):
        headers[0] = headers[0].split(":", 1)[1].strip()
    count_col = bool(headers) and headers[0].lower() == "count"
    if count_col:
        headers.pop(0)

    problems = []
    for i, line in enumerate(lines[1:], 1):
        if "," not in line and "\t" not in line:
            continue  # compact underscore / single token -> leave to the parser
        parts = re.split(r"[,\t]", line)
        m = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", parts[0])  # weight prefix
        if m:
            parts = [m.group(2)] + parts[1:]
        cells = [p.strip() for p in parts]
        if count_col and cells:
            cells = cells[1:]
        # A full row of one ballot-level marker (e.g. "~,~,~") is valid.
        nonblank = [c for c in cells if c != ""]
        if (nonblank and len(set(nonblank)) == 1
                and nonblank[0] in BALLOT_LEVEL_MARKERS):
            continue
        if len(cells) != len(headers):
            problems.append((i, line,
                             f"has {len(cells)} value(s), expected {len(headers)}"))
            continue
        bad = []
        for h, c in zip(headers, cells):
            if c == "" or c in MARKER_MEANINGS:
                continue
            try:
                v = int(c)
            except ValueError:
                bad.append(f"{h}={c}")
                continue
            if not (0 <= v <= max_score):
                bad.append(f"{h}={c}")
        if bad:
            problems.append((i, line, "invalid: " + ", ".join(bad)))
    return headers, problems


def run_election(
    csv_input,
    lot_numbers,
    show_matrix=True,
    matrix_finalists_only=False,
    brief=False,
    seats=1,
    method=None,
    show_condorcet=True,
    show_score_counts=True,
    collapse_ballots=True,
    count_separator="×",
    title=None,
    description=None,
    show_irv=False,
    eligible_voters=None,
    quorum=None,
):
    if method is None:
        method = starvote.star

    # Reject method/seats mismatches up front (before any tabulation), so the
    # intent must be corrected rather than silently guessed.
    method_name = getattr(method, "name", str(method))
    single_winner = method is starvote.star
    if single_winner and seats > 1:
        print(
            f"{COLOR_RED}Error:{COLOR_RESET} {method_name} elects a single winner,\n"
            f"  but got seats={seats}.\n"
            f"  Fix: set seats=1 (num_winners: 1),\n"
            f"       or choose a multi-winner method to elect {seats} winners:\n"
            f"       starvote.bloc, starvote.sss, starvote.rrv, starvote.allocated."
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

    # Optional scenario context from the YAML (election_title / scenario_description).
    if title or description:
        if title:
            print(f"\n{COLOR_HEADER}=== {title} ==={COLOR_RESET}")
        if description:
            for line in str(description).splitlines():
                print(f"  {line}" if line.strip() else "")

    # Validate raw rows first, so invalid characters / out-of-range scores /
    # wrong column counts error instead of being silently dropped.
    _hdrs, _star_problems = validate_star_rows(csv_input, max_score=5)
    if _star_problems:
        print(
            f"{COLOR_RED}Error: STAR ballots use scores 0..5 "
            f"(blank or a marker counts as 0).{COLOR_RESET}\n"
            f"  Offending ballot(s)  [{','.join(_hdrs)}]:"
        )
        for _i, _line, _reason in _star_problems:
            print(f"    ballot {_i}: {_line}   ({_reason})")
        print(f"  Accepted marks: 0..5, blank, or a marker "
              f"({', '.join(MARKER_MEANINGS)}).")
        sys.exit(1)

    # Parse once, return both headers and parsed ballots
    candidates, ballots, display_rows = parse_ballots_from_string(csv_input)

    if not ballots:
        # A '>' in the input means these are ranked ballots (e.g. "A>C>B"),
        # which STAR cannot tabulate — it needs scores. Point the user to the
        # RCV-IRV engine instead of a bare "no ballots" error.
        if ">" in (csv_input or ""):
            print(
                "Error: this file contains RANKED ballots (e.g. 'A>C>B'), which "
                "the STAR engine cannot tabulate — STAR needs score ballots.\n"
                "  Run it through the RCV-IRV engine instead:\n"
                "    python RCV_IRV_tabulation_engine/rcv_irv_tabulation.py "
                "<this_file>.yaml"
            )
        else:
            print("Error: No valid ballots found in input.")
        return

    # Quorum check (before declaring any winner). Only engaged when the file
    # opts in via eligible_voters and/or quorum; otherwise behaves as before.
    # Abstentions count toward quorum (a cast ballot is participation), so
    # participation = total ballots cast.
    if eligible_voters is not None or quorum is not None:
        _q_label = "single winner" if seats == 1 else f"{seats} winners"
        quorum_met, quorum_msg = evaluate_quorum(
            participation=len(ballots),
            total_cast=len(ballots),
            eligible_voters=eligible_voters,
            quorum_spec=quorum,
        )
        if quorum_met is False:
            print(f"\n{COLOR_HEADER}--- {method_name} Method ({_q_label}) "
                  f"---{COLOR_RESET}")
            print(f"{COLOR_RED} {quorum_msg}{COLOR_RESET}")
            print(f"{COLOR_RED} No winner declared — quorum not reached."
                  f"{COLOR_RESET}")
            return
        if quorum_met is None:
            print(f"{COLOR_DIM} {quorum_msg}{COLOR_RESET}")  # warning, continue
        else:
            print(f" {quorum_msg}")  # quorum MET

    # Which marker characters actually appear (for the legend).
    used_markers = markers_used(display_rows)

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

        # seats=1: election() returns a single winner or a list
        star_winner = (
            winners_silent[0] if isinstance(winners_silent, list) else winners_silent
        )

        # These analyses are independent toggles.
        if show_score_counts:
            print_score_counts(candidates, ballots, max_score=5)
        if show_matrix:
            print_matrix(
                candidates,
                matrix,
                finalists,
                star_winner,
                finalists_only=matrix_finalists_only,
            )
        if show_condorcet:
            print_condorcet(candidates, matrix, star_winner, finalists)

        # Always show the RCV-IRV / STAR / Approval comparison (Condorcet line
        # appears only when it differs from all three). priority == STAR's
        # tiebreak order, used for the score->rank conversion.
        print_method_comparison(candidates, ballots, star_winner, priority)

        print_extended_analysis(ballots, winners_silent)

    # Header banner naming the actual method + winner count.
    winners_label = "single winner" if seats == 1 else f"{seats} winners"
    method_label = method_name if method_name.endswith("Voting") else f"{method_name} Voting"
    print(f"\n{COLOR_HEADER}--- {method_label} Method ({winners_label}) ---{COLOR_RESET}")

    # Intercept the engine's print() to fix grammar and relabel the
    # "No Preference" bucket, re-aligning score columns so the longer
    # label doesn't shove the " -- " separator out of column.
    EQUAL_LABEL = "Equal Support"  # EVC (Equal Vote Coalition) terminology
    EQUAL_NOTE = "(aka Equal Preference, No Preference)"  # appended inline after value
    row_re = re.compile(r"^(\s*)(\S.*?)\s+--\s+(.*)$")
    # Pad the label column to the widest of any candidate name or "Equal Support"
    # so the " -- " separators line up even for long names like "Chocolate Chip".
    label_width = max([len(EQUAL_LABEL)] + [len(c) for c in candidates])

    # Round grouping: draw a faint rule before each new round's Scoring Round
    # header (but not the first), so multi-round methods like Bloc STAR read as
    # distinct blocks without spending another header color.
    round_state = {"scoring_seen": False, "in_runoff": False}
    ROUND_RULE = f"{COLOR_DIM}{'─' * 50}{COLOR_RESET}"

    def colorize_runoff_value(label, rest):
        """In an Automatic Runoff Round, color the leading count to match the
        Preference Matrix legend: winner=For(green), other finalist=Against(red),
        Equal Support=Equal Preference(blue). A tie is left neutral."""
        mm = re.match(r"^(\S+)(.*)$", rest)
        if not mm:
            return rest
        val, tail = mm.groups()
        if label == EQUAL_LABEL:
            color = COLOR_BLUE
        elif "Tied" in rest:
            color = ""  # tie not yet resolved -> no winner/loser
        elif "First place" in rest:
            color = COLOR_GREEN
        else:
            color = COLOR_RED
        if not color:
            return rest
        return f"{color}{val}{COLOR_RESET}{tail}"

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

            # Round separator: before each main "Scoring Round" header after the
            # first, emit a faint rule to visually group each round.
            if stripped.startswith("[") and stripped.endswith("]"):
                inner_h = stripped[1:-1].rstrip()
                # Only the *main* runoff header enables coloring; tiebreaker
                # sub-headers (which list raw scores) reset it.
                round_state["in_runoff"] = inner_h.endswith("Automatic Runoff Round")
                if inner_h.endswith("Scoring Round"):
                    if round_state["scoring_seen"]:
                        print(ROUND_RULE)
                    round_state["scoring_seen"] = True

            if brief and stripped.startswith("[") and stripped.endswith("]"):
                inner = stripped[1:-1]
                if ":" in inner:
                    label = inner.split(":", 1)[1].strip()
                    # Restate the method on the final Winner(s) line, since the
                    # top banner has usually scrolled off by then.
                    if label in ("Winner", "Winners"):
                        # "Winner" stays green; the restated method matches the
                        # purple top banner.
                        suffix = f" — {method_label} Method ({winners_label})"
                        text = (
                            f"{COLOR_WINNER}{label}{COLOR_RESET}"
                            f"{COLOR_HEADER}{suffix}{COLOR_RESET}"
                        )
                    else:
                        text = f"{header_color(label)}{label}{COLOR_RESET}"
                    args = (text + trailing,) + args[1:]
                    print(*args, **kwargs)
                else:
                    # Bare top-level method header -> suppress.
                    pass
                return
            if stripped.startswith("[") and stripped.endswith("]"):
                # Non-brief: keep the full "[...]" header but colorize it.
                inner_nb = stripped[1:-1]
                if inner_nb.rsplit(":", 1)[-1].strip() in ("Winner", "Winners"):
                    stripped = (
                        f"{stripped[:-1]} — {method_label} Method ({winners_label})]"
                    )
                text = f"{header_color(stripped)}{stripped}{COLOR_RESET}"
                args = (text + trailing,) + args[1:]
                print(*args, **kwargs)
                return

            # 1. Fix the singular/plural grammar.
            text = text.replace("Tabulating 1 ballots.", "Tabulating 1 ballot.")

            # 1b. After the "Tabulating N ballot(s)." line, list the
            #     normalized ballots as Standard CSV.
            if text.lstrip().startswith("Tabulating ") and "ballot" in text:
                # Note true abstentions: ballots that recorded NO numeric score
                # for any candidate — i.e. entirely blank / abstention markers
                # (e.g. "~,~,~" or "-,-,-"). An explicit all-zeros ballot
                # ("0,0,0") is a cast ballot that supports no one, NOT an
                # abstention, so it is not counted here.
                _abs = sum(
                    1 for r in display_rows
                    if not any(cell.strip().isdigit() for cell in r.split(","))
                )
                if _abs:
                    _n = len(ballots)
                    if _abs == 1:
                        text += f" Note: 1 of {_n} ballots is marked as an abstention."
                    else:
                        text += (f" Note: {_abs} of {_n} ballots are marked as "
                                 f"abstentions.")

                # Echo keeps original markers (display_rows), faithful to source,
                # followed by a legend for any markers used. Each column is padded
                # to its widest cell so it lines up — still valid, parseable CSV.
                ncols = len(candidates)
                has_dupes = len(set(display_rows)) < len(display_rows)
                if collapse_ballots and has_dupes:
                    # Collapse identical ballots into "count: scores" (matches the
                    # weight syntax, so it round-trips), most common first.
                    counts, first_idx = {}, {}
                    for i, r in enumerate(display_rows):
                        if r not in counts:
                            counts[r], first_idx[r] = 0, i
                        counts[r] += 1
                    unique = sorted(counts, key=lambda r: (-counts[r], first_idx[r]))
                    rows = [r.split(",") for r in unique]
                    widths = [
                        max(len(candidates[i]), max(len(rc[i]) for rc in rows))
                        for i in range(ncols)
                    ]
                    count_w = max(len("Count"), max(len(str(counts[r])) for r in unique))
                    # count_separator (":", "x"/"X", or "×") all round-trip.
                    sep = f" {count_separator} "
                    csv_rows = [
                        "Count".rjust(count_w)
                        + sep
                        + ",".join(candidates[i].rjust(widths[i]) for i in range(ncols))
                    ]
                    body_rows = []
                    for r in unique:
                        rc = r.split(",")
                        body = ",".join(rc[i].rjust(widths[i]) for i in range(ncols))
                        body_rows.append(
                            (f"{str(counts[r]).rjust(count_w)}{sep}{body}",
                             classify_ballot(r, candidates))
                        )
                    csv_rows += _append_ballot_flags(body_rows)
                else:
                    grid = [r.split(",") for r in display_rows]
                    header = list(candidates)
                    widths = [max(len(row[i]) for row in ([header] + grid))
                              for i in range(ncols)]
                    csv_rows = [
                        ",".join(c.rjust(widths[i]) for i, c in enumerate(header))
                    ]
                    body_rows = [
                        (",".join(c.rjust(widths[i]) for i, c in enumerate(row)),
                         classify_ballot(display_rows[j], candidates))
                        for j, row in enumerate(grid)
                    ]
                    csv_rows += _append_ballot_flags(body_rows)
                if used_markers:
                    csv_rows.append("")
                    csv_rows.append("[Legend] (these all count as score 0)")
                    csv_rows += [
                        f"  {mk}  {MARKER_MEANINGS[mk]}" for mk in used_markers
                    ]
                    # Clarify the blank-vs-explicit-zero distinction only when a
                    # blank actually appears (common with BetterVoting exports /
                    # hand-punched paper ballots).
                    if "-" in used_markers:
                        csv_rows.append(
                            "  Note: '-' = candidate left blank / skipped "
                            "(e.g. BetterVoting export);"
                        )
                        csv_rows.append(
                            "        '0' = explicitly scored zero. Both tabulate "
                            "as 0 stars — the"
                        )
                        csv_rows.append(
                            "        difference only preserves voter intent "
                            "(skipped vs rated low)."
                        )
                text = text + "\n" + "\n".join(csv_rows)

            # 2. Relabel the no-preference bucket.
            relabeled = "No Preference" in text
            text = text.replace("No Preference", EQUAL_LABEL)

            # 3. Re-align score rows ("   <label> -- <value>"), skipping
            #    section headers like "[STAR Voting: ...]".
            m = row_re.match(text)
            if m and not text.lstrip().startswith("["):
                indent, label, rest = m.groups()
                # The "(aka …)" note is explanatory but noisy on screen. Show it
                # only in verbose (non-brief) output — i.e. the saved _tabulated
                # file — and keep the live/brief demo output clean.
                if relabeled and not brief and EQUAL_NOTE not in rest:
                    rest = f"{rest} {EQUAL_NOTE}"
                if round_state["in_runoff"]:
                    rest = colorize_runoff_value(label.strip(), rest)
                text = f"{indent}{label:<{label_width}} -- {rest}"

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

    # TIEBREAKER SETTING
    # Provide a list like ["B", "A", "C"] for production ties.
    # Leave empty [] to auto-generate based on CSV columns for quick testing.
    LOT_NUMBERS = []

    # FLAG: Set to False to hide the Preference Matrix.
    SHOW_MATRIX = False

    # FLAG: Set to True to restrict the Preference Matrix to just the two
    # finalists (the decisive runoff head-to-head). Requires SHOW_MATRIX.
    MATRIX_FINALISTS_ONLY = False

    # FLAG: Set to False to hide the [Condorcet Winner] line.
    # Independent of SHOW_MATRIX — prints by default even when the matrix is off.
    SHOW_CONDORCET = False

    # NOTE: The [RCV-IRV, STAR, and Approval comparison] block is now ALWAYS
    # printed, so this flag no longer gates it; it is kept only so existing
    # YAML `options:` blocks that set show_irv still parse without error.
    SHOW_IRV = False

    # FLAG: Set to False to hide the per-candidate [Score Distribution] table.
    SHOW_SCORE_COUNTS = False

    # FLAG: Set to True for shorter output (collapses repetitive [STAR Voting: ...]
    # section headers into plain sub-headings and drops the bare "[STAR Voting]").
    BRIEF = True

    # FLAG: Collapse identical ballots in the echo into "count × scores"
    # (most common first). Set to False to echo every ballot individually.
    COLLAPSE_BALLOTS = True

    # FLAG: Separator for the collapsed count. "×" reads as "times";
    # ":" matches the input weight syntax. Both round-trip ("x"/"X" also work).
    COUNT_SEPARATOR = "×"

    # METHOD + SEATS.
    #   starvote.star  -> single-winner STAR (use SEATS = 1)
    #   starvote.bloc  -> Bloc STAR, multi-winner (use SEATS >= 2)
    # A mismatch (star with SEATS>1, or bloc with SEATS=1) is rejected with an
    # error and exits, so you must correct the combination.
    METHOD = starvote.star
    SEATS = 1

    # BALLOTS (the data).
    #
    # Demo workflow: pass a YAML/CSV file on the command line and it is used
    # instead of the inline csv_input below. In PyCharm, make a Run
    # Configuration whose "Parameters" is the macro  $FilePath$  — then whatever
    # election file is open in the editor is the one that gets tabulated. Open
    # the next file, hit Run again.
    #
    #   python starvote_larry_hastings.py elections_illustrations/99_01 tennessee_capital.yaml
    #
    # A .yaml/.yml file also supplies its own num_winners -> SEATS,
    # voting_method -> METHOD, and an optional `options:` block (see below).
    #
    # Add  --save  to write the result back into the YAML as an
    # `expected_results:` block (winners + plain-text report):
    #   python starvote_larry_hastings.py elections_illustrations/99_01 tennessee_capital.yaml --save
    args = [a for a in sys.argv[1:]]
    SAVE_RESULTS = "--save" in args
    positional = [a for a in args if not a.startswith("-")]
    BALLOTS_FILE = positional[0] if positional else None

    csv_input = """
Memphis,Nashville,Chattanooga,Knoxville
3, 3, 4, 2
2, 5, 4, 3
2, 3, 5, 4
5, 4, 3, 2
"""

    if BALLOTS_FILE:
        election = load_election(BALLOTS_FILE)
        csv_input = election["ballots"]

        # On-the-fly engine dispatch based on the declared voting_method (or the
        # ballot style), so one command routes STAR / RCV-IRV / Approval files.
        import difflib

        _mname = str(election.get("method_name") or "").strip().lower()
        _is_rcv = _mname in {"rcv", "irv", "rcv_irv", "rcv-irv", "rcv/irv",
                             "ranked_choice", "instant_runoff"}
        # Approval and its explicit single/multi-winner variants, tolerant of
        # typos like "Arroval". A name carrying "multi"/"single" must agree with
        # num_winners (checked below).
        _norm = _mname.replace("-", "_")
        _is_approval = (
            "approval" in _norm
            or _norm in {"approve", "av"}
            or bool(difflib.get_close_matches(_norm, ["approval"], cutoff=0.6))
        )

        # Ranked ballots ("A>C>B") can only be RCV-IRV, regardless of the label.
        if _is_rcv or ">" in (csv_input or ""):
            if _IRV_AVAILABLE:
                import rcv_irv_tabulation
                rcv_irv_tabulation.run(BALLOTS_FILE)
                sys.exit(0)
            print("Error: this file needs the RCV-IRV engine, but it could not "
                  "be imported (RCV_IRV_tabulation_engine missing?).")
            sys.exit(1)

        if _is_approval:
            _seats = election["seats"] if election["seats"] is not None else 1
            _raw = election.get("method_name")
            # Plain "Approval" means SINGLE winner. Multi-winner must be opted
            # into explicitly (Approval_Multi_Winner / block / *_mw).
            _wants_multi = ("multi" in _norm or "block" in _norm
                            or _norm.endswith("_mw"))

            # The method name must not contradict num_winners.
            if _wants_multi and _seats < 2:
                print(f"{COLOR_RED}Error: voting_method '{_raw}' is multi-winner, "
                      f"but num_winners is {_seats}.{COLOR_RESET}\n"
                      f"  Set num_winners >= 2, or use voting_method: Approval "
                      f"(single winner).")
                sys.exit(1)
            if not _wants_multi and _seats > 1:
                print(f"{COLOR_RED}Error: voting_method '{_raw}' is single-winner, "
                      f"but num_winners is {_seats}.{COLOR_RESET}\n"
                      f"  For multiple seats, use voting_method: "
                      f"Approval_Multi_Winner; otherwise set num_winners: 1.")
                sys.exit(1)

            if _norm not in {"approval", "approve", "av", "approval_voting",
                             "approval_single_winner", "approval_multi_winner"}:
                print(f"(Interpreting voting_method '{_raw}' as Approval.)")
            tabulate_approval(csv_input, seats=_seats)
            sys.exit(0)

        if election["seats"] is not None:
            SEATS = election["seats"]
        if election["method"] is not None:
            METHOD = election["method"]

        # A YAML `options:` block can override the display flags. Example:
        #   options:
        #     show_matrix: true
        #     show_score_counts: true
        #     brief: false
        #     count_separator: ":"
        def _as_bool(v):
            return (
                v
                if isinstance(v, bool)
                else str(v).strip().lower()
                in (
                    "1",
                    "true",
                    "yes",
                    "on",
                )
            )

        opts = election["options"]
        if "show_matrix" in opts:
            SHOW_MATRIX = _as_bool(opts["show_matrix"])
        if "matrix_finalists_only" in opts:
            MATRIX_FINALISTS_ONLY = _as_bool(opts["matrix_finalists_only"])
        if "show_condorcet" in opts:
            SHOW_CONDORCET = _as_bool(opts["show_condorcet"])
        if "show_irv" in opts:
            SHOW_IRV = _as_bool(opts["show_irv"])
        if "show_score_counts" in opts:
            SHOW_SCORE_COUNTS = _as_bool(opts["show_score_counts"])
        if "brief" in opts:
            BRIEF = _as_bool(opts["brief"])
        if "collapse_ballots" in opts:
            COLLAPSE_BALLOTS = _as_bool(opts["collapse_ballots"])
        if "count_separator" in opts:
            COUNT_SEPARATOR = str(opts["count_separator"])

    run_kwargs = dict(
        show_matrix=SHOW_MATRIX,
        matrix_finalists_only=MATRIX_FINALISTS_ONLY,
        brief=BRIEF,
        seats=SEATS,
        method=METHOD,
        show_condorcet=SHOW_CONDORCET,
        show_score_counts=SHOW_SCORE_COUNTS,
        collapse_ballots=COLLAPSE_BALLOTS,
        count_separator=COUNT_SEPARATOR,
        show_irv=SHOW_IRV,
        title=(election["title"] if BALLOTS_FILE else None),
        description=(election["description"] if BALLOTS_FILE else None),
        eligible_voters=(election["eligible_voters"] if BALLOTS_FILE else None),
        quorum=(election["quorum"] if BALLOTS_FILE else None),
    )

    if BALLOTS_FILE:
        # Keep the file's trailing '# file:' comment in sync with its name
        # (only writes if missing/stale).
        ensure_filename_comment(BALLOTS_FILE)

        # Capture the output so we can both display it and write a plain-text
        # '_tabulated' copy (and, with --save, embed results into the YAML).
        import contextlib
        import io

        def _capture(kwargs):
            b = io.StringIO()
            try:
                with contextlib.redirect_stdout(b):
                    w = run_election(csv_input, LOT_NUMBERS, **kwargs)
            except SystemExit:
                # run_election bailed out (e.g. a method/seats mismatch error).
                # Flush what it printed so the message isn't swallowed, then
                # propagate the exit code.
                sys.stdout.write(b.getvalue())
                raise
            return w, b.getvalue()

        # On-screen render: honors the file's own options.
        winners, out = _capture(run_kwargs)
        # Show which file produced this output (handy in demos / scrollback).
        print(f"{COLOR_DIM}# file: {Path(BALLOTS_FILE).name}{COLOR_RESET}")
        sys.stdout.write(out)  # still display on screen

        # The saved '_tabulated' file ALWAYS uses the full, most explanatory
        # render (every analysis on, maximum verbosity) regardless of the file's
        # own options — only the on-screen echo above honors those options.
        full_kwargs = dict(run_kwargs)
        full_kwargs.update(
            show_matrix=True,
            matrix_finalists_only=False,
            show_condorcet=True,
            show_score_counts=True,
            brief=False,
            collapse_ballots=True,  # collapsed counts are clearer than a raw dump
            show_irv=True,
        )
        _, file_out = _capture(full_kwargs)

        # The '_tabulated' file is the ORIGINAL election file copied as-is,
        # followed by the tabulation results.
        try:
            original = Path(BALLOTS_FILE).read_text(encoding="utf-8")
        except OSError:
            original = ""
        import datetime

        divider = "=" * 70
        src_name = Path(BALLOTS_FILE).name
        tab_path = tabulated_output_path(BALLOTS_FILE)
        out_name = tab_path.name
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z").strip()
        try:
            mtime = datetime.datetime.fromtimestamp(
                Path(BALLOTS_FILE).stat().st_mtime
            ).strftime("%Y-%m-%d %H:%M:%S")
        except OSError:
            mtime = "unknown"
        composed = (
            f"{divider}\n"
            f"SOURCE FILE:     {src_name}\n"
            f"SOURCE MODIFIED: {mtime}\n"
            f"TABULATED FILE:  {out_name}\n"
            f"TABULATED AT:    {timestamp}\n"
            f"{divider}\n\n"
            f"{original.rstrip()}\n\n"
            f"{divider}\n"
            f"TABULATION RESULTS\n"
            f"{divider}\n\n"
            f"{strip_ansi(file_out).lstrip()}"
        )
        write_tabulated_copy(BALLOTS_FILE, composed)

        if SAVE_RESULTS:
            names = winners if isinstance(winners, (list, tuple)) else [winners]
            save_results_to_file(BALLOTS_FILE, [str(w) for w in names], out)
            print(f"\n{COLOR_HEADER}[saved results to {BALLOTS_FILE}]{COLOR_RESET}")
    else:
        run_election(csv_input, LOT_NUMBERS, **run_kwargs)
