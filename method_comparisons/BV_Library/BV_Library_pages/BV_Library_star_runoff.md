# BV parity — STAR: runoff, lower total wins the runoff

*Generated from [`BV_Library_star_runoff.yaml`](../BV_Library_star_runoff.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bill

## Scenario

Ported from BetterVoting's tabulator unit tests (Star.test.ts :: "Runoff").
Bill wins the automatic runoff despite a simple two-ballot field.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill
0,5
2,4
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_runoff_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Allison  |  * Bill    |
--------------------------------------------
    * Allison > |     ---     | 0 - 0 - 2  |
       * Bill > |  2 - 0 - 0  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Bill — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Allison,Bill
      0,   5
      2,   4

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Allison  0  0  0  1  0  1  |     2   1.0
Bill     1  1  0  0  0  0  |     9   4.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bill          -- 9 -- First place
   Allison       -- 2 -- Second place
 Bill and Allison advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bill          -- 2 -- First place
   Allison       -- 0
   Equal Support -- 0
 Bill wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Bill 2 (100%)  ·  Allison 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bill
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_runoff.yaml
```

## See also

- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
