# RCV-IRV (Hare) — the method US "RCV" actually means

*The single-winner instant-runoff method on the Hare elimination rule: drop the
candidate with the **fewest first choices**, transfer, repeat. When an American
ballot or statute says "Ranked Choice Voting," **this** is almost always it.*

→ Family overview: [Which RCV-IRV?](RCV_IRV_variants.md) · why the name confuses:
[RCV vs. IRV vs. RCV-IRV](RCV-IRV-confusing-name.md)

---

## In one line

Count everyone's first choices. If someone has **more than half**, they win.
Otherwise **eliminate the candidate with the fewest first choices**, hand each of
those ballots to its next still-standing choice, and repeat until a candidate holds a
majority of the **active** (non-exhausted) ballots — or only two remain.

The rule is named for **Thomas Hare** (1857). "Hare" doesn't describe the ballot; it
describes *which candidate is eliminated each round* — the fewest-first-choices one.
That single design choice is what separates Hare from every other method on this
[variants page](RCV_IRV_variants.md).

## How the count works, step by step

1. Tally each ballot's **top** choice.
2. Does any candidate have **> 50%** of the active ballots? If yes → **winner**.
3. If no, **eliminate** the candidate with the **fewest** first choices.
4. Each eliminated ballot moves to its **next ranked, still-standing** candidate. A
   ballot whose choices are all eliminated is **exhausted** and sits out the rest.
5. Go back to step 2.

> **Batch elimination** is a common shortcut: in one step, drop *every* candidate who
> is mathematically out of reach (their total plus all transferable votes below them
> can't catch the next candidate up). It usually yields the same winner as one-at-a-
> time Hare and just speeds the count; North Carolina's "instant runoff" statute is
> written this way.

## Worked example — the 27-voter center squeeze

The repo's minimal squeeze, all on ranked ballots:

```
12  Left   > Center > Right
 9  Right  > Center > Left
 6  Center > Left   > Right
```

First choices: **Left 12, Right 9, Center 6** (27 total; majority = 14).

- Nobody has 14. The fewest first choices is **Center (6)** → eliminate Center.
- Center's 6 ballots have **Left** next → Left 12 + 6 = **18**, Right 9.
- Left has 18 of 27 → **Left wins.**

But look who got cut: **Center is the Condorcet winner** — Center beats Left 15–12
*and* beats Right 18–9 head-to-head. Hare eliminated the one candidate a majority
preferred over each rival, because Center was too few voters' *first* pick. That's
[center squeeze](RCV_IRV_center_squeeze.md), and it is specific to this Hare rule —
[BTR](RCV-IRV-BTR.md), [Coombs](RCV-IRV-Coombs.md), and
[Baldwin/Nanson](RCV-IRV-Baldwin-Nanson.md) all elect Center on these very ballots.

*(Verified on the engine: `RCV_IRV_tabulation_engine` elects Left; STAR and Ranked
Robin elect Center.)*

## Strengths

- **Familiar and adopted.** It's the method actually in use — Maine, Alaska, New York
  City, San Francisco, and dozens of US cities — so "RCV" reform usually means Hare.
- **Beats plain plurality** at the spoiler problem: a trailing similar candidate is
  eliminated and transfers, instead of splitting the vote outright.
- **Later-no-harm:** ranking a lower choice can never hurt your top choice (a property
  Hare advocates prize — though it's the flip side of the squeeze).

## Weaknesses

- **Center squeeze** — eliminates a broadly-liked moderate who'd win every head-to-head.
- **Not monotonic** — *ranking a candidate higher can cause them to lose*
  ([non-monotonicity](RCV_IRV_non_monotonicity.md)).
- **Not Condorcet** — can fail to elect a candidate who beats all others pairwise.
- **Not summable** — precincts can't just add up totals; ballots must be centralized to
  run the rounds ([summability](RCV_IRV_lack_of_summability.md)).
- **Exhausted ballots** when rankings are limited ([here](RCV_IRV_exhausted_ballots.md)).

## Where it's used

US single-winner "RCV" (Maine statewide, Alaska, NYC primaries, SF, ~50 cities);
internationally it's Australia's **Alternative Vote** for the House of Representatives
and was the UK's 2011 AV referendum proposal. The multi-winner relative is
**[STV](RCV_IRV_variants.md)**.

## Related concept pages

- [Which RCV-IRV? — Hare and the other variants](RCV_IRV_variants.md)
- [RCV vs. IRV vs. RCV-IRV — the naming problem](RCV-IRV-confusing-name.md)
- [Center squeeze](RCV_IRV_center_squeeze.md) · [Non-monotonicity](RCV_IRV_non_monotonicity.md) · [Exhausted ballots](RCV_IRV_exhausted_ballots.md) · [Lack of summability](RCV_IRV_lack_of_summability.md)

Sources: [Instant-runoff voting — Wikipedia](https://en.wikipedia.org/wiki/Instant-runoff_voting),
[Where RCV is used — FairVote](https://fairvote.org/our-reforms/ranked-choice-voting-information/),
[NYC Board of Elections — RCV](https://www.vote.nyc/page/ranked-choice-voting)
