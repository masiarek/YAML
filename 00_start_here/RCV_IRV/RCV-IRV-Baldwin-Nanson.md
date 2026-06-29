# RCV-IRV (Baldwin & Nanson) — Borda-elimination hybrids

*Two instant-runoff variants that eliminate by **Borda score** instead of first
choices. Both are **Condorcet-consistent** — they always elect the head-to-head
winner — and both come from the same E. J. Nanson who described center squeeze in 1882.*

→ Family: [Which RCV-IRV?](RCV_IRV_variants.md) · the default they fix: [RCV-IRV (Hare)](RCV-IRV-Hare.md)

---

## First, the Borda score

Give each ballot position points — with N candidates, a 1st choice = N−1, 2nd = N−2, …,
last = 0 — and add them up. A candidate's **Borda score** rewards being ranked *high by
many*, not just first by a few. Baldwin and Nanson both use this score to decide who to
eliminate, then **recompute it** on the smaller field each round.

## Baldwin — drop the lowest Borda score

1. Compute every candidate's Borda score.
2. **Eliminate the single candidate with the lowest** score.
3. Recompute Borda among those remaining; repeat until one is left.

## Nanson — drop everyone below average

1. Compute Borda scores and their **average**.
2. **Eliminate every candidate at or below the average** Borda score (can remove
   several at once).
3. Recompute among the survivors; repeat.

Both are **Condorcet methods**: a candidate who beats everyone head-to-head always has
an above-average Borda score and the highest of any pair, so they're never eliminated.

## Worked example — the same 27-voter squeeze

```
12  Left   > Center > Right
 9  Right  > Center > Left
 6  Center > Left   > Right
```

Borda (3 candidates → 1st = 2, 2nd = 1, 3rd = 0):

- **Left:** 12·2 + 6·1 + 9·0 = **30**
- **Center:** 6·2 + 12·1 + 9·1 = **33**
- **Right:** 9·2 + 0 + 0 = **18**

**Baldwin:** lowest is **Right (18)** → eliminate. Recompute on {Left, Center}: Center is
preferred 15–12, so Left has the lower score → eliminate Left → **Center wins.**

**Nanson:** average = (30+33+18)/3 = **27**. At or below 27 → **Right (18)** only;
eliminate it. Recompute on {Left, Center}: scores 12 vs 15, average 13.5, Left ≤ 13.5 →
eliminate Left → **Center wins.**

Same ballots as [Hare](RCV-IRV-Hare.md) (Left); both Borda-elimination methods elect
**Center**, the Condorcet winner — no center squeeze.

## Strengths & weaknesses

- ✅ **Condorcet-consistent** — always elect the head-to-head winner.
- ✅ Use the **whole ballot** (every rank contributes), so no center squeeze.
- ❌ **Not monotonic** (Baldwin), and Borda components are **vulnerable to strategy**
  (burying, clones) and to truncated ballots.
- ❌ **Not summable**; more arithmetic than Hare, which hurts explainability/adoption.

## Where it's used

Mostly **academic and organizational** elections (some societies use Nanson). Their
real value here is conceptual: they show that bolting a Condorcet-friendly score onto
instant-runoff elimination removes the squeeze — the same insight behind
[BTR](RCV-IRV-BTR.md).

> **History rhymes.** **Nanson** laid this out in *Methods of Election* (1882), the same
> paper quoted on the [center squeeze page](RCV_IRV_center_squeeze.md) warning that
> Hare ("Ware's method") "may return the next worst." He didn't just diagnose the
> flaw — he designed a cure.

## Related

- [RCV-IRV (Hare)](RCV-IRV-Hare.md) · [BTR](RCV-IRV-BTR.md) · [Coombs](RCV-IRV-Coombs.md) · [Contingent & Supplementary](RCV-IRV-contingent-supplementary.md)
- [Center squeeze](RCV_IRV_center_squeeze.md) · [Which RCV-IRV?](RCV_IRV_variants.md)

Sources: [Nanson's method — Wikipedia](https://en.wikipedia.org/wiki/Nanson%27s_method),
[Borda count — Wikipedia](https://en.wikipedia.org/wiki/Borda_count),
[Descriptions of ranked-ballot voting methods (R. LeGrand)](https://www.cs.angelo.edu/~rlegrand/rbvote/desc.html)
