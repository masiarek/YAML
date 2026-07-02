# YAML_library — the import pipeline & validation fixtures

Two jobs live here. **Teaching elections do not** — those live in
[`01_Single_winner/`](../01_Single_winner/), [`02_Multi_winner/`](../02_Multi_winner/),
and [`split_voting/`](../split_voting/), one canonical copy each.

## `1_positive/` — the BetterVoting import pipeline

- `01_convert_json_yaml.py` — converts a real BetterVoting JSON export into a
  canonical election YAML (real candidate names, aligned columns, the
  election's official lot order, embedded `expected_results`).
- `S_W1_N_*.json` — frozen real exports used as converter inputs.
- `_generated/` + `_generated_tabulated/` — converter output and its
  tabulation mirror.

Guarded by `tests/test_json_to_yaml_conversion.py` and
`tests/test_lot_number_tiebreak.py` (converter → YAML → engine, end to end).

## `2_negative/` — malformed fixtures

Every file here must make the engine **exit 1 with the right plain-language
message and no traceback**. Inventory-guarded by
`tests/test_negative_validation.py`: a fixture that "passes" is a bug.

## History note

Until 2026-07 this folder also held flattened copies of the `Runoff_*`,
`Flat_scores_ties_*`, `Whoops_*`, and `center_squeeze_voteline_1d` teaching
cases. They had already diverged from their canonical siblings and the test
harness runs the canonical files directly, so the copies were removed. If you
need one of those cases, use the canonical copy in `01_Single_winner/`.

# file: README_YAML_library.md
