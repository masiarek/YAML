"""
hits_to_star.py

Convert a divergence-hits CSV (from find_star_irv_sweep.py or
find_four_way_divergence.py) into regular STAR ballot grids.

Each `ballots_ABC` field like "001_001_340" becomes:

    A,B,C
    0,0,1
    0,0,1
    3,4,0

By default writes one combined text file with a labeled block per hit. With
--yaml it also writes one runnable .yaml per hit (voting_method: STAR) into a
subfolder, so each can be fed straight to starvote_larry_hastings.py.

Usage:
    python hits_to_star.py                         # star_irv_hits.csv -> .txt
    python hits_to_star.py four_way_hits.csv --yaml
    python hits_to_star.py star_irv_hits.csv --out my_blocks.txt
"""

import argparse
import csv
import os


def header(n_cands):
    return ",".join(chr(65 + i) for i in range(n_cands))


def ballots_block(ballots_abc):
    """'001_340' -> 'A,B,C\\n0,0,1\\n3,4,0' (header inferred from segment width)."""
    segments = ballots_abc.split("_")
    n = len(segments[0])
    lines = [header(n)]
    for seg in segments:
        lines.append(",".join(seg))  # one char (score) per candidate
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file", nargs="?", default="star_irv_hits.csv")
    ap.add_argument("--out", default=None, help="combined output text file")
    ap.add_argument("--yaml", action="store_true",
                    help="also write one runnable .yaml per hit")
    args = ap.parse_args()

    base = os.path.splitext(os.path.basename(args.csv_file))[0]
    out_txt = args.out or f"{base}_ballots.txt"
    yaml_dir = f"{base}_yaml"
    if args.yaml:
        os.makedirs(yaml_dir, exist_ok=True)

    rows = 0
    with open(args.csv_file, newline="", encoding="utf-8-sig") as f, \
         open(out_txt, "w", encoding="utf-8") as out:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            abc = (row.get("ballots_ABC") or "").strip()
            if not abc:
                continue
            block = ballots_block(abc)
            star = row.get("STAR", "?")
            irv = row.get("RCV_IRV", "?")
            cond = row.get("Condorcet")
            appr = row.get("Approval")
            label = f"# hit {i}: STAR={star}  RCV-IRV={irv}"
            if appr:
                label += f"  Approval={appr}"
            if cond:
                label += f"  Condorcet={cond}"
            out.write(f"{label}\n{block}\n\n")
            rows += 1

            if args.yaml:
                yml = (f"voting_method: STAR\nnum_winners: 1\n"
                       f"options:\n  show_irv: true\nballots: |-\n")
                yml += "\n".join("  " + ln for ln in block.splitlines())
                yml += f"\n\n# {label[2:]}\n"
                with open(os.path.join(yaml_dir, f"hit_{i:04d}.yaml"),
                          "w", encoding="utf-8") as yf:
                    yf.write(yml)

    print(f"Wrote {rows} STAR ballot blocks to {out_txt}")
    if args.yaml:
        print(f"Wrote {rows} runnable YAML files to {yaml_dir}/")


if __name__ == "__main__":
    main()
