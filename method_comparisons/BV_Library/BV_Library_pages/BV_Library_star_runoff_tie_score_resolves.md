# BV parity — STAR: runoff tie broken by score

*Generated from [`BV_Library_star_runoff_tie_score_resolves.yaml`](../BV_Library_star_runoff_tie_score_resolves.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bill

## Scenario

Ported from BetterVoting's tabulator unit tests (Star.test.ts :: "Runoff tie, score resolves").
The runoff ties, and the higher score total resolves it in Bill's favor.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill
0,5
3,2
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_runoff_tie_score_resolves_tabulated.txt) (regenerated on every run; every analysis forced on):

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
  STAR                   = Bill
  Choose-One (Plurality) = Allison   (differs from STAR)
  Approval               = Allison   (differs from STAR)
  RCV-RR                 = Allison   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: BV_Library_tabulated/BV_Library_star_runoff_tie_score_resolves_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Allison,Bill
      0,   5
      3,   2

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Allison  0  0  1  0  0  1  |     3   1.5
Bill     1  0  0  1  0  0  |     7   3.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bill          -- 7 -- First place
   Allison       -- 3 -- Second place
 Bill and Allison advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Allison       -- 1 -- Tied for first place
   Bill          -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Bill          -- 7 -- First place
   Allison       -- 3
 Bill wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bill
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_runoff_tie_score_resolves.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/BV_Library_star_runoff_tie_score_resolves.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md)
