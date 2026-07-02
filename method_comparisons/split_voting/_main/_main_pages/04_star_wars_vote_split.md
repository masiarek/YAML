# The Voting Dilemma — Skywalker & Leia split the Rebel vote

*Generated from [`04_star_wars_vote_split.yaml`](../04_star_wars_vote_split.yaml) — do not edit by hand. Regenerate: `python scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Leia

## Scenario

Matches the "THE VOTING DILEMMA" slide: you expect Skywalker and Vader to be the
frontrunners, but you actually prefer Leia. 100 voters. A 60% Rebel majority
prefers a Rebel (Skywalker or Leia) over the Empire's Vader — but they're split
on which Rebel.

Under Choose-One Plurality each voter names ONE candidate, so the Rebels split:
Skywalker 33, Leia 27. Vader wins with just 40 — the candidate 60% ranked LAST.
That is vote-splitting handing the seat to the minority.

STAR lets every voter score all three 0-5, so Rebel voters can back BOTH
Skywalker and Leia. The two highest totals advance (Leia and Skywalker), and the
automatic runoff elects Leia — the broad consensus Rebel, and the candidate who
beats every other head-to-head (the Condorcet winner). The one you actually
preferred wins. Watch the [Vote-splitting check] confirm it.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Skywalker,Leia,Vader
33:5,4,0   # Rebels who'd "hold their nose" for electable Luke — but love Leia
27:4,5,0   # Leia's base — Luke a strong second
40:0,1,5   # Empire / Vader bloc — a mild nod to Leia over Luke
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/04_star_wars_vote_split_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * Skywalker  |   * Leia     |     Vader    |
-----------------------------------------------------------------
    * Skywalker > |      ---      |33 -  0 - 67  |60 -  0 - 40  |
         * Leia > | 67 -  0 - 33  |     ---      |60 -  0 - 40  |
          Vader > | 40 -  0 - 60  |40 -  0 - 60  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Leia — matches the STAR winner

[Divergence from STAR]
  STAR                   = Leia
  Choose-One (Plurality) = Vader   (differs from STAR)
  RCV-IRV                = Skywalker   (differs from STAR)
  Approval               = Skywalker   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/04_star_wars_vote_split_RCV-IRV_tabulated.txt

[Vote-splitting check]
  Choose-One first choices: Vader 40, Skywalker 33, Leia 27
  Plurality winner: Vader (40, 40.0%)
  Bloc 'Rebellion' = Skywalker, Leia: combined 60 (60.0%); winner Vader is OUTSIDE it.
  => VOTE SPLITTING: the 'Rebellion' bloc is an outright majority (60 vs
     Vader's 40) but split across 2 candidates, so Vader won Choose-One.
     STAR elected Leia.

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Skywalker,Leia,Vader
   40 ×         0,   1,    5
   33 ×         5,   4,    0
   27 ×         4,   5,    0

[Score Distribution] (number of ballots giving each score)
            5   4   3   2   1   0  | Total   Avg
Skywalker  33  27   0   0   0  40  |   273   2.7
Leia       27  33   0   0  40   0  |   307   3.1
Vader      40   0   0   0   0  60  |   200   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Leia          -- 307 -- First place
   Skywalker     -- 273 -- Second place
   Vader         -- 200
 Leia and Skywalker advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Leia          -- 67 -- First place
   Skywalker     -- 33
   Equal Support --  0
 Leia wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Leia 67 (67%)  ·  Skywalker 33 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Leia
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/04_star_wars_vote_split.yaml
```

## See also

- [Methods disagree on this election](../../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/04_star_wars_vote_split.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README_condorcet.md)
- [Vote splitting (worked set)](../../README_split_voting.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README_YAML_test_case_index.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
