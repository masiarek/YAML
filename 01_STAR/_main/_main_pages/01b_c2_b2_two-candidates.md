# Again, very similar - this time second ballot is 5 and 0

*Generated from [`01b_c2_b2_two-candidates.yaml`](../01b_c2_b2_two-candidates.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Choco

## Scenario

Same as before (Caroline vote is the first), 
but this time with one more person (hence one more ballot 
- the second row) — from George:

George (new ballot) he likes only Choco:
- he loves the Choco flavor (5 stars)
- he dislikes Vanilla (0 stars)

We are adding up the scores given to each candidate (Tallying = Scoring Round).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Choco,Vanilla
    5,      3       # Caroline - she likes both flavors
    5,      0       # George - he likes only one flavor (Choco)
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/01b_c2_b2_two-candidates_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |   * Choco   | * Vanilla  |
--------------------------------------------
      * Choco > |     ---     | 2 - 0 - 0  |
    * Vanilla > |  0 - 0 - 2  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Choco — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Choco,Vanilla
    5,      3
    5,      0

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Choco    2  0  0  0  0  0  |    10   5.0
Vanilla  0  0  1  0  0  1  |     3   1.5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Choco         -- 10 -- First place
   Vanilla       --  3 -- Second place
 Choco and Vanilla advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Choco         -- 2 -- First place
   Vanilla       -- 0
   Equal Support -- 0
 Choco wins.
   Runoff math:
     2  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Choco 2 (100%)  ·  Vanilla 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Choco
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/01b_c2_b2_two-candidates.yaml
```

## See also

- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
