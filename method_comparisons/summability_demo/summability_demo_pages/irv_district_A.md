# Summability demo — RCV-IRV district A (B wins)

*Generated from [`irv_district_A.yaml`](../irv_district_A.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** B

## Scenario

District A of the RCV-IRV summability trio: C is eliminated, C's ballots
transfer to B, B wins. Looks precinct-friendly — until you try to combine
districts. See irv_combined.yaml: no fixed set of district-level IRV
subtotals can be added into the combined answer, because who gets eliminated
depends on ALL ballots at once.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:A
4:B
3:C>B>A
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/irv_district_A_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Summability demo — RCV-IRV district A (B wins)
 Tabulating 13 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                  6  Hopeful
B                  4  Hopeful
C                  3  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                  7  Elected
A                  6  Rejected
C                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/irv_district_A.yaml
```

## See also

- [This set's lesson (README)](../README_summability_demo.md) — the hand-written teaching context for every case in this folder
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_B](irv_district_B.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
