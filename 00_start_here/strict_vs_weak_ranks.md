# Strict vs. Weak Ranks — Not All Ranked Ballots Are the Same

*Many ranked methods let you mark two candidates **equal**. RCV-IRV (Hare) does **not** — and it never compares candidates head-to-head. Most people assume otherwise.*

---

"Ranked voting" is not one ballot rule. Ranked ballots differ along two independent axes, and the differences change both what you can say and who wins:

- **Strict vs. weak.** A **strict** ranking forbids ties — every candidate must get a distinct place (1, 2, 3…). A **weak** ranking allows **equal ranks** — you can say "I like these two the same." (Formally: a weak order / "order with ties.")
- **Complete vs. incomplete.** A **complete** ballot ranks everyone; an **incomplete** (truncated) ballot ranks only some. Whether you may *skip* a rank, and what happens if you do, is a per-method rule.

The standard data taxonomy (PrefLib) names the four combinations: **SOC/SOI** (strict, complete/incomplete) and **TOC/TOI** (ties allowed, complete/incomplete).

## The key point about RCV-IRV (Hare)

> **RCV-IRV uses *strict* ranks and is *not* pairwise.** You **cannot** give two candidates the same rank. And IRV never does head-to-head comparisons — each round it looks only at every ballot's *current top choice*, eliminates the candidate with the fewest first-place votes, and ignores all the down-ballot detail until a ballot's higher choice is eliminated. That's a plurality-style elimination rule, not a comparison of candidates against each other.

This matters because two of the things people most often *assume* RCV does — let me mark ties, and compare everyone head-to-head — are exactly what RCV-IRV does **not** do. Those belong to *other* ranked methods.

## Which ranked methods allow equal ranks? Which are pairwise?

| Method | Equal ranks? | How it counts | Pairwise (head-to-head)? |
|---|---|---|---|
| **RCV-IRV (Hare)** | ❌ No — strict | Sequential elimination of fewest first-choices | ❌ No |
| **STV** (multi-winner IRV) | ❌ No — strict | Quota + transfers, round by round | ❌ No |
| **Ranked Robin / Condorcet** (Schulze, Ranked Pairs, Minimax) | ✅ Yes — weak allowed | Every pair compared; most head-to-head wins | ✅ **Yes** |
| **Borda count** | ✅ Usually (ties shareable) | Positional points from rank | ❌ No (positional) |
| **Bucklin** | ✅ Often | Adds in lower ranks until a majority | ❌ No |
| **Scored** (STAR, Score, Approval) | ✅ Inherently (not a ranking) | Add scores; STAR adds an automatic runoff | STAR's runoff is one pairwise step |

The headline: **allowing equal ranks and using pairwise comparisons are features of *other* ranked methods — not of the RCV-IRV that's actually on US ballots.**

## False assumptions people make about RCV ballots

- *"I can rank two candidates equally."* — Not in RCV-IRV. Equal ranks are an **overvote** and can spoil that rank. (Ranked Robin and other Condorcet methods *do* allow it.)
- *"All my rankings get counted."* — No. IRV only ever counts your highest *continuing* choice; lower rankings are ignored unless and until higher ones are eliminated, and a ballot can be **exhausted** with no remaining choice counted.
- *"RCV compares the candidates head-to-head."* — No. That's **Condorcet** (e.g., Ranked Robin). IRV only counts top-choice tallies each round.
- *"I can skip ranks freely."* — Risky. Skipped or repeated rankings are handled differently by jurisdiction and can exhaust the ballot.
- *"Ranked = good, so all ranked methods behave alike."* — They don't. A weak-ranked Condorcet method reliably finds the candidate closest to the center of opinion; strict-rank IRV can eliminate that very candidate ([center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md)).

## Why equal ranks (weak ranking) matter

Forcing a **strict** order makes voters invent distinctions they don't feel — "is she my 4th or my 5th?" — and **studies suggest** this adds noise and may raise ballot-spoilage rates (the evidence is real but contested). Allowing **equal ranks** lets a voter honestly express indifference, and it adds real expressive power: on a strict ballot a second choice "could be as good as your favorite or almost as bad as your last choice," and the ballot can't tell the difference. In reform-advocate **simulations (e.g., voter-satisfaction-efficiency work)**, good weak-ranked Condorcet methods tend to perform on par with good score methods, while strict-rank IRV lags — a finding worth citing as such, not as settled fact.

(Scores go one step further: they carry order *and* strength. See [`scores_vs_ranks.md`](scores_vs_ranks.md).)

---

## Related concepts in this library

- [Scores vs. ranks — don't confuse ranks and ratings](scores_vs_ranks.md)
- [Scoring methods vs. ranked voting](scoring-methods-vs-ranked-voting.md)
- [RCV vs. IRV vs. RCV-IRV — terminology](RCV_IRV/RCV-IRV-confusing-name.md)
- [Ranked Robin (Consensus Voting)](RCV_Ranked_Robin/ranked_robin.md) — the Condorcet method that *does* allow equal ranks and compares pairwise
- [Is IRV "just plurality"?](RCV_IRV/RCV_IRV_and_plurality.md) — why elimination is a first-choice plurality test (and where that claim overreaches)
- [Center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) — what strict-rank IRV does to a strong compromise candidate
- [Is RCV "simple"? (201)](RCV_IRV/RCV_IRV_is_simple.md)

## Learn more

- [Rankings — transitive / complete-incomplete / strict-weak relations](https://docs.google.com/document/d/1541sZRC9Dyuuo13cTuzgB7j5gdc9-e9xcIwobR44Uj0/edit?tab=t.0)
- [Preference concept (what "preference" really means)](https://docs.google.com/document/d/12BOSgcZ2sF2VOC7_hCPKM7TWgE2Rrt_RW6KlE6wkxi8/edit?tab=t.0)
- [Expressiveness — scoring is more expressive than ranking](https://docs.google.com/document/d/1MkcT-4QblDAu5Y3PSNngZJwejVX1XLMgTw_fyASrDmM/edit?tab=t.0)
- [Expressive vs. inexpressive voting methods ("being heard")](https://docs.google.com/document/d/1Ms3mwwKVfCKhopteIKYg857ck0qgy1-5GelKd9Re7UE/edit?tab=t.0)
- [PrefLib data types (SOC / SOI / TOC / TOI)](https://www.preflib.org/format#toi)
