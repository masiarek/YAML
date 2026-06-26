# Scores vs. Ranks — Don't Confuse Ranks and Ratings

*The single most important distinction in ballot design — and the one people get wrong most often.*

---

There are two fundamentally different ways a ballot can ask for your opinion, and they are **not** interchangeable:

- **Ranking** (ordinal): put the candidates in **order** — 1st, 2nd, 3rd. This captures *relative* preference: "I like A more than B." It says nothing about **how much**.
- **Rating / Scoring** (cardinal): give each candidate an **independent value** — 0–5 stars, A–F. This captures *absolute* preference: "I like A **this much**." It carries both the order **and** the strength.

A rank answers *"which do you prefer?"* A score answers *"how much do you like each one?"* Those are different questions, and a ballot that asks one cannot be silently treated as if it asked the other.

> **The naming trap.** *Rank* and *rate* sound almost identical and get swapped constantly — but they are opposites in what they measure. This library uses **rank** only for ordering and **score** (synonyms: rate, grade) only for independent values. If you remember one thing: **equal rankings are still rankings; a score is not a ranking.**

## Relative vs. absolute preference

| | **Ranks** (ordinal) | **Scores** (cardinal) |
|---|---|---|
| The question | "Which do you prefer?" | "How much do you like each?" |
| Captures | Order only | Order **+ strength** |
| Utility type | Ordinal utility | Cardinal utility (interval scale) |
| Differences meaningful? | No — 1st vs. 2nd ≠ 2nd vs. 3rd | Yes — a 5 vs. a 3 is a real gap |
| Familiar from | A race: 1st, 2nd, 3rd | Amazon / movie **five-star** reviews |
| Methods | RCV-IRV, STV, Condorcet (Ranked Robin), Borda | STAR, Score, Approval (0/1) |

Because differences are meaningful only for scores, you can **average** scores (a column sum) but it makes no sense to "average" ranks. This is exactly why STAR is summable and IRV is not. (See [`summability.md`](STAR_Voting/summability.md) and [`tabulation_star_vs_irv.md`](./tabulation_star_vs_irv.md).)

## Why "ranked" is about the *data*, not just the ballot

A common point of confusion: **Ranked Robin allows equal rankings, so why isn't it a scoring method?** Because the method only ever reads the *order* (who beats whom), never a magnitude. Allowing ties in a ranking doesn't turn order into strength. The line between ranked and scored is **what information the tabulation uses** — pure order (ranked) vs. degree of support (scored) — not merely how the bubbles look.

## Why the distinction has real consequences

**Different winners from identical voters.** A candidate who wins under a ranked method can lose under a scored method on the very same electorate, because the two are measuring different things. Treating "ranked = scored" hides that.

**Expressiveness.** A rank carries order only; a score carries order *and* how strongly you feel. A broadly-liked compromise candidate can look weak on first-choice ranks yet clearly strong on scores — which is part of why IRV suffers [center squeeze](RCV_IRV/center_squeeze.md) and STAR doesn't.

**You can go one way but not the other.** Scores → ranks is easy (just read off the order). Ranks → scores is **impossible** without inventing information, because the strength was never collected.

**Ballot reliability.** Independent scoring removes the "grid" constraints of ranking (no overvotes, no skipped-rank traps, ties allowed, blanks = 0). Reported spoilage rates run roughly **0–2% for rated ballots vs. 4–9% for ranked ballots** (and 1–4% for single-mark). And research on values measurement (Maio, Roese, Seligman & Katz) found **ratings showed superior validity to rankings**, because forcing a full strict order captures noise — distinctions voters don't actually feel.

---

## Related concepts in this library

- [Strict vs. weak ranks](./strict_vs_weak_ranks.md) — equal ranks & pairwise comparison: which ranked methods allow them (IRV doesn't)
- [Scoring methods vs. ranked voting](./scoring-methods-vs-ranked-voting.md) — why Approval & STAR sit *outside* the RCV family
- [Is RCV "simple"? (201)](RCV_IRV/is_rcv_simple.md) — the five-star mental model vs. ordering strangers
- [Tabulation, step by step](./tabulation_star_vs_irv.md) — the same ballots counted as scores vs. ranks
- [Center squeeze](RCV_IRV/center_squeeze.md) — how order-only ballots can bury a strong compromise candidate
- [RCV vs. IRV vs. RCV-IRV — terminology](./RCV_IRV/RCV-IRV-confusing-name.md)

## Learn more

- [Scoring and rankings (slide deck)](https://docs.google.com/presentation/d/11CLQr6bQUH8iSGcicYisTfNT7piINbyq0r3C0fr2qRE/edit?slide=id.g2ed1db947c0_0_95#slide=id.g2ed1db947c0_0_95)
- [Relative preference vs. absolute preference](https://docs.google.com/document/d/1_hIt2CEk4fB4wy4Eu0Nn4R5NW_EFjj725IiSS42ev2k/edit?tab=t.0)
- [Ratings, rankings and preferences — main](https://docs.google.com/document/d/1ImJsgGzxkcdWwAJjDZEaWbgTRi4sPiDFSEP2OkfOhgI/edit?tab=t.0)
- [Compare ballots — STAR Voting and RCV](https://docs.google.com/document/d/1xMXONflRF8x1TOQxdTZpdYPlT8rXZ-h695PHnnBduhM/edit?tab=t.0)
- [Cardinal utility and ordinal utility (the math)](https://docs.google.com/document/d/1poWz45UuPwlaoPTe4nE-_tz2QCn0NiXlYpvoK4G6qWQ/edit?tab=t.0)
- [Maio et al. — "Rankings, Ratings, and the Measurement of Values: Evidence for the Superior Validity of Ratings"](https://www.researchgate.net/publication/233061022_Rankings_Ratings_and_the_Measurement_of_Values_Evidence_for_the_Superior_Validity_of_Ratings)
