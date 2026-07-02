# Vote splitting — two chocolates split the majority

*Generated from [`vote_splitting3.yaml`](../vote_splitting3.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** DarkChoco

## Scenario

Two chocolate flavors court the same majority while Vanilla consolidates the
rest — the classic vote-splitting shape. STAR shrugs it off: scores add up
per candidate, BOTH chocolates reach the runoff, and DarkChoco wins the
head-to-head 14-7. The blocs: entry makes the engine quantify the Chocolate
split explicitly ([Vote-Splitting Check]). For versions where splitting
actually flips a Choose-One winner, see method_comparisons/split_voting/.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:DarkChoco,MilkChoco,Vanilla
8:5,4,3   # love dark, like milk, vanilla is OK
7:4,5,0   # love milk, like dark, no vanilla
6:2,1,5   # love vanilla, mild on chocolate
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/vote_splitting3_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * DarkChoco  | * MilkChoco  |    Vanilla   |
-----------------------------------------------------------------
    * DarkChoco > |      ---      |14 -  0 -  7  |15 -  0 -  6  |
    * MilkChoco > |  7 -  0 - 14  |     ---      |15 -  0 -  6  |
        Vanilla > |  6 -  0 - 15  | 6 -  0 - 15  |     ---      |

[Condorcet Winner]
  Condorcet Winner: DarkChoco — matches the STAR winner

[Vote-splitting check]
  Choose-One first choices: DarkChoco 8, MilkChoco 7, Vanilla 6
  Plurality winner: DarkChoco (8, 38.1%)
  Bloc 'Chocolate' = DarkChoco, MilkChoco: combined 15 (71.4%); winner DarkChoco is INSIDE it.
  => No vote splitting: the bloc's own front-runner (DarkChoco) also wins
     Choose-One overall.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 21 ballots.
Count × DarkChoco,MilkChoco,Vanilla
    8 ×         5,        4,      3
    7 ×         4,        5,      0
    6 ×         2,        1,      5

[Score Distribution] (number of ballots giving each score)
           5  4  3  2  1  0  | Total   Avg
DarkChoco  8  7  0  6  0  0  |    80   3.8
MilkChoco  7  8  0  0  6  0  |    73   3.5
Vanilla    6  0  8  0  0  7  |    54   2.6

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   DarkChoco     -- 80 -- First place
   MilkChoco     -- 73 -- Second place
   Vanilla       -- 54
 DarkChoco and MilkChoco advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   DarkChoco     -- 14 -- First place
   MilkChoco     --  7
   Equal Support --  0
 DarkChoco wins.
   Runoff math:
     21  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     21  voters with a preference  (majority = 11)
           DarkChoco 14 (67%)  ·  MilkChoco 7 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 DarkChoco
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/vote_splitting3.yaml
```

## See also

- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README_split_voting.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
