# BV parity — Plurality (choose-one): most first-marks wins

*Generated from [`BV_Library_plurality_single_winner.yaml`](../BV_Library_plurality_single_winner.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Dave

## Scenario

Ported from BetterVoting's tabulator unit tests (Plurality.test.ts :: "Single Winner Test").
Choose-one ballots (a single 1 per voter); Dave has the most and wins. The original
had three spoiled/invalid ballots — one abstention, two out-of-bounds marks, and one
overvote — which BetterVoting counts as zero support; here the abstention is written
as blanks and the invalid rows as all-zero so the file validates while preserving the
winner. This engine tabulates choose-one 0/1 ballots via its STAR path, which for
single-mark ballots is equivalent to a plurality count.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Alice,Bob,Carol,Dave
0,1,0,0
0,1,0,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
-,-,-,-
0,0,0,0
0,0,0,0
0,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_plurality_single_winner_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     Alice    |     Bob     |  * Carol    |   * Dave    |
---------------------------------------------------------------------------
         Alice > |     ---      | 0 - 12 -  2 | 0 - 11 -  3 | 0 -  9 -  5 |
           Bob > |  2 - 12 -  0 |    ---      | 2 -  9 -  3 | 2 -  7 -  5 |
       * Carol > |  3 - 11 -  0 | 3 -  9 -  2 |    ---      | 3 -  6 -  5 |
        * Dave > |  5 -  9 -  0 | 5 -  7 -  2 | 5 -  6 -  3 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Dave — matches the STAR winner

[Divergence from STAR]
  STAR     = Dave
  Approval = Alice   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 14 ballots. Note: 1 of 14 ballots is marked as an abstention.
Count × Alice,Bob,Carol,Dave
    5 ×     0,  0,    0,   1
    3 ×     0,  0,    1,   0
    3 ×     0,  0,    0,   0
    2 ×     0,  1,    0,   0
    1 ×     -,  -,    -,   -
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (number of ballots giving each score)
        5   4   3   2   1   0  Abs  | Total   Avg
Alice   0   0   0   0   0  13    1  |     0   0.0
Bob     0   0   0   0   2  11    1  |     2   0.2
Carol   0   0   0   0   3  10    1  |     3   0.2
Dave    0   0   0   0   5   8    1  |     5   0.4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dave          -- 5 -- First place
   Carol         -- 3 -- Second place
   Bob           -- 2
   Alice         -- 0
 Dave and Carol advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dave          -- 5 -- First place
   Carol         -- 3
   Equal Support -- 6
 Dave wins.
   Runoff math:
     14  ballots cast
   −  6  Equal Support (no preference between the two finalists)
     ──
      8  voters with a preference  (majority = 5)
           Dave 5 (62%)  ·  Carol 3 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Dave
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_plurality_single_winner.yaml
```

## See also

- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
