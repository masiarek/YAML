# Voting styles — low-score ballots (continued)

*Generated from [`03b_c3_b3_2_expand_style-protest-vote.yaml`](../03b_c3_b3_2_expand_style-protest-vote.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Almond

## Scenario

Follow-up to the previous example. The voters and their preferences are
unchanged; we only raised each "least-bad" score from 1 to 2.

The winner is still Almond. That is the point: STAR decides this election by
the RELATIVE ordering on each ballot (and which candidate more voters prefer),
not by the absolute number. Scaling everyone's scores up the same way doesn't
change the result.

(Where higher scores DO matter is when voters differ - giving a candidate a 2
instead of a 1 adds more weight in the score round relative to other voters'
ballots.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Choco,Almond,Vanilla
    0,     2,      0   # least-bad = Almond
    0,     0,      2   # least-bad = Vanilla
    0,     2,      0   # least-bad = Almond
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/03b_c3_b3_2_expand_style-protest-vote_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |     Choco   | * Almond   | * Vanilla  |
---------------------------------------------------------
        Choco > |     ---     | 0 - 1 - 2  | 0 - 2 - 1  |
     * Almond > |  2 - 1 - 0  |    ---     | 2 - 0 - 1  |
    * Vanilla > |  1 - 2 - 0  | 1 - 0 - 2  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Almond — matches the STAR winner

[Divergence from STAR]
  STAR     = Almond
  Approval = Choco   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Count × Choco,Almond,Vanilla
    2 ×     0,     2,      0
    1 ×     0,     0,      2

[Score Distribution] (number of ballots giving each score)
         5  4  3  2  1  0  | Total   Avg
Choco    0  0  0  0  0  3  |     0   0.0
Almond   0  0  0  2  0  1  |     4   1.3
Vanilla  0  0  0  1  0  2  |     2   0.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 4 -- First place
   Vanilla       -- 2 -- Second place
   Choco         -- 0
 Almond and Vanilla advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 2 -- First place
   Vanilla       -- 1
   Equal Support -- 0
 Almond wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Almond 2 (67%)  ·  Vanilla 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Almond
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/03b_c3_b3_2_expand_style-protest-vote.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/03b_c3_b3_2_expand_style-protest-vote.md) — its entry in the divergence review ledger
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
