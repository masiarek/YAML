# The Math Behind Condorcet — Tournaments, the Smith Set, and Cycles

*The "graduate seminar" companion to Ranked Robin. None of this is needed to run or
advocate for a Condorcet election — [Ranked Robin](ranked_robin.md) ("most head-to-head
wins") is the practical, explainable method. But once you ask **what is the structure of
the pairwise results**, you walk straight into graph theory, game theory, and a few famous
impossibility theorems. Here's the map.*

→ Companion: [Ranked Robin vs. the Condorcet winner](ranked_robin_vs_condorcet.md) ·
[cycle resolution](cycle_resolution.md) · [Condorcet topic hub](../topics/condorcet/README_condorcet.md)
· **Level: Voting 301** — Curriculum [301.4](../CURRICULUM.md) (limits & theory),
[301.6](../CURRICULUM.md) (Condorcet/Score/Runoff disagree)

---

## The one mental shift: the pairwise matrix is a *graph*

Every pair of candidates has a head-to-head winner, so the pairwise results form a
**tournament** — a complete directed graph where an arrow A→B means "A beats B one-on-one."
**Almost every Condorcet idea below is just a question about this graph.** That's the key
move: Condorcet methods are *graph algorithms*, not vote-counting tricks.

- A **Condorcet winner** is a node that points to everyone (beats all) — a *source* with no
  incoming arrows.
- A **Condorcet loser** points to no one.
- A **cycle** (A→B→C→A) means the "beats" relation is **not transitive** — the famous
  **Condorcet paradox** (Condorcet, 1785). Majority rule, applied pairwise, can contradict
  itself. This is a property of the *voters' preferences*, not a flaw in any one method.

## When there's no single winner: the Smith and Schwartz sets

These generalize "the Condorcet winner" to the case where none exists.

- **Smith set** (a.k.a. *top cycle*): the **smallest** set of candidates who all beat
  everyone **outside** the set. If a Condorcet winner exists, the Smith set is just
  `{that winner}`; in a cycle, it's the whole cyclic clump at the top.
- **Schwartz set**: a slightly tighter cousin (always **Schwartz ⊆ Smith**); the two
  differ only when there are pairwise **ties**.
- A method is **Smith-efficient** if it always elects from the Smith set — a strong,
  desirable property (it implies Condorcet-efficiency).

**The math to compute them is graph theory:** the Smith set is the **top strongly connected
component** of the dominance graph. You find it with standard algorithms — Tarjan's or
Kosaraju's SCC, or by taking the transitive closure (Floyd–Warshall) and reading off the
maximal candidates. "Find the Smith set" = "find the top SCC."

## The cycle-resolving methods, mapped to their math

| Method | What it does | The math it *is* |
|--------|--------------|------------------|
| **Copeland / Ranked Robin** | elect the most head-to-head wins | tournament scoring (simplest) |
| **Minimax** | elect whoever's *worst* loss is smallest | optimization over the matrix |
| **Schulze (beatpaths)** | strongest *path* of majorities between candidates | widest-path / max-min **Floyd–Warshall** |
| **Ranked Pairs (Tideman)** | lock in the biggest majorities, skipping any that make a cycle | greedy + cycle detection |
| **Kemeny–Young** | the ranking that disagrees with the fewest voters | median ranking under **Kendall-tau** distance — **NP-hard** |
| **Maximal lotteries / bipartisan set** | mixed Nash equilibrium of the "majority game" | **game theory** + **linear programming** (von Neumann minimax) |

The last row is the gem: treat the margin matrix as a **symmetric zero-sum game** and solve
for its optimal *mixed* strategy. It connects voting directly to game theory, is solved by
an LP, and is beautifully well-behaved (Condorcet-, Smith-, and clone-consistent). If you
want one "wow" topic, it's maximal lotteries.

## The load-bearing theorems

- **Arrow's impossibility theorem** — no rank-aggregation rule can satisfy a short list of
  obviously-fair conditions at once.
- **Gibbard–Satterthwaite** — every reasonable non-dictatorial method is **manipulable**;
  strategy-proofness is impossible. (This is *why* favorite-betrayal incentives exist.)
- **McKelvey–Schofield chaos theorem** — in 2+ spatial dimensions, when there's no Condorcet
  winner the top cycle can wander *anywhere*, so agenda-setting power becomes decisive.
- **Probability of cycles** — under random ("impartial culture") preferences, a 3-candidate
  Condorcet cycle occurs ~**8.8%** of the time with many voters, and the chance of *no*
  Condorcet winner climbs toward 1 as candidates increase. (Exactly why a random
  6-candidate, 5-ballot sweep leaves the Condorcet column blank so often — see
  `tools_adam/random_star_divergence.py`.)

## What to learn, in order of payoff

1. **Graph / tournament theory** — strongly connected components, top cycle, paths. Unlocks
   Smith, Schwartz, and Schulze immediately.
2. **Order & relation theory** — transitivity, dominance, the majority relation.
3. **Game theory + linear programming** — minimax, Nash equilibria → maximal lotteries (the
   deepest, prettiest corner).
4. **Probability / combinatorics** — how often cycles actually occur.
5. **Complexity theory** — NP-hardness of Kemeny; manipulation-complexity
   (Bartholdi–Tovey–Trick).
6. **Social choice theory** — the umbrella that ties it together (Arrow, Gibbard–Satterthwaite, Sen).

## The honest caveat

You need **none** of this to run or advocate for a Condorcet election. **Ranked Robin
(Copeland)** — "whoever wins the most head-to-head matchups" — is the practical, teachable
method, and it resolves cycles fine for real-world use (margin, then lot). The
Smith/Schwartz/Schulze/maximal-lotteries machinery only matters when you care about
edge-case cycle behavior or want provable theoretical properties. It's deep and genuinely
fun — but it's the graduate seminar, not the voter pamphlet.

## Related

- [Ranked Robin (the method)](ranked_robin.md) · [Ranked Robin vs. Condorcet](ranked_robin_vs_condorcet.md) · [cycle resolution](cycle_resolution.md)
- [Condorcet efficiency — topic hub](../topics/condorcet/README_condorcet.md)
- Glossary: [`Condorcet`](../GLOSSARY.md)
