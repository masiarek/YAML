# Spoiler — a split coalition hands the seat to the minority

*Generated from [`01_political_left_split.yaml`](../01_political_left_split.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Labour

## Scenario

100 voters. A progressive coalition — Green, Labour, and SocialDem — is a clear
66% MAJORITY. One Conservative holds the other 34%.

Under Choose-One Plurality each voter names a single party, so the coalition
splits: Green 24, Labour 22, SocialDem 20. The Conservative wins with just 34
of 100 — a candidate two-thirds of voters ranked LAST. That is the spoiler
effect at full force.

STAR lets every voter score all four 0–5, so coalition voters can back all
three progressive parties. The two highest totals advance, and the automatic
runoff elects Labour — the coalition's broad consensus pick — not the minority
Conservative. Watch the [Vote-splitting check] confirm it.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Green,Labour,SocialDem,Conservative
24:5,4,2,0   # Green base — also like Labour
22:4,5,4,0   # Labour base — like the whole coalition
20:2,4,5,0   # SocialDem base — also like Labour
34:0,0,0,5   # Conservative bloc
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/01_political_left_split_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                     |     * Green      |    * Labour     |    SocialDem    |   Conservative  |
-----------------------------------------------------------------------------------------------
           * Green > |       ---        |  24 - 34 - 42   |  24 - 56 - 20   |  66 -  0 - 34   |
          * Labour > |   42 - 34 - 24   |      ---        |  46 - 34 - 20   |  66 -  0 - 34   |
         SocialDem > |   20 - 56 - 24   |  20 - 34 - 46   |      ---        |  66 -  0 - 34   |
      Conservative > |   34 -  0 - 66   |  34 -  0 - 66   |  34 -  0 - 66   |      ---        |

[Condorcet Winner]
  Condorcet Winner: Labour — matches the STAR winner

[Divergence from STAR]
  STAR                   = Labour
  Choose-One (Plurality) = Conservative   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Conservative 34, Green 24, Labour 22, SocialDem 20
  Plurality winner: Conservative (34, 34.0%)
  Bloc 'Coalition' = Green, Labour, SocialDem: combined 66 (66.0%); winner Conservative is OUTSIDE it.
  => VOTE SPLITTING: the 'Coalition' bloc is an outright majority (66 vs
     Conservative's 34) but split across 3 candidates, so Conservative won
     Choose-One. STAR elected Labour.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Green,Labour,SocialDem,Conservative
   34 ×     0,     0,        0,           5
   24 ×     5,     4,        2,           0
   22 ×     4,     5,        4,           0
   20 ×     2,     4,        5,           0

[Score Distribution] (number of ballots giving each score)
               5   4   3   2   1   0  | Total   Avg
Green         24  22   0  20   0  34  |   248   2.5
Labour        22  44   0   0   0  34  |   286   2.9
SocialDem     20  22   0  24   0  34  |   236   2.4
Conservative  34   0   0   0   0  66  |   170   1.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Labour        -- 286 -- First place
   Green         -- 248 -- Second place
   SocialDem     -- 236
   Conservative  -- 170
 Labour and Green advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Labour        -- 42 -- First place
   Green         -- 24
   Equal Support -- 34
 Labour wins.
   Runoff math:
     100  ballots cast
   −  34  Equal Support (no preference between the two finalists)
     ───
      66  voters with a preference  (majority = 34)
           Labour 42 (64%)  ·  Green 24 (36%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Labour
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/01_political_left_split.yaml
```

## See also

- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
