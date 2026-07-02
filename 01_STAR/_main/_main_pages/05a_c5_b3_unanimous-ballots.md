# Unanimous ballots (five candidates)

*Generated from [`05a_c5_b3_unanimous-ballots.yaml`](../05a_c5_b3_unanimous-ballots.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Andre

## Scenario

Every voter casts an identical ballot, so the outcome is unanimous and the
finalists are never in doubt. A simple sanity check / smallest-contrast case
for the five-candidate display.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andre,Blake,Carmen,David,Ella
    5,    1,     4,    3,   0
    5,    1,     4,    3,   0
    5,    1,     4,    3,   0
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/05a_c5_b3_unanimous-ballots_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Andre   |   Blake   | * Carmen  |   David   |    Ella   |
-----------------------------------------------------------------------------
     * Andre > |    ---     |3 - 0 - 0  |3 - 0 - 0  |3 - 0 - 0  |3 - 0 - 0  |
       Blake > | 0 - 0 - 3  |   ---     |0 - 0 - 3  |0 - 0 - 3  |3 - 0 - 0  |
    * Carmen > | 0 - 0 - 3  |3 - 0 - 0  |   ---     |3 - 0 - 0  |3 - 0 - 0  |
       David > | 0 - 0 - 3  |3 - 0 - 0  |0 - 0 - 3  |   ---     |3 - 0 - 0  |
        Ella > | 0 - 0 - 3  |0 - 0 - 3  |0 - 0 - 3  |0 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Andre — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Count × Andre,Blake,Carmen,David,Ella
    3 ×     5,    1,     4,    3,   0

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  | Total   Avg
Andre   3  0  0  0  0  0  |    15   5.0
Blake   0  0  0  0  3  0  |     3   1.0
Carmen  0  3  0  0  0  0  |    12   4.0
David   0  0  3  0  0  0  |     9   3.0
Ella    0  0  0  0  0  3  |     0   0.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Andre         -- 15 -- First place
   Carmen        -- 12 -- Second place
   David         --  9
   Blake         --  3
   Ella          --  0
 Andre and Carmen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Andre         -- 3 -- First place
   Carmen        -- 0
   Equal Support -- 0
 Andre wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Andre 3 (100%)  ·  Carmen 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Andre
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/05a_c5_b3_unanimous-ballots.yaml
```

## See also

- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
