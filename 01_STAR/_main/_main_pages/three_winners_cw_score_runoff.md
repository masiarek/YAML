# Three notions of "winner" disagree — Condorcet, Score, and Runoff

*Generated from [`three_winners_cw_score_runoff.yaml`](../three_winners_cw_score_runoff.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bob

## Scenario

One tiny election, three different "winners" depending on what you mean by the word.
Five voters, three candidates (Ann, Bob, Carl):

 - Condorcet winner = ANN — she beats both Bob and Carl one-on-one (3 of 5 prefer
   her each time). The "beats everyone head-to-head" winner.
 - Score winner = CARL — he has the most total stars (19). The "highest intensity /
   utility favorite" winner.
 - STAR winner = BOB — the Scoring Round sends the top two (Carl 19, Bob 18) to the
   Automatic Runoff, and a 3-2 majority prefers Bob there. The "broad compromise the
   majority actually picks between the finalists" winner.

No method is malfunctioning — they optimize for different things. STAR deliberately
lands on Bob: it uses scores to FIND the finalists, then a majority runoff to CHOOSE
between them. (Ann is shut out only because she's edged for second place in the
scoring round — a reminder STAR is not a Condorcet method, by design.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann, Bob, Carl
  5,   4,    3
  5,   4,    3
  5,   4,    3
  0,   3,    5
  0,   3,    5
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/three_winners_cw_score_runoff_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ann    |  * Bob    |  * Carl   |
-----------------------------------------------------
         Ann > |    ---     |3 - 0 - 2  |3 - 0 - 2  |
       * Bob > | 2 - 0 - 3  |   ---     |3 - 0 - 2  |
      * Carl > | 2 - 0 - 3  |2 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ann — STAR elected Bob instead (Ann was eliminated in the scoring round)

[Divergence from STAR]
  STAR                   = Bob
  Choose-One (Plurality) = Ann   (differs from STAR)
  RCV-IRV                = Ann   (differs from STAR)
  RCV-RR (Condorcet)     = Ann   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/three_winners_cw_score_runoff_RCV-IRV_tabulated.txt
  RCV-RR round-robin: _main_tabulated/three_winners_cw_score_runoff_RCV-RR_tabulated.txt

Majority Preference Enforcement Principle:
 - Score Round Winner(s) = (Carl)
 - Runoff Round Winner   = (Bob)
  Candidate Carl earned the highest total score,
  but Candidate Bob won the automatic runoff by being the head-to-head majority favorite.


--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 5 ballots.
Count × Ann,Bob,Carl
    3 ×   5,  4,   3
    2 ×   0,  3,   5

[Score Distribution] (number of ballots giving each score)
      5  4  3  2  1  0  | Total   Avg
Ann   3  0  0  0  0  2  |    15   3.0
Bob   0  3  2  0  0  0  |    18   3.6
Carl  2  0  3  0  0  0  |    19   3.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Carl          -- 19 -- First place
   Bob           -- 18 -- Second place
   Ann           -- 15
 Carl and Bob advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bob           -- 3 -- First place
   Carl          -- 2
   Equal Support -- 0
 Bob wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Bob 3 (60%)  ·  Carl 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bob
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/three_winners_cw_score_runoff.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/STAR_OUTLIER_RR_WITH_IRV/three_winners_cw_score_runoff.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01a_c2_b1_two-candidates](01a_c2_b1_two-candidates.md) · [01a_c2_b2_two-candidates](01a_c2_b2_two-candidates.md) · [01b_c2_b2_two-candidates](01b_c2_b2_two-candidates.md) · [01c_c2_b3_two-candidates](01c_c2_b3_two-candidates.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [Approval_ballot](Approval_ballot.md) · [abstentions](abstentions.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
