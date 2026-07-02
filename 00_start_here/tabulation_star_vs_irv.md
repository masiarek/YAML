# How the Count Works — STAR vs RCV-IRV, Step by Step

**One line:** the *same* ballots, counted two ways. **STAR** scores then holds one
runoff — **two steps.** **RCV-IRV** runs rounds of eliminate-and-transfer — here
**three.** In this example both elect **Carmen**, so the page isolates the *process*
(how each count works and what it costs), not the winner.

→ Companion to [`RCV_IRV_is_simple.md`](RCV_IRV/RCV_IRV_is_simple.md) (the "which half is simple?"
argument) and [`summability.md`](STAR_Voting/STAR_summability.md). When the two counts elect
*different* people, see [`RCV_IRV_center_squeeze.md`](RCV_IRV/RCV_IRV_center_squeeze.md). Level **201**.

Worked on one shared file:
[`01_Single_winner/count_simplicity_star_vs_irv.yaml`](../method_comparisons/_main/count_simplicity_star_vs_irv.yaml)
— 45 voters, 5 candidates (Andre, Blake, Carmen, Dana, Evan).

---

## The shared ballots

Every voter scores all five candidates 0–5. STAR reads the scores directly; RCV-IRV
reads each ballot as a *ranking* (highest score = 1st choice, and so on).

```
Count × Andre Blake Carmen Dana Evan
  14  ×   4     3     5     2    1      # Carmen base   (C > A > B > D > E)
  10  ×   5     3     4     2    1      # Andre first   (A > C > B > D > E)
   9  ×   3     5     4     2    1      # Blake first   (B > C > A > D > E)
   7  ×   3     2     4     5    1      # Dana first    (D > C > A > B > E)
   5  ×   3     2     4     1    5      # Evan first    (E > C > A > B > D)
```

Carmen is almost everyone's strong **second** choice but few voters' **first** — the
detail that makes the two counts behave so differently.

---

## STAR — two steps

**Step 1 — Scoring Round.** Add each candidate's scores (a column sum). The two
highest advance.

```
Carmen  -- 194  -- First place
Andre   -- 169  -- Second place
Blake   -- 141
Dana    -- 106
Evan    --  65
 Carmen and Andre advance.
```

**Step 2 — Automatic Runoff.** On every ballot, see which *finalist* it scored
higher. That's one head-to-head tally.

```
Carmen        -- 35  -- First place
Andre         -- 10
Equal Support --  0
 Carmen wins.
```

Two passes over the ballots — a sum, then one pairwise comparison. Both are
**summable**: each precinct can report its score totals and its Carmen-vs-Andre split,
and you just add them up.

---

## RCV-IRV — rounds of eliminate-and-transfer

Count only each ballot's **top surviving** choice. No majority? Drop the lowest,
move its ballots to their next choice, and re-count. Repeat.

```
ROUND 1                     ROUND 2                     FINAL RESULT
Carmen   14  Hopeful        Carmen   19  Hopeful        Carmen   26  Elected
Andre    10  Hopeful        Andre    10  Hopeful        Andre    10  Rejected
Blake     9  Hopeful        Blake     9  Hopeful        Blake     9  Rejected
Dana      7  Hopeful        Dana      7  Rejected        Dana      0  Rejected
Evan      5  Rejected        Evan      0  Rejected        Evan      0  Rejected
```

- **Round 1:** nobody has a majority (needs 23 of 45). Evan is lowest → eliminated.
  His 5 ballots' next choice is Carmen → **Carmen 14 → 19.**
- **Round 2:** still no majority. Dana is now lowest → eliminated. Her 7 ballots'
  next choice is Carmen → **Carmen 19 → 26.**
- **Final:** Carmen has 26 of 45 (>half) → elected.

Three rounds, and to follow it you have to track *which* ballots moved *where* each
time. That bookkeeping is why an IRV count is **not summable** — a precinct can't
report a partial result that adds up, because who gets eliminated depends on the whole
electorate. Every ballot has to be in one place.

> **Exhausted (inactive) ballots.** This example is tidy because every voter ranked all
> five candidates, so no ballot ever runs out of choices. In real RCV-IRV elections a
> ballot whose remaining ranks are all eliminated **stops counting** ("exhausted" /
> "inactive"), which is why an IRV winner's final-round majority is a majority of
> *continuing* ballots, not of everyone who voted. A faithful display should show the
> exhausted pile each round. STAR has no equivalent: every ballot's full score is read
> in the scoring round, and every ballot counts in the runoff. (See
> [`../../interviews_conversations/exhausted_ballots_301.md`](../interviews_conversations/exhausted_ballots_301.md).)

---

## Side by side

| | STAR | RCV-IRV |
|---|---|---|
| Steps here | **2** (score sum → one runoff) | **3 rounds** (eliminate + transfer ×2, then a majority) |
| Each step is… | a column sum; one head-to-head tally | re-tallying top choices among survivors, following every transfer |
| Reads… | the whole ballot at once (all scores) | only each ballot's top *surviving* mark |
| Summable / precinct-local? | **Yes** — add precinct totals | **No** — needs all ballots centrally, re-counted each round |
| Hand-auditable? | totals and one runoff split | re-run the whole transfer sequence |
| Winner (this example) | **Carmen** | **Carmen** |

Same answer — but one count you can do with a calculator and a precinct sheet, the
other needs the full ballot set and software to walk the rounds.

## When the rounds change the *winner*

Here the methods agree, and Carmen even led the first round — but **the first-round
leader is not always the winner.** In a **center squeeze**, the consensus candidate is
almost everyone's second choice, so IRV eliminates her early (too few *firsts*) while
STAR's scoring round keeps her in and she wins. Same ballots, different count,
**different winner** — traced in [`RCV_IRV_center_squeeze.md`](RCV_IRV/RCV_IRV_center_squeeze.md) (demos
`center_squeeze_irv.yaml` / `center_squeeze_star.yaml`). This is exactly why RCV-IRV
results have to be read to the *final* round, never reported from first choices alone.

> **On displaying RCV-IRV results.** The round-by-round table above follows the
> standard best practice (FairVote; Center for Civic Design): show every round with a
> written explanation, name the majority threshold, and treat the final round — not the
> first-choice lead — as the result. We deliberately show *all* the rounds rather than
> de-emphasizing the eliminations, because the whole point here is to see how the count
> works. See `interviews_conversations/LINKS.md` → "FairVote: displaying RCV results."

## Run it yourself

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_Single_winner/count_simplicity_star_vs_irv.yaml
python3 RCV_IRV_tabulation_engine/rcv_irv_tabulation.py    01_Single_winner/count_simplicity_star_vs_irv.yaml
```

---

## Cross-references
- [`RCV_IRV_is_simple.md`](RCV_IRV/RCV_IRV_is_simple.md) — the simplicity argument this trace backs up.
- [`summability.md`](STAR_Voting/STAR_summability.md) — why STAR's count adds up locally and IRV's doesn't.
- [`RCV_IRV_center_squeeze.md`](RCV_IRV/RCV_IRV_center_squeeze.md) — when the two counts elect different people.
- [`../../interviews_conversations/what_is_a_voting_method.md`](../interviews_conversations/what_is_a_voting_method.md)
  — ballot vs count, the 101 foundation.
