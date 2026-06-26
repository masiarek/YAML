#!/usr/bin/env python3
"""
BV demo dropbox watcher  —  frictionless drop-to-results for ad-hoc demos.

Watch this folder (_demo_dropbox/) for BetterVoting JSON exports. For each new
file the watcher runs the standard repo pipeline and echoes the result to screen:

    drop file.json  ->  convert (JSON -> YAML)  ->  tabulate (STAR engine)
                    ->  ECHO results  ->  archive everything into processed/

Nothing here is part of the test suite — _demo_dropbox/ lives outside the tested
paths (01_Single_winner/, split_voting/, YAML_library/1_positive/), so dropping
throwaway demo elections here never touches `pytest`.

Run it:
    double-click  "Run BV Demo Watcher.command"
    or:           python _demo_dropbox/watch_bv.py

Stop it: Ctrl-C in the terminal window.

Dependency-free: plain polling loop, no `watchdog` needed.
"""

import importlib.util
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml

# ----- locations (all derived from this file, so cwd doesn't matter) ----------
DROP = Path(__file__).resolve().parent          # _demo_dropbox/
REPO = DROP.parent                              # repo root (…/YAML)
CONVERTER = REPO / "YAML_library" / "1_positive" / "01_convert_json_yaml.py"
ENGINE = REPO / "STARVote_LH_tabulation_engine" / "starvote_larry_hastings.py"
ENGINE_DIR = ENGINE.parent
GEN = DROP / "_generated"                       # staging for produced YAML
GEN_TAB = DROP / "_generated_tabulated"         # staging for produced _tabulated.txt
PROCESSED = DROP / "processed"                  # archive of finished demos
ERRORS = PROCESSED / "_errors"                  # JSON that failed to convert

POLL_SECONDS = 1                                # how often to scan the folder

# Keep the full BetterVoting export as-is (default). The BV `lot_numbers` are the
# OFFICIAL tie-break sequence and must be preserved for a faithful tabulation —
# dropping them would silently change tie outcomes. Set True only if you want a
# bare scratch-file look (no  === title ===  header, ties fall back to CSV column
# order); not recommended for real demos.
DEMO_FORMAT = False


# ----- load the repo's converter + engine as importable modules ---------------
def _load_module(name, path):
    """Import a .py file by path (needed because 01_convert_json_yaml.py starts
    with a digit and can't be imported by name)."""
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_engine():
    """Engine module is optional — it only enriches the YAML with an
    `expected_results:` block during conversion. If it can't load we still
    convert + tabulate fine."""
    if str(ENGINE_DIR) not in sys.path:
        sys.path.append(str(ENGINE_DIR))   # so the vendored `starvote` resolves
    try:
        return _load_module("starvote_larry_hastings", ENGINE)
    except Exception as e:  # noqa: BLE001 - best-effort, demo tool
        print(f"  (note: engine module not loaded, expected_results skipped — {e})")
        return None


def _demoize(yaml_path, converter):
    """Rewrite the generated YAML to the clean "ver1" demo format: drop the
    BV title/description header echo and the official lot_numbers (so ties fall
    back to CSV column order), and drop the stored expected_results block.
    Tabulation winner is unaffected; only presentation changes."""
    data = yaml.safe_load(yaml_path.read_text())
    elec = data.get("election", data)
    elec.pop("election_title", None)
    elec.pop("election_description", None)
    races = elec.get("races", [elec])
    for race in races:
        race.pop("lot_numbers", None)
        race.pop("expected_results", None)
        # keep the ballots block readable as a literal scalar
        if isinstance(race.get("ballots"), str):
            race["ballots"] = converter.LiteralString(race["ballots"])
    yaml_path.write_text(
        yaml.dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False)
    )


# ----- one file, full pipeline ------------------------------------------------
def process(json_path, converter, engine_module):
    stamp = datetime.now()
    # The name exactly as dropped, captured BEFORE the converter renames the JSON
    # to the generated base name — otherwise the original drop name is lost.
    orig_name = json_path.name
    # BV election id (e.g. "4c7kp9"); used as the short archive base name.
    try:
        bv_id = ((json.loads(json_path.read_text()).get("Election") or {})
                 .get("election_id") or "").strip()
    except Exception:  # noqa: BLE001 - best-effort, demo tool
        bv_id = ""
    print("\n" + "=" * 64)
    print(f"  {stamp:%H:%M:%S}  new file: {json_path.name}")
    print("=" * 64)

    # 1) convert -------------------------------------------------------------
    before = {p.name for p in GEN.glob("*.yaml")} if GEN.exists() else set()
    try:
        # embed_report=False → MINIMAL demo yaml (winner kept, full report dropped).
        # include_candidates=False → drop the redundant candidates: block (the
        # ballots header already lists them). The full report still lands in the
        # sibling _tabulated.txt.
        converter.convert_election_data(
            str(json_path), engine_module,
            embed_report=False, include_candidates=False,
        )
    except Exception as e:  # noqa: BLE001
        print(f"  ✗ conversion failed: {e}")
        ERRORS.mkdir(parents=True, exist_ok=True)
        dest = ERRORS / json_path.name
        if json_path.exists():
            shutil.move(str(json_path), str(dest))
            print(f"  → moved bad file to processed/_errors/{json_path.name}")
        return

    # The converter renames the JSON and writes YAML into _generated/.
    # Pick the newest YAML there as the one we just produced.
    yamls = sorted(GEN.glob("*.yaml"), key=lambda p: p.stat().st_mtime, reverse=True)
    new_yaml = yamls[0] if yamls else None
    if new_yaml is None:
        print("  ✗ no YAML was produced — skipping.")
        return
    base = new_yaml.stem
    gen_base = base  # repo-standard generated name (S_W1_N_…_<id>) — kept for provenance

    # Name all demo artifacts by the BV election id plus a timestamp
    # (e.g. "4c7kp9_20260626_181840"), instead of the long dropped filename or
    # the generated pascal name. Falls back to the dropped stem if the JSON had
    # no election_id. Demo path only — the tested pipeline in
    # YAML_library/1_positive/ keeps the generated naming convention.
    ts = f"{stamp:%Y%m%d_%H%M%S}"
    new_base = f"{bv_id}_{ts}" if bv_id else f"{Path(orig_name).stem}_{ts}"
    if new_base != base:
        renamed_yaml = new_yaml.with_name(f"{new_base}.yaml")
        new_yaml.replace(renamed_yaml)
        new_yaml = renamed_yaml
        src_json = DROP / f"{base}.json"
        if src_json.exists():
            src_json.replace(DROP / f"{new_base}.json")
        base = new_base

    print()  # spacer after converter's own prints

    # 1b) demoize -> clean "ver1" format (no title header, column-order ties) -
    if DEMO_FORMAT:
        try:
            _demoize(new_yaml, converter)
        except Exception as e:  # noqa: BLE001
            print(f"  (note: demoize skipped — {e})")

    # 2) tabulate + echo -----------------------------------------------------
    result = subprocess.run(
        [sys.executable, str(ENGINE), str(new_yaml)],
        capture_output=True, text=True,
    )
    sys.stdout.write(result.stdout)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        print(f"  ✗ tabulation exited {result.returncode}")
        # leave artifacts in place for inspection; don't archive a failure
        return

    # 3) archive everything into processed/<base>/  (base already carries the
    #    timestamp, e.g. processed/4c7kp9_20260626_181840/) ------------------
    out_dir = PROCESSED / base
    out_dir.mkdir(parents=True, exist_ok=True)
    moved = []
    candidates = [
        DROP / f"{base}.json",                       # the renamed source export
        new_yaml,                                    # the generated YAML
        GEN_TAB / f"{base}_tabulated.txt",           # the full tabulated report
    ]
    for src in candidates:
        if src.exists():
            shutil.move(str(src), str(out_dir / src.name))
            moved.append(src.name)

    # Preserve the original dropped filename (the converter renames the JSON to
    # the generated base name, so without this the drop name would be lost).
    (out_dir / "_source.txt").write_text(
        f"original_dropped_filename: {orig_name}\n"
        f"artifact_base:             {base}\n"
        f"generated_base:            {gen_base}\n"
        f"processed_at:              {stamp:%Y-%m-%d %H:%M:%S}\n"
    )
    print(f"\n  ✓ archived {len(moved)} file(s) → processed/{out_dir.name}/")
    print(f"    (original drop name '{orig_name}' recorded in _source.txt)")


# ----- watch loop -------------------------------------------------------------
def main():
    # Line-buffer stdout so results echo live even when piped/redirected.
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:  # noqa: BLE001
        pass
    for d in (GEN, GEN_TAB, PROCESSED):
        d.mkdir(parents=True, exist_ok=True)
    converter = _load_module("bv_converter", CONVERTER)
    engine_module = _load_engine()

    print("BV demo watcher running.")
    print(f"  drop BetterVoting .json files into:  {DROP}")
    print(f"  results echo here; files archive to: {PROCESSED.name}/")
    print("  press Ctrl-C to stop.\n")

    # Track files until they stop changing (so we don't grab a half-copied file).
    pending = {}   # name -> (size, mtime)
    try:
        while True:
            for jp in sorted(DROP.glob("*.json")):
                stat = jp.stat()
                sig = (stat.st_size, stat.st_mtime)
                if pending.get(jp.name) == sig:
                    # stable since last poll → process it
                    pending.pop(jp.name, None)
                    process(jp, converter, engine_module)
                else:
                    # new or still being written → remember and wait one cycle
                    pending[jp.name] = sig
            # forget records for files that disappeared (archived/removed)
            present = {p.name for p in DROP.glob("*.json")}
            for gone in [n for n in pending if n not in present]:
                pending.pop(gone, None)
            time.sleep(POLL_SECONDS)
    except KeyboardInterrupt:
        print("\nstopped.")


if __name__ == "__main__":
    main()
