# Spoiler — the veggie majority splits, the burger wins the lunch vote

*Generated from [`03_lunch_veggie_vs_meat.yaml`](../03_lunch_veggie_vs_meat.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** VeggieCurry

## Scenario

100 people vote on ONE dish to cater. A 70% MAJORITY wants vegetarian, but the
veggie vote is spread across three dishes — VeggieCurry, TofuStirFry, and
GardenSalad. A single BeefBurger holds the other 30%.

Under Choose-One each person picks one dish, so the veggie vote splits:
TofuStirFry 28, VeggieCurry 26, GardenSalad 16. BeefBurger wins with just 30 of
100 — even though 70% wanted something vegetarian. The split handed the win to
the minority.

STAR lets veggie voters score all three vegetarian dishes, so the majority
isn't split. The runoff elects VeggieCurry — the dish the most veggie voters
can agree on — instead of the spoiler BeefBurger.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:VeggieCurry,TofuStirFry,GardenSalad,BeefBurger
26:5,4,4,0   # curry base — like the other veggies
28:4,5,2,0   # tofu base — curry is a fine backup
16:4,2,5,0   # salad base — curry is a fine backup
30:0,0,0,5   # burger bloc
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/03_lunch_veggie_vs_meat_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |  * VeggieCurry  | * TofuStirFry  |   GardenSalad  |   BeefBurger   |
------------------------------------------------------------------------------------------
    * VeggieCurry > |       ---       | 42 - 30 - 28   | 54 - 30 - 16   | 70 -  0 - 30   |
    * TofuStirFry > |  28 - 30 - 42   |      ---       | 28 - 56 - 16   | 70 -  0 - 30   |
      GardenSalad > |  16 - 30 - 54   | 16 - 56 - 28   |      ---       | 70 -  0 - 30   |
       BeefBurger > |  30 -  0 - 70   | 30 -  0 - 70   | 30 -  0 - 70   |      ---       |

[Condorcet Winner]
  Condorcet Winner: VeggieCurry — matches the STAR winner

[Divergence from STAR]
  STAR                   = VeggieCurry
  Choose-One (Plurality) = BeefBurger   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: BeefBurger 30, TofuStirFry 28, VeggieCurry 26, GardenSalad 16
  Plurality winner: BeefBurger (30, 30.0%)
  Bloc 'Veggie' = VeggieCurry, TofuStirFry, GardenSalad: combined 70 (70.0%); winner BeefBurger is OUTSIDE it.
  => VOTE SPLITTING: the 'Veggie' bloc is an outright majority (70 vs
     BeefBurger's 30) but split across 3 candidates, so BeefBurger won
     Choose-One. STAR elected VeggieCurry.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × VeggieCurry,TofuStirFry,GardenSalad,BeefBurger
   30 ×           0,          0,          0,         5
   28 ×           4,          5,          2,         0
   26 ×           5,          4,          4,         0
   16 ×           4,          2,          5,         0

[Score Distribution] (number of ballots giving each score)
              5   4   3   2   1   0  | Total   Avg
VeggieCurry  26  44   0   0   0  30  |   306   3.1
TofuStirFry  28  26   0  16   0  30  |   276   2.8
GardenSalad  16  26   0  28   0  30  |   240   2.4
BeefBurger   30   0   0   0   0  70  |   150   1.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   VeggieCurry   -- 306 -- First place
   TofuStirFry   -- 276 -- Second place
   GardenSalad   -- 240
   BeefBurger    -- 150
 VeggieCurry and TofuStirFry advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   VeggieCurry   -- 42 -- First place
   TofuStirFry   -- 28
   Equal Support -- 30
 VeggieCurry wins.
   Runoff math:
     100  ballots cast
   −  30  Equal Support (no preference between the two finalists)
     ───
      70  voters with a preference  (majority = 36)
           VeggieCurry 42 (60%)  ·  TofuStirFry 28 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 VeggieCurry
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/03_lunch_veggie_vs_meat.yaml
```

## See also

- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
