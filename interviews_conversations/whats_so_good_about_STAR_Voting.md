# What's So Good About STAR Voting?
### A recorded conversation — Larry (curious host) & Adam (expert)

A spoken, demo-driven conversation for a live recording. **Larry** asks the
questions a smart newcomer would ask; **Adam** answers and drives the live
demos. Cues in the margin:

- **[DEMO]** — run a file from this repo live on screen (the STAR engine).
- **[SLIDE]** — show a slide from one of the decks (see `README.md` for the map).
- **[REPO]** — a lesson file to pull language or framing from.

Pacing target: ~25–30 min. Each segment can also stand alone as a short clip.

---

## Segment 0 — Cold open (90 seconds)

**Larry:** Adam, you keep telling me STAR Voting is better. In one breath — what's
so good about it?

**Adam:** Three things. You can finally vote your honest opinion without it
backfiring. The winner actually has majority support. And anyone can re-add the
count by hand. STAR does all three at once, and that combination is the whole
story.

**Larry:** That's the trailer. Now make me believe it.

**Adam:** Deal. Let's start with the problem it fixes — because once you *feel*
the problem, STAR stops looking clever and starts looking obvious.

> [SLIDE] Full Deck — "Why STAR Voting?" title + the one-line pitch.
> [REPO] `00_start_here/00_START_HERE.md` (the one-sentence pitch).

---

## Segment 1 — The problem: vote splitting & the spoiler effect

**Larry:** Okay, what's actually broken about how we vote now?

**Adam:** Our Choose-One ballot is only accurate when there are exactly two
candidates. The moment a third shows up, votes split. Two similar candidates can
divide the people who like both of them, and a candidate the *majority* didn't
want slips through the middle. That's the spoiler effect.

**Larry:** Give me the cartoon version.

**Adam:** Star Wars. You expect Skywalker and Vader are the frontrunners, but you
actually prefer Leia. If you vote your heart — Leia — you might "waste" your vote
and help Vader win. So you hold your nose and vote Skywalker. Multiply that
across millions of people and you get our whole political mess: lesser-evil
voting, gate-kept candidates, and two parties that demonize each other.

**Larry:** Can you *show* me a spoiler, not just describe one?

**Adam:** Let's run a real election.

> [DEMO] `split_voting/01_political_left_split.yaml` — a 66% coalition (Green,
> Labour, SocialDem) splits three ways; under Choose-One the **Conservative wins
> with 34%**, a candidate two-thirds ranked last. The `[Vote-splitting check]`
> block says it in numbers. Then point out: *STAR elects Labour* — the
> coalition's consensus.
> [SLIDE] Full Deck — "PROBLEM: VOTE-SPLITTING" and "VOTE-SPLITTING SETS OFF A
> DOMINO EFFECT."

**Adam (after the demo):** Notice what just happened. Nobody was dishonest. The
majority just got divided and conquered by their own ballot. That's not a freak
event — it can happen in *any* race with more than two candidates.

> [REPO] The deeper *diagnosis* — is the system really broken, how often, how
> serious? — `interviews_conversations/our_voting_system_is_broken.md` (the
> foundational "Problem with Plurality" episode).

---

## Segment 2 — Ranks vs Scores (the key conceptual move)

**Larry:** People say "just use Ranked Choice." Isn't ranking already more
expressive than picking one?

**Adam:** It's more expressive than Choose-One, yes. But there's a deeper fork in
the road here, and it's the thing most people never get told: there are two
*families* of better ballots — **ranked** and **scored** — and they're not the
same tool.

**Larry:** What's the difference, concretely?

**Adam:** Ranking gives you *order only*: 1st, 2nd, 3rd. You can't say two
candidates are equally good, and you can't say your 1st is a mile ahead while
your 2nd and 3rd are basically tied. Scoring — rating each candidate 0 to 5, like
stars on a movie — gives you order *plus intensity*, and it lets you mark equals.

**Larry:** Why does intensity matter? Order seems like enough.

**Adam:** Because elections are about finding the candidate who best represents
everyone, and "how much" is real information. "She's my 2nd choice and I love
her" and "he's my 2nd choice and he's the lesser evil" are completely different
statements — and a ranked ballot writes them down *identically*. A scored ballot
keeps the difference. More information in means a more representative winner out.

**Larry:** So scores are a superset of ranks?

**Adam:** Essentially — from a score ballot you can always read off the ranking,
but from a ranking you can never recover the scores. That's why STAR uses a score
ballot as its raw material.

> [SLIDE] Full Deck — "INTRODUCING: ALTERNATIVE VOTING! (Rating vs Ranking)" and
> "That changed with the invention of STAR Voting… Score + Instant Runoff."
> [REPO] `00_start_here/GLOSSARY.md` — "Scored (cardinal)" vs "Ranked (ordinal)."

---

## Segment 3 — The STAR ballot: how you actually vote

**Larry:** Walk me through filling one out.

**Adam:** Four rules, that's it:
- Give your favorite(s) **5 stars**.
- Give your last choice(s) **0**, or leave them blank.
- **Equal scores are allowed** — rate two candidates the same if you feel the
  same.
- Score everyone else anywhere from 0 to 5, however you like.

**Larry:** And if I only like one candidate?

**Adam:** Then "bullet vote" — give them 5 and leave the rest blank. STAR lets you.
It's just not usually your strongest move, because the rest of your ballot is
where you get a say in who the finalists are.

**Larry:** It feels suspiciously easy.

**Adam:** That's the point — it's the five-star rating everyone already does for
movies and rideshares. Low error rates, no "I accidentally spoiled my ballot,"
and nothing gets thrown away.

> [SLIDE] Full Deck — "INTRODUCING STAR VOTING (Instructions)" and the 5-star
> ballot graphic.

---

## Segment 4 — The two rounds (the dual nature)

**Larry:** STAR stands for Score Then Automatic Runoff. What are the two steps?

**Adam:** You vote once; the count happens in two rounds.
- **Scoring Round:** add up all the stars. The two highest-scoring candidates
  become finalists.
- **Automatic Runoff:** for those two finalists, your ballot counts as a full
  vote for whichever one you scored higher. Whoever more voters preferred wins.

**Larry:** Why two rounds? Why not just elect the highest total score?

**Adam:** Because pure score has a weakness: if all that mattered was the total,
some voters would be tempted to exaggerate — give their favorite a 5 and everyone
else a 0. The runoff is the antidote. In the runoff the *size* of your score
doesn't matter, only which finalist you put higher. So exaggerating can backfire
— you might hand the runoff to someone you'd have preferred to influence.

**Larry:** So the two rounds are doing two different jobs.

**Adam:** Exactly — that's the dual nature. The Scoring Round measures **how much**
support there is — candidate quality, strength. The runoff measures **how many**
supporters — number of people, a real majority. One finds the genuine
contenders; the other decides between them by majority. Strength, then numbers.

**Larry:** Can you show the two rounds turning, slowly, on something tiny?

**Adam:** The smallest election possible.

> [DEMO] `01_Single_winner/00a_c2_b1_two-candidates.yaml` — one voter, two flavors.
> Watch the Scoring Round, then the Automatic Runoff. With two candidates STAR
> agrees with ordinary voting — that's *why* we start here: the gears are
> visible, nothing surprising competes for attention.
> [DEMO] Then `01_Single_winner/vote_splitting2.yaml` (or `split_voting/02…`) —
> add a third candidate and watch the winner become the broad compromise.
> [SLIDE] Full Deck — "HOW DOES STAR VOTING WORK?" and "STAR RESULTS: 1) Add up
> the stars. 2) Add up the votes."
> [REPO] `00_start_here/00_START_HERE.md` — "Why TWO rounds and not just scores?"

**Adam (tie-in):** There's a lovely way the core Python developer Tim Peters put
it: STAR treats your scores as *numbers* to pick the finalists, then treats the
same scores as mere *order* to decide the runoff. The big "5" is decisive in step
one and irrelevant in step two — and that's exactly what makes it hard to game.

---

## Segment 5 — Why this is better: the benefits

**Larry:** Sell me the upside in a list I can remember.

**Adam:** Equal Vote uses five yardsticks — Simple, Honest, Expressive, Accurate,
Equal — and STAR is built to hit all five:
- **Honest:** it's safe to give your true favorite a 5. No favorite betrayal.
- **Expressive:** you show both order *and* degree, and you can mark equals.
- **Accurate:** in the satisfaction studies, STAR tops the charts — it collects
  the best data and then *uses all of it*. No ballot is wasted or ignored.
- **Equal:** every voter has the identical 0–5 range for every candidate, and an
  equal vote in both rounds. It eliminates vote-splitting, which is the thing
  that makes some voters' votes count less.
- **Simple:** five stars to vote, addition to count.

**Larry:** And counting?

**Adam:** This is the sleeper feature. STAR is **precinct-summable** — each
precinct reports its score totals and a small for/equal/against table, and you
just add precincts together. No shipping every ballot to one central computer.
That means fast results, easy audits, and it works with paper ballots and vote-
by-mail. Any citizen can re-add the numbers.

> [SLIDE] Full Deck — "WHAT DO WE WANT IN A VOTING METHOD?", "FAIR-ACCURATE-EQUAL",
> the accuracy chart ("YOU ARE HERE / YOU COULD BE HERE"), and the summability
> slides.
> [REPO] `00_start_here/Why_STAR_Voting.md` — Slides 5–9 bullets.

---

## Segment 6 — STAR vs RCV-IRV (the honest comparison)

**Larry:** Ranked Choice Voting is the one people have heard of. How is STAR
different — and be fair, what does RCV do *well*?

**Adam:** Fair is the right instinct. RCV-IRV is a real improvement over Choose-One,
and where there are only two viable candidates it cleanly kills the old "Nader"
spoiler. Credit where due. But it has structural problems that STAR doesn't, and
they show up exactly in the competitive races that matter most.

**Larry:** Name the big ones.

**Adam:** Three:
1. **It doesn't count all your rankings.** RCV-IRV only ever looks at your top
   *remaining* choice each round. If your favorite is eliminated, your next
   choice is counted — but only sometimes, depending on the order of
   elimination. Lots of marked rankings are simply never read.
2. **Exhausted ballots.** When your ranked candidates are all eliminated, your
   ballot is discarded. On average around 10–11% of ballots aren't counted in the
   deciding round of competitive races, so the "majority winner" is often a
   majority of *remaining* ballots, not of voters.
3. **Center squeeze.** A broadly-liked moderate can be eliminated early precisely
   because few people rank them *first* — and the polarizing candidate the
   majority actually opposed wins. That's the spoiler effect sneaking back in.

**Larry:** Do you have a real election, not a thought experiment?

**Adam:** Two famous ones.
- **Burlington, Vermont, 2009:** Montroll was preferred head-to-head over *both*
  opponents — the candidate the majority actually wanted — but he had fewer
  first-choice votes, so RCV-IRV eliminated him early and Kiss won. The city repealed
  RCV-IRV afterward.
- **Alaska 2022 special:** Begich would have beaten either opponent head-to-head,
  but the two Republicans split and Begich was eliminated; Peltola won and the
  seat flipped. Voters who ranked Palin first effectively helped elect their last
  choice — favorite betrayal, live.

**Larry:** So how does STAR avoid all that?

**Adam:** Because the score ballot lets you fully support everyone on your side at
once — the coalition doesn't split — and STAR counts *every* ballot in *both*
rounds. Nothing is exhausted, nothing is ignored. And it's summable, which RCV-IRV
structurally is not: RCV-IRV needs every ballot in one place to know the elimination
order, so you can't tally precincts independently or report meaningful early
results.

**Larry:** Give me the one-card scorecard.

**Adam:**

| | Choose-One | RCV (IRV) | STAR |
|---|---|---|---|
| Spoiler / vote-splitting? | Yes | Yes, with 3+ viable | **No** |
| Wasted / exhausted ballots? | Yes | Yes (~11% avg) | **No** |
| Summable / local tally? | Yes | **No** | **Yes** |
| Accuracy (voter satisfaction) | ~72–86% | ~80–91% | **~91–98%** |
| Strategy incentive | strong | weak | **lowest** |

**Larry:** And the honest caveat?

**Adam:** No method is perfect — that's a theorem, not an opinion (Gibbard). STAR
isn't strategy-*proof*, just strongly strategy-*resistant*. And it's not formally
Condorcet-compliant — very rarely it won't elect the pairwise winner. But when it
diverges, it's choosing a candidate with broad, strong support over a
weakly-liked compromise — and that's a defensible philosophical call, not a bug.
Saying that out loud is what earns you the room.

> [SLIDE] Full Deck — "RCV COMMON FALSE CLAIMS" table, "Burlington 2009",
> "Alaska '22 Special", "Single-Winner Voting Method Scorecard" (Torrance deck).
> [REPO] `00_start_here/Why_STAR_Voting.md` Part 2 — Tier 1 #2/#3 and Tier 3 #9
> (later-no-harm / center squeeze) for the rebuttals.
> [DEMO] Optional: run a strict 4-candidate file through both engines and show
> the `[Divergence from STAR]` block where RCV-IRV and STAR disagree.

---

## Segment 7 — Wrap & call to action

**Larry:** Bring it home. Why should I care today?

**Adam:** Because the ballot is upstream of everything — polarization, money in
politics, who even gets to run. Fix the ballot and you loosen all of it. STAR is
the simplest change that lets you vote your conscience, guarantees a real majority
winner, and stays easy to count and trust. It's the next generation of voting
reform, and you can try it in about thirty seconds.

**Larry:** Where?

**Adam:** Go to **BetterVoting.com** and cast a STAR ballot right now. Bring it to
your next club, board, or HOA vote — that's how it spreads. And dig into the
science at **equal.vote/accuracy** and **equal.vote/star-vs-rcv**.

> [SLIDE] Full Deck — "GET INVOLVED!" / "LET'S LEAD ON THIS ISSUE!"
> [DEMO] Close by sending the audience to a live BetterVoting poll (QR on screen).

---

## Appendix — quick demo index (files to have open)

| Beat | File | Shows |
|------|------|-------|
| Spoiler | `split_voting/01_political_left_split.yaml` | majority split → minority wins Choose-One; STAR fixes |
| Spoiler (food) | `split_voting/03_lunch_veggie_vs_meat.yaml` | same effect, lighter theme |
| Two rounds | `01_Single_winner/00a_c2_b1_two-candidates.yaml` | gears visible, no surprise |
| Compromise | `01_Single_winner/vote_splitting2.yaml` | 3rd candidate → consensus winner |
| Method divergence | any 4-candidate file with `show_irv` | `[Divergence from STAR]` block |
| Vote-split check | any file with a `blocs:` block | yes/no spoiler verdict in numbers |

See `interviews_conversations/README.md` for the full series plan, slide map,
sync strategy, and demo-software recommendation.
