# RCV-IRV (Contingent & Supplementary Vote) — instant runoff in *one* round

*The "quick" instant runoffs: don't eliminate one candidate at a time — jump
straight to the **top two** in a single transfer. The Supplementary Vote is the same
idea with the ballot capped at two choices.*

→ Family: [Which RCV-IRV?](RCV_IRV_variants.md) · full Hare version: [RCV-IRV (Hare)](RCV-IRV-Hare.md)

---

## Contingent Vote — in one line

Tally first choices. If someone has a majority, they win. If not, **eliminate everyone
except the top two at once**, and transfer every other ballot to whichever of the two
finalists it ranks higher. Highest total wins. It's [Hare](RCV-IRV-Hare.md) collapsed
into a **single** elimination step.

## Supplementary Vote — in one line

A **Contingent Vote with only two columns**: voters mark a **first** and **second**
choice, nothing more. Same top-two-runoff logic, but a ballot that named neither
finalist simply **exhausts**. This is the form famously used for the **Mayor of London**.

## How the count works (Contingent)

1. Count first choices. Majority (> 50%)? → winner.
2. Otherwise keep the **top two**; eliminate all others **in one batch**.
3. Move each eliminated ballot to whichever finalist it ranks higher (ballots ranking
   neither are exhausted).
4. The finalist with more votes wins.

## Worked example — the same 27-voter squeeze

```
12  Left   > Center > Right
 9  Right  > Center > Left
 6  Center > Left   > Right
```

First choices: Left 12, Right 9, **Center 6.** No majority.

- **Top two = Left, Right.** Center (the bottom one) is eliminated in the single round.
- Center's 6 ballots (Center > **Left** > Right) move to **Left** → Left 18, Right 9.
- **Left wins.**

Same result as [Hare](RCV-IRV-Hare.md) — and the **same center squeeze.** With only
three candidates, Contingent Vote *is* Hare, so it inherits the flaw: Center, the
Condorcet winner, never even reaches the runoff. These one-shot methods are **not**
Condorcet-safe; the fix is [BTR](RCV-IRV-BTR.md) or [Baldwin/Nanson](RCV-IRV-Baldwin-Nanson.md).

## Strengths & weaknesses

- ✅ **Simple and fast** — one transfer, easy to hand-count and explain.
- ✅ Guarantees the winner has **broad** (top-two) support, beating plain plurality.
- ❌ **Center squeeze** survives (worse with Supplementary's 2-choice cap, which exhausts
  more ballots).
- ❌ Can eliminate a candidate who *would* have won a full Hare count, because it cuts
  everyone below 2nd place in a single step.

## Where it's used

- **Supplementary Vote:** Mayor of London and other English mayors + Police & Crime
  Commissioners — **until the Elections Act 2022**, which replaced it with
  first-past-the-post (so the 2024 London election used FPTP).
- **Contingent Vote:** the **President of Sri Lanka** (voters rank up to three);
  historically Queensland, Australia.

## Related

- [RCV-IRV (Hare)](RCV-IRV-Hare.md) — the full, multi-round version
- [Exhausted ballots](RCV_IRV_exhausted_ballots.md) — why the 2-choice cap matters
- [Center squeeze](RCV_IRV_center_squeeze.md) · [Which RCV-IRV?](RCV_IRV_variants.md)

Sources: [Supplementary vote — Wikipedia](https://en.wikipedia.org/wiki/Supplementary_vote),
[Contingent vote — Wikipedia](https://en.wikipedia.org/wiki/Contingent_vote),
[Electoral Commission — Elections Act 2022 voting changes](https://www.electoralcommission.org.uk/news-and-views/elections-act/changes-voting-system-mayoral-and-pcc-elections)
