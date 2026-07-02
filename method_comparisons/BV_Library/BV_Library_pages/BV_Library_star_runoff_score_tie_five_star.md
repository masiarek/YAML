# BV parity — STAR: runoff & score tie, five-star tiebreaker

*Generated from [`BV_Library_star_runoff_score_tie_five_star.yaml`](../BV_Library_star_runoff_score_tie_five_star.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Allison

## Scenario

Ported from BetterVoting's tabulator unit tests
(Star.test.ts :: "Runoff & Score Tie, use five-star tiebreaker to resolve").
Score totals and runoff both tie; the five-star count breaks it for Allison.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill
2,4
5,3
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_runoff_score_tie_five_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Allison  |  * Bill    |
--------------------------------------------
    * Allison > |     ---     | 1 - 0 - 1  |
       * Bill > |  1 - 0 - 1  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Allison, Bill (pairwise ties)

[Divergence from STAR]
  STAR     = Allison
  Approval = Bill   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Allison,Bill
      2,   4
      5,   3

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Allison  1  0  0  1  0  0  |     7   3.5
Bill     0  1  1  0  0  0  |     7   3.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Allison       -- 7 -- First place
   Bill          -- 7 -- Second place
 Allison and Bill advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Allison       -- 1 -- Tied for first place
   Bill          -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Allison       -- 7 -- Tied for first place
   Bill          -- 7 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Allison       -- 1 -- First place
   Bill          -- 0
 Allison wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Allison
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_runoff_score_tie_five_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/BV_Library_star_runoff_score_tie_five_star.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
