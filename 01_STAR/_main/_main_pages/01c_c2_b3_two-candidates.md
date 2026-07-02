# Equal support example ("I like both flavors")

*Generated from [`01c_c2_b3_two-candidates.yaml`](../01c_c2_b3_two-candidates.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Choco

## Scenario

Now we add a third ballot, from Julia, who likes both flavors equally (both 5 stars).
Because she scores the two finalists the same, her ballot counts as
"Equal Support = 1" in the Automatic Runoff Round.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Choco,Vanilla
    5,      3       # Caroline - she likes both flavors
    5,      0       # George - he likes only one flavor (Choco)
    5,      5       # Julia - she likes both flavors equally
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/01c_c2_b3_two-candidates_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |   * Choco   | * Vanilla  |
--------------------------------------------
      * Choco > |     ---     | 2 - 1 - 0  |
    * Vanilla > |  0 - 1 - 2  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Choco — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Choco,Vanilla
    5,      3
    5,      0
    5,      5

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Choco    3  0  0  0  0  0  |    15   5.0
Vanilla  1  0  1  0  0  1  |     8   2.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Choco         -- 15 -- First place
   Vanilla       --  8 -- Second place
 Choco and Vanilla advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Choco         -- 2 -- First place
   Vanilla       -- 0
   Equal Support -- 1
 Choco wins.
   Runoff math:
     3  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           Choco 2 (100%)  ·  Vanilla 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Choco
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/01c_c2_b3_two-candidates.yaml
```

## See also

- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
