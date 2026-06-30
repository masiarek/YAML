# The Math Behind Proportional STAR — Quotas, Apportionment, and Fair Division

*The "graduate seminar" companion to [STAR-PR](README_STAR_PR.md). None of this is needed
to run or advocate for proportional STAR — you mainly need the **quota** and the
**spend-a-quota / reweighting** intuition. But if you want to know **why** it's provably
fair, you walk into apportionment theory, optimization, and fair-division (cooperative game)
theory. This is a different branch of math than [Condorcet](../../RCV_Ranked_Robin/the_math_behind_condorcet.md)
— that's graph theory; this is apportionment + optimization.*

→ The method pages: [STAR-PR](README_STAR_PR.md) · [STV vs STAR-PR](../stv/proportional_stv_vs_star.md) ·
Glossary: [`Proportional STAR`](../../GLOSSARY.md) ·
**Level: Voting 301** — Curriculum [301.1](../../CURRICULUM.md) (proportional STAR),
[301.4](../../CURRICULUM.md) (limits & theory)

---

## The one mental shift: from "the favorite" to "a fair division of seats"

Single-winner asks *who is the favorite?* Proportional representation asks *how do we split
k seats so each group of voters gets seats in proportion to its size?* Every idea below is
about making "in proportion" precise and computable.

## 1. Quotas — the unit of "one seat's worth of support"

- **Hare quota** = votes ÷ seats. **Droop quota** = ⌊votes ÷ (seats + 1)⌋ + 1.
- Proportional STAR's official method, **Allocated Score** (the engine's `allocated`),
  repeatedly elects the top-scoring candidate and then **"spends" one quota** of the
  ballots that supported them most. Quota arithmetic is the beating heart — learn it first.

## 2. Apportionment / divisor methods — the deep root

The reweighting tricks in score-PR are classic apportionment in disguise:

- **Jefferson / D'Hondt** (divisors 1, 2, 3, …) ↔ **Reweighted Range Voting** (`rrv`):
  after each winner a ballot's weight becomes `1 / (1 + its already-spent support)`. That
  `1, ½, ⅓, …` *is* D'Hondt.
- **Webster / Sainte-Laguë** (divisors 1, 3, 5, …) — a "more proportional" alternative.
- **Hamilton / largest-remainder** — the quota-and-remainder approach.
- **Balinski–Young theorem** — *no* apportionment rule can satisfy quota **and** avoid all
  paradoxes (Alabama, population). The PR analogue of Arrow's impossibility.

## 3. Reweighting / vote-spending — the mechanic that makes it proportional

The whole game: when a candidate wins, the ballots that elected them must be **partly used
up**, so a majority can't sweep every seat. The three flavors the engine ships:

| Method (engine) | How it spends / deweights | The math it is |
|---|---|---|
| **Allocated Score** (`allocated`) — *Proportional STAR* | remove one **quota** of the winner's strongest ballots | quota + (fractional) surplus allocation |
| **Sequentially Spent Score** (`sss`) | each ballot has a **budget** it spends on winners | budget / flow, surplus scaling |
| **Reweighted Range Voting** (`rrv`) | **deweight** ballots by how satisfied they already are | D'Hondt divisor on scores |

The key structural fact: representation has **diminishing returns** — your 2nd and 3rd
winners "count less" (harmonic weights `1, ½, ⅓, …`). That **concavity** — a fancy word for
*diminishing returns*, where each extra unit gives less benefit than the last — is *why* the
method is proportional instead of majoritarian.

**Concretely** (3 seats; 60 voters back slate A,B,C; 40 back X,Y,Z):

- **Linear value** (no diminishing — this *is* Bloc / majoritarian): 60 > 40 for every seat,
  so the 60 sweep **all three → 3–0**, and the minority gets nothing.
- **Concave value** (diminishing, via D'Hondt divisors): the majority's strength is
  `60/1, 60/2, 60/3 = 60, 30, 20`; the minority's is `40/1, 40/2 = 40, 20`. Rank them —
  **60 → 40 → 30** — so the seats fall **majority, minority, majority = 2–1**, mirroring the
  60:40 split.

The reweighting *is* the concavity: deweighting a group's ballots after it wins a seat is
exactly what makes its *next* seat "count less," letting an unrepresented group compete.
Remove the diminishing returns and the majority sweeps everything.

## 4. What "fair" means formally — the axiomatic layer (modern, ~2015+)

- **PSC** (Proportionality for Solid Coalitions) — the classic STV-era guarantee.
- **JR → PJR → EJR** (Justified / Proportional / Extended Justified Representation) — a
  hierarchy of set-based guarantees that any large-enough cohesive group gets its share.
- **The core** (cooperative game theory) — no group can break off to a committee they'd all
  prefer in proportion to their size. The strongest notion.
- **KP-transform** (Kotze–Pereira) — converts score ballots into approval layers, bridging
  score-PR to the proportional-*approval* theory (PAV) where these guarantees are proven.

## 5. Optimization & complexity

- **Thiele methods** (maximize a concave satisfaction sum; **PAV** = harmonic weights) and
  **Phragmén methods** (minimize the maximal voter "load") — the two classical 1890s families.
- **Chamberlin–Courant** — maximize each voter's single best representative.
- Most *optimal* versions are **NP-hard** — which is exactly why the practical methods
  (`allocated`, `sss`, `rrv`) are **sequential/greedy approximations**. Greedy works here
  because the satisfaction functions are **submodular** (diminishing returns again) — a
  beautiful structural reason the cheap methods come with guarantees.

## What to learn, in order of payoff

1. **Apportionment theory** (quotas; D'Hondt / Sainte-Laguë; Balinski–Young) — directly
   explains the reweighting.
2. **Fair division / cooperative game theory** (the core, proportionality) — what
   "proportional" actually *means*.
3. **Axiomatic multiwinner social choice** (PSC, JR / PJR / EJR) — the modern guarantees.
4. **Optimization + submodularity + complexity** — why greedy methods exist and are good.
5. A little **linear algebra / probability** for the reweighting bookkeeping.

## The honest caveat

To *use or advocate* STAR-PR you need **(a) the quota** and **(b) the spend-a-quota /
deweighting intuition** — both already covered, with worked numbers, in
[the STAR-PR page](README_STAR_PR.md). The JR/EJR/core/Thiele/Phragmén machinery is the
graduate seminar: it proves *why* the method is fair, but you can run and explain
`allocated` / `sss` / `rrv` without it.

The single thing to internalize: **electing a winner "uses up" a quota of the ballots that
supported them — that one move is what turns scoring into *proportional* scoring.**

## Related

- [STAR-PR (the methods)](README_STAR_PR.md) · [STV vs STAR-PR](../stv/proportional_stv_vs_star.md) · [Proportional Representation overview](../README_proportional_representation.md)
- Parallel deep-dive for single-winner: [The Math Behind Condorcet](../../RCV_Ranked_Robin/the_math_behind_condorcet.md)
- Glossary: [`Proportional STAR`](../../GLOSSARY.md)
