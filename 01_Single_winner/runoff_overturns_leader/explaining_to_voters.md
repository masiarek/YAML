# Explaining Runoff Reversal to Voters — and a Fix for the BetterVoting Popover

When a real BetterVoting election produces a **Runoff Reversal** (the Scoring-Round
leader losing the Automatic Runoff), voters see a little "Why is the top scoring
candidate different from the winner?" popover. Its current wording is *almost* right
but muddled — and worse, it trips over the word **equal**, which has a specific,
opposite meaning in STAR. This page is the clean version to use instead.

→ The full lesson with worked examples: [`README.md`](./README.md).
Glossary: [`Runoff Reversal`](../../00_start_here/GLOSSARY.md).
The exact election behind this popover is reproduced in
[`05_c3_b5_low-scores-bv1265.yaml`](./05_c3_b5_low-scores-bv1265.yaml) (a *low-score*
reversal: C leads the Scoring Round with just 7 stars, but A wins the runoff 3–2).

---

## What the popover says (verbatim)

> *The top-scoring candidate often matches the runoff winner, but not always. In the
> runoff, only the most preferred votes count, which can shift the outcome. For
> example, a 5 vs. 4-star vote has less impact in scoring but counts fully in the
> runoff, while a 5 vs. 0-star vote makes a big difference in scoring but is equal in
> the runoff. The runoff winner comes out on top because more voters prefer them over
> the runner-up.*

## What's off about it

1. **"only the most preferred votes count"** — sounds like ballots are discarded.
   They aren't. *Every* ballot counts in the runoff; each becomes **one full vote** for
   whichever finalist it scored higher.
2. **"a 5 vs. 0-star vote … is equal in the runoff"** — a 5-vs-0 is a *clear*
   preference (a full vote for the 5). It is **not** "equal." The intended point is
   that it counts as the *same single vote* as a 5-vs-4 — but the word **equal**
   collides with **Equal Support**, STAR's term for a genuine *no-preference* tie
   ([what that actually means](../../interviews_conversations/are_equal_score_votes_discounted.md)).
   Telling a voter "5 vs 0 is equal" states the opposite of the truth.
3. **The good sentence is buried.** "More voters prefer them over the runner-up" is the
   whole answer — it should lead, not trail.
4. **No shared vocabulary.** "Second round," "top scoring candidate," "runner-up" — it
   never says **Scoring Round**, **Automatic Runoff**, or **Finalists**, and it gives
   the phenomenon no name.

## The fix — a clean, correct version

> **Why isn't the top-scoring candidate always the winner?**
>
> STAR counts in two rounds that ask two different questions. The **Scoring Round**
> adds up the stars and sends the two highest — the **Finalists** — to the **Automatic
> Runoff**. The runoff asks a simpler question: between those two finalists, which one
> do **more voters** prefer? Every ballot still counts — in full — for whichever
> finalist it scored higher.
>
> The difference is that **margins matter in scoring but not in the runoff.** Scoring a
> finalist 5 vs. 4 adds just one star to their lead — but in the runoff it's a *full
> vote*. Scoring 5 vs. 0 adds five stars in the scoring round — but in the runoff it's
> still that *same one vote*. So a candidate can pile up stars from a few enthusiastic
> voters and lead the Scoring Round, yet lose the runoff to the finalist **more voters
> actually prefer**. That's a **Runoff Reversal**, and it's the runoff doing its job:
> making sure the winner has majority support, not just intensity.

## The one idea to land

The Scoring Round measures **how much** support (margins count). The Automatic Runoff
measures **how many** voters (each ballot = one vote between the two finalists). When
those two disagree, STAR sides with *how many* — on purpose. Say that, and you've
explained Runoff Reversal correctly in two sentences.

## Presenter cheat-sheet

| Don't say | Say instead |
|-----------|-------------|
| "second round" | **Automatic Runoff** |
| "scoring" / "first round" | **Scoring Round** |
| "the top two" | the **Finalists** |
| "5 vs 0 is equal in the runoff" | "5 vs 0 counts as the same *one vote* as 5 vs 4" |
| "only the preferred votes count" | "every ballot counts, as one vote for its higher-scored finalist" |
| (no name) | **Runoff Reversal** |

> Reserve **Equal Support** for its real meaning: scoring the two finalists the *same*,
> which counts as *no preference* between them in the runoff. Never use "equal" to
> describe a 5-vs-0 ballot.
