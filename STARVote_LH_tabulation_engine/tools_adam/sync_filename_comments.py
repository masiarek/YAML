#!/usr/bin/env python3
"""
sync_filename_comments.py
=========================
Ensure every scenario file ends with a trailing comment naming itself:

    # file: 01a_c2_b1_two-candidates.yaml

A comment can't update itself when you rename the file, so run this after a
rename (or as part of tabulate_all.py) and it rewrites that last line to match
the file's CURRENT name. Any previous '# file:' trailer is replaced, so it never
accumulates or goes stale.

Usage:
    python tools_adam/sync_filename_comments.py            # apply to all
    python tools_adam/sync_filename_comments.py --dry-run  # show changes only
"""

import argparse
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
ROOT = ENGINE_DIR / "elections_illustrations"
PREFIX = "# file:"


def scenario_files():
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p.suffix.lower() in (".yaml", ".yml"):
            if not any(part.endswith("_tabulated") for part in p.relative_to(ROOT).parts):
                yield p


def desired_text(path):
    text = path.read_text(encoding="utf-8")
    # Drop any trailing blank lines and any existing '# file:' trailer lines.
    lines = text.splitlines()
    while lines and (not lines[-1].strip() or lines[-1].lstrip().startswith(PREFIX)):
        lines.pop()
    body = "\n".join(lines).rstrip()
    return f"{body}\n\n{PREFIX} {path.name}\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="show changes, don't write")
    args = ap.parse_args(argv)

    changed = 0
    for p in scenario_files():
        new_text = desired_text(p)
        if new_text == p.read_text(encoding="utf-8"):
            continue
        changed += 1
        rel = p.relative_to(ROOT)
        if args.dry_run:
            print(f"  would update {rel}")
        else:
            p.write_text(new_text, encoding="utf-8")
            print(f"  updated {rel}  ->  {PREFIX} {p.name}")

    if not changed:
        print("All filename comments are in sync.")
    elif args.dry_run:
        print(f"\n{changed} file(s) would change. Run without --dry-run to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
