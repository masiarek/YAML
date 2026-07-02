# Teaching Runoff Reversal — a step-by-step guide

The single question STAR raises most often: *"Why didn't the candidate with the most
stars win?"* This is the presenter's playbook for answering it — the order to teach
it in, the examples to use, **why a reversal is a good thing**, and the hard
("devil's advocate") questions with answers.

- Concept hub: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md) (has the flow diagram)
- The concept lesson + all cases: [`README.md`](README_runoff_overturns_leader.md)
- Voter-facing one-paragraph version (and a BetterVoting popover fix): [`explaining_to_voters.md`](explaining_to_voters.md)
- Glossary: [`Runoff Reversal`](../../00_start_here/GLOSSARY.md)

---

## The one-sentence answer (lead with this)

> Leading the Scoring Round makes you a **finalist**, not the winner. The winner is
> whichever of the top two **more voters actually prefer** — and that's the whole
> point of the runoff.

## Why a reversal is a *good* thing (the core message)

A big star total can come from **intensity** or **breadth** — not from being the
candidate the most people prefer head-to-head. The Automatic Runoff asks the
majority-protecting question that raw scores can't: *of the two finalists, which one
do more voters prefer?* When those agree (the usual case) the leader wins. When they
disagree, **majority preference is exactly what should win** — otherwise a passionate
minority could outvote the majority just by scoring harder. The reversal is the
safeguard doing its job, not a glitch.

A bonus: because your runoff vote is set by the scores you already gave, you **never
have to lowball** a rival to protect your favorite. Honest scoring is also optimal
strategy.

## The two voter patterns that cause a reversal

Almost every reversal is one of these (both are the same lesson — stars measure
support, the runoff measures *preference*):

1. **The narrow-but-deep leader (polarizing).** A candidate piles up stars from an
   enthusiastic **minority** (lots of 5s) while the **majority** rates them low or 0.
   Big total, but loses the head-to-head. *(See `02`, `05`.)*
2. **The broadly-liked-but-second-choice leader.** A candidate everyone rates *well*
   (a high consensus total) but who is most voters' **second** pick; the majority's
   actual favorite wins the runoff. *(See `01a` below.)*

## Step by step

### Step 1 — the atom (3 voters): [`01a`](01a_c3_b3_more-stars-fewer-voters.yaml)

Show the ballots, then the result. Everyone likes Almond — but two of the three
*prefer* Brownie:

```
Almond, Brownie, Cocoa
     5,       1,     2
     4,       5,     0
     4,       5,     0
```
```
Scoring Round
   Almond        -- 13 -- First place      <- most stars (everyone rates it high)
   Brownie       -- 11 -- Second place
   Cocoa         --  2
 Almond and Brownie advance.
Automatic Runoff Round
   Brownie       -- 2 -- First place       <- 2 of 3 voters prefer Brownie
   Almond        -- 1
   Equal Support -- 0
 Brownie wins.
```

Talking point: Almond's 13 is real — it *is* broadly liked. But when each voter must
pick between the two finalists, the majority chose Brownie. Stars found the finalists;
the runoff picked the winner.

### Step 2 — the control (same machinery, leader CONFIRMED): [`04`](04_c4_b3_runoff-confirms-leader.yaml)

Immediately defuse "the runoff is rigged against the leader" by showing the *same*
process keep a leader who *is* most-preferred:

```
Amber, Blue, Coral, Dune
    2,    5,     1,    0
    2,    5,     0,    1
    5,    4,     0,    0
```
```
Scoring Round
   Blue          -- 14 -- First place
   Amber         --  9 -- Second place
 Blue and Amber advance.
Automatic Runoff Round
   Blue          -- 2 -- First place
   Amber         -- 1
 Blue wins.
```

Talking point: the runoff isn't biased against the leader — it just *checks* the
leader. Here Blue leads **and** is preferred, so Blue wins. The reversal only happens
when intensity and majority preference point at different candidates.

### Step 3 — it holds at scale, and it's real

- [`01b`](01b_c3_b9_overturn-holds-at-scale.yaml) — the same election with more
  voters: 67% / 33%. The atom wasn't a small-numbers fluke.
- [`02`](02_c5_b5_leader-overturned.yaml) — 5 candidates: a high-ceiling favorite
  (the *narrow-but-deep* pattern) loses to the broad compromise.
- [`03`](03_c7_b3_ice-cream-live.yaml) (real BV `4c7kp9`) and
  [`05`](05_c3_b5_low-scores-bv1265.yaml) (real BV `BV1265`) — actual recorded
  elections; `05` is the one that triggers BetterVoting's own "why is the top scorer
  different?" popover.

## Devil's-advocate questions (with answers)

**"Isn't it undemocratic to deny the candidate with the most points?"**
Points aren't votes for *winning* — they're how voters describe how much they like
each candidate, and they're used to pick the two finalists. The win goes to whichever
finalist **more voters prefer**. Denying that would let a minority's high scores
override a majority's preference — *that* would be undemocratic.

**"Doesn't this punish popular candidates / reward being everyone's bland second
choice?"**
No — the runoff is a head-to-head majority. A "bland" candidate only wins if, one on
one, more voters genuinely prefer them to the other finalist. If the popular candidate
is truly most-preferred, they win (that's the control case).

**"Couldn't I game it by scoring strategically?"**
Your runoff vote is whatever your *own* scores already imply, so there's no gain from
lowballing a rival or burying your second choice. Honest scoring is the best strategy
— a property pure-score methods lack.

**"Why only the top two? What about third place?"**
The top two carry the most support, so the decisive question is which of *them* the
majority prefers. If you worry the "right" candidate was a finalist at all, check the
**Condorcet** winner (the candidate who beats everyone head-to-head) in the full
report — STAR's runoff winner usually matches it. → [three notions of "winner"](../../00_start_here/STAR_Voting/STAR_three_winner_notions.md)

**"Is the reversal random, or tied to a tie-break?"**
Neither. It's fully deterministic from the ballots, and it has nothing to do with
tie-breaking — a reversal isn't a tie. (Tie-breaking only runs on an exact runoff
split; see [the flow](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md#the-flow).)

**"Voters will be confused/angry when their leader loses."**
That's the real risk — so name it and explain it in one breath, the way
[`explaining_to_voters.md`](explaining_to_voters.md) does. Confusion comes from an
*unexplained* reversal, not the reversal itself.

## Two views of the real cases (BV + LH) — assets to add

For the recorded races (`03` = BV `4c7kp9`, `05` = BV `BV1265`), the strongest proof
is the same election shown both ways — BetterVoting's screenshot beside the LH report.
To complete this (mirrors the pattern in `pet_real_bv_election/`):

1. Screenshot each BV result and save under `runoff_overturns_leader/img/`
   (e.g. `img/REPLACE_4c7kp9_bv_result.png`, `img/bv1265_bv_result.png`).
2. Export each BV JSON, drop it here, and convert it to YAML
   (`YAML_library/1_positive/01_convert_json_yaml.py`) — the
   **BV JSON → YAML → LH report** flow — so the ballots and both tabulations sit side
   by side.

<!-- Once captured:
![BetterVoting result for BV 4c7kp9 (ice cream): ChocoDrk leads, ChocoAlm wins](img/REPLACE_4c7kp9_bv_result.png)
-->

See also: the full audit report for each case in
[`runoff_overturns_leader_tabulated/`](runoff_overturns_leader_tabulated), and how
often reversals occur in [`simulations/runoff_reversal_simulation.py`](../../simulations/runoff_reversal_simulation.py).
