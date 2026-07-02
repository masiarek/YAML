# BV Abstentions and flat scores (Apple/Banana/Cherry, 8 ballots)

*Generated from [`flat_scores_abstention_c3_b8.yaml`](../flat_scores_abstention_c3_b8.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Banana

## Scenario

A REAL BetterVoting election (BV id dq2dmm), captured 2026-06-28. The canonical
small case for how BetterVoting and the LH engine differ on "no preference"
ballots — richer than two candidates because a third candidate (Cherry)
separates three distinct ideas a single election usually blurs:

  • a TRUE abstention (a blank ballot — no score for anyone): 1
  • a FLAT ballot (every candidate scored the same) — what BetterVoting files
    as an "abstention": 3   (the blank, 0,0,0, AND 3,3,3)
  • EQUAL SUPPORT in the runoff (the two finalists tied): 4
    (those 3 flat ballots PLUS 5,5,0, which is tied on Apple/Banana but is NOT
    flat, so BetterVoting counts it normally)

The point: BetterVoting's "flat = abstention" rule and STAR's "Equal Support"
are different sets. 3,3,3 is a fully engaged vote (Cherry got 3 too) that BV
drops; 5,5,0 is Equal Support that BV keeps. BetterVoting reports
nAbstentions = 3, nTallyVotes = 5; the LH engine counts all 8 and marks only
the blank an abstention. Same winner (Banana). Frozen export:
flat_scores_abstention_c3_b8_bv_export.json. Full write-up:
small_case_abstention_lesson.md.

BetterVoting issue: https://github.com/Equal-Vote/bettervoting/issues/1407
How to read this report (LH): 00_start_here/STAR_reporting/reporting_LH/
The reporting options used below: STAR_reporting/reporting_LH/options.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Apple, Banana, Cherry
    0,      5,      1
    -,      -,      -
    5,      4,      1
    4,      5,      2
    0,      0,      0
    3,      3,      3
    3,      5,      0
    5,      5,      0
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_real_bv_election_tabulated/flat_scores_abstention_c3_b8_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Apple   | * Banana  |   Cherry  |
-----------------------------------------------------
     * Apple > |    ---     |1 - 4 - 3  |4 - 3 - 1  |
    * Banana > | 3 - 4 - 1  |   ---     |5 - 3 - 0  |
      Cherry > | 1 - 3 - 4  |0 - 3 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Banana — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 8 ballots. Note: 1 of 8 ballots is marked as an abstention.
Apple,Banana,Cherry
    0,     5,     1
    -,     -,     -
    5,     4,     1
    4,     5,     2
    0,     0,     0
    3,     3,     3
    3,     5,     0
    5,     5,     0
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  Abs  | Total   Avg
Apple   2  1  2  0  0  2    1  |    20   2.9
Banana  4  1  1  0  0  1    1  |    27   3.9
Cherry  0  0  1  1  2  3    1  |     7   1.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Banana        -- 27 -- First place
   Apple         -- 20 -- Second place
   Cherry        --  7
 Banana and Apple advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Banana        -- 3 -- First place
   Apple         -- 1
   Equal Support -- 4
 Banana wins.
   Runoff math:
     8  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           Banana 3 (75%)  ·  Apple 1 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Banana
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/pet_real_bv_election/flat_scores_abstention_c3_b8.yaml
```

## See also

- [This set's lesson (README)](../README_pet_real_bv_election.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [abstention_reconciliation_min_c2_b6](abstention_reconciliation_min_c2_b6.md) · [best_pet_c7_b461](best_pet_c7_b461.md) · [small_abstention_c2_b5](small_abstention_c2_b5.md)
