# Large field (9 candidates) — STAR scales, and Equal Support decides

*Generated from [`06a_c9_b3_large-field-equal-support.yaml`](../06a_c9_b3_large-field-equal-support.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Carmen

## Scenario

The ballot-visual election: 9 candidates, scored 0–5. STAR handles a big field
with no extra machinery — the scoring round is just addition (no elimination
rounds, unlike IRV, which would need up to 8).

Carmen (15) and David (14) are the two highest totals, so they're the finalists.
In the automatic runoff, 2 of the 3 voters scored BOTH finalists equally (Equal
Support); the one voter who preferred Carmen decides it. Carmen wins.

Discussion (Larry):
 - 9 candidates, one screen — why no rounds? (Scoring is addition.)
 - Most of the runoff is "Equal Support" — were those votes wasted? (No: they
   picked the finalists; neutral only on the Carmen-vs-David tie they declared.)
 - Helena and Gabe got plenty of stars — why aren't they in the runoff? (Only
   the top two by score are finalists.)
 - Did the runoff change the result or confirm it? (Confirms here; see
   06b_c9_runoff-overturns-leader.yaml for a case where it OVERTURNS the leader.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andre,Blake,Carmen,David,Ella,Fernando,Gabe,Helena,Ira
4,0,5,5,1,3,5,4,0
4,3,5,5,1,3,5,4,1
1,0,5,4,1,3,1,4,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/06a_c9_b3_large-field-equal-support_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     Andre    |    Blake    |  * Carmen   |  * David    |     Ella    |   Fernando  |     Gabe    |    Helena   |     Ira     |
-------------------------------------------------------------------------------------------------------------------------------------------------
         Andre > |     ---      | 3 - 0 - 0   | 0 - 0 - 3   | 0 - 0 - 3   | 2 - 1 - 0   | 2 - 0 - 1   | 0 - 1 - 2   | 0 - 2 - 1   | 3 - 0 - 0   |
         Blake > |  0 - 0 - 3   |    ---      | 0 - 0 - 3   | 0 - 0 - 3   | 1 - 0 - 2   | 0 - 1 - 2   | 0 - 0 - 3   | 0 - 0 - 3   | 1 - 2 - 0   |
      * Carmen > |  3 - 0 - 0   | 3 - 0 - 0   |    ---      | 1 - 2 - 0   | 3 - 0 - 0   | 3 - 0 - 0   | 1 - 2 - 0   | 3 - 0 - 0   | 3 - 0 - 0   |
       * David > |  3 - 0 - 0   | 3 - 0 - 0   | 0 - 2 - 1   |    ---      | 3 - 0 - 0   | 3 - 0 - 0   | 1 - 2 - 0   | 2 - 1 - 0   | 3 - 0 - 0   |
          Ella > |  0 - 1 - 2   | 2 - 0 - 1   | 0 - 0 - 3   | 0 - 0 - 3   |    ---      | 0 - 0 - 3   | 0 - 1 - 2   | 0 - 0 - 3   | 2 - 1 - 0   |
      Fernando > |  1 - 0 - 2   | 2 - 1 - 0   | 0 - 0 - 3   | 0 - 0 - 3   | 3 - 0 - 0   |    ---      | 1 - 0 - 2   | 0 - 0 - 3   | 3 - 0 - 0   |
          Gabe > |  2 - 1 - 0   | 3 - 0 - 0   | 0 - 2 - 1   | 0 - 2 - 1   | 2 - 1 - 0   | 2 - 0 - 1   |    ---      | 2 - 0 - 1   | 3 - 0 - 0   |
        Helena > |  1 - 2 - 0   | 3 - 0 - 0   | 0 - 0 - 3   | 0 - 1 - 2   | 3 - 0 - 0   | 3 - 0 - 0   | 1 - 0 - 2   |    ---      | 3 - 0 - 0   |
           Ira > |  0 - 0 - 3   | 0 - 2 - 1   | 0 - 0 - 3   | 0 - 0 - 3   | 0 - 1 - 2   | 0 - 0 - 3   | 0 - 0 - 3   | 0 - 0 - 3   |    ---      |

[Condorcet Winner]
  Condorcet Winner: Carmen — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots.
Andre,Blake,Carmen,David,Ella,Fernando,Gabe,Helena,Ira
    4,    0,     5,    5,   1,       3,   5,     4,  0
    4,    3,     5,    5,   1,       3,   5,     4,  1
    1,    0,     5,    4,   1,       3,   1,     4,  0

[Score Distribution] (number of ballots giving each score)
          5  4  3  2  1  0  | Total   Avg
Andre     0  2  0  0  1  0  |     9   3.0
Blake     0  0  1  0  0  2  |     3   1.0
Carmen    3  0  0  0  0  0  |    15   5.0
David     2  1  0  0  0  0  |    14   4.7
Ella      0  0  0  0  3  0  |     3   1.0
Fernando  0  0  3  0  0  0  |     9   3.0
Gabe      2  0  0  0  1  0  |    11   3.7
Helena    0  3  0  0  0  0  |    12   4.0
Ira       0  0  0  0  1  2  |     1   0.3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Carmen        -- 15 -- First place
   David         -- 14 -- Second place
   Helena        -- 12
   Gabe          -- 11
   Andre         --  9
   Fernando      --  9
   Blake         --  3
   Ella          --  3
   Ira           --  1
 Carmen and David advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Carmen        -- 1 -- First place
   David         -- 0
   Equal Support -- 2
 Carmen wins.
   Runoff math:
     3  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Carmen 1 (100%)  ·  David 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Carmen
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/06a_c9_b3_large-field-equal-support.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README_ties.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
