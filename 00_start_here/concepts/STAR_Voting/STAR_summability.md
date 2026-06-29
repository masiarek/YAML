# STAR Is Summable — Add Up Precinct Totals

**One line:** a method is *summable* (precinct-summable) if you can get the final
result by **adding up independent precinct totals**. STAR is summable, which makes it
precinct-auditable and gives meaningful early/partial results.

→ Cross-method **topic hub**: [Summability](../topics/summability/README.md) (STAR / Ranked
Robin / IRV side by side). The method that is *not* summable is RCV-IRV —
[`IRV's lack of summability`](../RCV_IRV/RCV_IRV_lack_of_summability.md).
Glossary: [`summability`](../../GLOSSARY.md).

---

## Why STAR is summable

STAR's whole count reduces to **sums**:

- The **scoring round** is just each candidate's total stars — add the precinct
  totals together.
- The **runoff** uses the **pairwise (For / Equal / Against) matrix**: for every pair
  of candidates, how many ballots scored A over B, equal, or B over A. Those counts
  **add** across precincts too.

So each precinct can publish a small fixed-size table, and the statewide result is
simply their sum. That makes STAR **precinct-auditable**, lets observers verify
locally, and gives partial counts that actually mean something.

## Worked example — two districts, subtotals that add up

The mirror of [IRV's non-summable example](../RCV_IRV/RCV_IRV_lack_of_summability.md#worked-example--two-districts-both-won-by-b-merged-b-loses).
Same setup, opposite result — run [`summability_demo/`](../../../01_Single_winner/summability_demo/)
(three trees: Maple, Oak, Pine). The two districts even have *different* winners (Maple in
A, Oak in B — district B is a runoff reversal), so the merge is genuinely non-trivial:

**Score totals add:**

| | Maple | Oak | Pine |
|---|--:|--:|--:|
| District A | 10 | 9 | 6 |
| District B | 5 | 10 | 12 |
| **Sum** | **15** | **19** | **18** |

That sum *is* the combined election's score round (Oak 19, Pine 18, Maple 15 →
**Oak & Pine** advance).

**The pairwise matrix adds too** — e.g. the decisive Oak-vs-Pine head-to-head:

```
District A:  Oak 2 – Pine 1
District B:  Oak 2 – Pine 1
  Sum:       Oak 4 – Pine 2   → Oak wins the runoff → Oak wins
```

Every number the statewide result needs — score totals and the For/Equal/Against matrix —
is just the **sum of the precinct tables**. No recount, no pooling ballots, no central
elimination order: each precinct publishes a fixed-size table (C scores + a C×C matrix)
and anyone can add them and check the winner.

## Verifiable, not just summable

Because the whole count is **addition**, STAR is hand-countable, runs on existing
optical-scan equipment, and supports paper-ballot recounts and risk-limiting audits — a
precinct can verify its own contribution. Independent confirmation that the engine's
pairwise/runoff math (the summable artifact) is correct comes from the
[`pref_voting` cross-check](../tabulation_engines/cross_checking_with_pref_voting.md) — a
second, independent engine agrees on every example.

External references (advocacy, but the summability math is standard):
[Is STAR Voting Precinct Summable? (starvoting.org)](https://www.starvoting.org/summable)
· [STAR Voting security & audits](https://www.starvoting.org/security)
· [STAR Voting — Equal Vote Coalition](https://www.equal.vote/star).

## The nuance — it's about the tabulation, not the ballot

Summability is a property of the **count**, not the ballot. A *ranked* ballot counted
by a **Condorcet** method (Ranked Robin) is also summable, via the very same pairwise
matrix. So "ranked ballots aren't summable" is wrong — it's **IRV's elimination
count** specifically that isn't (see the [IRV page](../RCV_IRV/RCV_IRV_lack_of_summability.md)).
More on keeping the terms straight: [`TIPS_terminology.md`](../../TIPS_terminology.md).
