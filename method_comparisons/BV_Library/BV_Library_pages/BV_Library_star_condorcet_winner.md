# BV parity — STAR: highest-scoring Condorcet winner

*Generated from [`BV_Library_star_condorcet_winner.yaml`](../BV_Library_star_condorcet_winner.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Allison

## Scenario

Ported from BetterVoting's tabulator unit tests (Star.test.ts :: "Condorcet Winner").
Allison is both the highest-scoring candidate and the Condorcet winner; Carmen is
the runner-up in BetterVoting's result.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill,Carmen,Doug
5,2,1,4
5,2,1,0
5,2,1,0
5,2,1,0
5,3,4,0
5,1,4,0
5,1,4,0
4,0,5,1
3,4,5,0
3,5,5,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_condorcet_winner_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Allison  |    Bill    | * Carmen   |    Doug    |
----------------------------------------------------------------------
    * Allison > |     ---     | 8 - 0 - 2  | 7 - 0 - 3  | 9 - 0 - 1  |
         Bill > |  2 - 0 - 8  |    ---     | 4 - 1 - 5  | 7 - 1 - 2  |
     * Carmen > |  3 - 0 - 7  | 5 - 1 - 4  |    ---     | 8 - 1 - 1  |
         Doug > |  1 - 0 - 9  | 2 - 1 - 7  | 1 - 1 - 8  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Allison — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 10 ballots.
Count × Allison,Bill,Carmen,Doug
    3 ×       5,   2,     1,   0
    2 ×       5,   1,     4,   0
    1 ×       5,   2,     1,   4
    1 ×       5,   3,     4,   0
    1 ×       4,   0,     5,   1
    1 ×       3,   4,     5,   0
    1 ×       3,   5,     5,   5

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Allison  7  1  2  0  0  0  |    45   4.5
Bill     1  1  1  4  2  1  |    22   2.2
Carmen   3  3  0  0  4  0  |    31   3.1
Doug     1  1  0  0  1  7  |    10   1.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Allison       -- 45 -- First place
   Carmen        -- 31 -- Second place
   Bill          -- 22
   Doug          -- 10
 Allison and Carmen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Allison       -- 7 -- First place
   Carmen        -- 3
   Equal Support -- 0
 Allison wins.
   Runoff math:
     10  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     10  voters with a preference  (majority = 6)
           Allison 7 (70%)  ·  Carmen 3 (30%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Allison
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_condorcet_winner.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
