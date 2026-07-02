# Center squeeze — STAR elects the consensus (Center)

*Generated from [`center_squeeze_star.yaml`](../center_squeeze_star.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Center

## Scenario

The SAME 27-voter profile as center_squeeze_irv.yaml, translated to 0–5 scores.
Center is the broad consensus — the 2nd choice of both poles and the Condorcet
winner — but has the fewest first-choices.

RCV-IRV eliminates Center first (too little "core support") and elects the polar
Left. STAR counts every ballot in both rounds: Center reaches the runoff on
strength of support and wins. The [Divergence from STAR] and [Condorcet Winner]
lines below show Choose-One = Left, RCV-IRV = Left, STAR = Center = Condorcet
winner (also what Ranked Robin would elect).
See 00_start_here/center_squeeze.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Left,Center,Right
12:5,4,3   # Left > Center > Right
9:3,4,5    # Right > Center > Left
6:4,5,3    # Center > Left > Right
```

## What the engine says

Full report from the [`_tabulated` mirror](../center_squeeze_tabulated/center_squeeze_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Left    |  * Center   |    Right    |
-------------------------------------------------------------
        * Left > |     ---      |12 -  0 - 15 |18 -  0 -  9 |
      * Center > | 15 -  0 - 12 |    ---      |18 -  0 -  9 |
         Right > |  9 -  0 - 18 | 9 -  0 - 18 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Center — matches the STAR winner

[Divergence from STAR]
  STAR                   = Center
  Choose-One (Plurality) = Left   (differs from STAR)
  RCV-IRV                = Left   (differs from STAR)
  Approval               = Left   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: center_squeeze_tabulated/center_squeeze_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 27 ballots.
Count × Left,Center,Right
   12 ×    5,     4,    3
    9 ×    3,     4,    5
    6 ×    4,     5,    3

[Score Distribution] (number of ballots giving each score)
         5   4   3   2   1   0  | Total   Avg
Left    12   6   9   0   0   0  |   111   4.1
Center   6  21   0   0   0   0  |   114   4.2
Right    9   0  18   0   0   0  |    99   3.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Center        -- 114 -- First place
   Left          -- 111 -- Second place
   Right         --  99
 Center and Left advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Center        -- 15 -- First place
   Left          -- 12
   Equal Support --  0
 Center wins.
   Runoff math:
     27  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     27  voters with a preference  (majority = 14)
           Center 15 (56%)  ·  Left 12 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Center
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze/center_squeeze_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/center_squeeze_star.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README_center_squeeze.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [center_squeeze_irv](center_squeeze_irv.md) · [center_squeeze_voteline_1d](center_squeeze_voteline_1d.md)
