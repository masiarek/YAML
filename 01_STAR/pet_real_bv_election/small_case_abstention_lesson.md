# When "no preference" gets called an "abstention" — a real BetterVoting case

**One line:** in a real eight-ballot STAR election, BetterVoting reports **3
abstentions** — but only **one** ballot is actually blank. The other two are an
all-zero ballot and a voter who scored **every** candidate **3**. This small case
(three candidates, so it separates ideas a two-candidate race blurs) is the cleanest
picture of the [abstention reconciliation](BV_result_snapshot.md) seen at scale in
the 461-ballot [pet race](README_pet_real_bv_election.md).

> Filed with BetterVoting: **[Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)**.

→ Reading results: [How to read a STAR report](../../00_start_here/tabulation_engines/LH_starvote/reading_a_star_report.md) (LH engine)
· [BetterVoting and the LH engine — when the reports differ](../../00_start_here/tabulation_engines/bettervoting_and_the_engine.md#when-the-two-reports-differ--abstentions-vs-equal-support) (both)
· [Runoff percentages](../../00_start_here/STAR_Voting/runoff_percentages.md)
· What an "Equal Support" ballot is: [`GLOSSARY`](../../00_start_here/GLOSSARY.md).

---

## The election

A real BetterVoting STAR election (**BV id `dq2dmm`**, captured 2026-06-28), three
candidates `Apple` / `Banana` / `Cherry`, eight ballots:

| # | Apple | Banana | Cherry | What it is |
|---|--:|--:|--:|---|
| 1 | 0 | 5 | 1 | prefers Banana |
| 2 | — | — | — | **blank** — a true abstention |
| 3 | 5 | 4 | 1 | prefers Apple |
| 4 | 4 | 5 | 2 | prefers Banana |
| 5 | 0 | 0 | 0 | **all-zero** — cast, supports no one |
| 6 | 3 | 3 | 3 | **all-3s** — flat, but fully engaged |
| 7 | 3 | 5 | 0 | prefers Banana |
| 8 | 5 | 5 | 0 | **Equal Support** — Apple = Banana (Cherry 0) |

- Frozen raw export: [`flat_scores_abstention_c3_b8_bv_export.json`](flat_scores_abstention_c3_b8_bv_export.json)
- Converted election (LH-tabulatable): [`flat_scores_abstention_c3_b8.yaml`](flat_scores_abstention_c3_b8.yaml)
- Full engine report: [`flat_scores_abstention_c3_b8_tabulated.txt`](pet_real_bv_election_tabulated/flat_scores_abstention_c3_b8_tabulated.txt)

## Three ideas a third candidate pulls apart

With only two candidates, "no preference," "flat ballot," and "abstention" all
collapse into the same thing. Add a third candidate and they separate — and you can
see exactly where BetterVoting's rule sits:

| Ballot | True abstention? (blank) | Flat? (BV "abstention") | Equal Support in runoff? (Apple = Banana) |
|---|:--:|:--:|:--:|
| `-,-,-` blank | ✅ | ✅ | ✅ |
| `0,0,0` | — | ✅ | ✅ |
| `3,3,3` | — | ✅ | ✅ |
| `5,5,0` | — | — *(Cherry differs)* | ✅ |
| **Count** | **1** | **3** | **4** |

- **BetterVoting** flags a ballot as an *abstention* when it is **flat** (every
  candidate equal) → it counts **3** (the blank, `0,0,0`, **and** `3,3,3`) and
  tallies 5.
- **STAR / the [LH engine](../../00_start_here/tabulation_engines/bettervoting_and_the_engine.md)** only calls the **blank** an abstention (**1**); the
  runoff sets aside the **4** ballots with no preference *between the two finalists*
  as **Equal Support** — which includes `5,5,0` but counts all of them in the score
  round.

So the two notions genuinely disagree on two ballots: `3,3,3` (a real, engaged vote
BetterVoting drops) and `5,5,0` (Equal Support BetterVoting keeps).

## Two reports

| | BetterVoting (frozen) | LH engine |
|---|---:|---:|
| Ballots tallied | **5** (`nTallyVotes`) | **8** |
| Abstentions | **3** (flat ballots) | **1** (blank only) |
| `3,3,3` ballot | abstention ❌ | counted; Equal Support in runoff ✓ |
| Automatic Runoff | Banana / Apple | Banana 3, Apple 1, Equal Support 4 |
| **Winner** | **Banana** | **Banana** |

BetterVoting's own result, from the export:

```json
{ "nAbstentions": 3, "nTallyVotes": 5 }
```

## What the LH engine prints

```
 Tabulating 8 ballots. Note: 1 of 8 ballots is marked as an abstention.
 Scoring Round
   Banana        -- 27 -- First place
   Apple         -- 20 -- Second place
   Cherry        --  7
 Banana and Apple advance.
 Automatic Runoff Round
   Banana        -- 3 -- First place
   Apple         -- 1
   Equal Support -- 4
 Banana wins.
   Voters with a preference: 4 of 8 (4 Equal Support).
   Banana 3 (75%) vs Apple 1 (25%); majority = 3.
```

and in the saved `_tabulated` copy, the same as a funnel that adds up:

```
   Runoff math:
     8  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           Banana 3 (75%)  ·  Apple 1 (25%)
```

Cherry's low scores still **counted** (they're inside the 7) — they just didn't make
the top two. The 4 Equal Support ballots counted in the score round and are set aside
only from the runoff percentage; 4 voters had a preference, and Banana takes 3 of
them (75%), clearing the majority of 3.

## The LH report (echo)

This is a small election, so here is the **on-screen echo** in full (the saved
[`flat_scores_abstention_c3_b8_tabulated.txt`](pet_real_bv_election_tabulated/flat_scores_abstention_c3_b8_tabulated.txt)
mirror additionally forces the full N×N matrix, the Condorcet line, and the
"Runoff math" funnel):

```
--- Runoff (Preference) Matrix ---
Legend: For - Equal Support - Against        * indicates Top 2 Finalist
               |  * Apple   | * Banana  |
     * Apple > |    ---     |1 - 4 - 3  |
    * Banana > | 3 - 4 - 1  |   ---     |

 Tabulating 8 ballots. Note: 1 of 8 ballots is marked as an abstention.
Apple,Banana,Cherry
    0,     5,     1
    -,     -,     -
    5,     4,     1
    4,     5,     2
    0,     0,     0
    3,     3,     3
    3,     5,     0
    5,     5,     0
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Score Distribution] (number of ballots giving each score)
        5  4  3  2  1  0  Abs  | Total   Avg
Apple   2  1  2  0  0  2    1  |    20   2.9
Banana  4  1  1  0  0  1    1  |    27   3.9
Cherry  0  0  1  1  2  3    1  |     7   1.0

Scoring Round
 The two highest-scoring candidates advance to the next round.
   Banana        -- 27 -- First place
   Apple         -- 20 -- Second place
   Cherry        --  7
 Banana and Apple advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Banana        -- 3 -- First place
   Apple         -- 1
   Equal Support -- 4
 Banana wins.
   Voters with a preference: 4 of 8 (4 Equal Support).
   Banana 3 (75%) vs Apple 1 (25%); majority = 3.
```

## Why it matters

A ballot that scores everyone the same is a **vote**, not a missing one:

1. **The `3,3,3` voter participated.** Calling it an "abstention" tells an auditor the
   ballot was empty. It wasn't — Cherry got a 3 too.
2. **In STAR the score round adds every star.** Dropping flat ballots lowers the
   totals and makes BetterVoting's published numbers fail a hand count of the ballots.
3. **"No preference" already has a correct home: Equal Support** — counted in the
   score round, neutral only in the runoff denominator. Folding it into "abstention"
   conflates "no preference between these two" with "didn't vote."

## How this scales

The full [pet race](README_pet_real_bv_election.md) (461 ballots) shows the identical rule at size:
BetterVoting reports **6 abstentions**, all flat ballots — including one voter who
scored **all seven** candidates **5** and another **all 4**. Frozen evidence:
[`BV_result_snapshot.md`](BV_result_snapshot.md).

## Variants & reproduction

- **Even simpler (2 candidates):** [`small_abstention_c2_b5_lesson.md`](small_abstention_c2_b5_lesson.md)
  — with only two candidates a `5,5` *is* flat, so BetterVoting flags it directly
  (2 abstentions / 3 tallied). Good for the tightest one-ballot statement of the bug;
  this 3-candidate case is better for showing *why* flat ≠ no-preference.
- **Synthetic illustration:** [`abstention_reconciliation_min_c2_b6.yaml`](abstention_reconciliation_min_c2_b6.yaml)
- **Reproduce on BetterVoting:** [`SMALL_CASE_reproduce_on_BV.md`](SMALL_CASE_reproduce_on_BV.md)
- **The reconciliation / issue write-up:** [`LH_BV_reconciliation_issue.md`](LH_BV_reconciliation_issue.md)
  (→ [Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407))
