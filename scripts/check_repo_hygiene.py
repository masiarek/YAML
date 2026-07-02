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


# --------------------------------------------------------------------------- #
# Relative-link checker: every [text](relative/path) in a tracked .md must
# resolve. Folder reorganizations silently break these; this catches them.
# (External http(s)/mailto links and pure #anchors are not checked.)
# --------------------------------------------------------------------------- #
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
_EXTERNAL = re.compile(r"(?i)^\s*(https?:|mailto:|#)")
_FENCED = re.compile(r"```.*?```", re.S)
_INLINE_CODE = re.compile(r"`[^`\n]*`")


def check_links():
    """Return sorted [(md_file, raw_link)] for every relative link that does
    not resolve to an existing file or directory."""
    from urllib.parse import unquote
    broken = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dirpath, REPO)
        if rel_dir != "." and _skip(rel_dir):
            continue
        for fn in filenames:
            if not fn.lower().endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.normpath(os.path.join(rel_dir, fn))
            try:
                text = open(full, encoding="utf-8").read()
            except OSError:
                continue
            # Links inside code blocks / inline code are examples, not links.
            text = _INLINE_CODE.sub("", _FENCED.sub("", text))
            for m in MD_LINK.finditer(text):
                raw = m.group(1).strip()
                if _EXTERNAL.match(raw):
                    continue
                target = raw.split()[0].strip("<>")     # drop optional "title"
                target = target.split("#")[0]           # drop #fragment
                if not target:
                    continue
                # 'REPLACE_*' basenames are deliberate placeholders (e.g. a
                # screenshot not yet captured) — skip, don't report.
                if os.path.basename(target).startswith("REPLACE_"):
                    continue
                p = os.path.normpath(
                    os.path.join(dirpath, unquote(target).replace("/", os.sep)))
                if not os.path.exists(p):
                    broken.append((rel, raw))
    return sorted(set(broken))


def main(argv):
    rc = 0
    hits = scan()
    if not hits:
        print("repo-hygiene: ✓ no misplaced/junk files found.")
    else:
        rc = 1
        print("repo-hygiene: ⚠️  misplaced or junk files detected "
              f"({len(hits)}). These are ignored by git, but check each — a *real*")
        print("              file pasted with the wrong name/place would otherwise be lost:")
        for rel, msg in hits:
            print(f"   • {rel}\n       {msg}")
        print("\n  (House rules: BV screenshots → img/<bv_id>_*.png; BV exports → "
              "<descriptor>_<bvid>_bv_export.json. See CLAUDE.md.)")
    dead = check_links()
    if not dead:
        print("repo-hygiene: ✓ all relative Markdown links resolve.")
    else:
        rc = 1
        print(f"repo-hygiene: ⚠️  broken relative links ({len(dead)}) — a folder "
              "move probably left these behind:")
        for rel, raw in dead:
            print(f"   • {rel}  →  ({raw})")
    # exit non-zero so a caller *can* gate on it; the pre-commit hook runs it
    # warn-only, and tests/test_md_links.py gates on the link half.
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
