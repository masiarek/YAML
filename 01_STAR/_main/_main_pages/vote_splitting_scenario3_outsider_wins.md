# Vote splitting — scenario 3 of 3 — no spoiler (the outsider truly wins)

*Generated from [`vote_splitting_scenario3_outsider_wins.yaml`](../vote_splitting_scenario3_outsider_wins.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Vanilla

## Scenario

When the outsider is the genuine favorite, there is no spoiler — uniting the
bloc would not change the result.

62 voters. Vanilla 40, DarkChoco 12, MilkChoco 10. Chocolate combined is only
22, far short of Vanilla's 40.

Choose-One first choices: Vanilla 40, DarkChoco 12, MilkChoco 10. Vanilla wins —
and would still win even if the two chocolates merged into one (22 < 40). STAR
also elects Vanilla. Fair and square.

The [Vote-splitting check] reports: even combined, the bloc does not out-poll
the winner, so no spoiler occurred.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:DarkChoco,MilkChoco,Vanilla
12:5,4,0   # love dark, like milk, no vanilla
10:4,5,0   # love milk, like dark, no vanilla
40:1,0,5   # love vanilla, mild on chocolate
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/vote_splitting_scenario3_outsider_wins_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * DarkChoco  |   MilkChoco  |  * Vanilla   |
-----------------------------------------------------------------
    * DarkChoco > |      ---      |52 -  0 - 10  |22 -  0 - 40  |
      MilkChoco > | 10 -  0 - 52  |     ---      |22 -  0 - 40  |
      * Vanilla > | 40 -  0 - 22  |40 -  0 - 22  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Vanilla — matches the STAR winner

[Vote-splitting check]
  Choose-One first choices: Vanilla 40, DarkChoco 12, MilkChoco 10
  Plurality winner: Vanilla (40, 64.5%)
  Bloc 'Chocolate' = DarkChoco, MilkChoco: combined 22 (35.5%); winner Vanilla is OUTSIDE it.
  => No vote splitting: even combined (22), the 'Chocolate' bloc does not
     outpoll Vanilla (40).

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 62 ballots.
Count × DarkChoco,MilkChoco,Vanilla
   40 ×         1,        0,      5
   12 ×         5,        4,      0
   10 ×         4,        5,      0

[Score Distribution] (number of ballots giving each score)
            5   4   3   2   1   0  | Total   Avg
DarkChoco  12  10   0   0  40   0  |   140   2.3
MilkChoco  10  12   0   0   0  40  |    98   1.6
Vanilla    40   0   0   0   0  22  |   200   3.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Vanilla       -- 200 -- First place
   DarkChoco     -- 140 -- Second place
   MilkChoco     --  98
 Vanilla and DarkChoco advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Vanilla       -- 40 -- First place
   DarkChoco     -- 22
   Equal Support --  0
 Vanilla wins.
   Runoff math:
     62  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     62  voters with a preference  (majority = 32)
           Vanilla 40 (65%)  ·  DarkChoco 22 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Vanilla
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/vote_splitting_scenario3_outsider_wins.yaml
```

## See also

- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README_split_voting.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md)
