# Topic: Condorcet Efficiency (electing the head-to-head winner)

**Topic hub — a cross-method view.** A **Condorcet winner** is a candidate who beats every
other candidate one-on-one (by majority). A method is **Condorcet-efficient** if it elects
that candidate whenever one exists. (Sometimes nobody qualifies — the pairwise results form
a **cycle** — which is a separate, rarer problem.)

> **The one idea to take away:** *the Condorcet winner is the "majority's head-to-head
> choice."* Some methods guarantee it, some get it almost always, and RCV-IRV (Hare) can
> miss it precisely because of [center squeeze](../center_squeeze/README_center_squeeze.md).

## Which methods elect the Condorcet winner — and where each is treated

| Method | Condorcet winner? | Notes | Full page |
|--------|:---:|------|-----------|
| **Ranked Robin / Copeland** | ✅ always | it *is* a Condorcet method — most pairwise wins | [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) |
| **BTR / Baldwin / Nanson** | ✅ always | Condorcet-safe IRV variants | [Which RCV-IRV?](../../RCV_IRV/RCV_IRV_variants.md) |
| **STAR** | ⚠️ very often | highly Condorcet-efficient, not guaranteed; the runoff usually recovers it | [STAR automatic runoff](../../STAR_Voting/STAR_Automatic_Runoff.md) |
| **RCV-IRV (Hare)** | ❌ not guaranteed | can eliminate the Condorcet winner before the final round | [Center squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md) |
| **Approval / Plurality** | ❌ | don't use the full pairwise picture | [scoring methods](../../scoring-methods-vs-ranked-voting.md) |

When there's **no** Condorcet winner (a cycle), methods differ in how they resolve it —
see [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md). The repo's
[divergence ledger](../../../divergence_review/INDEX.md) catalogs real library elections
where STAR, IRV, and the Condorcet winner disagree.

Glossary: [`Condorcet`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the
per-method folders linked above. See [`../`](../README_topics.md) for the other topic hubs.*
