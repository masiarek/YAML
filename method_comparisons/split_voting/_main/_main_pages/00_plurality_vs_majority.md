# Plurality vs Majority — most votes isn't more than half

*Generated from [`00_plurality_vs_majority.yaml`](../00_plurality_vs_majority.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Blake

## Scenario

100 voters, three candidates. First choices: Andre 40, Blake 35, Carmen 25.

Under Choose-One Plurality, Andre wins with 40 — the MOST votes. But 60 of 100
voters preferred someone else, so Andre has no MAJORITY. Blake and Carmen appeal
to the same 60-voter coalition; Choose-One splits it across two names and hands
the seat to the candidate a majority actively voted against.

STAR scores all three 0–5, so coalition voters back both Blake and Carmen. The two
highest totals (Blake, Carmen) advance, and the automatic runoff produces a winner
who holds a majority between the finalists — Blake. Watch [Divergence from STAR]
show Choose-One (Plurality) = Andre disagreeing with STAR, and the [Vote-splitting
check] confirm the 60-vote coalition. ("Most votes" and "over half" are different
bars; the gap only appears with 3+ candidates — that gap is where vote splitting
lives.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Andre,Blake,Carmen
40:5,0,0   # Andre bloc — most first choices, but a minority of the whole
35:0,5,4   # Blake base — also support coalition ally Carmen
25:0,4,5   # Carmen base — also support coalition ally Blake
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/00_plurality_vs_majority_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     Andre    |  * Blake    |  * Carmen   |
-------------------------------------------------------------
         Andre > |     ---      |40 -  0 - 60 |40 -  0 - 60 |
       * Blake > | 60 -  0 - 40 |    ---      |35 - 40 - 25 |
      * Carmen > | 60 -  0 - 40 |25 - 40 - 35 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Blake — matches the STAR winner

[Divergence from STAR]
  STAR                   = Blake
  Choose-One (Plurality) = Andre   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Andre 40, Blake 35, Carmen 25
  Plurality winner: Andre (40, 40.0%)
  Bloc 'Coalition' = Blake, Carmen: combined 60 (60.0%); winner Andre is OUTSIDE it.
  => VOTE SPLITTING: the 'Coalition' bloc is an outright majority (60 vs
     Andre's 40) but split across 2 candidates, so Andre won Choose-One.
     STAR elected Blake.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Andre,Blake,Carmen
   40 ×     5,    0,     0
   35 ×     0,    5,     4
   25 ×     0,    4,     5

[Score Distribution] (number of ballots giving each score)
         5   4   3   2   1   0  | Total   Avg
Andre   40   0   0   0   0  60  |   200   2.0
Blake   35  25   0   0   0  40  |   275   2.8
Carmen  25  35   0   0   0  40  |   265   2.6

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Blake         -- 275 -- First place
   Carmen        -- 265 -- Second place
   Andre         -- 200
 Blake and Carmen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blake         -- 35 -- First place
   Carmen        -- 25
   Equal Support -- 40
 Blake wins.
   Runoff math:
     100  ballots cast
   −  40  Equal Support (no preference between the two finalists)
     ───
      60  voters with a preference  (majority = 31)
           Blake 35 (58%)  ·  Carmen 25 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blake
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/00_plurality_vs_majority.yaml
```

## See also

- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
