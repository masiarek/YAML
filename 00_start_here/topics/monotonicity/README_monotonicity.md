# Topic: Monotonicity (more support shouldn't hurt you)

**Topic hub — a cross-method view.** A method is **monotonic** if ranking or scoring the
eventual winner *higher* can never cause them to **lose** (and moving a loser *down* can
never make them win). It's the property that makes "vote your honest favorite first" safe.

> **The one idea to take away:** *non-monotonicity comes from sequential **elimination**,
> not from ranked ballots.* RCV-IRV (Hare) — and the other eliminate-and-transfer variants —
> can punish a candidate for gaining support, because added first-choices change *who is
> eliminated when*. Methods that read the whole ballot at once (Ranked Robin, STAR) don't
> have this hole.

## Which methods are monotonic — and where each is treated

| Method | Monotonic? | Why | Full page |
|--------|:---:|-----|-----------|
| **STAR** | ✅ | scores are added, not eliminated — raising a candidate only helps them | [STAR monotonicity](../../STAR_Voting/STAR_monotonicity.md) |
| **Ranked Robin / Condorcet** | ✅ | pairwise wins only improve when you rank someone higher | [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) |
| **Approval / Score** | ✅ | more approval/points can't hurt | [scoring methods](../../scoring-methods-vs-ranked-voting.md) |
| **RCV-IRV (Hare)** | ❌ | added first-choices can change the elimination order and flip the winner | [IRV non-monotonicity](../../RCV_IRV/RCV_IRV_non_monotonicity.md) |
| **Other IRV variants** (BTR, Coombs, Baldwin, Nanson) | ❌ | same cause — they still eliminate round by round | [Which RCV-IRV?](../../RCV_IRV/RCV_IRV_variants.md) |

So unlike [center squeeze](../center_squeeze/README_center_squeeze.md) (which is *Hare-specific*),
non-monotonicity is shared by **all** the sequential-elimination methods — only the
non-eliminating methods (STAR, Ranked Robin) escape it.

Glossary: [`monotonicity`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the
per-method folders linked above. See [`../`](../README_topics.md) for the other topic hubs.*
