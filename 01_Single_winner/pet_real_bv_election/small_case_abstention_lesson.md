# When a `5,5` is called an "abstention" — a minimal BetterVoting vs LH case

**One line:** in a real five-ballot STAR election, BetterVoting counts a voter who
scored **both** candidates **5** as an *abstention*. That voter didn't abstain —
they gave maximum support to everyone. This is the smallest possible demonstration
of the [abstention reconciliation](./BV_result_snapshot.md) seen in the 461-ballot
[pet race](./README.md); same effect, five ballots you can check by hand.

→ Reading results: [How to read a STAR report](../../00_start_here/concepts/tabulation_engines/LH_starvote/reading_a_star_report.md) (LH engine)
· [BetterVoting and the LH engine — when the reports differ](../../00_start_here/concepts/tabulation_engines/bettervoting_and_the_engine.md#when-the-two-reports-differ--abstentions-vs-equal-support) (both)
· [Runoff percentages](../../00_start_here/concepts/STAR_Voting/runoff_percentages.md)
· What an "Equal Support" ballot is: [`GLOSSARY`](../../00_start_here/GLOSSARY.md).

---

## The election

A real BetterVoting STAR election (**BV id `3w6v4b`**, captured 2026-06-28), two
candidates `A` and `B`, five ballots:

| Ballot | A | B | What it is |
|---|--:|--:|---|
| 1 | 0 | 5 | prefers **B** |
| 2 | 4 | 0 | prefers **A** |
| 3 | **5** | **5** | **Equal Support** — loves both equally (a cast vote) |
| 4 | 5 | 0 | prefers **A** |
| 5 | — | — | blank — the one true **abstention** |

- Frozen raw export: [`small_abstention_c2_b5_bv_export.json`](./small_abstention_c2_b5_bv_export.json)
- Converted election (LH-tabulatable): [`small_abstention_c2_b5.yaml`](./small_abstention_c2_b5.yaml)
- Full engine report: [`small_abstention_c2_b5_tabulated.txt`](../pet_real_bv_election_tabulated/small_abstention_c2_b5_tabulated.txt)

## Two reports, one ballot of disagreement

| | BetterVoting (frozen) | LH engine |
|---|---:|---:|
| Ballots tallied | **3** (`nTallyVotes`) | **5** |
| Abstentions | **2** (`nAbstentions`) — the `5,5` **and** the blank | **1** — the blank only |
| The `5,5` ballot | counted as an **abstention** ❌ | **Equal Support**: counted in the score round, neutral in the runoff ✓ |
| Automatic Runoff | A 2, B 1 | A 2, B 1, Equal Support 2 |
| **Winner** | **A** | **A** |

BetterVoting's own result, straight from the export:

```json
{ "nAbstentions": 2, "nTallyVotes": 3 }
```

The two "abstentions" are the only two **flat** ballots (every candidate scored the
same): the `5,5` and the blank. So BetterVoting treats "rated everyone the same" as
"didn't vote." The winner is unaffected — but the `5,5` voter is mislabeled, and in
a larger or asymmetric race their dropped stars would skew the published score
totals.

## What the LH engine prints

```
 Tabulating 5 ballots. Note: 1 of 5 ballots is marked as an abstention.
 ...
 Automatic Runoff Round
   A             -- 2 -- First place
   B             -- 1
   Equal Support -- 2
 A wins.
   Voters with a preference: 3 of 5 (2 Equal Support). A 2 (67%) vs B 1 (33%); majority = 2.
```

and in the saved `_tabulated` copy, the same thing as a funnel that adds up:

```
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           A 2 (67%)  ·  B 1 (33%)
```

Read it: **5 cast, 1 abstention** (the blank). The `5,5` and the blank both score
A == B, so both sit in **Equal Support** and are excluded *only* from the runoff
percentage — the 3 voters with a preference decide it, and A wins 2–1.

## Why it matters

A ballot that scores everyone equally is a **vote**, not an absence of one:

1. **The `5,5` voter participated** — maximally. Calling that an "abstention" tells
   an auditor the ballot was empty. It wasn't.
2. **In STAR the score round adds every star.** A `5,5` adds 5 to each candidate.
   Dropping it lowers the totals and makes the published numbers fail a hand count.
   (Here it's symmetric so the *winner* is safe; that's luck of the example, not a
   property to rely on.)
3. **"No preference" already has a correct home: Equal Support.** It is rightly
   neutral in the *runoff denominator* (a flat ballot can't prefer either finalist)
   — but it still counts in the score round. Folding it into "abstention" conflates
   "I have no preference between these two" with "I didn't vote."

## How this scales

The full [pet race](./README.md) (461 ballots) shows the same thing at size:
BetterVoting reports **6 abstentions**, all flat ballots — including one voter who
scored **all seven** candidates **5** and another who scored them all **4**. Those
two carry `5 + 4 = 9` stars per candidate, which is exactly why BetterVoting's score
totals run 9 below a full count. Evidence frozen in
[`BV_result_snapshot.md`](./BV_result_snapshot.md).

## Reproduce / verify it yourself

- Recipe to build it on BetterVoting: [`SMALL_CASE_reproduce_on_BV.md`](./SMALL_CASE_reproduce_on_BV.md)
- Idealized synthetic variant (adds an explicit `0,0` row): [`abstention_reconciliation_min_c2_b6.yaml`](./abstention_reconciliation_min_c2_b6.yaml)
- The reconciliation / GitHub issue write-up: [`LH_BV_reconciliation_issue.md`](./LH_BV_reconciliation_issue.md)
