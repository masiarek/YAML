# Proportional — Reweighted Range Voting

*Generated from [`02c_c5_b63_proportional-rrv.yaml`](../02c_c5_b63_proportional-rrv.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Alice, Ben, Dan

## Scenario

Same majority/minority ballots as the other proportional examples, tabulated
with Reweighted Range Voting (RRV). Older and not part of STAR's score-then-
runoff family, but it also seats the minority bloc — included for comparison.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Ben,Cara,Dan,Eve
18: 5, 4, 3, 0, 0
12: 4, 5, 3, 0, 0
 9: 3, 4, 5, 0, 0
15: 0, 0, 0, 5, 4
 9: 0, 0, 0, 4, 5
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/02c_c5_b63_proportional-rrv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Alice    |   * Ben     |     Cara    |     Dan     |     Eve     |
-----------------------------------------------------------------------------------------
       * Alice > |     ---      |18 - 24 - 21 |30 - 24 -  9 |39 -  0 - 24 |39 -  0 - 24 |
         * Ben > | 21 - 24 - 18 |    ---      |30 - 24 -  9 |39 -  0 - 24 |39 -  0 - 24 |
          Cara > |  9 - 24 - 30 | 9 - 24 - 30 |    ---      |39 -  0 - 24 |39 -  0 - 24 |
           Dan > | 24 -  0 - 39 |24 -  0 - 39 |24 -  0 - 39 |    ---      |15 - 39 -  9 |
           Eve > | 24 -  0 - 39 |24 -  0 - 39 |24 -  0 - 39 | 9 - 39 - 15 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Ben — matches the STAR winner

[Divergence from STAR]
  STAR                   = Ben
  Choose-One (Plurality) = Alice   (differs from STAR)
  Approval               = Alice   (differs from STAR)

--- Reweighted Range Voting Method (3 winners) ---
[Reweighted Range Voting]
 Tabulating 63 ballots.
Count × Alice,Ben,Cara,Dan,Eve
   18 ×     5,  4,   3,  0,  0
   15 ×     0,  0,   0,  5,  4
   12 ×     4,  5,   3,  0,  0
    9 ×     3,  4,   5,  0,  0
    9 ×     0,  0,   0,  4,  5

[Score Distribution] (number of ballots giving each score)
        5   4   3   2   1   0  | Total   Avg
Alice  18  12   9   0   0  24  |   165   2.6
Ben    12  27   0   0   0  24  |   168   2.7
Cara    9   0  30   0   0  24  |   135   2.1
Dan    15   9   0   0   0  39  |   111   1.8
Eve     9  15   0   0   0  39  |   105   1.7
 Want to fill 3 seats.

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Ben           -- 168 -- First place
   Alice         -- 165
   Cara          -- 135
   Dan           -- 111
   Eve           -- 105
 Ben wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 39 ballots:
   27 ballots reweighted from 1 to 5/9.
   12 ballots reweighted from 1 to 1/2.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Dan           -- 111 -- First place
   Eve           -- 105
   Alice         --  89
   Cara          --  73
 Dan wins a seat.

[Reweighted Range Voting: Round 2: Reweighing Ballots]
 Reweighted 24 ballots:
   15 ballots reweighted from 1 to 1/2.
   9 ballots reweighted from 1 to 5/9.

[Reweighted Range Voting: Round 3: Score round]
 The highest-scoring candidate wins a seat.
   Alice         -- 89 -- First place
   Cara          -- 73
   Eve           -- 55
 Alice wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (3 winners)]
 Alice
 Ben
 Dan
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/_main/02c_c5_b63_proportional-rrv.yaml
```

## See also

- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [02a_c5_b63_proportional-allocated-score](02a_c5_b63_proportional-allocated-score.md) · [02b_c5_b63_proportional-sss](02b_c5_b63_proportional-sss.md) · [03b_star_pr_3seats](03b_star_pr_3seats.md) · [rrv_sample_c15_b13_three-parties](rrv_sample_c15_b13_three-parties.md)
