# Equal Support — counted in both rounds, neutral only in the tie-break

*Generated from [`equal_support_runoff_demo.yaml`](../equal_support_runoff_demo.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

A demo for the "discounted votes" objection. 100 voters, candidates A, B, C.

40 voters score A=5 AND B=5 (they love both) and C=0. 35 prefer A (A=5, B=3).
25 prefer C (A=0, B=0, C=5).

Scoring Round: A and B have the highest totals and advance — and the 40
"equal support" ballots are exactly what pushed them there. So those ballots
were COUNTED: they chose the finalists.

Automatic Runoff: between A and B, the 40 equal-A-B ballots and the 25 C-lovers
(who scored both finalists 0) have no preference, so they are "Equal Support."
The runoff is decided by the 35 voters who did prefer one finalist: A wins.

Takeaway: an Equal Support ballot is a voter who DECLARED A TIE between the
finalists, not a voter who lost their voice. It counted in the scoring round
and is simply neutral in a tie-break it has no preference in.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
40:5,5,0   # love BOTH A and B -> helps advance them; neutral in the runoff
35:5,3,0   # prefer A over B -> decides the runoff
25:0,0,5   # prefer C -> no preference between A and B
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/equal_support_runoff_demo_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |
-------------------------------------------------------------
           * A > |     ---      |35 - 65 -  0 |75 -  0 - 25 |
           * B > |  0 - 65 - 35 |    ---      |75 -  0 - 25 |
             C > | 25 -  0 - 75 |25 -  0 - 75 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × A,B,C
   40 × 5,5,0
   35 × 5,3,0
   25 × 0,0,5

[Score Distribution] (number of ballots giving each score)
    5   4   3   2   1   0  | Total   Avg
A  75   0   0   0   0  25  |   375   3.8
B  40   0  35   0   0  25  |   305   3.0
C  25   0   0   0   0  75  |   125   1.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 375 -- First place
   B             -- 305 -- Second place
   C             -- 125
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 35 -- First place
   B             --  0
   Equal Support -- 65
 A wins.
   Runoff math:
     100  ballots cast
   −  65  Equal Support (no preference between the two finalists)
     ───
      35  voters with a preference  (majority = 18)
           A 35 (100%)  ·  B 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/equal_support_runoff_demo.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
