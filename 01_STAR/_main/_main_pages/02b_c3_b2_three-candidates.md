# Three candidates, two ballots - single-winner STAR

*Generated from [`02b_c3_b2_three-candidates.yaml`](../02b_c3_b2_three-candidates.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Vanilla

## Scenario

Election: Pick your favorite ice cream flavor. Two voters (two ballots).
Same as before, but now we add a second ballot from David.

David:
- He likes Vanilla best (5 stars)
- He quite likes Almond (4 stars)
- He dislikes Choco (0 stars)

Watch the winner change. Choco flavor candidate is polarizing (Caroline 5, David 0), while
Vanilla has broad support (Caroline 3, David 5) - so Vanilla now wins. 
STAR rewards the broadly-liked compromise over a candidate that half the voters reject.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Choco,Vanilla,Almond
    5,      3,     0 # Caroline likes Choco (5) and Vanilla (3)
    0,      5,     4 # David likes Vanilla (5) best and Almond (4)
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/02b_c3_b2_three-candidates_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |   * Choco   | * Vanilla  |   Almond   |
---------------------------------------------------------
      * Choco > |     ---     | 1 - 0 - 1  | 1 - 0 - 1  |
    * Vanilla > |  1 - 0 - 1  |    ---     | 2 - 0 - 0  |
       Almond > |  1 - 0 - 1  | 0 - 0 - 2  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Choco, Vanilla (pairwise ties)

[Divergence from STAR]
  STAR                   = Vanilla
  Choose-One (Plurality) = Choco   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Choco,Vanilla,Almond
    5,      3,     0
    0,      5,     4

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Choco    1  0  0  0  0  1  |     5   2.5
Vanilla  1  0  1  0  0  0  |     8   4.0
Almond   0  1  0  0  0  1  |     4   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Vanilla       -- 8 -- First place
   Choco         -- 5 -- Second place
   Almond        -- 4
 Vanilla and Choco advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Choco         -- 1 -- Tied for first place
   Vanilla       -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Vanilla       -- 8 -- First place
   Choco         -- 5
 Vanilla wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Vanilla
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/02b_c3_b2_three-candidates.yaml
```

## See also

- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
