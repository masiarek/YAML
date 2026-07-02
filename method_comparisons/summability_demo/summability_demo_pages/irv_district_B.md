# Summability demo — RCV-IRV district B (B wins)

*Generated from [`irv_district_B.yaml`](../irv_district_B.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** B

## Scenario

District B of the RCV-IRV summability trio: B wins here too — both districts
independently elect B. Yet the combined electorate does NOT elect B (see
irv_combined.yaml: B is eliminated first there). District winners, and even
full district round-by-round tallies, cannot be summed into the combined
result — the non-summability this trio demonstrates.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:C
4:B
3:A>B>C
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/irv_district_B_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Summability demo — RCV-IRV district B (B wins)
 Tabulating 13 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
C                  6  Hopeful
B                  4  Hopeful
A                  3  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                  7  Elected
C                  6  Rejected
A                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/irv_district_B.yaml
```

## See also

- [This set's lesson (README)](../README_summability_demo.md) — the hand-written teaching context for every case in this folder
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
