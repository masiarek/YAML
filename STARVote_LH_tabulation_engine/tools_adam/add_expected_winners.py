#!/usr/bin/env python3
"""
add_expected_winners.py
=======================
One-time / refresh helper: tabulate every election file under
elections_illustrations/ and embed an `expected_winners:` list into each YAML
(unless it already has one, or --force is given). The test suite asserts the
engine still elects exactly these winners.

Only the winners are recorded — no verbatim report text — so the expectations
stay robust to display/formatting changes.

Usage:
    python tools_adam/add_expected_winners.py          # add where missing
    python tools_adam/add_expected_winners.py --force  # rewrite all
"""

import argparse
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))

from scenario_eval import scenario_winners  # noqa: E402

YAML_EXTS = (".yaml", ".yml")
BLOCK_KEY = "expected_winners:"


def scenario_files(root):
    out = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in YAML_EXTS:
            if not any(part.endswith("_tabulated") for part in p.relative_to(root).parts):
                out.append(p)
    return out


def strip_existing_block(text):
    """Remove a trailing top-level expected_winners block, if present."""
    lines = text.splitlines()
    keep, i = [], 0
    while i < len(lines):
        if lines[i].rstrip() == BLOCK_KEY or lines[i].startswith(BLOCK_KEY):
            # drop this line and the indented list items that follow
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                i += 1
            continue
        keep.append(lines[i])
        i += 1
    return "\n".join(keep).rstrip()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=str(ENGINE_DIR / "elections_illustrations"))
    ap.add_argument("--force", action="store_true", help="rewrite even if present")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    files = scenario_files(root)
    print(f"Found {len(files)} scenario file(s).")

    for f in files:
        text = f.read_text(encoding="utf-8")
        has_block = BLOCK_KEY in text
        if has_block and not args.force:
            print(f"  skip (has expected_winners): {f.relative_to(root)}")
            continue
        try:
            winners, _seats = scenario_winners(f)
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {f.relative_to(root)}: {e}")
            continue
        body = strip_existing_block(text) if has_block else text.rstrip()
        block = "\n".join([BLOCK_KEY] + [f"  - {w}" for w in winners])
        f.write_text(body + "\n\n" + block + "\n", encoding="utf-8")
        print(f"  wrote {winners} -> {f.relative_to(root)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
