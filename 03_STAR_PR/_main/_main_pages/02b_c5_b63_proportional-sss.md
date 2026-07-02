# Proportional STAR — Sequentially Spent Score

*Generated from [`02b_c5_b63_proportional-sss.yaml`](../02b_c5_b63_proportional-sss.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [Sequentially Spent Score (proportional STAR)](../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Alice, Ben, Dan

## Scenario

Same majority/minority ballots as the Allocated Score example, tabulated with
Sequentially Spent Score (SSS), a modern proportional-score method. The
minority bloc again earns a seat that Bloc STAR would deny.

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

Full report from the [`_tabulated` mirror](../_main_tabulated/02b_c5_b63_proportional-sss_tabulated.txt) (regenerated on every run; every analysis forced on):

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

--- Sequentially Spent Score Voting Method (3 winners) ---
[Sequentially Spent Score]
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
 Hare score quota is 105.

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Ben           -- 168 -- First place
   Alice         -- 165
   Cara          -- 135
   Dan           -- 111
   Eve           -- 105
 Ben wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 168, Hare score quota is 105, giving back surplus.
 Reducing each ballot's stars by their vote * 3/8.
 Reweighted 39 ballots:
    27 ballots voted 4, stars reduced from 5 to 5/2, reweighted to 1/2.
    12 ballots voted 5, stars reduced from 5 to 15/8, reweighted to 3/8.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Dan           -- 111     -- First place
   Eve           -- 105
   Alice         --  76+1/2
   Cara          --  63
 Dan wins a seat.

[Sequentially Spent Score: Round 2: Ballot allocation round]
 Total score is 111, Hare score quota is 105, giving back surplus.
 Reducing each ballot's stars by their vote * 2/37.
 Reweighted 24 ballots:
    15 ballots voted 5, stars reduced from 5 to 10/37, reweighted to 2/37.
    9 ballots voted 4, stars reduced from 5 to 45/37, reweighted to 9/37.

[Sequentially Spent Score: Round 3]
 The highest-scoring candidate wins a seat.
   Alice         -- 76+1/2  -- First place
   Cara          -- 63
   Eve           -- 14+7/37
 Alice wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (3 winners)]
 Alice
 Ben
 Dan
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/_main/02b_c5_b63_proportional-sss.yaml
```

## See also

- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [02a_c5_b63_proportional-allocated-score](02a_c5_b63_proportional-allocated-score.md) · [02c_c5_b63_proportional-rrv](02c_c5_b63_proportional-rrv.md) · [03b_star_pr_3seats](03b_star_pr_3seats.md) · [rrv_sample_c15_b13_three-parties](rrv_sample_c15_b13_three-parties.md)
