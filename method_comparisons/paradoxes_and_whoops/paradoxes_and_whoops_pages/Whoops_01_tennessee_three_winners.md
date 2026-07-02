# Whoops 01 — same ballots, three methods, three winners (Tennessee)

*Generated from [`Whoops_01_tennessee_three_winners.yaml`](../Whoops_01_tennessee_three_winners.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Nashville

## Scenario

The classic Tennessee state-capital example. One set of ballots; Plurality picks
MEMPHIS, RCV-IRV picks KNOXVILLE, and Condorcet + STAR pick NASHVILLE (the central
compromise that beats everyone head-to-head). Nobody is being strategic — these are
sincere ballots. The whoops belongs to Plurality and IRV here. Scores are a simple
geographic-distance spatial model. Level 201. Fairness note in the lesson.
Lesson: Whoops_01_tennessee_three_winners.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Memphis, Nashville, Chattanooga, Knoxville
42 × 5, 2, 1, 0      # Memphis voters (far west)
26 × 1, 5, 3, 2      # Nashville voters (central)
15 × 0, 3, 5, 4      # Chattanooga voters (southeast)
17 × 0, 3, 4, 5      # Knoxville voters (east)
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/Whoops_01_tennessee_three_winners_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |      Memphis    |  * Nashville   | * Chattanooga  |    Knoxville   |
------------------------------------------------------------------------------------------
          Memphis > |       ---       | 42 -  0 - 58   | 42 -  0 - 58   | 42 -  0 - 58   |
      * Nashville > |  58 -  0 - 42   |      ---       | 68 -  0 - 32   | 68 -  0 - 32   |
    * Chattanooga > |  58 -  0 - 42   | 32 -  0 - 68   |      ---       | 83 -  0 - 17   |
        Knoxville > |  58 -  0 - 42   | 32 -  0 - 68   | 17 -  0 - 83   |      ---       |

[Condorcet Winner]
  Condorcet Winner: Nashville — matches the STAR winner

[Divergence from STAR]
  STAR                   = Nashville
  Choose-One (Plurality) = Memphis   (differs from STAR)
  RCV-IRV                = Knoxville   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: paradoxes_and_whoops_tabulated/Whoops_01_tennessee_three_winners_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Memphis,Nashville,Chattanooga,Knoxville
   42 ×       5,        2,          1,        0
   26 ×       1,        5,          3,        2
   17 ×       0,        3,          4,        5
   15 ×       0,        3,          5,        4

[Score Distribution] (number of ballots giving each score)
              5   4   3   2   1   0  | Total   Avg
Memphis      42   0   0   0  26  32  |   236   2.4
Nashville    26   0  32  42   0   0  |   310   3.1
Chattanooga  15  17  26   0  42   0  |   263   2.6
Knoxville    17  15   0  26   0  42  |   197   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Nashville     -- 310 -- First place
   Chattanooga   -- 263 -- Second place
   Memphis       -- 236
   Knoxville     -- 197
 Nashville and Chattanooga advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nashville     -- 68 -- First place
   Chattanooga   -- 32
   Equal Support --  0
 Nashville wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Nashville 68 (68%)  ·  Chattanooga 32 (32%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Nashville
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/Whoops_01_tennessee_three_winners.yaml
```

## See also

- [This set's lesson (README)](../README_paradoxes_and_whoops.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/Whoops_01_tennessee_three_winners.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [Whoops_02_star_misses_condorcet](Whoops_02_star_misses_condorcet.md) · [Whoops_03_condorcet_cycle_rps](Whoops_03_condorcet_cycle_rps.md) · [Whoops_04_ossipoff_centrist_irv](Whoops_04_ossipoff_centrist_irv.md) · [Whoops_05_brams_many_pathologies_irv](Whoops_05_brams_many_pathologies_irv.md)
