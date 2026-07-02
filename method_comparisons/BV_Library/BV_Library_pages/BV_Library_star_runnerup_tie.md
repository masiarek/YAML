# BV parity — STAR: runner-up tie, Allison wins

*Generated from [`BV_Library_star_runnerup_tie.yaml`](../BV_Library_star_runnerup_tie.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Allison

## Scenario

Ported from BetterVoting's tabulator unit tests (Star.test.ts :: "Runnerup tie").
Allison wins; Bill is the runner-up after tie handling.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill,Carmen,Doug
5,4,3,3
4,5,1,1
4,5,1,2
3,5,1,0
5,4,3,0
5,0,4,1
5,0,4,0
4,0,5,1
3,4,5,0
3,5,5,4
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_runnerup_tie_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Allison  |  * Bill    |   Carmen   |    Doug    |
----------------------------------------------------------------------
    * Allison > |     ---     | 5 - 0 - 5  | 7 - 0 - 3  | 9 - 0 - 1  |
       * Bill > |  5 - 0 - 5  |    ---     | 5 - 1 - 4  | 7 - 1 - 2  |
       Carmen > |  3 - 0 - 7  | 4 - 1 - 5  |    ---     | 7 - 2 - 1  |
         Doug > |  1 - 0 - 9  | 2 - 1 - 7  | 1 - 2 - 7  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Allison, Bill (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 10 ballots.
Allison,Bill,Carmen,Doug
      5,   4,     3,   3
      4,   5,     1,   1
      4,   5,     1,   2
      3,   5,     1,   0
      5,   4,     3,   0
      5,   0,     4,   1
      5,   0,     4,   0
      4,   0,     5,   1
      3,   4,     5,   0
      3,   5,     5,   4

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Allison  4  3  3  0  0  0  |    41   4.1
Bill     4  3  0  0  0  3  |    32   3.2
Carmen   3  2  2  0  3  0  |    32   3.2
Doug     0  1  1  1  3  4  |    12   1.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Allison       -- 41 -- First place
   Bill          -- 32 -- Tied for second place
   Carmen        -- 32 -- Tied for second place
   Doug          -- 12
 Allison advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Bill          -- 5 -- Second place
   Carmen        -- 4
   Equal Support -- 1
 Allison and Bill advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Allison       -- 5 -- Tied for first place
   Bill          -- 5 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Allison       -- 41 -- First place
   Bill          -- 32
 Allison wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Allison
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_runnerup_tie.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
