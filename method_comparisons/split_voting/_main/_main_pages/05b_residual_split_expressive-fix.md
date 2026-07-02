# The cure — score your ally, and STAR's split disappears

*Generated from [`05b_residual_split_expressive-fix.yaml`](../05b_residual_split_expressive-fix.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ada

## Scenario

Same three candidates and the same factions as 05a, with one change: the Ada/Ben
side actually USES the score ballot. Ada-fans still favor Ada but give ally Ben a
3; Ben-fans favor Ben but give Ada a 3. They sincerely prefer either ally to Cara.

Scores now: Ada 250, Ben 230, Cara 200. The two finalists are Ada and Ben — the
opponent Cara is shut out — and the runoff keeps the seat on the majority side.
Nothing about the electorate's true preferences changed between 05a and 05b; only
whether voters expressed support for their ally. That is the whole point: STAR
removes FORCED vote-splitting, and hands voters the tool to avoid the self-
inflicted kind.

Note the [Divergence from STAR] block: Choose-One (Plurality) still elects Cara on
first-choices (Ada 35, Ben 25, Cara 40) — STAR diverges and fixes the split.
Deep dive: 00_start_here/residual_vote_splitting.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cara
35:5,3,0   # Ada-fans — favorite Ada, but honestly score ally Ben a 3
25:3,5,0   # Ben-fans — favorite Ben, but honestly score ally Ada a 3
40:0,0,5   # Cara bloc (the minority side)
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/05b_residual_split_expressive-fix_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ada     |   * Ben     |     Cara    |
-------------------------------------------------------------
         * Ada > |     ---      |35 - 40 - 25 |60 -  0 - 40 |
         * Ben > | 25 - 40 - 35 |    ---      |60 -  0 - 40 |
          Cara > | 40 -  0 - 60 |40 -  0 - 60 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Divergence from STAR]
  STAR                   = Ada
  Choose-One (Plurality) = Cara   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Cara 40, Ada 35, Ben 25
  Plurality winner: Cara (40, 40.0%)
  Bloc 'Allies' = Ada, Ben: combined 60 (60.0%); winner Cara is OUTSIDE it.
  => VOTE SPLITTING: the 'Allies' bloc is an outright majority (60 vs Cara's
     40) but split across 2 candidates, so Cara won Choose-One. STAR elected
     Ada.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Ada,Ben,Cara
   40 ×   0,  0,   5
   35 ×   5,  3,   0
   25 ×   3,  5,   0

[Score Distribution] (number of ballots giving each score)
       5   4   3   2   1   0  | Total   Avg
Ada   35   0  25   0   0  40  |   250   2.5
Ben   25   0  35   0   0  40  |   230   2.3
Cara  40   0   0   0   0  60  |   200   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 250 -- First place
   Ben           -- 230 -- Second place
   Cara          -- 200
 Ada and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 35 -- First place
   Ben           -- 25
   Equal Support -- 40
 Ada wins.
   Runoff math:
     100  ballots cast
   −  40  Equal Support (no preference between the two finalists)
     ───
      60  voters with a preference  (majority = 31)
           Ada 35 (58%)  ·  Ben 25 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/05b_residual_split_expressive-fix.yaml
```

## See also

- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md)
