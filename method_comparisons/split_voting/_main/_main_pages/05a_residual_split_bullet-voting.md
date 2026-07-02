# STAR's residual split — a coalition bullet-votes itself apart

*Generated from [`05a_residual_split_bullet-voting.yaml`](../05a_residual_split_bullet-voting.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cara

## Scenario

The honest caveat to "STAR ends vote-splitting": it ends the FORCED kind. A
faction can still split ITSELF if it refuses to use the score ballot.

Ada and Ben are on the same side (60 voters); Cara is the opponent (40). Here the
Ada/Ben side bullet-votes tribally — Ada-fans give Ben a 0, Ben-fans give Ada a
0 — instead of scoring their ally honestly. Scores: Ada 175, Ben 125, Cara 200.
Cara grabs a finalist slot on a split field and wins the runoff, even though 60%
preferred that side. STAR did not rescue a split the voters inflicted on
themselves: the residual lives only in the top-two runoff.

The cure is in their hands — see 05b_residual_split_expressive-fix.yaml, where the
SAME factions score their ally even a 3 and STAR elects the majority side.
Deep dive: 00_start_here/residual_vote_splitting.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cara
35:5,0,0   # Ada-fans bullet-vote — refuse to score their ally Ben
25:0,5,0   # Ben-fans bullet-vote — refuse to score their ally Ada
40:0,0,5   # Cara bloc (the minority side)
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/05a_residual_split_bullet-voting_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ada     |     Ben     |   * Cara    |
-------------------------------------------------------------
         * Ada > |     ---      |35 - 40 - 25 |35 - 25 - 40 |
           Ben > | 25 - 40 - 35 |    ---      |25 - 35 - 40 |
        * Cara > | 40 - 25 - 35 |40 - 35 - 25 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cara — matches the STAR winner

[Vote-splitting check]
  Choose-One first choices: Cara 40, Ada 35, Ben 25
  Plurality winner: Cara (40, 40.0%)
  Bloc 'Allies' = Ada, Ben: combined 60 (60.0%); winner Cara is OUTSIDE it.
  => VOTE SPLITTING: the 'Allies' bloc is an outright majority (60 vs Cara's
     40) but split across 2 candidates, so Cara won Choose-One. STAR elected
     Cara.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Ada,Ben,Cara
   40 ×   0,  0,   5
   35 ×   5,  0,   0
   25 ×   0,  5,   0

[Score Distribution] (number of ballots giving each score)
       5   4   3   2   1   0  | Total   Avg
Ada   35   0   0   0   0  65  |   175   1.8
Ben   25   0   0   0   0  75  |   125   1.2
Cara  40   0   0   0   0  60  |   200   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cara          -- 200 -- First place
   Ada           -- 175 -- Second place
   Ben           -- 125
 Cara and Ada advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cara          -- 40 -- First place
   Ada           -- 35
   Equal Support -- 25
 Cara wins.
   Runoff math:
     100  ballots cast
   −  25  Equal Support (no preference between the two finalists)
     ───
      75  voters with a preference  (majority = 38)
           Cara 40 (53%)  ·  Ada 35 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cara
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/05a_residual_split_bullet-voting.yaml
```

## See also

- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
