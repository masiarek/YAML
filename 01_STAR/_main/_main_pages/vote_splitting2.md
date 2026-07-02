# Vote splitting — two chocolates split the majority

*Generated from [`vote_splitting2.yaml`](../vote_splitting2.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** DarkChoco

## Scenario

Election: pick ONE dessert for the party. 360 voters.

220 of the 360 are chocolate lovers — a clear 61% majority. But there are TWO
chocolates on the menu, DarkChoco and MilkChoco, and 140 voters prefer Vanilla.

Under Choose-One Plurality each voter may name only one flavor, so the
chocolate majority splits its vote — 120 for DarkChoco, 100 for MilkChoco —
and Vanilla wins with just 140 of 360 (38.9%), a dessert a 61% majority
actively dislikes. That is vote splitting / the spoiler effect.

STAR fixes it without asking chocolate to drop a flavor: every voter scores
all three 0–5, so a chocolate lover can give BOTH chocolates a high score
instead of choosing between them. The two highest totals advance to an
automatic runoff, and the winner has majority support head-to-head.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:DarkChoco,MilkChoco,Vanilla
120:5,4,0   # love dark, like milk, no vanilla
100:4,5,0   # love milk, like dark, no vanilla
140:2,1,5   # love vanilla, mild on chocolate
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/vote_splitting2_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |   * DarkChoco   |  * MilkChoco   |     Vanilla    |
-------------------------------------------------------------------------
      * DarkChoco > |       ---       |260 -   0 - 100 |220 -   0 - 140 |
      * MilkChoco > | 100 -   0 - 260 |      ---       |220 -   0 - 140 |
          Vanilla > | 140 -   0 - 220 |140 -   0 - 220 |      ---       |

[Condorcet Winner]
  Condorcet Winner: DarkChoco — matches the STAR winner

[Divergence from STAR]
  STAR                   = DarkChoco
  Choose-One (Plurality) = Vanilla   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Vanilla 140, DarkChoco 120, MilkChoco 100
  Plurality winner: Vanilla (140, 38.9%)
  Bloc 'Chocolate' = DarkChoco, MilkChoco: combined 220 (61.1%); winner Vanilla is OUTSIDE it.
  => VOTE SPLITTING: the 'Chocolate' bloc is an outright majority (220 vs
     Vanilla's 140) but split across 2 candidates, so Vanilla won Choose-
     One. STAR elected DarkChoco.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 360 ballots.
Count × DarkChoco,MilkChoco,Vanilla
  140 ×         2,        1,      5
  120 ×         5,        4,      0
  100 ×         4,        5,      0

[Score Distribution] (number of ballots giving each score)
             5    4    3    2    1    0  | Total   Avg
DarkChoco  120  100    0  140    0    0  |  1280   3.6
MilkChoco  100  120    0    0  140    0  |  1120   3.1
Vanilla    140    0    0    0    0  220  |   700   1.9

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   DarkChoco     -- 1280 -- First place
   MilkChoco     -- 1120 -- Second place
   Vanilla       --  700
 DarkChoco and MilkChoco advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   DarkChoco     -- 260 -- First place
   MilkChoco     -- 100
   Equal Support --   0
 DarkChoco wins.
   Runoff math:
     360  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     360  voters with a preference  (majority = 181)
           DarkChoco 260 (72%)  ·  MilkChoco 100 (28%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 DarkChoco
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/vote_splitting2.yaml
```

## See also

- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README_split_voting.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
