# Whoops 03 — a Condorcet cycle (rock-paper-scissors, no winner)

*Generated from [`Whoops_03_condorcet_cycle_rps.yaml`](../Whoops_03_condorcet_cycle_rps.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Rock

## Scenario

The paradox of voting itself. Rock beats Paper, Paper beats Scissors, Scissors beats
Rock — a majority CYCLE with NO Condorcet winner at all. So Condorcet / Ranked Robin
cannot name a winner without a cycle-breaking rule: this is THEIR whoops. The score
methods still finish: STAR elects Rock (271 vs Paper 270 — razor thin), Approval picks
Paper. Sincere ballots. The whole point is that 'majority rule' can be intransitive.
Level 301. Lesson: Whoops_03_condorcet_cycle_rps.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Rock, Paper, Scissors
35 × 5, 3, 0      # Rock > Paper > Scissors
33 × 0, 5, 3      # Paper > Scissors > Rock
32 × 3, 0, 5      # Scissors > Rock > Paper
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/Whoops_03_condorcet_cycle_rps_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Rock    |  * Paper    |   Scissors  |
-------------------------------------------------------------
        * Rock > |     ---      |67 -  0 - 33 |35 -  0 - 65 |
       * Paper > | 33 -  0 - 67 |    ---      |68 -  0 - 32 |
      Scissors > | 65 -  0 - 35 |32 -  0 - 68 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Rock > Paper > Scissors > Rock)

[Divergence from STAR]
  STAR     = Rock
  Approval = Paper   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Rock,Paper,Scissors
   35 ×    5,    3,       0
   33 ×    0,    5,       3
   32 ×    3,    0,       5

[Score Distribution] (number of ballots giving each score)
           5   4   3   2   1   0  | Total   Avg
Rock      35   0  32   0   0  33  |   271   2.7
Paper     33   0  35   0   0  32  |   270   2.7
Scissors  32   0  33   0   0  35  |   259   2.6

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Rock          -- 271 -- First place
   Paper         -- 270 -- Second place
   Scissors      -- 259
 Rock and Paper advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Rock          -- 67 -- First place
   Paper         -- 33
   Equal Support --  0
 Rock wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Rock 67 (67%)  ·  Paper 33 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Rock
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/Whoops_03_condorcet_cycle_rps.yaml
```

## See also

- [This set's lesson (README)](../README_paradoxes_and_whoops.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/Whoops_03_condorcet_cycle_rps.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Whoops_01_tennessee_three_winners](Whoops_01_tennessee_three_winners.md) · [Whoops_02_star_misses_condorcet](Whoops_02_star_misses_condorcet.md) · [Whoops_04_ossipoff_centrist_irv](Whoops_04_ossipoff_centrist_irv.md) · [Whoops_05_brams_many_pathologies_irv](Whoops_05_brams_many_pathologies_irv.md)
