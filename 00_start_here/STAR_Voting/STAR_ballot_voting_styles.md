# Filling Out the 5-Star Ballot — Voting Styles

*There is no wrong way to fill out a STAR ballot. This page is the gallery of
legal styles — from a plain old choose-one vote to a fully expressive spread —
and what each one actually says to the count.*

---

STAR uses a **5-star ballot**: you give every candidate an independent score
from 0 to 5, like rating movies. Two facts do most of the work on this page:

- **Equal scores are allowed.** Two candidates can both get a 5 (or a 0).
  You're never forced to invent a difference you don't feel.
- **Skipping is allowed.** A candidate you leave blank simply counts as 0.
  You can't spoil the ballot by skipping, doubling, or "over-voting."

Because each score stands alone, filling the ballot out is quick: give your
favorite a 5, your least favorite a 0, then place everyone else relative to
those two. You never have to hold the whole field in your head at once — even
in a 20-candidate race you're only ever comparing a candidate against your two
anchors. (Contrast a ranked ballot, where each slot means re-scanning everyone
you haven't ranked yet.)

## The style gallery — eight voters, eight legal ballots

Same six candidates for every voter: **Allen, Bianca, Chris, Desi, Edith,
Frank**. Each row below is one voter's complete, valid ballot.

| Style | Allen | Bianca | Chris | Desi | Edith | Frank | What the voter is saying |
|---|--:|--:|--:|--:|--:|--:|---|
| **Traditional (choose-one)** | 0 | 5 | 0 | 0 | 0 | 0 | "Bianca. Period." — the familiar single-choice vote, transplanted. |
| **Strong backup** | 0 | 5 | 0 | 0 | 0 | 4 | "Bianca — and if not her, Frank is nearly as good." |
| **Weak backup** | 0 | 5 | 0 | 0 | 0 | 1 | "Bianca — and Frank only over the rest, reluctantly." |
| **Partisan slate** | 5 | 5 | 0 | 0 | 0 | 5 | "My party's three candidates, full support; nobody else." |
| **Ranked-style** | 2 | 5 | 0 | 3 | 1 | 4 | "I'll use each score once, like a ranking: B > F > D > A > E > C." |
| **Nuanced** | 3 | 4 | 0 | 3 | 1 | 5 | "Full range, and Allen = Desi because I truly can't split them." |
| **"Anyone but…"** | 5 | 5 | 0 | 5 | 5 | 5 | "Anyone but Chris." |
| **Protest / least-bad** | 0 | 0 | 0 | 0 | 0 | 1 | "I dislike them all; Frank is the least bad." |

Every one of these is legal, and every one is counted. A few are worth a second
look:

- **Traditional / choose-one** works exactly as the voter intends — but it's a
  bullet vote, and it under-uses the ballot: if Bianca doesn't reach the
  runoff, this ballot has no say in the final head-to-head. (The dedicated
  small demo: [`03a_c3_b3_style-bullet-vote.yaml`](../../01_STAR/_main/03a_c3_b3_style-bullet-vote.yaml).)
- **Backups are free.** The strong-backup and weak-backup ballots are the
  everyday super-power of a scored ballot: supporting a second choice can
  never hurt your first choice in the scoring round — a 5 is a 5 no matter
  what else you mark. (Honest fine print: the runoff compares your two scores,
  so *if both* end up finalists, your 4 says "prefer Bianca, but Frank is
  fine." That's the message the voter chose to send. See
  [STAR's honest limits](STAR_honest_limits.md).)
- **Ranked-style is legal but never required.** Using each score exactly once
  mimics a ranking. STAR reads it happily — but you've volunteered a
  constraint the ballot doesn't impose. The nuanced ballot right below it
  carries *more* honest information (equal 3s where the voter is truly
  indifferent) with *less* effort.
- **Partisan and "anyone but" ballots score equal 5s** — and that's fine. If
  two of those 5s become the finalists, the ballot is **Equal Support** in the
  runoff: no preference between the finalists, by the voter's own choice. It
  still counted fully in the scoring round, where it helped decide *who* the
  finalists were. An equal-score ballot is never discarded.
- **The protest vote still works.** All 0s and a single 1 registers a
  least-bad preference and can decide a race. Caveat: compressing your scores
  into the bottom of the range also shrinks your voice in the scoring round —
  a least-bad choice counts, but the full range counts louder.
  ([`03b_c3_b3_1_style-protest-vote.yaml`](../../01_STAR/_main/03b_c3_b3_1_style-protest-vote.yaml).)

## All eight styles in one election

The gallery above is a real, tabulatable election:
[`03c_c6_b8_style-gallery.yaml`](../../01_STAR/_main/03c_c6_b8_style-gallery.yaml).
Bianca and Frank reach the runoff on scores; Bianca wins it 4–2, with the
partisan and "anyone but Chris" voters counted as Equal Support (they scored
both finalists 5):

```
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Bianca        -- 34 -- First place
   Frank         -- 25 -- Second place
   Allen         -- 15
   Desi          -- 11
   Edith         --  7
   Chris         --  0
 Bianca and Frank advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Bianca        -- 4 -- First place
   Frank         -- 2
   Equal Support -- 2
 Bianca wins.
   Voters with a preference: 6 of 8 (2 Equal Support).
   Bianca 4 (67%) vs Frank 2 (33%); majority = 4.
```

Full report: [`03c_c6_b8_style-gallery_tabulated.txt`](../../01_STAR/_main/_main_tabulated/03c_c6_b8_style-gallery_tabulated.txt).

## Blanks, and what they mean

Leaving a candidate's line blank counts as **0** — always, with no penalty to
the rest of the ballot. In this library's YAML files a blank is written `-`,
and there are markers for the other real-world cases (race abstention `~`,
candidate abstention `&`, spoiled `?`, spoiled-and-reissued `%`) — all
tabulate as 0 but are reported honestly. See
[`ballot_and_terminology_basics.md`](../ballot_and_terminology_basics.md) and
the [GLOSSARY](../GLOSSARY.md).

Contrast RCV-IRV: skipped or repeated rankings are, in many jurisdictions,
ballot *errors* — one reason reported spoilage runs roughly **4–9% for ranked
ballots vs. 0–2% for rated ballots** (and 1–4% for the familiar single-mark
ballot). A scored ballot is very hard to fill out wrong.

## Why the 5-star ballot earns its keep

**Expressive.** A choose-one ballot carries one bit of your opinion; an
approval ballot, one yes/no per candidate; a ranked ballot, order but never
strength. The 0–5 ballot carries order *and* strength — "Bianca by a mile" and
"Bianca by a hair" are finally different votes. Six levels (0–5) sits near the
sweet spot: enough resolution to matter, few enough that every step means
something.

**Accurate.** Research comparing ratings and rankings finds ratings have
superior validity — forced full rankings capture *noise*, differences voters
don't actually feel. Equal scores let voters express exactly the distinctions
that matter to them and no more. (The deep dive:
[Scores vs. Ranks](../scores_and_ranks/scores_vs_ranks.md).)

**Equal.** Any way you fill out your ballot, someone else can fill theirs out
in the equal and opposite way — no style has secret extra weight. That's the
[Equally Weighted Vote](equally_weighted_vote.md), and it's why the gallery
above is safe to publish as a how-to: there is no trick style to teach.

## Related concepts in this library

- [Scores vs. Ranks](../scores_and_ranks/scores_vs_ranks.md) — the ballot-design distinction underneath this whole page
- [STAR's Automatic Runoff](STAR_Automatic_Runoff.md) — where Equal Support ballots land
- [Equally Weighted Vote](equally_weighted_vote.md) — why no style out-muscles another
- [STAR's honest limits](STAR_honest_limits.md) — what a backup score does and doesn't risk
- [Curriculum 101.3 — How you're allowed to vote](../CURRICULUM.md) — this page's slot in the learning path
- Small demos: [`03a` bullet vote](../../01_STAR/_main/03a_c3_b3_style-bullet-vote.yaml) · [`03b` protest vote](../../01_STAR/_main/03b_c3_b3_1_style-protest-vote.yaml) · [`03c` the full gallery](../../01_STAR/_main/03c_c6_b8_style-gallery.yaml)

## Learn more

- [Voting Scenarios — traditional, partisan, "ranked" — ballot examples](https://docs.google.com/document/d/1jrRYt7NhCKEBqnBZCzjx_9eTVBlENfIHl8bahjH8g4k/edit?tab=t.0) (Adam's source notes for this page)
- [Why I like STAR voting: the 5-star ballot](https://bternarytau.github.io/2021/06/06/why-i-like-star-voting-the-5-star-ballot) — BTernaryTau, *Technically Exists* (spoilage rates, ratings validity, expressiveness)
- [Ballot spoilage rate summary](https://www.rangevoting.org/SPRatesSumm.html) — rangevoting.org
