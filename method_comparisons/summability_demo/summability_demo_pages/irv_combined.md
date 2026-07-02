# Summability demo — RCV-IRV combined A+B (B eliminated; not summable)

*Generated from [`irv_combined.yaml`](../irv_combined.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** A

## Scenario

Districts A + B merged, counted by RCV-IRV. B won BOTH districts — but in
the combined electorate B has the fewest first choices (8 vs 9 and 9), is
eliminated first, and both B-bullet blocs exhaust. The race then ends in a
GENUINE 9-9 tie between A and C; the engine's seeded coin flip elects A (see
the note at expected_winners). No district subtotal can produce this result:
IRV needs every ballot in one pile. Compare the star_* trio, where
subtotals simply add.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:A
4:B
3:C>B>A
6:C
4:B
3:A>B>C
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/irv_combined_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Summability demo — RCV-IRV combined A+B (B eliminated; not summable)
 Tabulating 26 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                  9  Hopeful
C                  9  Hopeful
B                  8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
A                  9  Elected
C                  9  Rejected
B                  0  Rejected
Blank Votes        8  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/irv_combined.yaml
```

## See also

- [This set's lesson (README)](../README_summability_demo.md) — the hand-written teaching context for every case in this folder
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Exhausted ballots (conversation)](../../../interviews_conversations/exhausted_ballots_301.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
