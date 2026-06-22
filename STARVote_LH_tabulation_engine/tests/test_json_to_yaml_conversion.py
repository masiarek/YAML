"""
test_json_to_yaml_conversion.py
===============================
Guards the BetterVoting-export -> YAML pipeline (`YAML_library/1_positive/
01_convert_json_yaml.py`). It runs the converter on an ISOLATED copy of a real
BetterVoting JSON export (in pytest's tmp_path, so the repo is never mutated) and
checks that:
  * exactly one YAML file is produced,
  * it has the expected structure (candidates + ballots),
  * the expected-winners step actually ran — non-empty winners, no error in the
    report (this is the regression guard for the `parse_ballots_from_string`
    arity drift that silently emptied the winners),
  * the embedded winners agree with a fresh tabulation of the produced file.
"""

import importlib.util
import shutil
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
LIB_POS = REPO_ROOT / "YAML_library" / "1_positive"
CONVERTER = LIB_POS / "01_convert_json_yaml.py"
SOURCE_JSON = LIB_POS / "S_W1_N_BV001a_UnderstandingStarBallotFullSelection_q83qj6.json"

sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))
import starvote_larry_hastings as engine  # noqa: E402
from scenario_eval import scenario_winners  # noqa: E402


def _load_converter():
    spec = importlib.util.spec_from_file_location("bv_json_converter", CONVERTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.mark.skipif(
    not (CONVERTER.exists() and SOURCE_JSON.exists()),
    reason="converter or source BetterVoting JSON not present",
)
def test_bettervoting_json_converts_to_tabulating_yaml(tmp_path):
    conv = _load_converter()

    # Run on an isolated copy so the repo's files are never touched.
    work_json = tmp_path / SOURCE_JSON.name
    shutil.copy(SOURCE_JSON, work_json)
    conv.convert_election_data(str(work_json), engine)

    # The converter writes into a "_generated/" staging subfolder.
    produced = list((tmp_path / "_generated").glob("*.yaml"))
    assert len(produced) == 1, f"expected exactly one produced YAML, got {produced}"
    yml = produced[0]

    data = yaml.safe_load(yml.read_text(encoding="utf-8"))
    race = data["election"]["races"][0]
    assert str(race["ballots"]).strip(), "no ballots block produced"
    assert race["candidates"], "no candidates produced"

    embedded = [str(w) for w in race["expected_results"]["winners"]]
    report = str(race["expected_results"]["report"])

    # Regression guard: the expected-results step must actually run.
    assert embedded, "converter produced EMPTY expected winners (pipeline broken)"
    assert "Error generating expected results" not in report, report

    # The embedded winners must agree with a fresh tabulation of the produced file.
    winners, _seats = scenario_winners(yml)
    assert sorted(winners) == sorted(embedded), (
        f"produced file tabulates {winners}, but its embedded winners are {embedded}"
    )
    # Known answer for BV001a (candidate id A = Andre scores 5).
    assert embedded == ["A"], f"unexpected winners for BV001a: {embedded}"
