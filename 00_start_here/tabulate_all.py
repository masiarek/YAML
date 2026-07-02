#!/usr/bin/env python3
"""
tabulate_all.py
===============
Run every election file in `elections_illustrations/` (recursively) through the
STAR tabulation engine and write a plain-text result for each.

For every folder that contains election files, a sibling "mirror" folder is
created with the `_tabulated` suffix (e.g. `03_STAR_PR` -> `03_STAR_PR_tabulated`,
and the top-level `elections_illustrations` -> `elections_illustrations_tabulated`).
Each output file also gets a `_tabulated` suffix, e.g.:

    elections_illustrations/03_STAR_PR/foo.yaml
    -> elections_illustrations/Multi_winner_tabulated/foo_tabulated.txt

All `*_tabulated` mirror folders are WIPED before the run, so the output always
reflects the current inputs (no stale files left behind).

Usage:
    python tools_adam/tabulate_all.py
    python tools_adam/tabulate_all.py --root some/other/folder
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# Make the engine importable so we reuse the SAME path logic the main script
# uses when writing individual `_tabulated` copies.
ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))

import starvote_larry_hastings as engine  # noqa: E402

MAIN_SCRIPT = ENGINE_DIR / "starvote_larry_hastings.py"
YAML_EXTS = (".yaml", ".yml")


def find_election_files(root):
    """All election files under root, skipping any '*_tabulated' mirror dirs."""
    files = []
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        if p.suffix.lower() not in YAML_EXTS:
            continue
        if any(part.endswith("_tabulated") for part in p.relative_to(root).parts):
            continue
        files.append(p)
    return files


def wipe_tabulated_dirs(root, files):
    """Delete EVERY '*_tabulated' mirror dir under (and beside) the root.

    We remove all of them — not just the dirs this run will write to — so that
    renaming or deleting source folders never leaves orphaned or doubled mirrors
    (e.g. 'Old_tabulated', 'X_tabulated_tabulated') behind.

    Best-effort: if the filesystem blocks deletion of a file (e.g. some external
    drives), we don't crash — the per-file writes below overwrite in place, and
    we warn so the user knows a folder may still hold stale files.
    """
    targets = {d for d in root.rglob("*_tabulated") if d.is_dir()}
    # The mirror for files directly in root is a sibling: root + '_tabulated'.
    targets.add(root.parent / (root.name + "_tabulated"))

    for d in sorted(t for t in targets if t.exists()):
        errors = []
        shutil.rmtree(d, onerror=lambda fn, path, exc: errors.append(path))
        if errors:
            print(f"  WARN could not fully wipe {d} ({len(errors)} item(s) kept)")
        else:
            print(f"  wiped {d}")
    return targets


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--root",
        default=str(ENGINE_DIR / "elections_illustrations"),
        help="folder to scan for election files",
    )
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        sys.exit(f"ERROR: not a folder: {root}")

    files = find_election_files(root)
    if not files:
        sys.exit(f"No .yaml/.yml election files found under {root}")

    print(f"Found {len(files)} election file(s) under {root}")
    print("Wiping existing '_tabulated' folders:")
    wipe_tabulated_dirs(root, files)

    print("\nTabulating:")
    failures = []
    for f in files:
        # The main script writes the '_tabulated' copy itself; we just invoke it.
        # NO_COLOR keeps the saved text clean (it strips ANSI anyway, but this
        # also keeps the console summary readable).
        result = subprocess.run(
            [sys.executable, str(MAIN_SCRIPT), str(f)],
            capture_output=True,
            text=True,
        )
        out_path = engine.tabulated_output_path(f)
        if result.returncode == 0:
            print(
                f"  OK   {f.relative_to(root)}  ->  {out_path.relative_to(root.parent)}"
            )
        else:
            failures.append(f)
            print(f"  FAIL {f.relative_to(root)}")
            err = (result.stderr or result.stdout).strip().splitlines()
            for line in err[-3:]:
                print(f"         {line}")

    print(f"\nDone: {len(files) - len(failures)} ok, {len(failures)} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
