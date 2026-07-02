# Vote splitting — scenario 1 of 3 — the spoiler strikes

*Generated from [`vote_splitting_scenario1_spoiler.yaml`](../vote_splitting_scenario1_spoiler.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** DarkChoco

## Scenario

A bloc that is a MAJORITY can still LOSE under Choose-One when it splits.

90 voters. 55 are chocolate lovers (a 61% majority), but they split across two
chocolates — 30 for DarkChoco, 25 for MilkChoco. The other 35 prefer Vanilla.

Choose-One first choices: Vanilla 35, DarkChoco 30, MilkChoco 25. Vanilla wins
with 38.9% even though 61% wanted chocolate — that is the spoiler effect.

STAR lets chocolate lovers score BOTH chocolates, so the bloc is not split and
DarkChoco wins. Watch the [Vote-splitting check] confirm it.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:DarkChoco,MilkChoco,Vanilla
30:5,4,0   # love dark, like milk, no vanilla
25:4,5,0   # love milk, like dark, no vanilla
35:2,1,5   # love vanilla, mild on chocolate
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/vote_splitting_scenario1_spoiler_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * DarkChoco  | * MilkChoco  |    Vanilla   |
-----------------------------------------------------------------
    * DarkChoco > |      ---      |65 -  0 - 25  |55 -  0 - 35  |
    * MilkChoco > | 25 -  0 - 65  |     ---      |55 -  0 - 35  |
        Vanilla > | 35 -  0 - 55  |35 -  0 - 55  |     ---      |

[Condorcet Winner]
  Condorcet Winner: DarkChoco — matches the STAR winner

[Divergence from STAR]
  STAR                   = DarkChoco
  Choose-One (Plurality) = Vanilla   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Vanilla 35, DarkChoco 30, MilkChoco 25
  Plurality winner: Vanilla (35, 38.9%)
  Bloc 'Chocolate' = DarkChoco, MilkChoco: combined 55 (61.1%); winner Vanilla is OUTSIDE it.
  => VOTE SPLITTING: the 'Chocolate' bloc is an outright majority (55 vs
     Vanilla's 35) but split across 2 candidates, so Vanilla won Choose-One.
     STAR elected DarkChoco.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 90 ballots.
Count × DarkChoco,MilkChoco,Vanilla
   35 ×         2,        1,      5
   30 ×         5,        4,      0
   25 ×         4,        5,      0

[Score Distribution] (number of ballots giving each score)
            5   4   3   2   1   0  | Total   Avg
DarkChoco  30  25   0  35   0   0  |   320   3.6
MilkChoco  25  30   0   0  35   0  |   280   3.1
Vanilla    35   0   0   0   0  55  |   175   1.9

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   DarkChoco     -- 320 -- First place
   MilkChoco     -- 280 -- Second place
   Vanilla       -- 175
 DarkChoco and MilkChoco advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   DarkChoco     -- 65 -- First place
   MilkChoco     -- 25
   Equal Support --  0
 DarkChoco wins.
   Runoff math:
     90  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     90  voters with a preference  (majority = 46)
           DarkChoco 65 (72%)  ·  MilkChoco 25 (28%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 DarkChoco
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/vote_splitting_scenario1_spoiler.yaml
```

## See also

- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README_split_voting.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
