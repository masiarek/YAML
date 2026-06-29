# Whoops 04 — IRV buries the centrist (Ossipoff, 303 voters)

**Level 301 · the "core support" defense, demolished.** IRV defenders excuse center
squeeze by saying the eliminated moderate "lacked core support" (first-choice votes). This
example (Mike Ossipoff, via [rangevoting.org §12](https://www.rangevoting.org/rangeVirv.html))
kills that defense: candidate **C has the *most* first choices of anyone *and* beats every
rival head-to-head — and IRV eliminates C anyway**, electing D.

A ranked-ballot case (no scores invented). → fairness test:
[`reading_these_fairly.md`](reading_these_fairly.md) · cousin:
[center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md) · [`README`](README.md).

---

## The ballots (303 voters, a 1-D spectrum A…E)

```
 50 : A>B>C>D>E
 51 : B>A>C>D>E
100 : C>D>B>E>A
 53 : D>E>C>B>A
 49 : E>D>C>B>A
```

A realistic "one-dimensional politics" taper — support falls off with distance from each
voter's favorite. Source:
[`Whoops_04_ossipoff_centrist_irv.yaml`](Whoops_04_ossipoff_centrist_irv.yaml).

## C is the favorite by two measures — and still loses

- **Plurality winner:** C has **100 first-choices**, more than any other candidate
  (A 50, B 51, D 53, E 49).
- **Condorcet winner:** C beats *every* rival head-to-head — A 202–101, B 202–101,
  D 201–102, E 201–102 (≈ 2-to-1 each).
- **IRV winner: D.** Here is the elimination, straight from the engine:

```
Round 1:  C 100 · D 53 · B 51 · A 50 · E 49      → E eliminated, flows to D
Round 2:  D 102 · C 100 · B 51 · A 50            → A eliminated, flows to B
Round 3:  D 102 · B 101 · C 100                  → C eliminated (!), flows to D
Final:    D 202 · B 101                          → D wins
```

C — the plurality leader and the candidate a 2-to-1 majority prefers over everyone — is
knocked out in the **last** round and the win goes to **D**, whom most voters rank fourth
or fifth. The "core support" alibi fails on its own terms: C had the *most* core support.

## Why it's a fair, not cheap, example

Sincere ballots, a textbook 1-D electorate (the source calls it "highly realistic"), and
the failure is **structural** — it's the same center-squeeze mechanism, just dramatic
enough to make the point unmissable.

> ### Reading this fairly
> - **How common:** *structural* — center squeeze is a whole region of 1-D electorates;
>   this is a vivid instance, not a knife-edge.
> - **Sincere or strategic:** fully **sincere**.
> - **What IRV does well:** guarantees the final pair has majority support and is simple to
>   explain; the failure is specific to squeezed centrists.
> - **The symmetric whoops:** STAR isn't spotless — see [Whoops 02](Whoops_02_star_misses_condorcet.md),
>   where STAR itself misses the Condorcet winner. The honest tally is in the
>   [README balance ledger](README.md#balance-ledger).
