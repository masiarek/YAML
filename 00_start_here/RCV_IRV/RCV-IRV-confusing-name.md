# RCV vs. IRV vs. RCV-IRV — A Note on Terminology

*A short explainer on why "Ranked Choice Voting" is a confusing name, and what to say instead.*

---

"Ranked Choice Voting" (RCV) is **not a single voting method** — it's an umbrella term for any system that uses ranked ballots. The family includes Instant Runoff Voting (IRV), the Single Transferable Vote (STV) for multi-winner races, Condorcet methods (Schulze, Ranked Pairs, Minimax), Ranked Robin (Consensus Voting), Borda Count, and Bucklin. These methods can produce **different winners from the very same ballots**, so treating "RCV" as one thing obscures real and consequential differences.

> **Not even ranked:** Scoring methods like Approval Voting and STAR Voting are often lumped in with "RCV" too, but they don't use ranked ballots at all — voters score or approve candidates rather than ordering them — so they sit outside the ranked-voting family entirely.
>
> → See: [Scoring Methods vs. Ranked Voting (Approval & STAR)](../scoring-methods-vs-ranked-voting.md)

The confusion is largely a **naming problem**. The same method goes by different labels across countries:

- **Ranked Choice Voting** in the US
- **Alternative Vote (AV)** in the UK
- **Preferential Voting** in Australia

> **"Preferential Voting" is itself a misnomer.** *Every* voting method lets voters express preferences — approval, score, and STAR included — so the name claims a broad, general word for one specific method. Worse, in the everyday sense a "preference" includes *strength of feeling*, which a **score** captures but a strict **rank** discards — so the label attaches the wider concept to the narrower mechanism. See [`preference.md`](../preference.md).

In the US specifically, the advocacy group FairVote popularized "Ranked Choice Voting" as an accessible brand for IRV starting in the early 2000s, and the label stuck — in journalism, legislation, and everyday speech, "RCV" now almost always means IRV. That's a misnomer, since IRV is just one of many ranked methods.

When people say "RCV," they usually mean **IRV-Hare**: count everyone's first choices, eliminate the candidate with the fewest, redistribute those ballots to their next choice, and repeat until someone has a majority. (Other elimination rules exist — Coombs' method drops the candidate with the *most* last-place votes — which is why the fully precise label is **RCV-IRV (Hare)**.)

This sequential, plurality-style elimination is also IRV's weak point: it can squeeze out a moderate "compromise" candidate who would beat every rival head-to-head, and it doesn't fully solve the spoiler problem that other ranked methods handle better. By contrast, methods that don't rely on sequential elimination tend to handle this far better: Condorcet methods like **RCV-RR** (Ranked Robin / Consensus Voting) elect the candidate who beats every other head-to-head, and scoring methods like **STAR** and **Approval** let voters support several candidates at once, so similar candidates no longer split each other's support.

---

## Why "Hare," and what the alternatives would do

The method FairVote promotes for a single seat is **Instant-Runoff Voting under the Hare elimination rule**. The count is a series of automatic runoffs: tally first choices; if someone holds more than half, they win; otherwise **eliminate the candidate with the fewest first choices**, transfer each of those ballots to its next still-standing choice, and repeat until a candidate has a majority of the remaining active ballots (or only two remain).

The word **"Hare"** (after Thomas Hare) is not decoration — it names *which* candidate is dropped each round, and that single choice is exactly where the ranked methods part ways on the very same ballots:

| Elimination / counting rule | What it does each round | Same ballots, different winner? |
|---|---|---|
| **Hare (IRV)** — what US "RCV" means | drops the candidate with the **fewest first-place** votes | — |
| **Coombs** | drops the candidate with the **most last-place** votes | yes |
| **Borda** | eliminates no one — each rank scores points (e.g. 2-1-0), highest total wins | yes |
| **Bucklin** | eliminates no one — adds 2nd, then 3rd choices until someone crosses a majority | yes |

All four read an identical ranked ballot and can crown different winners. So **RCV-IRV** fixes the *family* (ranked ballots counted by sequential runoff), but only **RCV-IRV (Hare)** fixes the *exact* elimination rule — which is why statutes, election specs, and academic papers reach for the longer name. (Borda and Bucklin are ranked but **not** Condorcet, and none of these is the pairwise **RCV-RR**.)

> **There's more than one "IRV," too.** Beyond Hare, the instant-runoff *shape* also covers batch elimination, the contingent / supplementary vote, Condorcet-safe variants (BTR, Baldwin, Nanson), plus implementation knobs (how many candidates you may rank, how "majority" is counted) that change the winner on the same ballots. For the full catalog and when the precision matters, see [Which RCV-IRV? — Hare and the other variants](RCV_IRV_variants.md).

## Multi-winner: the same Hare family, renamed STV

FairVote's multi-winner reform is the **Single Transferable Vote (STV)** — the proportional relative in the same Hare lineage, used to fill several seats at once (e.g. a city council elected at large). STV keeps the ranked ballot and the transfer idea but swaps "win a majority" for "reach a **quota**" — the Droop quota, `⌊total ÷ (seats + 1)⌋ + 1`. A candidate who meets the quota is elected, and the **surplus** above it transfers to next choices; candidates in last place are eliminated and their ballots transfer; this repeats until every seat is filled. Run STV with a single seat and it collapses back to IRV-Hare — which is why the two are siblings rather than separate inventions, and why "RCV" in the US covers *both*: **RCV-IRV (Hare)** for one winner, **STV** for many.

---

## TL;DR — which term to use

| If you mean… | Say… |
|---|---|
| Any ranked-ballot method (the whole family) | **Ranked voting** |
| The method FairVote promotes in the US (single-winner) | **RCV-IRV** |
| …its exact elimination rule, for papers & specs | **[RCV-IRV (Hare)](RCV-IRV-Hare.md)** — eliminate fewest-first-choices, transfer, repeat |
| The Condorcet round-robin alternative | **RCV-RR** (Ranked Robin) |
| Score/approve methods (not ranked at all) | **STAR**, **Approval** |

When in doubt in conversation, the safest opener is: *"Which form of ranked voting do you mean?"*

---

## Related concept pages

- [Which RCV-IRV? — Hare and the other variants](RCV_IRV_variants.md) — batch / contingent / BTR / Coombs / Baldwin / Nanson, STV, and the ballot-rule knobs
- [Strict vs. weak ranks](../scores_and_ranks/strict_vs_weak_ranks.md) — RCV-IRV forbids equal ranks and isn't pairwise; other ranked methods differ
- [Scores vs. ranks — don't confuse ranks and ratings](../scores_and_ranks/scores_vs_ranks.md)
- [Scoring methods vs. ranked voting](../scoring-methods-vs-ranked-voting.md)

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
