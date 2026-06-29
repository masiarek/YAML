# Scoring Methods vs. Ranked Voting

*Why Approval Voting and STAR Voting are **not** forms of RCV.*

---

Ranked (ordinal) methods ask voters to **order** candidates: 1st, 2nd, 3rd, and so on. Scoring (cardinal) methods ask voters to **rate** candidates independently — so two candidates can get the same score, and the ballot captures *how much* a voter likes each one, not just the order.

Because they use a fundamentally different ballot, scoring methods sit **outside** the ranked-voting family. Lumping them under "RCV" is a common but real category error.

> **A note on the word "rating."** *Rating*, *scoring*, and *grading* all name the same thing — a **cardinal** ballot where each candidate gets an independent value (0–5 stars, A–F, etc.). The term is slippery because it sounds like *ranking* and gets used loosely, so this library treats **score** as the precise term and uses *rate/rating/grade* only as everyday synonyms — never as a kind of ranking.

| | Ballot | What it captures | Examples |
|---|---|---|---|
| **Ranked (ordinal)** | Order candidates 1, 2, 3… | Relative order only | RCV-IRV, STV, Condorcet (Ranked Robin, Schulze, Ranked Pairs), Borda, Bucklin |
| **Scored (cardinal)** | Rate/approve each candidate | Strength of support | Approval, Score, **STAR** |

## Approval Voting

Voters simply mark every candidate they approve of — no ranking, no scoring beyond yes/no. The candidate approved by the most voters wins. Because you can approve several candidates at once, similar candidates don't split each other's support, which directly attacks the spoiler problem.

## STAR Voting (Score Then Automatic Runoff)

Voters score each candidate 0–5. The two highest-scoring candidates advance to an automatic runoff, where each ballot counts for whichever finalist it scored higher. This combines the expressiveness of scoring with a final majoritarian check.

## Where scoring methods are weak (for balance)

Scoring isn't free of trade-offs, and an honest case names them. **STAR and Score fail Later-No-Harm and the Majority criterion** — a candidate a majority scores highest can still lose — which is a legitimate objection ranked-method advocates raise. Score ballots also reward **strategic min/max exaggeration** (rate everyone 0 or 5), and **Approval's** single threshold is comparatively blunt. The "equal vote / Test of Balance" argument made for STAR is **contested**, not a neutral fact, and **no method escapes Gibbard–Satterthwaite** — every system has some scenario where honesty is punished. The fair claim is about *specific* trade-offs, not overall superiority.

---

## Related concepts in this library

- [Scores vs. ranks — don't confuse ranks and ratings](scores_vs_ranks.md) — the core ballot distinction: order vs. strength
- [Is RCV "simple"? (201)](RCV_IRV/RCV_IRV_is_simple.md) — the five-star/scoring mental model vs. ranking a field of strangers
- [Tabulation, step by step](tabulation_star_vs_irv.md) — the same ballots counted as scores vs. ranks
- [RCV vs. IRV vs. RCV-IRV — A Note on Terminology](RCV_IRV/RCV-IRV-confusing-name.md)

## Learn more

- [Scoring and rankings (slide deck)](https://docs.google.com/presentation/d/11CLQr6bQUH8iSGcicYisTfNT7piINbyq0r3C0fr2qRE/edit?slide=id.g27f6bb33467_0_1#slide=id.g27f6bb33467_0_1) — expressing voter "preferences": scoring/grading/rating vs. ranking
- [STAR Voting — official site](https://www.starvoting.org/)
- [STAR Voting — RCV vs. STAR](https://www.starvoting.org/rcv_v_star)
- [Equal Vote Coalition](https://www.equal.vote/)
- [Center for Election Science — Approval Voting](https://electionscience.org/approval-voting-101/)
