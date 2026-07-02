# 01_STAR — single-winner STAR Voting

The library's headline method: **STAR** (Score Then Automatic Runoff) for one
seat. Score every candidate 0–5; the two highest-scoring candidates go to an
automatic runoff decided by which of the two each ballot prefers.

| Where | What |
|---|---|
| [`_main/`](_main/) | the teaching progression — two-candidate intros, ballot styles, abstentions, quorum, vote-splitting scenarios, display options |
| [`runoff_overturns_leader/`](runoff_overturns_leader/) | the Runoff Reversal set — real BetterVoting elections where the runoff confirms or overturns the score leader |
| [`Flat_scores_ties/`](Flat_scores_ties/) | ties and flat-score edge cases, and how the tiebreakers resolve them |
| [`pet_real_bv_election/`](pet_real_bv_election/) | a real 461-ballot BetterVoting race, imported and reconciled line by line |

Cross-method contrasts featuring STAR (vs RCV-IRV, Approval, Score) live in
[`../method_comparisons/`](../method_comparisons/). Multi-winner STAR:
[`../02_STAR_Bloc/`](../02_STAR_Bloc/) and [`../03_STAR_PR/`](../03_STAR_PR/).
Concept docs: [`../00_start_here/STAR_Voting/`](../00_start_here/STAR_Voting/).

# file: README_01_STAR.md
