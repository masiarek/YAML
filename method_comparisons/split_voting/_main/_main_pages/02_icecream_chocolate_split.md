# Spoiler — chocolate's majority splits, vanilla steals the win

*Generated from [`02_icecream_chocolate_split.yaml`](../02_icecream_chocolate_split.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** MilkChoco

## Scenario

100 dessert voters. Chocolate lovers are a 66% MAJORITY, but there are THREE
chocolates on the menu — DarkChoco, MilkChoco, and ChocoChip. Only 34 prefer
Vanilla.

Under Choose-One each voter picks one flavor, so chocolate splits: DarkChoco
24, MilkChoco 22, ChocoChip 20. Vanilla wins with 34 of 100 — a flavor a
two-thirds majority didn't want. Classic vote splitting.

STAR lets chocolate lovers give all three chocolates high scores, so the
majority isn't split. The runoff elects MilkChoco — the chocolate everyone in
the bloc can live with — over the spoiler Vanilla.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:DarkChoco,MilkChoco,ChocoChip,Vanilla
24:5,4,2,0   # dark base — also like milk
22:4,5,4,0   # milk base — like all chocolate
20:2,4,5,0   # chip base — also like milk
34:0,0,0,5   # vanilla bloc
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/02_icecream_chocolate_split_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * DarkChoco  | * MilkChoco  |   ChocoChip  |    Vanilla   |
--------------------------------------------------------------------------------
    * DarkChoco > |      ---      |24 - 34 - 42  |24 - 56 - 20  |66 -  0 - 34  |
    * MilkChoco > | 42 - 34 - 24  |     ---      |46 - 34 - 20  |66 -  0 - 34  |
      ChocoChip > | 20 - 56 - 24  |20 - 34 - 46  |     ---      |66 -  0 - 34  |
        Vanilla > | 34 -  0 - 66  |34 -  0 - 66  |34 -  0 - 66  |     ---      |

[Condorcet Winner]
  Condorcet Winner: MilkChoco — matches the STAR winner

[Divergence from STAR]
  STAR                   = MilkChoco
  Choose-One (Plurality) = Vanilla   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Vanilla 34, DarkChoco 24, MilkChoco 22, ChocoChip 20
  Plurality winner: Vanilla (34, 34.0%)
  Bloc 'Chocolate' = DarkChoco, MilkChoco, ChocoChip: combined 66 (66.0%); winner Vanilla is OUTSIDE it.
  => VOTE SPLITTING: the 'Chocolate' bloc is an outright majority (66 vs
     Vanilla's 34) but split across 3 candidates, so Vanilla won Choose-One.
     STAR elected MilkChoco.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × DarkChoco,MilkChoco,ChocoChip,Vanilla
   34 ×         0,        0,        0,      5
   24 ×         5,        4,        2,      0
   22 ×         4,        5,        4,      0
   20 ×         2,        4,        5,      0

[Score Distribution] (number of ballots giving each score)
            5   4   3   2   1   0  | Total   Avg
DarkChoco  24  22   0  20   0  34  |   248   2.5
MilkChoco  22  44   0   0   0  34  |   286   2.9
ChocoChip  20  22   0  24   0  34  |   236   2.4
Vanilla    34   0   0   0   0  66  |   170   1.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   MilkChoco     -- 286 -- First place
   DarkChoco     -- 248 -- Second place
   ChocoChip     -- 236
   Vanilla       -- 170
 MilkChoco and DarkChoco advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   MilkChoco     -- 42 -- First place
   DarkChoco     -- 24
   Equal Support -- 34
 MilkChoco wins.
   Runoff math:
     100  ballots cast
   −  34  Equal Support (no preference between the two finalists)
     ───
      66  voters with a preference  (majority = 34)
           MilkChoco 42 (64%)  ·  DarkChoco 24 (36%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 MilkChoco
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/02_icecream_chocolate_split.yaml
```

## See also

- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
