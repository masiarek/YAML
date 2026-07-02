# RCV-IRV — a basic ranked-ballot example (3 candidates)

*Generated from [`RCV_ballot_example.yaml`](../RCV_ballot_example.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** A

## Scenario

A first ranked-ballot count: 100 voters, three candidates, weighted rows
like "40:A>C>B". A leads with 40 first choices but no majority; C (25) is
eliminated, C's ballots transfer to A, and A wins 65-35. Use it to learn the
round-by-round report before the pathology cases (center_squeeze,
monotonicity, summability in method_comparisons/) show what elimination
order can do.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
40:A>C>B
35:B>C>A
25:C>A>B
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/RCV_ballot_example_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  RCV-IRV — a basic ranked-ballot example (3 candidates)
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                 40  Hopeful
B                 35  Hopeful
C                 25  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
A                 65  Elected
B                 35  Rejected
C                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py other_methods/_main/RCV_ballot_example.yaml
```

## See also

- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README_center_squeeze.md)
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README_monotonicity.md)
- [Summability (topic hub)](../../../00_start_here/topics/summability/README_summability.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [03a_stv_3seats](03a_stv_3seats.md)
