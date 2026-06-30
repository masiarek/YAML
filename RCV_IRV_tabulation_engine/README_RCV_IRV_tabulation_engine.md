# RCV / IRV Tabulation Engine

A single-winner **Instant-Runoff Voting (IRV)** tabulator that reads the same
YAML election format as the STAR engine. It wraps the vendored
[`pyrankvote`](https://github.com/jontingvold/pyrankvote) library (MIT, see
`pyrankvote/LICENSE.txt`); `tabulate` is vendored alongside as its only
dependency, so the folder is self-contained.

## Usage

```bash
python rcv_irv_tabulation.py example_tennessee.yaml
```

Any STAR-style YAML works, since ballots are read as scores and converted to
ranks on the fly.

## Score → rank conversion

IRV needs *ranked* ballots, but the YAML stores *scores* (0..5). Each ballot is
converted with these rules:

- **Higher score = higher preference.**
- **Score 0** (or a blank/marker cell) means **unranked** — the candidate is
  left off that ballot. The ballot exhausts rather than transferring to a
  zero-scored candidate (matches STAR's "0 = no support" semantics).
- **Equal non-zero scores** are a **tie**. IRV requires a strict order, so ties
  are broken deterministically by candidate column order (left-to-right in the
  ballot header). This is a documented simplification — equal-rank IRV is not
  represented.

A ballot scored entirely 0 counts as a blank/exhausted vote.

## Status

Minimal first pass: correct round-by-round elimination and winner, using
pyrankvote's built-in result table. Colorized banners, `_tabulated` output
files, and `--save` parity with the STAR engine can be added later.
