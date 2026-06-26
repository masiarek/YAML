# RCV vs. IRV vs. RCV-IRV — A Note on Terminology

*A short explainer on why "Ranked Choice Voting" is a confusing name, and what to say instead.*

---

"Ranked Choice Voting" (RCV) is **not a single voting method** — it's an umbrella term for any system that uses ranked ballots. The family includes Instant Runoff Voting (IRV), the Single Transferable Vote (STV) for multi-winner races, Condorcet methods (Schulze, Ranked Pairs, Minimax), Ranked Robin (Consensus Voting), Borda Count, and Bucklin. These methods can produce **different winners from the very same ballots**, so treating "RCV" as one thing obscures real and consequential differences.

> **Not even ranked:** Scoring methods like Approval Voting and STAR Voting are often lumped in with "RCV" too, but they don't use ranked ballots at all — voters score or approve candidates rather than ordering them — so they sit outside the ranked-voting family entirely.
>
> → See: [Scoring Methods vs. Ranked Voting (Approval & STAR)](./scoring-methods-vs-ranked-voting.md)

The confusion is largely a **naming problem**. The same method goes by different labels across countries:

- **Ranked Choice Voting** in the US
- **Alternative Vote (AV)** in the UK
- **Preferential Voting** in Australia

In the US specifically, the advocacy group FairVote popularized "Ranked Choice Voting" as an accessible brand for IRV starting in the early 2000s, and the label stuck — in journalism, legislation, and everyday speech, "RCV" now almost always means IRV. That's a misnomer, since IRV is just one of many ranked methods.

When people say "RCV," they usually mean **IRV-Hare**: count everyone's first choices, eliminate the candidate with the fewest, redistribute those ballots to their next choice, and repeat until someone has a majority. (Other elimination rules exist — Coombs' method drops the candidate with the *most* last-place votes — which is why the fully precise label is **RCV-IRV (Hare)**.)

This sequential, plurality-style elimination is also IRV's weak point: it can squeeze out a moderate "compromise" candidate who would beat every rival head-to-head, and it doesn't fully solve the spoiler problem that other ranked methods handle better. By contrast, methods that don't rely on sequential elimination tend to handle this far better: Condorcet methods like **RCV-RR** (Ranked Robin / Consensus Voting) elect the candidate who beats every other head-to-head, and scoring methods like **STAR** and **Approval** let voters support several candidates at once, so similar candidates no longer split each other's support.

---

## TL;DR — which term to use

| If you mean… | Say… |
|---|---|
| Any ranked-ballot method (the whole family) | **Ranked voting** |
| The specific method FairVote promotes in the US | **RCV-IRV** |
| …and you need the exact elimination rule (papers, specs) | **RCV-IRV (Hare)** |
| The Condorcet round-robin alternative | **RCV-RR** (Ranked Robin) |
| Score/approve methods (not ranked at all) | **STAR**, **Approval** |

When in doubt in conversation, the safest opener is: *"Which form of ranked voting do you mean?"*

---

## Related concept pages

- [Strict vs. weak ranks](./strict_vs_weak_ranks.md) — RCV-IRV forbids equal ranks and isn't pairwise; other ranked methods differ
- [Scores vs. ranks — don't confuse ranks and ratings](./scores_vs_ranks.md)
- [Scoring methods vs. ranked voting](./scoring-methods-vs-ranked-voting.md)

## Learn more — in this library

- [Index — voting topic pages / FAQ](https://docs.google.com/document/d/1ChP00lDS4c8v30KxqZ8dC5EnqHVmQnjrbISQZBWWPVs/edit)
- [RCV-IRV — confusing name (long explanation)](https://docs.google.com/document/d/1Yr0oERKfnFAKeilclT6YUTVtOGNbfaKunbqsF5qkDf0/edit)
- [RCV IRV tabulation is confusing and lacks transparency](https://docs.google.com/document/d/18Ai1vBTudOUdJOmEIbeVw7wO8aY288DDMQtnG9YaxGs/edit)
- [Exhausted Ballots](https://docs.google.com/document/d/1ASC5BS10rCfAYZWGeCyS7dKdKc4p5wwI6DHs4F7ScGc/edit)
- [RCV is an ambiguous term that can refer to different voting methods](https://docs.google.com/document/d/1TNXnll-82mPwp_mrnFtFUlXIEP4zSjAM7ED0IwwwlFo/edit)

## Learn more — external resources

- [LWVBC: "Which form of RCV are you talking about?" — Celeste Landry](https://lwvbc.clubexpress.com/content.aspx?page_id=5&club_id=629866&item_id=63120)
- [Basic Voting Theory: "Ranked Choice Voting" (what's in a name)](https://medium.com/basic-voting-theory/ranked-choice-voting-eabe8b9139fe)
- [Common myths about Ranked Choice Voting, debunked (psephomancy)](https://medium.com/@psephomancy/common-myths-about-ranked-choice-voting-debunked-b2e54a81da1b)
- [Equal Vote — Ranked Robin](https://www.equal.vote/ranked_robin)
- [STAR Voting — RCV vs. STAR](https://www.starvoting.org/rcv_v_star)
