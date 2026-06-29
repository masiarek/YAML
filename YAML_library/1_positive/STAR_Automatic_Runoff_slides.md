# The Automatic Runoff — slide outline

> **Library copy.** Source of truth lives at
> `00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff_slides.md`;
> filed here beside the `Runoff_01–07` test cases.

A presentation deck for STAR's second step, built to **scale 101 → 201 → 301**: open
plain-language for a general audience, then add the machinery (reversal, Equal Support,
two denominators) for a technical/debate crowd. Stop wherever your audience is.

- **Format:** one slide per `##` heading; bullets are the on-slide text, `> Notes:` is
  the speaker note (don't put it on the slide).
- **Live results:** every example slide links the real **BetterVoting** result so you
  can show it on screen, plus the matching repo **lesson** (BV screenshots beside the
  LH text report).
- **Concept hub backing this deck:** [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md)
  · the worked teaching set: [`runoff_overturns_leader/`](../../01_Single_winner/runoff_overturns_leader/README.md)
  · presenter's guide: [`teaching_runoff_reversal.md`](../../01_Single_winner/runoff_overturns_leader/teaching_runoff_reversal.md).

---

## 1 · Title — The Automatic Runoff

- **STAR = Score Then Automatic Runoff.** The runoff *is* the "AR."
- One promise to plant up front: *you can score honestly — and the majority still wins.*
- Today: **how much vs how many**, why the top scorer can lose, and what that buys you.

> Notes: Say the acronym out loud and unpack it — most people hear "STAR" and don't know
> the runoff is half of it. Keep the room's eyes on one phrase: *how much vs how many.*

---

## 2 · The ballot (60 seconds)

- Score every candidate **0–5 stars** — like rating movies. High = love, 0 = no.
- You can give the **same** score to more than one (no forced ranking).
- That's the whole voter experience. Everything next is just *counting*.

> Notes: For a public audience this is the only "how to vote" slide. The runoff is a
> counting rule — voters never do anything extra for it.

---

## 3 · STAR counts in two steps

- **Step 1 — Scoring Round:** add every candidate's stars. **Top two = Finalists.**
- **Step 2 — Automatic Runoff:** look *only* at those two. Each ballot's full vote goes
  to whichever finalist it scored higher. **The finalist more voters prefer wins.**
- Two steps, hand-countable. That second step is the whole point of the method.

> Notes: Resist explaining *why* yet — just establish the mechanism. The "why" is the
> next slide.
> Concept: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md).

---

## 4 · Why a second step at all? — *how much vs how many*

- **Scores measure _how much_** support a candidate has (points).
- **The runoff counts _how many_** voters prefer each finalist (people).
- Points and people aren't the same thing — a few very high scores can inflate a total.
- The runoff makes the winner the **majority's** choice, not the biggest pile of stars.

> Notes: This is the spine of the whole talk. Everything else is an illustration of
> *how much vs how many.* If they remember one phrase, make it this one.

---

## 5 · The runoff keeps the ballot honest

- Without a runoff, the smart move is to score only your favorite **5** and everyone
  else **0** — any in-between score just helps a rival.
- If everyone does that, the 0–5 ballot collapses to 0s and 5s — that's **Approval voting.**
- STAR's runoff removes that incentive: it only asks *which finalist you scored higher*,
  so your honest **3s and 4s still do real work.**
- **The runoff is what lets STAR keep an expressive ballot people can use honestly.**

> Notes: The "strategic scoring degenerates to Approval" argument. Powerful with a
> technical crowd; for a public crowd, the one-liner is "you never have to exaggerate."
> Glossary: [Approval](../../00_start_here/GLOSSARY.md).

---

## 6 · What the runoff does — three buckets

- For each ballot, compare **the two finalists' scores on that ballot:**
  - scored one **higher** → a full vote **For** that finalist;
  - scored them the **same** → **Equal Support** (no preference between these two).
- Finalist with more votes wins. Losers of the score round get **no** second count.
- The result names all three buckets, then states the decisive split.

> Notes: "Equal Support" gets a full slide later (slide 13). Flag it here, don't dwell.
> Concept: [What the round does](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md#what-the-round-does).

---

## 7 · The flow (one picture)

- Scoring Round → **Top two** → each ballot picks its preferred finalist → tally → winner.
- Branch the audience can read off it: if the winner **isn't** the score leader, that's
  a **Runoff Reversal** — the safeguard firing, not a glitch.
- Equal Support leaves the **percentage** but still counts in the **scores**.

> Notes: Show the mermaid flowchart from the concept hub. Don't narrate every node — point
> at the one fork that matters (winner = leader? yes/no).
> Diagram: [The flow](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md#the-flow).

---

## 8 · Live baseline — the runoff *confirms* the leader

- **Runoff 01 (control).** Aspen leads the Scoring Round (12) **and** wins the runoff 2–1.
- Most of the time the score leader is also the majority's pick — the runoff just **checks**.
- Show this first so the next slide's reversal can't look "rigged."

> Notes: Open the BV link live; point at the dashed majority line Aspen clears.
> Live result: <https://bettervoting.com/r2pvc9/results>
> Lesson: [Runoff 01 — confirms the leader](../../01_Single_winner/runoff_overturns_leader/Runoff_01_confirms_leader_r2pvc9.md).

---

## 9 · The key move — the top scorer can *lose*

- A score total **can't tell your #1 from your strong #2** — a 4 looks the same either way.
- So a candidate who's *everyone's solid second choice* can pile up the most stars
  without being *anyone's* first choice.
- The runoff forces the question the total can't answer: *between these two, which is #1?*
- When *how much* and *how many* point at different candidates → **Runoff Reversal.**

> Notes: This is the hardest idea for learners. The "a 4 can't tell #1 from a strong #2"
> line does most of the work — say it slowly.

---

## 10 · Live reversal — the atom

- **Runoff 02 (smallest reversal).** Everyone likes Austin (most stars, 13) — but two of
  three voters *prefer* Boston, so **Boston wins the runoff 2–1 (67/33).**
- Same machinery as the baseline; only the ballots changed.
- BetterVoting itself pops up *"Why is the top-scoring candidate different from the winner?"*

> Notes: Put slide 8 (Aspen) and this side by side if you can — identical mechanism,
> opposite outcome, because the preferences differ.
> Live result: <https://bettervoting.com/yx9447/results>
> Lesson: [Runoff 02 — the atom](../../01_Single_winner/runoff_overturns_leader/Runoff_02_atom_reversal_yx9447.md).

---

## 11 · It's not a small-numbers fluke — at scale

- **Runoff 04.** The atom blown up to nine voters: Maple leads on stars (39), but **Olive
  wins the runoff 6–3** — a clean 2-to-1 majority (67/33).
- Adding voters in the same proportions doesn't rescue the score leader — it makes the
  majority's verdict **louder.**
- *How many* is a headcount; headcounts grow with the crowd, a few enthusiasts' extra
  stars don't.

> Notes: Use this to kill the "cute toy example" objection. Same shape, bigger room.
> Live result: <https://bettervoting.com/bfjqmg/results>
> Lesson: [Runoff 04 — reversal at scale](../../01_Single_winner/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.md).

---

## 12 · The other face — intense minority vs majority *(201)*

- **Runoff 03.** Two voters *love* Dakota (5s) → Dakota tops the scores (22). But three
  others prefer **Eden**, who wins the runoff **3–2.**
- A passionate minority can top the score chart; it can't outvote the majority in the runoff.
- Where Runoff 02 had a *broadly-liked* leader, this is an *intense-minority* leader — same
  reversal, opposite flavor.

> Notes: First 201 slide. Good place to say: STAR rewards breadth of support, not just
> intensity. Eden is also the Condorcet winner — a calm case, no cross-method drama.
> Live result: <https://bettervoting.com/rkgtpk/results>
> Lesson: [Runoff 03 — enthusiasts vs majority](../../01_Single_winner/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.md).

---

## 13 · Equal Support — a cast vote with no preference *(201)*

- Scored the two finalists **the same**? You have **no preference** between *these two* —
  that's **Equal Support**, set aside from the runoff %.
- It is **not an abstention**: it counts fully in the Scoring Round; only a fully-blank
  ballot abstains.
- **Runoff 05.** Rosa leads (21), but two voters rate Rosa = Sage, so **3 of 5** decide —
  and they pick **Sage 2–1.**

> Notes: The single most-confused term in STAR. Hammer "cast vote, no preference ≠ didn't
> vote." This is the bridge to the two-denominator slide.
> Live result: <https://bettervoting.com/xgkw3w/results>
> Lesson: [Runoff 05 — reversal with Equal Support](../../01_Single_winner/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.md)
> · term: [`GLOSSARY`](../../00_start_here/GLOSSARY.md).

---

## 14 · Two denominators — *how many* of *whom* *(201)*

- The winner needs a **majority of voters who expressed a preference** between the two
  finalists — **not** a majority of everyone.
- **% Between Finalists** = out of the *decided* voters; **% Runoff Votes** = out of *all*
  ballots. Same votes, two denominators.
- LH names its denominator inline: *"Voters with a preference: 3 of 5 (2 Equal Support)."*

> Notes: Show the BV Runoff Table (both % columns) and the LH one-line summary together —
> they're the same numbers, different words.
> Detail: [Runoff percentages — two denominators](../../00_start_here/concepts/STAR_Voting/runoff_percentages.md)
> · why the words differ: [reporting_diff_BV_LH](../../00_start_here/concepts/STAR_reporting/reporting_diff_BV_LH.md#same-numbers-different-words).

---

## 15 · A second control — the leader confirmed at scale

- **Runoff 06.** Wren leads the scores (21) **and** wins the runoff **4–1.**
- Bookend to the reversals: the runoff doesn't *change* the answer here — but it **asked
  the question**, which is the safeguard.
- A reversal only happens when *how much* and *how many* point at **different** candidates.

> Notes: Reassures the room the runoff isn't out to overturn leaders for sport. It
> confirms far more often than it reverses.
> Live result: <https://bettervoting.com/d664xw/results>
> Lesson: [Runoff 06 — confirms at scale](../../01_Single_winner/runoff_overturns_leader/Runoff_06_confirms_at_scale_d664xw.md).

---

## 16 · Variations to know

- **Exact tie in the runoff** → even split → **tie-break ladder** (Scoring Round, then a
  documented lot). On a true 50/50 the % line is suppressed.
- **Two candidates** → the Scoring Round is a formality; the runoff *is* the election.
- **Everyone gives everyone 5** → all Equal Support → tie → ladder decides (the silly case).

> Notes: Keep this brisk — it's the "edge cases exist and are handled" slide.
> Detail: [Variations](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md#variation-2--exact-ties).

---

## 17 · Devil's advocate — the questions you'll get

- *"Most stars = most popular, how can he lose?"* — Most stars ≠ most preferred. Stars say
  *how much*; the runoff counts *how many*.
- *"Then just crown the highest total!"* — Then everyone votes 5s-and-0s and STAR becomes
  Approval. The runoff keeps scoring honest **and** guarantees a majority winner.
- *"Isn't it unfair to the score leader?"* — They didn't win; they earned a **spot** in
  the runoff. Leading the scores makes you a finalist, not the office-holder.
- *"Could the winner be almost nobody's favorite?"* — No: preferred **head-to-head by a
  majority** of decided voters.

> Notes: These are verbatim the questions audiences ask. Full list with answers:
> [Quick questions](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md#quick-questions-the-ones-learners-actually-ask).

---

## 18 · What the runoff buys you

- A **majority-backed** winner — beats the runner-up among voters with a preference.
- **Honest scoring is safe** — no reward for exaggerating; the 0–5 ballot doesn't degrade
  to Approval.
- **Resists intensity capture and center squeeze** — a loud minority can't win on volume;
  a broadly-acceptable middle candidate isn't eliminated early (unlike **IRV**).
- Still **simple** — two steps, easy to hand-count.

> Notes: "Center squeeze" is an **IRV**-specific failure — name IRV precisely here, not
> "RCV." STAR's runoff is what avoids it.
> Comparison: [center squeeze, STAR vs IRV](../../01_Single_winner/center_squeeze_star.yaml).

---

## 19 · …and its limits *(301)*

- It only considers the **top two**: a candidate who'd beat *both* finalists but finished
  3rd never enters — so STAR can, rarely, **miss the Condorcet winner.**
- The reversal **surprises** people; unexplained, it can feel illegitimate (the cost these
  lessons exist to fix).
- One extra step + the Equal-Support wrinkle (two denominators) over a plain score count.
- Like every method, it **can't satisfy every fairness criterion at once** (Arrow/Gibbard).

> Notes: Don't hide the limits — naming them honestly builds credibility. Keep the
> Condorcet-miss for 301; it's not a beginner's first lesson.
> Detail: [three winner notions](../../00_start_here/concepts/STAR_Voting/STAR_three_winner_notions.md).

---

## 20 · Reading the real reports — BV vs LH *(201/301)*

- BetterVoting and the LH engine show the **same numbers in different words** — match them
  once and either report is readable.
- LH folds BV's *Runoff Votes* + *% Between Finalists* + *Equal Support* into one
  self-reconciling line that **names its denominator**.
- Every example in this deck has both views side by side in its lesson file.

> Notes: For an audience that will actually run elections. Skip for a pure intro talk.
> Detail: [reporting_diff_BV_LH](../../00_start_here/concepts/STAR_reporting/reporting_diff_BV_LH.md)
> · the full set: [`runoff_overturns_leader/`](../../01_Single_winner/runoff_overturns_leader/README.md).

---

## 21 · A live edge case — when a tool gets it wrong *(301, WIP)*

- **Runoff 07.** A flat `3,3,3` ballot (every candidate equal) is **Equal Support** — a
  cast vote. BetterVoting currently **mis-files it as an abstention**, dropping it.
- Same winner (Blair), but BV's counts and score totals don't reconcile with a hand count
  of all four ballots.
- Tracked as **[bettervoting#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)**;
  kept as a teaching illustration until fixed.

> Notes: Optional 301 capstone — shows the audience how to *audit* a result and why the
> Equal-Support vs abstention distinction (slide 13) actually matters in practice.
> Live result: <https://bettervoting.com/tf73v9/results>
> Lesson: [Runoff 07 — flat ballot / BV bug (WIP)](../../01_Single_winner/runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.md)
> · the bug in full: [`small_case_abstention_lesson.md`](../../01_Single_winner/pet_real_bv_election/small_case_abstention_lesson.md).

---

## 22 · Recap — one slide to remember

- STAR = **S**core **T**hen **A**utomatic **R**unoff. The runoff is the second half.
- **Scores = how much. Runoff = how many.** The majority's pick wins.
- The runoff lets you **score honestly** and still get a **majority winner** — and when
  it overturns the leader, that's the safeguard *working.*

> Notes: End on the promise you opened with (slide 1). If you only had three sentences,
> these are them.
> Concept hub: [The Automatic Runoff Round](../../00_start_here/concepts/STAR_Voting/STAR_Automatic_Runoff.md)
> · teaching guide: [`teaching_runoff_reversal.md`](../../01_Single_winner/runoff_overturns_leader/teaching_runoff_reversal.md).

---

## Appendix — every example at a glance

| # | Slide | Level | BetterVoting result | Repo lesson |
|---|-------|:---:|---------------------|-------------|
| 01 | confirms the leader (control) | 101 | [r2pvc9](https://bettervoting.com/r2pvc9/results) | [Runoff_01](../../01_Single_winner/runoff_overturns_leader/Runoff_01_confirms_leader_r2pvc9.md) |
| 02 | the atom (smallest reversal) | 101 | [yx9447](https://bettervoting.com/yx9447/results) | [Runoff_02](../../01_Single_winner/runoff_overturns_leader/Runoff_02_atom_reversal_yx9447.md) |
| 03 | enthusiasts vs majority | 201 | [rkgtpk](https://bettervoting.com/rkgtpk/results) | [Runoff_03](../../01_Single_winner/runoff_overturns_leader/Runoff_03_enthusiasts_vs_majority_rkgtpk.md) |
| 04 | reversal at scale (67/33) | 101 | [bfjqmg](https://bettervoting.com/bfjqmg/results) | [Runoff_04](../../01_Single_winner/runoff_overturns_leader/Runoff_04_reversal_at_scale_bfjqmg.md) |
| 05 | reversal with Equal Support | 201 | [xgkw3w](https://bettervoting.com/xgkw3w/results) | [Runoff_05](../../01_Single_winner/runoff_overturns_leader/Runoff_05_reversal_with_equal_support_xgkw3w.md) |
| 06 | confirms at scale (control) | 101 | [d664xw](https://bettervoting.com/d664xw/results) | [Runoff_06](../../01_Single_winner/runoff_overturns_leader/Runoff_06_confirms_at_scale_d664xw.md) |
| 07 ⚠️ | flat ballot / BV bug (WIP) | 301 | [tf73v9](https://bettervoting.com/tf73v9/results) | [Runoff_07](../../01_Single_winner/runoff_overturns_leader/Runoff_07_flat_ballot_bv_bug_tf73v9.md) |

**Suggested cuts by audience:** *public intro (101)* → slides 1–11, 15–18, 22. *Technical
/ debate (201+)* → all of it. *Lightning (8–10 min)* → 1, 3, 4, 5, 9, 10, 18, 22.
