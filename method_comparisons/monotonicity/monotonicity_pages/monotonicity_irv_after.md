# Non-monotonicity (RCV-IRV) — part 2: raising X makes X lose

*Generated from [`monotonicity_irv_after.yaml`](../monotonicity_irv_after.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Z

## Scenario

Part 2 of the RCV-IRV monotonicity pair: four Y>Z voters move X up to first
(12:X>Y becomes 16:X>Y), a pure GAIN of support for X — and X now loses.
The extra support changed the elimination order: Y goes out first, Y's
ballots feed Z, and Z beats X 18-16. More support made the winner lose —
IRV's non-monotonicity. STAR cannot do this (more points never hurt); see
the monotonicity_star_* pair and the monotonicity topic hub.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
16:X>Y
8:Y>Z
10:Z>X
```

## What the engine says

Full report from the [`_tabulated` mirror](../monotonicity_tabulated/monotonicity_irv_after_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Non-monotonicity (RCV-IRV) — part 2: raising X makes X lose
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
X                 16  Hopeful
Z                 10  Hopeful
Y                  8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Z                 18  Elected
X                 16  Rejected
Y                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Z
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/monotonicity_irv_after.yaml
```

## See also

- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README_monotonicity.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [monotonicity_irv_before](monotonicity_irv_before.md) · [monotonicity_star_after](monotonicity_star_after.md) · [monotonicity_star_before](monotonicity_star_before.md)
