# _demo_dropbox — frictionless drop-to-results for BetterVoting exports

Ad-hoc demo zone. Drop a BetterVoting (BV) `.json` export in here and it gets
converted, tabulated, and echoed to screen automatically. **Outside the test
suite** — nothing dropped here is picked up by `pytest`.

## Use it

1. Start the watcher once per session:
   - double-click **`Run BV Demo Watcher.command`**, or
   - run `python _demo_dropbox/watch_bv.py` in a terminal.
2. Drop one or more BV `.json` files into this folder.
3. Watch the results print in the terminal. Press **Ctrl-C** to stop.

## What happens to each file

```
file.json  →  convert (JSON → YAML)  →  tabulate (STAR engine)  →  ECHO
           →  archive into processed/<timestamp>__<name>/
```

Each finished demo lands in `processed/<timestamp>__<name>/` containing three
files: the renamed source `.json`, the generated `.yaml`, and the full
`_tabulated.txt` report. The drop zone stays empty between drops.

A file that fails to convert (bad JSON) is moved to `processed/_errors/` so it
doesn't reprocess in a loop.

## Output format

By default the watcher keeps the **full BV export** — including the
`=== title ===` header and BV's official `lot_numbers` tie-break sequence. The
lot numbers are the real, official tiebreaker and are preserved so the
tabulation faithfully matches the BetterVoting result.

A `DEMO_FORMAT` flag near the top of `watch_bv.py` (default `False`) can strip
the title and lot_numbers for a bare scratch-file look, but that changes how ties
resolve (falls back to CSV column order), so leave it off for real demos.

## Notes

- The pipeline reuses the exact repo tools — `YAML_library/1_positive/01_convert_json_yaml.py`
  and `STARVote_LH_tabulation_engine/starvote_larry_hastings.py` — so results
  match the rest of the repo.
- `_generated/` and `_generated_tabulated/` are transient staging dirs; the
  watcher empties them into `processed/` after each run.
- Demo data is git-ignored (see `.gitignore`); only the scripts + this README
  are tracked.
