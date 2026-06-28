# The minimal case — BetterVoting calls a `5,5` an "abstention" (2 candidates)

**One line:** the tightest possible demonstration. Two candidates, five ballots. One
voter scores **both** candidates **5** — maximum support for everyone — and
BetterVoting files that ballot as an **abstention**. An independent STAR engine
counts it as **Equal Support** and still elects the same winner.

> Filed with BetterVoting: **[Equal-Vote/bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)**.

This is the **2-candidate** member of the pair. Its richer sibling, which adds a
third candidate to show that BetterVoting's rule is "*any* flat ballot = abstention"
(it even drops an engaged `3,3,3`), is
[`small_case_abstention_lesson.md`](./small_case_abstention_lesson.md). At full scale:
the 461-ballot [pet race](./README.md).

→ Reading results: [How to read a STAR report](../../00_start_here/concepts/tabulation_engines/LH_starvote/reading_a_star_report.md)
· [BetterVoting vs the LH engine — when the reports differ](../../00_start_here/concepts/tabulation_engines/bettervoting_and_the_engine.md#when-the-two-reports-differ--abstentions-vs-equal-support)
· [Runoff percentages](../../00_start_here/concepts/STAR_Voting/runoff_percentages.md)
· [`GLOSSARY`](../../00_start_here/GLOSSARY.md)

---

## The election

A real BetterVoting STAR election (**BV id `3w6v4b`**, captured 2026-06-28), two
candidates `A` and `B`, five ballots:

| # | A | B | What it is |
|---|--:|--:|---|
| 1 | 0 | 5 | prefers **B** |
| 2 | 4 | 0 | prefers **A** |
| 3 | **5** | **5** | **Equal Support** — loves both equally (a cast vote) |
| 4 | 5 | 0 | prefers **A** |
| 5 | — | — | blank — the one true **abstention** |

- Frozen raw export: [`small_abstention_c2_b5_bv_export.json`](./small_abstention_c2_b5_bv_export.json)
- Converted election (LH-tabulatable): [`small_abstention_c2_b5.yaml`](./small_abstention_c2_b5.yaml)
- Full engine report: [`small_abstention_c2_b5_tabulated.txt`](../pet_real_bv_election_tabulated/small_abstention_c2_b5_tabulated.txt)

## Two reports — one ballot of disagreement

| | BetterVoting (frozen) | LH engine |
|---|---:|---:|
| Ballots tallied | **3** (`nTallyVotes`) | **5** |
| Abstentions | **2** — the `5,5` **and** the blank | **1** — the blank only |
| The `5,5` ballot | counted as an **abstention** ❌ | **Equal Support**: counted in the score round, neutral in the runoff ✓ |
| Automatic Runoff | A 2, B 1 | A 2, B 1, Equal Support 2 |
| **Winner** | **A** | **A** |

BetterVoting's own result, from the export:

```json
{ "nAbstentions": 2, "nTallyVotes": 3 }
```

With only two candidates, a `5,5` ballot *is* flat (every candidate equal), so
BetterVoting's "flat = abstention" rule flags it directly. That's what makes this the
cleanest one-sentence statement of the problem — though it can look like a harmless
edge case, which is exactly why the 3-candidate sibling matters: there, a flat
`3,3,3` is dropped while a genuine `5,5,0` no-preference ballot is kept, proving the
two ideas are different.

## What the LH engine prints

```
 Tabulating 5 ballots. Note: 1 of 5 ballots is marked as an abstention.
 Automatic Runoff Round
   A             -- 2 -- First place
   B             -- 1
   Equal Support -- 2
 A wins.
   Voters with a preference: 3 of 5 (2 Equal Support). A 2 (67%) vs B 1 (33%); majority = 2.
```

and in the saved `_tabulated` copy, the same as a funnel that adds up:

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
percentage. The 3 voters with a preference decide it, and A wins 2–1.

## Why it matters

1. **The `5,5` voter participated** — maximally. Calling that an "abstention" tells an
   auditor the ballot was empty. It wasn't.
2. **In STAR the score round adds every star.** A `5,5` adds 5 to each candidate;
   dropping it lowers the totals and makes the published numbers fail a hand count.
   (Here the example is symmetric, so the *winner* is safe — luck of the example, not
   a property to rely on.)
3. **"No preference" already has a correct home: Equal Support** — counted in the
   score round, neutral only in the runoff denominator. Folding it into "abstention"
   conflates "no preference between these two" with "didn't vote."

## See also

- Richer 3-candidate version (the canonical lesson): [`small_case_abstention_lesson.md`](./small_case_abstention_lesson.md)
- Synthetic illustration (adds an explicit `0,0` row): [`abstention_reconciliation_min_c2_b6.yaml`](./abstention_reconciliation_min_c2_b6.yaml)
- Full 461-ballot race + frozen BV evidence: [`README.md`](./README.md) · [`BV_result_snapshot.md`](./BV_result_snapshot.md)
- The reconciliation / issue write-up: [`LH_BV_reconciliation_issue.md`](./LH_BV_reconciliation_issue.md) (→ [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407))
- How it was reproduced on BetterVoting: [`SMALL_CASE_reproduce_on_BV.md`](./SMALL_CASE_reproduce_on_BV.md)
