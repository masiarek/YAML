# Center Squeeze

**One line:** a broadly-liked moderate is eliminated *early* because few voters
rank/score them **first**, so a more polarizing candidate the majority actually
opposed goes on to win. It's an **RCV-IRV** failure (the eliminate-and-transfer
count); STAR avoids it.

→ Glossary: [`center squeeze`](../GLOSSARY.md) · deeper debate version:
[`favorite_betrayal_voting_301.md`](../../interviews_conversations/favorite_betrayal_voting_301.md)

---

## Why it happens (IRV-specific)

IRV only ever looks at each ballot's **top remaining** choice. A moderate who is
almost everyone's strong **second** choice — but few people's first — has the
fewest first-place votes, so IRV eliminates them before their broad support is ever
counted. The two wings survive; the consensus candidate doesn't.

This is **not** a property of ranked ballots in general. **[Ranked Robin](./ranked_robin.md)** (a
Condorcet count of the *same* ballot) reads every ranking and elects the head-to-head
winner, so it has **no** center squeeze. Saying "RCV has center squeeze" is
imprecise — it's **IRV**. (See [`TIPS_terminology.md`](../TIPS_terminology.md).)

## Minimal test case — run it

The smallest clean squeeze, as a matched pair (27 voters, Left / Center / Right):

→ [`center_squeeze_irv.yaml`](../../01_Single_winner/center_squeeze_irv.yaml)
 · [`center_squeeze_star.yaml`](../../01_Single_winner/center_squeeze_star.yaml)

Center is the **Condorcet winner** (beats Left 15–12, Right 18–9) but has the
**fewest first-choices (6)**. The STAR file's output shows all four methods on the
same ballots:

```
Choose-One (Plurality) = Left     RCV-IRV = Left     Approval = Left
STAR = Center   ( = Condorcet winner — also what Ranked Robin would elect )
```

IRV eliminates Center in round 1; STAR advances Center on strength of support and
wins the runoff. (Verified on the engine.) A richer themed version is the Star Wars
vote-split demo, [`04_star_wars_vote_split.yaml`](../../split_voting/04_star_wars_vote_split.yaml).

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

Sources: [center squeeze (electionscience)](https://electionscience.org/library/the-center-squeeze-effect/),
[Ogren 2023, Candidate Incentive Distributions (arXiv)](https://arxiv.org/abs/2306.07147),
[Burlington 2009 (Wikipedia)](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election),
[Alaska 2022 center squeeze (arXiv)](https://arxiv.org/abs/2303.00108).
