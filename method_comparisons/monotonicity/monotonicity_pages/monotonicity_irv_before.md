# Non-monotonicity (RCV-IRV) — part 1: baseline, X wins

*Generated from [`monotonicity_irv_before.yaml`](../monotonicity_irv_before.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** X

## Scenario

Part 1 of the RCV-IRV monotonicity pair: 34 voters, X wins (Z is eliminated,
Z's ballots transfer to X). This is the baseline for the paradox — in part 2
(monotonicity_irv_after.yaml) four voters RAISE X from second to first
choice, change nothing else, and X LOSES. Keep both files side by side; the
ballots differ only in those four voters.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:X>Y
12:Y>Z
10:Z>X
```

## What the engine says

Full report from the [`_tabulated` mirror](../monotonicity_tabulated/monotonicity_irv_before_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Non-monotonicity (RCV-IRV) — part 1: baseline, X wins
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Y                 12  Hopeful
X                 12  Hopeful
Z                 10  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
X                 22  Elected
Y                 12  Rejected
Z                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  X
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/monotonicity_irv_before.yaml
```

## See also

- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README_monotonicity.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [monotonicity_irv_after](monotonicity_irv_after.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md)
