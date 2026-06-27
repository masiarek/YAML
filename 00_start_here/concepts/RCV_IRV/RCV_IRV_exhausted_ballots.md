# Exhausted (Inactive) Ballots in RCV-IRV

*When a validly-cast ranked ballot stops counting before the final round — and why the "majority" IRV reports is a majority of the **ballots still active**, not of everyone who voted.*

---

In RCV-IRV, ballots are counted in rounds. In each round your ballot counts for your highest-ranked candidate who is **still in the race**. A ballot becomes **exhausted** when, at some round, it has **no remaining ranked candidate left to count for** — so from that point on it sits out the tally entirely. RCV-IRV's algorithm only ever reads a *subset* of the rankings a voter wrote down; which rankings get counted depends entirely on the order of elimination.

This isn't necessarily a spoiled or mismarked ballot. A voter can fill out their ballot perfectly and still have it exhaust.

**Same idea, many names:** inactive ballots, exhausted choices/ranks, non-transferable ballots, untransferred ballots, discarded/"wasted" ballots.

## Two distinct failures (often lumped together)

It's worth separating two things, because advocates and critics frequently blur them:

- **Exhausted / untransferable ballot.** Your top choice is eliminated, but the candidates you ranked *below* were already eliminated too — so there's nowhere left to transfer. The ballot drops out of the count entirely.
- **Nonexhausted, *untransferred* ballot.** Your top *remaining* choice reaches the deciding round and **loses** — so your lower rankings are never consulted at all. The ballot isn't technically "exhausted," yet your down-ballot preferences still did nothing.

The second case is why the popular slogan is misleading even for voters whose ballots never exhaust: *some* voters whose favorite is eliminated get their next choice counted, and others don't — and which group you land in depends on elimination order, not on how you voted.

## How exhaustion happens

- **Voluntary truncation (bullet voting).** You chose to rank only some candidates (or one). A legitimate choice — but if those are eliminated, nothing transfers.
- **Involuntary truncation (ranking limit).** Many jurisdictions cap how many candidates you may rank regardless of field size — **Minneapolis = 3, New York City = 5.** If your continuing choices fall outside the cap, the ballot exhausts even though you'd have ranked more.
- **All ranked candidates eliminated**, even on an otherwise full ballot.
- **Marking issues, under some rules.** Depending on jurisdiction, an **overvote** (two candidates at one rank), a **skipped rank**, or a **repeated rank** may either be skipped over or may exhaust the ballot — the rules vary and are themselves a source of confusion.

(See the taxonomy diagram in this folder: [`inactive_ballot_taxonomy.svg`](./inactive_ballot_taxonomy.svg).)

## Why it matters

- **The "majority" is of remaining ballots.** IRV declares a winner with a majority of **still-active** ballots in the final round — not of all ballots cast. Heavy exhaustion can leave that "majority" resting on well under half the original electorate.
- **It can be decisive.** Exhaustion changes the result whenever the **final-round margin of victory is smaller than the number of exhausted ballots** (Kilgour, Grégoire & Foley, 2019, who also find via simulation that *even small amounts of truncation can alter outcomes*, and that voluntary truncation is common and hard to explain strategically).
- **It's unevenly distributed.** Voters who rank a strong underdog first are **more likely** to exhaust or go untransferred — quietly disadvantaging exactly those voters and favoring supporters of more polarizing candidates.
- **It can hide the most-preferred candidate.** Because most rankings go unread, IRV can fail to elect a candidate who was actually preferred over all others head-to-head.

### How common is it? (real elections)

- A 2015 study (Burnett & Kogan) of four US local elections found exhaustion rates of **9.6%–27.1%**.
- **2014 Oakland mayoral:** ~24% exhausted by the final round.
- **2011 San Francisco mayoral:** ~27% of ballots ranked *neither* finalist.
- **2021 NYC City Council special elections:** ~12% exhausted on average.

A rough rule of thumb cited in the literature: in competitive RCV elections, **over 10% of ballots are commonly exhausted or spoiled** — and even a few percent can decide a close race.

## A claim to state precisely

The common advocacy line — *"if your first choice is eliminated, your vote transfers to your next choice"* — is only true if that next choice is **still in the race**, and only for voters whose favorite is eliminated *before* the final round. The accurate version: *"…transfers to your next **continuing** choice, if you have one — and not at all if your favorite survives to the final round and loses."*

## For balance — the proponent's view, fairly stated

A fair page has to give the other side, because some of this is a **design choice**, not a pure defect:

- **It can be a feature, not a bug.** RCV proponents frame each round as a simulated runoff where you have one active vote at a time. Not counting your 3rd choice *while your 1st is still winning* is exactly **Later-No-Harm** — it ensures your lower preferences can't hurt your favorite. (The catch: monotonicity failures show this guarantee isn't absolute.)
- **FPTP wastes more.** Under plain Choose-One, *every* vote for a losing candidate is effectively discarded immediately. RCV generally captures **more** voter intent than the status quo, even though it doesn't capture all of it. Implying the current system is better *in this specific respect* would be unfair.
- **Some truncation is the voter's own choice.** Voluntary bullet-voting isn't something done *to* a voter, and removing **ranking-limit caps** mitigates the involuntary kind.

Scored methods sidestep exhaustion by design — a blank on a STAR/Score ballot is read as **0**, so a ballot never drops out of the count — which is why a STAR "no-preference" between the two finalists is still *counted* and can still help advance the more-preferred candidate. But that's a different trade-off, not a free lunch: a 0 is itself a meaningful (lowest) score, not a neutral abstention. (See [scores_vs_ranks.md](../scores_vs_ranks.md).)

---

## Related concept pages

- [Is IRV "just plurality"?](RCV_IRV_and_plurality.md) — round-by-round elimination is what creates exhaustion
- [Strict vs. weak ranks](../strict_vs_weak_ranks.md) — ranking limits and forbidden equal ranks feed exhaustion
- [Center squeeze](RCV_IRV_center_squeeze.md) — the related way IRV discards a broadly-liked candidate
- [Monotonicity](./RCV_IRV_non_monotonicity.md) — why "your lower choices can't hurt you" isn't an absolute guarantee
- [Tabulation, step by step](../tabulation_star_vs_irv.md)

## Learn more — in this library

- [Exhausted Ballots — main](https://docs.google.com/document/d/1ASC5BS10rCfAYZWGeCyS7dKdKc4p5wwI6DHs4F7ScGc/edit)
- [Exhausted Ballots (slide deck) — RCV exhaustion vs. STAR "no-preference"](https://docs.google.com/presentation/d/1ipof9WSSy0GenVKWfKLu_jlYwUIT0TU0WVSAap0VZ5Q/edit)
- [Commentary — exhausted ballots (Electowiki, with proponent/critic framing)](https://docs.google.com/document/d/1-iim_UdVhbZpuIGzo4idBr3glCW6pRGB_AUWu5-mdUs/edit)
- [Exhausted Ballot — definitions](https://docs.google.com/document/d/1cZa8RdDeTZF25tfQ3zvLN8QQGhctNUAM-Hnr82ePxWg/edit)
- [Ballot truncation — prevalence and consequences (Kilgour, Grégoire & Foley, 2019)](https://docs.google.com/document/d/1NLudb3YSlupSFvGT12NHHLrq0y8vmlK-AwAJ_gM2poU/edit)
- [Involuntary ballot truncation](https://docs.google.com/document/d/1umfB-BgeIRjzbCZ_H212FiUIbpv1_iIv3NnC1SE-7Y4/edit)

## Learn more — external

- [STAR Voting — Wasted Votes](https://www.starvoting.org/wasted_votes)
