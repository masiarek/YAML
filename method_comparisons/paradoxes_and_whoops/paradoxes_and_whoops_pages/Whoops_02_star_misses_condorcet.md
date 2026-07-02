# Whoops 02 — STAR misses the Condorcet winner (STAR's own whoops)

*Generated from [`Whoops_02_star_misses_condorcet.yaml`](../Whoops_02_star_misses_condorcet.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ada

## Scenario

STAR is not perfect, and this is its signature failure. Cleo is the CONDORCET WINNER
(beats Ada 60-40 and Bruno 65-35 head-to-head) but is a low-scored compromise: the two
wings score Cleo only a 2, so Cleo finishes THIRD on score and never reaches the runoff.
STAR elects ADA. Sincere ballots, no strategy. This is the score-method cousin of IRV's
center squeeze: the broadly-acceptable middle is excluded before the final comparison.
Rare (STAR is ~98% Condorcet-efficient in spatial models) but structural. Level 301.
Cross-ref: STAR_three_winner_notions. Lesson: Whoops_02_star_misses_condorcet.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada, Bruno, Cleo
40 × 5, 1, 2      # Ada > Cleo > Bruno
35 × 1, 5, 2      # Bruno > Cleo > Ada
25 × 3, 3, 5      # Cleo > (Ada = Bruno)
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/Whoops_02_star_misses_condorcet_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ada     |  * Bruno    |     Cleo    |
-------------------------------------------------------------
         * Ada > |     ---      |40 - 25 - 35 |40 -  0 - 60 |
       * Bruno > | 35 - 25 - 40 |    ---      |35 -  0 - 65 |
          Cleo > | 60 -  0 - 40 |65 -  0 - 35 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cleo — STAR elected Ada instead (Cleo was eliminated in the scoring round)

[Divergence from STAR]
  STAR               = Ada
  RCV-RR (Condorcet) = Cleo   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: paradoxes_and_whoops_tabulated/Whoops_02_star_misses_condorcet_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Ada,Bruno,Cleo
   40 ×   5,    1,   2
   35 ×   1,    5,   2
   25 ×   3,    3,   5

[Score Distribution] (number of ballots giving each score)
        5   4   3   2   1   0  | Total   Avg
Ada    40   0  25   0  35   0  |   310   3.1
Bruno  35   0  25   0  40   0  |   290   2.9
Cleo   25   0   0  75   0   0  |   275   2.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 310 -- First place
   Bruno         -- 290 -- Second place
   Cleo          -- 275
 Ada and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 40 -- First place
   Bruno         -- 35
   Equal Support -- 25
 Ada wins.
   Runoff math:
     100  ballots cast
   −  25  Equal Support (no preference between the two finalists)
     ───
      75  voters with a preference  (majority = 38)
           Ada 40 (53%)  ·  Bruno 35 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/Whoops_02_star_misses_condorcet.yaml
```

## See also

- [This set's lesson (README)](../README_paradoxes_and_whoops.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/Whoops_02_star_misses_condorcet.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README_center_squeeze.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Whoops_01_tennessee_three_winners](Whoops_01_tennessee_three_winners.md) · [Whoops_03_condorcet_cycle_rps](Whoops_03_condorcet_cycle_rps.md) · [Whoops_04_ossipoff_centrist_irv](Whoops_04_ossipoff_centrist_irv.md) · [Whoops_05_brams_many_pathologies_irv](Whoops_05_brams_many_pathologies_irv.md)
