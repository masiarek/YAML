# Large field (9 candidates) — the runoff OVERTURNS the score leader

*Generated from [`06b_c9_runoff-overturns-leader.yaml`](../06b_c9_runoff-overturns-leader.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Carmen

## Scenario

STAR's headline move, in a 9-candidate field with just 3 voters. Andre has the
highest score total (9 stars), so he leads the scoring round — but in the
automatic runoff a 2-of-3 majority prefers Carmen, so Carmen wins 2–1.

STAR elects the majority-preferred Carmen, not the highest-scoring Andre: the
runoff is the majority check that stops a high-ceiling / low-floor candidate from
winning on intensity alone. (Carmen is also the Condorcet winner.)

Discussion (Larry):
 - "Andre got the most stars — why didn't he win?" (The runoff asks a different
   question: which finalist do MORE voters prefer? That's Carmen, 2–1.)
 - Contrast 06a_c9_b3_large-field-equal-support.yaml, where the runoff merely
   CONFIRMS the scoring leader. Same method, two different jobs the runoff does.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andre,Blake,Carmen,David,Ella,Fernando,Gabe,Helena,Ira
5,3,0,2,1,1,1,1,0   # intense Andre voter (Andre 5, Carmen 0)
2,0,3,1,0,2,0,1,1   # prefers Carmen over Andre
2,1,3,0,1,0,2,0,1   # prefers Carmen over Andre
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/06b_c9_runoff-overturns-leader_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Andre    |    Blake    |  * Carmen   |    David    |     Ella    |   Fernando  |     Gabe    |    Helena   |     Ira     |
-------------------------------------------------------------------------------------------------------------------------------------------------
       * Andre > |     ---      | 3 - 0 - 0   | 1 - 0 - 2   | 3 - 0 - 0   | 3 - 0 - 0   | 2 - 1 - 0   | 2 - 1 - 0   | 3 - 0 - 0   | 3 - 0 - 0   |
         Blake > |  0 - 0 - 3   |    ---      | 1 - 0 - 2   | 2 - 0 - 1   | 1 - 2 - 0   | 2 - 0 - 1   | 1 - 1 - 1   | 2 - 0 - 1   | 1 - 1 - 1   |
      * Carmen > |  2 - 0 - 1   | 2 - 0 - 1   |    ---      | 2 - 0 - 1   | 2 - 0 - 1   | 2 - 0 - 1   | 2 - 0 - 1   | 2 - 0 - 1   | 2 - 1 - 0   |
         David > |  0 - 0 - 3   | 1 - 0 - 2   | 1 - 0 - 2   |    ---      | 2 - 0 - 1   | 1 - 1 - 1   | 2 - 0 - 1   | 1 - 2 - 0   | 1 - 1 - 1   |
          Ella > |  0 - 0 - 3   | 0 - 2 - 1   | 1 - 0 - 2   | 1 - 0 - 2   |    ---      | 1 - 1 - 1   | 0 - 2 - 1   | 1 - 1 - 1   | 1 - 1 - 1   |
      Fernando > |  0 - 1 - 2   | 1 - 0 - 2   | 1 - 0 - 2   | 1 - 1 - 1   | 1 - 1 - 1   |    ---      | 1 - 1 - 1   | 1 - 2 - 0   | 2 - 0 - 1   |
          Gabe > |  0 - 1 - 2   | 1 - 1 - 1   | 1 - 0 - 2   | 1 - 0 - 2   | 1 - 2 - 0   | 1 - 1 - 1   |    ---      | 1 - 1 - 1   | 2 - 0 - 1   |
        Helena > |  0 - 0 - 3   | 1 - 0 - 2   | 1 - 0 - 2   | 0 - 2 - 1   | 1 - 1 - 1   | 0 - 2 - 1   | 1 - 1 - 1   |    ---      | 1 - 1 - 1   |
           Ira > |  0 - 0 - 3   | 1 - 1 - 1   | 0 - 1 - 2   | 1 - 1 - 1   | 1 - 1 - 1   | 1 - 0 - 2   | 1 - 0 - 2   | 1 - 1 - 1   |    ---      |

[Condorcet Winner]
  Condorcet Winner: Carmen — matches the STAR winner

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Andre)
 - Runoff Round Winner   = (Carmen)
  Candidate Andre earned the highest total score,
  but Candidate Carmen won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Andre,Blake,Carmen,David,Ella,Fernando,Gabe,Helena,Ira
    5,    3,     0,    2,   1,       1,   1,     1,  0
    2,    0,     3,    1,   0,       2,   0,     1,  1
    2,    1,     3,    0,   1,       0,   2,     0,  1

[Score Distribution] (number of ballots giving each score)
          5  4  3  2  1  0  | Total   Avg
Andre     1  0  0  2  0  0  |     9   3.0
Blake     0  0  1  0  1  1  |     4   1.3
Carmen    0  0  2  0  0  1  |     6   2.0
David     0  0  0  1  1  1  |     3   1.0
Ella      0  0  0  0  2  1  |     2   0.7
Fernando  0  0  0  1  1  1  |     3   1.0
Gabe      0  0  0  1  1  1  |     3   1.0
Helena    0  0  0  0  2  1  |     2   0.7
Ira       0  0  0  0  2  1  |     2   0.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Andre         -- 9 -- First place
   Carmen        -- 6 -- Second place
   Blake         -- 4
   David         -- 3
   Fernando      -- 3
   Gabe          -- 3
   Ella          -- 2
   Helena        -- 2
   Ira           -- 2
 Andre and Carmen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Carmen        -- 2 -- First place
   Andre         -- 1
   Equal Support -- 0
 Carmen wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Carmen 2 (67%)  ·  Andre 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Carmen
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/06b_c9_runoff-overturns-leader.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
