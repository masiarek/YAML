#!/usr/bin/env python3
"""
build_yaml_index.py — regenerate the by-voting-method index of YAML elections.

Scans the repo for election YAML files (wherever they live — the test harnesses
glob specific folders, so we DON'T move files; we index them in place), reads each
file's `voting_method` and `num_winners`, and writes a Markdown catalog grouped by
method to:

    00_start_here/YAML_test_case_index/README.md

Run from the repo root:   python scripts/build_yaml_index.py
A pytest (test_yaml_index_current.py) regenerates this and fails if the committed
file is stale, so the index can't silently drift out of date.
"""
import os
import sys
import glob
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "00_start_here", "YAML_test_case_index", "README.md")

# Exclude generated mirrors, raw drops, and deliberately-malformed fixtures.
EXCLUDE = ("/.venv/", "/.git/", "node_modules", "_tabulated",
           "_demo_dropbox", "/_generated", "/negative_cases/",
           "/harness_cases/", "/2_negative/", "/tests/")

# Friendly section names + ordering for the methods we expect.
METHOD_ORDER = ["STAR", "RCV_IRV", "RCV", "RANKEDROBIN", "APPROVAL",
                "STV", "BLOC", "SSS", "RRV", "ALLOCATED"]
METHOD_LABEL = {
    "STAR": "STAR", "RCV_IRV": "RCV-IRV (Hare)", "RCV": "RCV-IRV (Hare)",
    "RANKEDROBIN": "Ranked Robin (RCV-RR / Copeland)",
    "APPROVAL": "Approval", "STV": "STV (proportional RCV)",
    "BLOC": "Bloc STAR", "SSS": "STAR-PR (Sequential Selection)",
    "RRV": "Reweighted Range", "ALLOCATED": "Allocated Score (STAR-PR)",
}


def _race(d):
    if isinstance(d, dict) and "election" in d and d.get("election", {}).get("races"):
        return d["election"]["races"][0]
    return d if isinstance(d, dict) else {}


def _title(d, race):
    """Prefer the explicit `election_title` field (machine-readable, the house
    convention). Comments are NOT parsed by YAML, so a `#`-comment title is only a
    fallback (see `_first_comment`)."""
    el = d.get("election", {}) if isinstance(d, dict) else {}
    return (el.get("election_title")
            or (race.get("election_title") if isinstance(race, dict) else None)
            or "").strip().replace("\n", " ")


def _first_comment(path):
    """Fallback title: the first descriptive `# comment` line (skips the
    `# file:` trailer and structural lines). Used only when `election_title` is
    absent — add an `election_title:` field to make a file's title explicit."""
    try:
        for ln in open(path):
            s = ln.strip()
            if not s.startswith("#"):
                continue
            s = s.lstrip("#").strip()
            if not s or s.lower().startswith("file:") or ":" == s[-1:]:
                continue
            if len(s) > 90:
                s = s[:88].rstrip() + "…"
            return "_" + s + "_"     # italic = scraped from a comment, not an explicit title
    except Exception:
        pass
    return ""


def _expected(race):
    for key in ("expected_winners",):
        v = race.get(key)
        if isinstance(v, list):
            return ", ".join(str(x) for x in v)
    er = race.get("expected_results")
    if isinstance(er, dict) and isinstance(er.get("winners"), list):
        return ", ".join(str(x) for x in er["winners"])
    return ""


def collect():
    rows = []
    for p in glob.glob(os.path.join(REPO, "**", "*.yaml"), recursive=True):
        rel = os.path.relpath(p, REPO)
        if any(s in "/" + rel.replace(os.sep, "/") for s in EXCLUDE):
            continue
        if any(t in os.path.basename(rel).lower() for t in ("temp", "trash", "scratch")):
            continue                       # scratch files, not real cases
        try:
            d = yaml.safe_load(open(p))
        except Exception:
            continue
        race = _race(d)
        if not isinstance(race, dict) or "ballots" not in race:
            continue
        method = str(race.get("voting_method", "STAR")).strip().upper() or "STAR"
        if method == "RCV":          # "RCV" and "RCV_IRV" are the same method
            method = "RCV_IRV"
        try:
            nw = int(race.get("num_winners", 1) or 1)
        except Exception:
            nw = 1
        explicit = _title(d, race)
        rows.append({
            "method": method, "nw": nw, "rel": rel.replace(os.sep, "/"),
            "name": os.path.basename(p), "dir": os.path.dirname(rel).replace(os.sep, "/"),
            "title": explicit or _first_comment(p), "expected": _expected(race),
            "has_title": bool(explicit),     # explicit election_title field?
        })
    rows.sort(key=lambda r: r["rel"])
    return rows


def render(rows):
    out = []
    out.append("# YAML test-case index — by voting method\n")
    out.append("**Auto-generated — do not edit by hand.** "
               "Run `python scripts/build_yaml_index.py` to refresh "
               "(a pytest fails if it's stale).\n")
    out.append("Election YAMLs live in many folders (the test harnesses glob specific "
               "ones, so they're indexed *in place*, not moved). Each file declares a "
               "`voting_method` and `num_winners`; this catalog groups them so you can "
               "browse by method. Excludes `_tabulated` mirrors, raw `_demo_dropbox` "
               "drops, generated copies, and deliberately-malformed negative fixtures.\n")
    out.append("Titles come from each file's **`election_title`** field (the convention — "
               "add one to make a file's title explicit & searchable). Where that's "
               "missing, a file's first `#` comment line is shown *in italics* as a "
               "fallback.\n")

    by_method = {}
    for r in rows:
        by_method.setdefault(r["method"], []).append(r)

    total = len(rows)
    multi = sum(1 for r in rows if r["nw"] > 1)
    out.append(f"**{total} election files** "
               f"({total - multi} single-winner, {multi} multi-winner) across "
               f"{len(by_method)} method(s).\n")

    # summary table
    out.append("| Method | Files |")
    out.append("|--------|------:|")
    seen = []
    for m in METHOD_ORDER + sorted(by_method):
        if m in by_method and m not in seen:
            seen.append(m)
            out.append(f"| {METHOD_LABEL.get(m, m)} | {len(by_method[m])} |")
    out.append("")

    for m in seen:
        items = sorted(by_method[m], key=lambda r: (r["nw"], r["dir"], r["name"]))
        out.append(f"## {METHOD_LABEL.get(m, m)}  ({len(items)})\n")
        out.append("| File | Folder | Winners | Title / expected |")
        out.append("|------|--------|:------:|------------------|")
        for r in items:
            link = f"[`{r['name']}`](../../{r['rel']})"
            note = r["title"] or ""
            if r["expected"]:
                note = (note + " " if note else "") + f"→ _{r['expected']}_"
            out.append(f"| {link} | `{r['dir']}/` | {r['nw']} | {note} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def audit_titles():
    """List indexed files that lack an explicit `election_title` field (a comment
    fallback may still be shown in the index, but adding the field makes the title
    explicit & searchable). Returns the list of relative paths."""
    missing = [r["rel"] for r in collect() if not r["has_title"]]
    if not missing:
        print("title-audit: ✓ every indexed election file has an election_title.")
    else:
        print(f"title-audit: ⚠️  {len(missing)} file(s) have no election_title "
              "(add one so the index title is explicit, not a scraped comment):")
        for rel in missing:
            print(f"   • {rel}")
    return missing


def main():
    rows = collect()
    text = render(rows)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write(text)
    print(f"wrote {os.path.relpath(OUT, REPO)} ({len(rows)} files indexed)")
    return text


if __name__ == "__main__":
    if "--audit-titles" in sys.argv[1:]:
        sys.exit(1 if audit_titles() else 0)
    main()
