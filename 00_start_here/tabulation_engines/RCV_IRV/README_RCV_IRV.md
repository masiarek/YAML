# RCV-IRV — the ranked-ballot tabulation (for comparison)

STAR uses **score** ballots (rate each candidate 0–5). The other family taught in this
repo uses **ranked** ballots, counted by **instant-runoff (IRV)** — what the US usually
calls "RCV." It's a genuinely different count: eliminate the candidate with the fewest
first choices, transfer those ballots to their next choice, and repeat until one
candidate has a majority of the still-active ballots.

Because the count is different, so are its failure modes — center squeeze, exhausted
ballots, non-monotonicity — none of which are STAR's. In this repo, ranked ballots are
tabulated by a **separate** engine; STAR / score files never touch it, and vice versa.

This folder is the RCV-IRV slot in the tabulation-engines hub, next to
[`../BV/`](../BV/README_BV.md) (BetterVoting's display) and
[`../LH_starvote/`](../LH_starvote/reading_a_star_report.md) (the LH STAR report). The
substantive RCV-IRV explainers live with the other concept pages:

- [RCV is a confusing name](../../RCV_IRV/RCV-IRV-confusing-name.md)
- [Is IRV "just plurality"?](../../RCV_IRV/RCV_IRV_and_plurality.md)
- [Center squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md)
- [IRV non-monotonicity](../../RCV_IRV/RCV_IRV_non_monotonicity.md)
- [Exhausted ballots](../../RCV_IRV/RCV_IRV_exhausted_ballots.md)
- [IRV isn't summable](../../RCV_IRV/RCV_IRV_lack_of_summability.md)

Side-by-side with STAR: [STAR vs RCV-IRV, step by step](../../tabulation_star_vs_irv.md)
· [RCV-IRV vs. STAR](../../rcv_irv_vs_star.md).
