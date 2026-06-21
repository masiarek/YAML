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

This is **not** a property of ranked ballots in general. **Ranked Robin** (a
Condorcet count of the *same* ballot) reads every ranking and elects the head-to-head
winner, so it has **no** center squeeze. Saying "RCV has center squeeze" is
imprecise — it's **IRV**. (See [`TIPS_terminology.md`](../TIPS_terminology.md).)

## Test case (run it)

→ [`split_voting/04_star_wars_vote_split.yaml`](../../split_voting/04_star_wars_vote_split.yaml)

Leia is the **Condorcet winner** (beats both others head-to-head) but has the
**fewest first-choices (27)**, so she'd be eliminated first under IRV. The engine's
`[Divergence from STAR]` block shows it directly:

```
STAR                   = Leia
Choose-One (Plurality) = Vader
RCV-IRV                = Skywalker   (differs from STAR)
```

STAR elects Leia; IRV elects Skywalker — the squeeze, in numbers.

## Real elections

- **Burlington, VT 2009 (mayor).** Montroll was the Condorcet winner — preferred
  over Wright 56–44 and over Kiss 54–46 — but had too few first-choices, was
  eliminated, and **Kiss won**. IRV was repealed there in 2010.
- **Alaska 2022 (US House special).** Begich beat both Peltola and Palin
  head-to-head, but was eliminated first; **Peltola won.** (Worked through in
  [`favorite_betrayal_voting_301.md`](../../interviews_conversations/favorite_betrayal_voting_301.md).)

## How STAR avoids it

STAR's scoring round advances the **two highest totals**, so a candidate who is
broadly liked (lots of 4s and 5s) reaches the runoff on *strength of support*, not
just first-place counts — exactly the support a moderate has and IRV ignores. STAR
is also highly **Condorcet-efficient**: it usually elects the head-to-head winner.

Sources: [Burlington 2009 (Wikipedia)](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election),
[center squeeze / monotonicity criterion (Wikipedia)](https://en.wikipedia.org/wiki/Monotonicity_criterion).
