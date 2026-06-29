# RCV-IRV (BTR) — Bottom-Two-Runoff

*An instant-runoff variant that fixes center squeeze: each round, the **two lowest**
candidates meet head-to-head and the **loser** is eliminated. Because a Condorcet
winner beats everyone, BTR can never eliminate them.*

→ Family: [Which RCV-IRV?](RCV_IRV_variants.md) · the default it fixes: [RCV-IRV (Hare)](RCV-IRV-Hare.md)

---

## In one line

Like [Hare](RCV-IRV-Hare.md), BTR eliminates one candidate per round and transfers
ballots — but instead of cutting whoever has the fewest first choices, it takes the
**two candidates with the fewest** and **eliminates the one who loses their direct
head-to-head**. This one change makes it **Condorcet-efficient**: it always elects the
candidate who beats every other one-on-one, when such a candidate exists.

## How the count works, step by step

1. Tally first choices (with transfers from any prior rounds).
2. Find the **two candidates with the fewest** votes.
3. Compare *those two* **head-to-head** across all ballots; **eliminate the loser**.
4. Transfer the loser's ballots to next choices; repeat from step 1 until one remains.

The intuition: Hare can eliminate a strong candidate just because few people rank them
*first*. BTR only ever eliminates a candidate who **loses a head-to-head** — and the
Condorcet winner loses none, so they survive to the end.

## Worked example — the same 27-voter squeeze

```
12  Left   > Center > Right
 9  Right  > Center > Left
 6  Center > Left   > Right
```

First choices: Left 12, Right 9, **Center 6**.

- **Two lowest:** Center (6) and Right (9). Head-to-head **Center vs Right**: Center is
  ranked above Right on 18 ballots, Right above Center on 9 → **Center wins, Right is
  eliminated.** (Hare would have cut Center here instead.)
- Right's 9 ballots go to **Center** → Center 15, Left 12.
- Final pair **Center vs Left**: Center 15, Left 12 → **Center wins.**

Same ballots as the [Hare page](RCV-IRV-Hare.md), opposite result: BTR elects **Center**,
the Condorcet winner. No center squeeze.

## Strengths & weaknesses

- ✅ **Condorcet-efficient** — elects the head-to-head winner; **no center squeeze**.
- ✅ Keeps the familiar round-by-round runoff "feel" of RCV.
- ❌ Still **not monotonic** in general, and still **not summable** (you need the full
  ballots to run the head-to-heads).
- ❌ Slightly more to explain than Hare ("why those two?"), which matters for adoption.

## Where it's used

Mostly a **reform proposal** rather than current law — introduced by Rob LeGrand
(2006) as "BTR-STV," and a frequent suggestion for making RCV Condorcet-compliant with
minimal change to how it already works. Compare with the no-elimination Condorcet
method, **[Ranked Robin (RCV-RR)](../RCV_Ranked_Robin/ranked_robin.md)**.

## Related

- [RCV-IRV (Hare)](RCV-IRV-Hare.md) · [Coombs](RCV-IRV-Coombs.md) · [Baldwin & Nanson](RCV-IRV-Baldwin-Nanson.md) · [Contingent & Supplementary](RCV-IRV-contingent-supplementary.md)
- [Center squeeze](RCV_IRV_center_squeeze.md) — the flaw BTR removes
- [Which RCV-IRV?](RCV_IRV_variants.md)

Sources: [Instant-runoff voting — Wikipedia](https://en.wikipedia.org/wiki/Instant-runoff_voting),
[Descriptions of ranked-ballot voting methods (R. LeGrand, Angelo State)](https://www.cs.angelo.edu/~rlegrand/rbvote/desc.html),
[Condorcet method — electowiki](https://electowiki.org/wiki/Condorcet_method)
