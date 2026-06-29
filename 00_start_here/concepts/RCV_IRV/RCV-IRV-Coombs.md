# RCV-IRV (Coombs) — eliminate the *most-hated*, not the least-loved

*A mirror image of Hare: instead of dropping the candidate with the fewest **first**
choices, Coombs drops the one with the most **last** choices each round. It tends to
protect a broadly-acceptable moderate.*

→ Family: [Which RCV-IRV?](RCV_IRV_variants.md) · the default it contrasts with: [RCV-IRV (Hare)](RCV-IRV-Hare.md)

---

## In one line

Same instant-runoff shape, opposite elimination rule. Each round, if no one has a
majority of first choices, **eliminate the candidate ranked *last* by the most
voters**, transfer those ballots, and repeat. Where [Hare](RCV-IRV-Hare.md) asks
"who has the weakest core?", Coombs asks **"who is the most widely rejected?"** — and
removes them.

## How the count works, step by step

1. Tally first choices. Majority? → winner.
2. Otherwise, count **last-place** rankings for each candidate.
3. **Eliminate the candidate with the most last-place** rankings.
4. Transfer their ballots to next choices; repeat.

Because it looks at the *bottom* of the ballot, Coombs leans toward consensus: a
polarizing candidate that many voters rank dead-last is removed early, even if they
have lots of first-place support.

## Worked example — the same 27-voter squeeze

```
12  Left   > Center > Right     (Right is last)
 9  Right  > Center > Left      (Left  is last)
 6  Center > Left   > Right     (Right is last)
```

No majority. **Last-place tally:** Right 18 (the 12 + 6), Left 9, **Center 0.**

- Most last-place is **Right (18)** → eliminate Right.
- Right's 9 ballots go to **Center** → first choices now Left 12, **Center 15.**
- Center has 15 of 27 (majority) → **Center wins.**

Same ballots as [Hare](RCV-IRV-Hare.md) (which elected Left); Coombs elects **Center**,
the Condorcet winner, because Center is *nobody's* last choice.

## Strengths & weaknesses

- ✅ **Resists center squeeze** and usually elects the Condorcet/centrist candidate.
- ❌ **Not formally Condorcet** (it can still miss in constructed cases), unlike
  [BTR](RCV-IRV-BTR.md) / [Baldwin / Nanson](RCV-IRV-Baldwin-Nanson.md).
- ❌ **Leans hard on last-place data**, so it's very sensitive to **truncated ballots**
  (voters who don't rank everyone) and to burying/strategy.
- ❌ Still not monotonic or summable in general.

## Where it's used

Essentially **academic / classroom** — named for Clyde Coombs (1964). It's the
textbook foil to Hare ("if you like the Alternative Vote, you should know about
Coombs"), rarely used in public elections, but valuable for showing that *which end of
the ballot you read* completely changes the outcome.

## Related

- [RCV-IRV (Hare)](RCV-IRV-Hare.md) — the fewest-first-choices opposite
- [BTR](RCV-IRV-BTR.md) · [Baldwin & Nanson](RCV-IRV-Baldwin-Nanson.md) — formally Condorcet
- [Center squeeze](RCV_IRV_center_squeeze.md) · [Which RCV-IRV?](RCV_IRV_variants.md)

Sources: [Coombs' method — Wikipedia](https://en.wikipedia.org/wiki/Coombs%27_method),
[If You Like the Alternative Vote… You Ought to Know about the Coombs Rule (Grofman & Feld)](https://www.researchgate.net/publication/222436249),
[Descriptions of ranked-ballot voting methods (R. LeGrand)](https://www.cs.angelo.edu/~rlegrand/rbvote/desc.html)
