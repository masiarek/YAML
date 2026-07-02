# Topic: Summability (precinct-summable / additive counts)

**Topic hub — a cross-method view.** A method is **summable** if you can split the ballots
into precincts, tally each precinct into a small fixed-size table, and **add those tables**
to get the statewide winner — no pooling of ballots, no central recount. Summability is
what makes a method **precinct-auditable**, gives meaningful partial/early results, and
runs on existing equipment.

> **The one idea to take away:** *summability is a property of the **count**, not the
> ballot.* The same ranked ballot is summable under Ranked Robin (add the pairwise matrix)
> and **not** summable under IRV (the winner depends on the elimination order). So "ranked
> ballots can't be summed" is a myth — it's **IRV's count** specifically that can't.

## Which methods are summable — and where each is treated

| Method | Summable? | The summable artifact (what precincts publish & add) | Full page |
|--------|:---:|------------------------------------------------------|-----------|
| **STAR** | ✅ | score totals **+** the For/Equal/Against pairwise matrix | [STAR is summable](../../STAR_Voting/STAR_summability.md) |
| **Ranked Robin / Condorcet** | ✅ | the pairwise matrix (adds cell by cell) | [RR is summable](../../RCV_Ranked_Robin/RCV_RR_summability.md) |
| **Approval** | ✅ | one approval count per candidate | [scoring methods](../../scoring-methods-vs-ranked-voting.md) |
| **Plurality** | ✅ | one vote count per candidate | — |
| **RCV-IRV (Hare)** | ❌ | *none exists* — needs every ballot centrally | [IRV isn't summable](../../RCV_IRV/RCV_IRV_lack_of_summability.md) |

## See it both ways (runnable)

The same two-district example, counted two ways — [`summability_demo/`](../../../method_comparisons/summability_demo):

- **IRV (not summable):** B wins both districts, but is *eliminated* when they merge — no
  subtotal predicts it. → [worked example](../../RCV_IRV/RCV_IRV_lack_of_summability.md#worked-example--two-districts-both-won-by-b-merged-b-loses)
- **STAR (summable):** precinct score totals *and* the pairwise matrix add to the combined
  result. → [worked example](../../STAR_Voting/STAR_summability.md#worked-example--two-districts-subtotals-that-add-up)
- **Ranked Robin (summable):** the *same ranked ballots* IRV couldn't combine — the pairwise
  matrices add cell by cell and recover the winner. → [RR is summable](../../RCV_Ranked_Robin/RCV_RR_summability.md#worked-example--the-same-ballots-irv-couldnt-combine)

## Verifiable, too

Summability makes a result locally checkable; the
[`pref_voting` cross-check](../../tabulation_engines/cross_checking_with_pref_voting.md)
independently confirms the pairwise/runoff math the summable artifact depends on.

External: [Is STAR Voting Precinct Summable? (starvoting.org)](https://www.starvoting.org/summable).
Glossary: [`summability`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the
per-method folders linked above; this page just gathers the summability angle in one place
for folks browsing by topic. See [`../`](../README_topics.md) for the other topic hubs.*
