# Center Squeeze

**One line:** a broadly-liked moderate is eliminated *early* because few voters
rank/score them **first**, so a more polarizing candidate the majority actually
opposed goes on to win. It's an **[RCV-IRV (Hare)](RCV-IRV-Hare.md)** failure — a
property of the *eliminate-the-fewest-first-choices* rule specifically, not of ranked
ballots in general (and not of every instant-runoff variant); STAR avoids it.

→ Glossary: [`center squeeze`](../GLOSSARY.md) · deeper debate version:
[`favorite_betrayal_voting_301.md`](../../interviews_conversations/favorite_betrayal_voting_301.md)

---

## Why it happens — and how you know it's *Hare*

IRV only ever looks at each ballot's **top remaining** choice, and each round it
**eliminates the candidate with the fewest first choices** — *that* elimination rule
is what "**Hare**" names. A moderate who is almost everyone's strong **second** choice
— but few people's first — has the fewest first-place votes, so the Hare rule drops
them before their broad support is ever counted. The two wings survive; the consensus
candidate doesn't.

**So when a page says "center squeeze," assume Hare.** It's a property of the
fewest-first-choices elimination rule — the one US "RCV" uses — and it is **not** a
property of ranked ballots in general, nor even of every instant-runoff variant:

- **[Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md)** (a Condorcet count of the
  *same* ballot) doesn't eliminate at all, so it has **no** center squeeze.
- The **Condorcet-safe IRV variants** — **BTR-IRV, Baldwin, Nanson** — keep the
  instant-runoff *shape* but stop eliminating on first-choices alone, so a Condorcet
  winner can never be squeezed out. Fittingly, **Nanson** — quoted at the bottom of
  this page warning about exactly this flaw in **1882** — designed one of those fixes.

So the precise statement isn't "RCV has center squeeze," or even "IRV" — it's
**RCV-IRV (Hare)**. For the full family, see
[Which RCV-IRV? — Hare and the other variants](RCV_IRV_variants.md) and
[`TIPS_terminology.md`](../TIPS_terminology.md).

## Minimal test case — run it

The smallest clean squeeze, as a matched pair (27 voters, Left / Center / Right):

→ [`center_squeeze_irv.yaml`](../../method_comparisons/center_squeeze/center_squeeze_irv.yaml)
 · [`center_squeeze_star.yaml`](../../method_comparisons/center_squeeze/center_squeeze_star.yaml)

Center is the **Condorcet winner** (beats Left 15–12, Right 18–9) but has the
**fewest first-choices (6)**. The STAR file's output shows all four methods on the
same ballots:

```
Choose-One (Plurality) = Left     RCV-IRV = Left     Approval = Left
STAR = Center   ( = Condorcet winner — also what Ranked Robin would elect )
```

IRV eliminates Center in round 1; STAR advances Center on strength of support and
wins the runoff. (Verified on the engine.) A richer themed version is the Star Wars
vote-split demo, [`04_star_wars_vote_split.yaml`](../../method_comparisons/split_voting/_main/04_star_wars_vote_split.yaml).

## A visual example — the voteline 1-D spectrum

The squeeze is easiest to *see* on a left–right spectrum. In the classic
**voteline** demo ([zesty.ca/voting/voteline](http://zesty.ca/voting/voteline/);
walkthrough in this video, [youtu.be/7btAd1HYvjU?t=1782](https://youtu.be/7btAd1HYvjU?t=1782)),
three candidates sit on a line — **Red** (left), **Green** (center), **Yellow**
(right) — and voters are spread across it. Slide the voters around and you can watch
IRV *cross a threshold* into the squeeze. Here is the configuration where it bites:

```
red > green > yellow : 33.2%      green > yellow > red : 17.5%
green > red > yellow : 13.8%      yellow > green > red : 35.3%
```

**First choices:** Yellow 35.3%, Red 33.2%, **Green 31.3% (fewest).** So:

- **RCV-IRV** eliminates **Green** first (the center!), its ballots split to the two
  wings, and **Yellow wins 52.9%.**
- But **Green is the Condorcet winner** — it beats Red (66.6 vs 33.2) *and* Yellow
  (64.5 vs 35.3) head-to-head. IRV threw out the one candidate a majority preferred
  over each rival.
- **STAR** advances Green on its scores (lots of 3s from both wings + 5s from the
  center) and wins the runoff **65–35**.

Run it: [`center_squeeze_voteline_1d.yaml`](../../method_comparisons/center_squeeze/center_squeeze_voteline_1d.yaml)
(scores are a simple 1-D spatial model: own side 5, the adjacent center 3, the far
side 0–1; weights are the percentages ×10). The engine's own divergence block:

```
[Divergence from STAR]
  STAR                   = Green
  Choose-One (Plurality) = Yellow   (differs from STAR)
  RCV-IRV                = Yellow   (differs from STAR)

Scoring Round      Green 3620 (1st) · Yellow 2428 (2nd) · Red 2249
Automatic Runoff   Green 645 (65%) vs Yellow 353 (35%)   → Green wins
```

| Method | Winner |
|---|---|
| Plurality | Yellow |
| **RCV-IRV / Hare** | **Yellow** ❌ — squeezes out the center |
| Approval · Borda · Condorcet · Ranked Robin | Green |
| **STAR** | **Green** ✅ (= the Condorcet winner) |

**The threshold, made concrete.** This isn't randomness — it's structural. With the
voters more *centered*, Green has enough first-choices to survive elimination and
RCV-IRV happens to elect Green too. Shift the electorate so the wings (Red, Yellow)
each out-poll the center on *first* choices, and Green is eliminated first — the
squeeze appears. STAR and the Condorcet methods elect Green on **both** sides of that
line, because they read the whole ballot, not just the top choice. *(This is also why
"RCV ≠ Random" — IRV fails here predictably, every time the geometry repeats.)*

## Vote splitting vs center squeeze

They look alike but aren't. **Vote splitting** is *similar* candidates sharing one
pool of supporters. **Center squeeze** is a *distinct* moderate squeezed by two
poles whose voters are different — the moderate can beat each pole head-to-head and
still be eliminated for too few first-choices. (Volić, *Making Democracy Count*, 2024.)

## "Core support" doesn't rescue IRV

IRV advocates excuse the squeeze by saying the moderate simply lacked **"core
support"** (first-place votes). But the squeezed Condorcet winner can have *more*
first-place votes than the eventual IRV winner and still be eliminated — so the
"core support" defense doesn't hold. (A sharper 4-candidate version of this can be
added as a test case on request.)

## Why it matters: polarization

Center squeeze is a depolarization argument, not just a fairness one. A simulation
study of candidate incentives (**Ogren 2023**, *Candidate Incentive Distributions*,
arXiv 2306.07147) finds IRV pushes candidates to court their **base** far more than
opposing voters, while **STAR and Condorcet methods** reward appealing to
opposing-side voters roughly *as much* as the base — and the gap grows with more
candidates. Electing squeezed moderates is how a method lowers the temperature.

## Real elections

- **Burlington, VT 2009 (mayor).** Montroll was the Condorcet winner — preferred
  over Wright 56–44 and over Kiss 54–46 — but had too few first-choices, was
  eliminated, and **Kiss won**. IRV was repealed there in 2010.
- **Alaska 2022 (US House special).** Begich beat both Peltola and Palin
  head-to-head, but was eliminated first; **Peltola won.** (Worked through in
  [`favorite_betrayal_voting_301.md`](../../interviews_conversations/favorite_betrayal_voting_301.md).)

## How STAR avoids it

STAR's scoring round advances the **two highest totals**, so a broadly-liked
candidate (lots of 4s and 5s) reaches the runoff on *strength of support*, not just
first-place counts — exactly the support a moderate has and IRV ignores. STAR is
highly **Condorcet-efficient**: it usually elects the head-to-head winner.

→ More source notes: **RCV-IRV center-squeeze & polarization** group in
[`LINKS.md`](../../interviews_conversations/LINKS.md).

**Watch it happen (simulation).** endolith's *elsim* has animated 2-D spatial
simulations of the worst-case **"core collapse"** center squeeze. As its write-up puts it:

> Under IRV, vote-splitting causes the most-representative candidate to be eliminated
> first, then the second-best eliminated second, and so on until only the worst two are
> left in the final round and the second-worst wins… Under TVR [Total Vote Runoff], on the
> other hand, all voter preferences are included, so the least-representative candidates
> are eliminated first, transferring their ballots inwards such that support converges to
> the consensus candidate in the middle of the electorate (who… is the Condorcet winner).

**A 140-year-old warning.** This isn't new — E. J. Nanson described it in **1882**, calling
IRV "Ware's method":

> Then on the single vote method [plurality] R may win; on Ware's method A, B, C, D, … P,
> may be excluded one after another on the successive scrutinies, and at the final scrutiny
> the contest will be between Q and R, and Q, of course, wins… Thus the single vote method
> may return the worst of all the candidates; and although **Ware's method cannot return
> the worst, it may return the next worst.**
> — Nanson, *Methods of Election* (1882)

Animations + the full quote: [elsim — core-collapse center-squeeze](https://github.com/endolith/elsim/blob/collapse_2d/examples/README.md).

Sources: [center squeeze (electionscience)](https://electionscience.org/library/the-center-squeeze-effect/),
[Ogren 2023, Candidate Incentive Distributions (arXiv)](https://arxiv.org/abs/2306.07147),
[Burlington 2009 (Wikipedia)](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election),
[Alaska 2022 center squeeze (arXiv)](https://arxiv.org/abs/2303.00108).
