# STAR Is Summable — Add Up Precinct Totals

**One line:** a method is *summable* (precinct-summable) if you can get the final
result by **adding up independent precinct totals**. STAR is summable, which makes it
precinct-auditable and gives meaningful early/partial results.

→ The method that is *not* summable is RCV-IRV — see
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

## Test case (run it)

→ [`01_Single_winner/04b_c4_b3_display-options-all.yaml`](../../../01_Single_winner/04b_c4_b3_display-options-all.yaml)
with `show_matrix: true`.

The printed **Runoff (Preference) Matrix** *is* the summable artifact — the
head-to-head table any precinct can produce, and which precinct tables add up to the
whole election.

## The nuance — it's about the tabulation, not the ballot

Summability is a property of the **count**, not the ballot. A *ranked* ballot counted
by a **Condorcet** method (Ranked Robin) is also summable, via the very same pairwise
matrix. So "ranked ballots aren't summable" is wrong — it's **IRV's elimination
count** specifically that isn't (see the [IRV page](../RCV_IRV/RCV_IRV_lack_of_summability.md)).
More on keeping the terms straight: [`TIPS_terminology.md`](../../TIPS_terminology.md).
