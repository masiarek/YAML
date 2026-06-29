#!/usr/bin/env python3
"""
check_repo_hygiene.py — warn about misplaced / junk files.

The recurring problem: pasting screenshots or BetterVoting exports lands generic
names in the wrong place (PyCharm drops `img_5.png` into a folder root; BV exports
arrive as `Ballot Data ... .json`). `.gitignore` keeps those out of commits, but
silent ignoring is risky — a *real* screenshot pasted as `img_3.png` would vanish
unnoticed. So this script scans the working tree (ignored files included) and
**warns** with where each file should actually go.

It does NOT delete or move anything — it just tells you. Run it directly, or let
the pre-commit hook run it (warn-only; it never blocks a commit).

    python scripts/check_repo_hygiene.py
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories we never police (raw staging, generated, vendored, caches).
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__",
             "_demo_dropbox", ".idea", ".claude"}


def _skip(rel):
    parts = rel.split(os.sep)
    return any(p in SKIP_DIRS for p in parts) or "_tabulated" in rel or "_generated" in rel


# Each rule: (compiled regex on the basename, human message with where it belongs).
RULES = [
    (re.compile(r"(?i)^(img|image)[ _-]?\d+\.png$"),
     "generic paste image — BV screenshots belong in an `img/` subfolder, renamed "
     "`<bv_id>_<what>.png` (e.g. img/r2pvc9_result_bars.png)."),
    (re.compile(r"(?i)^screen ?shot.*\.png$"),
     "raw screenshot name — move into the case's `img/` subfolder and rename "
     "`<bv_id>_<what>.png`."),
    (re.compile(r"(?i)^ballot data.*\.json$"),
     "raw BetterVoting export drop — convert/rename to the case's "
     "`<descriptor>_<bvid>_bv_export.json`, or delete if it's a stray."),
    (re.compile(r"(?i).* - copy.*"),
     "looks like a duplicated file (\" - Copy\") — rename or delete."),
    (re.compile(r"(?i)^untitled.*"),
     "placeholder name (\"Untitled…\") — rename to something meaningful or delete."),
]


def scan():
    hits = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dirpath, REPO)
        if rel_dir != "." and _skip(rel_dir):
            continue
        for fn in filenames:
            for rx, msg in RULES:
                if rx.match(fn):
                    rel = os.path.normpath(os.path.join(rel_dir, fn))
                    hits.append((rel, msg))
                    break
    hits.sort()
    return hits


def main(argv):
    hits = scan()
    if not hits:
        print("repo-hygiene: ✓ no misplaced/junk files found.")
        return 0
    print("repo-hygiene: ⚠️  misplaced or junk files detected "
          f"({len(hits)}). These are ignored by git, but check each — a *real*")
    print("              file pasted with the wrong name/place would otherwise be lost:")
    for rel, msg in hits:
        print(f"   • {rel}\n       {msg}")
    print("\n  (House rules: BV screenshots → img/<bv_id>_*.png; BV exports → "
          "<descriptor>_<bvid>_bv_export.json. See CLAUDE.md.)")
    # exit non-zero so a caller *can* gate on it; the pre-commit hook runs it warn-only.
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
