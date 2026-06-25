"""
test_lot_number_tiebreak.py
===========================
Guards the official tie-break ("lot number") path added for BetterVoting
imports:

  * the LH engine HONORS a `lot_numbers:` order declared in a YAML file
    (reversing the order flips the winner of a true tie);
  * the JSON->YAML converter translates BetterVoting's `perm` sequence into a
    `lot_numbers:` list in cand_id space (index 0 = highest priority, wins
    ties), and that order reproduces BetterVoting's `elected` winner;
  * SELF-CHECK (non-vacuous guard): scrambling the lot order makes the engine
    DISAGREE with BetterVoting's `elected` winner — proving the positive checks
    above actually depend on the lot order, not luck.

The scenario is a perfect symmetric two-candidate tie (one ballot each way), so
every earlier STAR tiebreaker (score, five-star, pairwise) is ALSO tied and the
outcome is decided ONLY by the lot order. That is what makes the self-check
meaningful: in this election, lot order is the whole ballgame.
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
LIB_POS = REPO_ROOT / "YAML_library" / "1_positive"
CONVERTER = LIB_POS / "01_convert_json_yaml.py"

sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))
import starvote_larry_hastings as engine  # noqa: E402
from scenario_eval import scenario_winners  # noqa: E402


# A perfect symmetric tie: candidate (lot) order is the ONLY thing that can
# decide it. {order} is filled in per test; doubled braces escape the flow maps.
SYMMETRIC_TIE_YAML = """\
election:
  races:
  - num_winners: 1
    voting_method: STAR
    candidates:
    - {{cand_id: Ada, candidate_name: Ada}}
    - {{cand_id: Ben, candidate_name: Ben}}
    ballots: |-
      Ada, Ben
        5,   0
        0,   5
    lot_numbers: [{order}]
"""


# Same symmetric tie, but with NO `lot_numbers:` and the column order
# parameterized. Models a HAND-WRITTEN file: when no official order is given,
# the engine assumes CSV ballot-column order, so the FIRST column wins the tie.
SYMMETRIC_TIE_NO_LOT_YAML = """\
election:
  races:
  - num_winners: 1
    voting_method: STAR
    candidates:
    - {{cand_id: {c1}, candidate_name: {c1}}}
    - {{cand_id: {c2}, candidate_name: {c2}}}
    ballots: |-
      {c1}, {c2}
      5, 0
      0, 5
"""


def _write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return p


# --- 1. Engine honors lot_numbers from the YAML ---------------------------

def test_engine_honors_lot_numbers_from_yaml(tmp_path):
    """index 0 of `lot_numbers` wins the tie; reversing it flips the winner."""
    ada_first = _write(tmp_path, "ada.yaml",
                       SYMMETRIC_TIE_YAML.format(order="Ada, Ben"))
    ben_first = _write(tmp_path, "ben.yaml",
                       SYMMETRIC_TIE_YAML.format(order="Ben, Ada"))

    ada_winners, _ = scenario_winners(ada_first)
    ben_winners, _ = scenario_winners(ben_first)

    assert ada_winners == ["Ada"], ada_winners
    assert ben_winners == ["Ben"], ben_winners
    # Non-vacuous: the winner genuinely tracks the declared lot order.
    assert ada_winners != ben_winners


# --- BetterVoting export fixtures + converter helpers ---------------------

def _bv_export(perm=None, elected_id="u-ben", tiebreak_order=None):
    """A minimal BetterVoting-shaped export for the symmetric Ada/Ben tie.

    `perm` is the provider's tie-break order (UUIDs, highest priority first).
    `tiebreak_order` is an alternative {uuid: tieBreakOrder} mapping carried on
    the result's summaryData candidates (the converter's fallback when `perm`
    is absent). Pass neither to model an OLD export that carries no sequence at
    all. `elected_id` is the UUID the provider reports as the winner.
    """
    names = {"u-ada": "Ada", "u-ben": "Ben"}
    result = {
        "votingMethod": "STAR",
        "elected": [{"id": elected_id, "name": names[elected_id]}],
    }
    if perm is not None:
        result["perm"] = perm
    if tiebreak_order is not None:
        result["summaryData"] = {"candidates": [
            {"id": cid, "name": names[cid], "tieBreakOrder": order}
            for cid, order in tiebreak_order.items()
        ]}
    return {
        "Election": {
            "election_id": "tie01",
            "title": "Lot Tie Demo",
            "races": [{
                "race_id": "0",
                "num_winners": 1,
                "voting_method": "STAR",
                "candidates": [
                    {"candidate_id": "u-ada", "candidate_name": "Ada"},
                    {"candidate_id": "u-ben", "candidate_name": "Ben"},
                ],
            }],
        },
        "Ballots": [
            {"votes": [{"race_id": "0", "scores": [
                {"candidate_id": "u-ada", "score": 5},
                {"candidate_id": "u-ben", "score": 0}]}]},
            {"votes": [{"race_id": "0", "scores": [
                {"candidate_id": "u-ada", "score": 0},
                {"candidate_id": "u-ben", "score": 5}]}]},
        ],
        "Results": [result],
    }


def _load_converter():
    spec = importlib.util.spec_from_file_location("bv_json_converter", CONVERTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _convert(tmp_path, export):
    """Convert an in-memory export in an isolated tmp dir; return the YAML path."""
    src = tmp_path / "tie01.json"
    src.write_text(json.dumps(export), encoding="utf-8")
    _load_converter().convert_election_data(str(src), engine)
    produced = list((tmp_path / "_generated").glob("*.yaml"))
    assert len(produced) == 1, produced
    return produced[0]


# --- 2. Converter maps perm -> lot_numbers (and reproduces elected) --------

@pytest.mark.skipif(not CONVERTER.exists(), reason="converter not present")
def test_converter_maps_perm_to_lot_numbers(tmp_path):
    # perm puts u-ben first -> BetterVoting elects Ben.
    yml = _convert(tmp_path, _bv_export(perm=["u-ben", "u-ada"],
                                        elected_id="u-ben"))
    race = yaml.safe_load(yml.read_text(encoding="utf-8"))["election"]["races"][0]

    # cand_ids are the real names; the lot order is mapped into that space.
    assert [c["cand_id"] for c in race["candidates"]] == ["Ada", "Ben"]
    assert race["lot_numbers"] == ["Ben", "Ada"], race["lot_numbers"]

    embedded = [str(w) for w in race["expected_results"]["winners"]]
    assert embedded == ["Ben"], embedded
    # The produced file tabulates to BetterVoting's elected winner.
    assert scenario_winners(yml)[0] == ["Ben"]


# --- 3. Self-check: wrong lot order must DIVERGE from BetterVoting ----------

@pytest.mark.skipif(not CONVERTER.exists(), reason="converter not present")
def test_wrong_lot_order_diverges_from_bettervoting(tmp_path):
    """Corrupting the lot order must make the engine DISAGREE with the
    provider's elected winner. If this negative case still matched, the positive
    test above would be vacuous (the result wouldn't actually hinge on lot)."""
    bv_elected = "Ben"
    yml = _convert(tmp_path, _bv_export(perm=["u-ben", "u-ada"],
                                        elected_id="u-ben"))

    # As generated, the engine agrees with BetterVoting.
    assert scenario_winners(yml)[0] == [bv_elected]

    # Scramble the official order and rewrite the file.
    data = yaml.safe_load(yml.read_text(encoding="utf-8"))
    race = data["election"]["races"][0]
    race["lot_numbers"] = list(reversed(race["lot_numbers"]))  # ["Ada", "Ben"]
    yml.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
                   encoding="utf-8")

    diverged, _ = scenario_winners(yml)
    assert diverged == ["Ada"], diverged
    assert diverged != [bv_elected], (
        "wrong lot order still matched BetterVoting — the tie does not actually "
        "depend on lot order, so the positive test would be vacuous"
    )


# --- Flow 1 (JSON->YAML->tabulation): more provider shapes -----------------

@pytest.mark.skipif(not CONVERTER.exists(), reason="converter not present")
def test_converter_uses_tiebreakorder_when_perm_absent(tmp_path):
    """Older exports may omit `perm` but still carry per-candidate
    `tieBreakOrder` on summaryData. The converter must fall back to that
    (ascending order = higher priority) and reproduce the elected winner."""
    export = _bv_export(perm=None,
                        tiebreak_order={"u-ben": 0, "u-ada": 1},
                        elected_id="u-ben")
    yml = _convert(tmp_path, export)
    race = yaml.safe_load(yml.read_text(encoding="utf-8"))["election"]["races"][0]

    assert race["lot_numbers"] == ["Ben", "Ada"], race["lot_numbers"]
    assert scenario_winners(yml)[0] == ["Ben"]


@pytest.mark.skipif(not CONVERTER.exists(), reason="converter not present")
def test_converter_without_sequence_omits_lot_numbers(tmp_path):
    """An export with no `perm` and no `tieBreakOrder` carries no official
    sequence. The converter must NOT invent one: it omits `lot_numbers`, and
    tabulation then falls back to CSV column order (first column = Ada wins).
    (This is exactly why the provider sequence matters — without it we cannot
    reproduce BetterVoting's tiebreak.)"""
    export = _bv_export(perm=None, tiebreak_order=None, elected_id="u-ben")
    yml = _convert(tmp_path, export)
    race = yaml.safe_load(yml.read_text(encoding="utf-8"))["election"]["races"][0]

    assert "lot_numbers" not in race, race.get("lot_numbers")
    # Column order is [Ada, Ben]; the fallback elects the first column.
    assert scenario_winners(yml)[0] == ["Ada"]


# --- Flow 2 (YAML->tabulation, hand-written): the assumed order ------------

def test_yaml_without_lot_numbers_uses_column_order(tmp_path):
    """With no `lot_numbers:`, the engine assumes CSV ballot-column order — the
    FIRST column wins the tie. Swapping the columns flips the winner, proving
    the fallback really is column order (not alphabetical or arbitrary)."""
    ada_left = _write(tmp_path, "ada_left.yaml",
                      SYMMETRIC_TIE_NO_LOT_YAML.format(c1="Ada", c2="Ben"))
    ben_left = _write(tmp_path, "ben_left.yaml",
                      SYMMETRIC_TIE_NO_LOT_YAML.format(c1="Ben", c2="Ada"))

    assert scenario_winners(ada_left)[0] == ["Ada"]
    assert scenario_winners(ben_left)[0] == ["Ben"]


def test_yaml_lot_numbers_override_column_order(tmp_path):
    """An explicit `lot_numbers:` overrides the column-order assumption. Columns
    are [Ada, Ben] (which alone would elect Ada), but lot_numbers [Ben, Ada]
    elects Ben."""
    # Column order would pick Ada...
    no_lot = _write(tmp_path, "cols.yaml",
                    SYMMETRIC_TIE_NO_LOT_YAML.format(c1="Ada", c2="Ben"))
    assert scenario_winners(no_lot)[0] == ["Ada"]

    # ...but an explicit lot order [Ben, Ada] overrides it.
    with_lot = _write(tmp_path, "cols_lot.yaml",
                      SYMMETRIC_TIE_YAML.format(order="Ben, Ada"))
    assert scenario_winners(with_lot)[0] == ["Ben"]
