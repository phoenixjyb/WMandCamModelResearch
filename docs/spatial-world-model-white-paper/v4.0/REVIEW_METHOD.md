# V4 review method and evidence policy

**Date:** 2026-09-06. **Type:** Targeted, documented literature and protocol review. This is not an exhaustive systematic-review certification.

## Search strategy

The review uses task families as search roots: camera-conditioned generation; posed/unposed reconstruction; novel views and explicit 3D; joint spatial learning; world memory; dynamic refilming; world construction; embodied sensing and cinematography. It follows direct Atlas comparators and method/benchmark references, then checks newer related work, official releases, model cards and correction notices. Contradictory evidence remains in the comparison set.

Representative queries used in the v4 preparation included:

```text
camera controlled video world model September 2026 benchmark
spatial reconstruction generation world model September 2026 Atlas Pi3X
camera intrinsic video generation 2026 evaluation SEVA WorldScore
WorldReward world models unified reward action consistency Fudan Tencent 2026
```

The final query was restricted toward primary arXiv/GitHub records. Primary URLs were then opened directly for targeted checks. Repository reads for this research project's own files use the connected GitHub interface. Search-engine snippets or third-party numerical summaries are not used to fill missing Atlas scores.

## Review activities

| Activity | Evidence required | Does not establish |
|---|---|---|
| Identity/abstract check | Correct work, task and primary source | Full methods or result audit |
| Technical reading | Representation, assumptions, training or limitations examined | Reproduction of reported gains |
| Results audit | Exact table, variant, data, units, conditioning and alignment recorded | Independent benchmark result |
| Release inspection | Code/weight/data status, model card, corrections and terms | Complete reproducibility or legal clearance |
| Reproduction | Our execution with exact configuration and measured outcomes | Universal generalization |

A source may have several activities, and a result audit is not automatically complete when some metric metadata remain unresolved. The registry uses explicit scope strings rather than one ordinal confidence value. All v4 `reproduced` fields are false.

## Source and result accounting

The active register contains P01–P38. It does not replace or claim a fresh full read of all 71 historical v3 entries. Sources can be a paper and its separate repository/model card, so count source records separately from unique scientific methods. The coverage ledger groups work by role; it is not a list of completed reproductions.

RESULTS.csv contains protocol-specific literature excerpts, not a synthetic leaderboard. DA3 Table 3, SANA-WM Table 9 and HY-World 2.0 Table 6 form separate groups. Source-native or unresolved metric conventions are marked, not guessed. A result with unresolved alignment cannot support an absolute metric claim.

The direct Atlas reconstruction comparator set is identified from the official article. Exact values from Atlas's graphical panels remain untranscribed in a verified primary record. Preserve that gap. The VGGT-Omega warning applies to identified released-1B paper rows; do not generalize it into a claim about Atlas or every Omega variant.

## Update policy

Recheck a source when a decision depends on its current release status, license, correction notice or checkpoint. Record checked dates and exact revisions when available; a mutable README URL plus checked date is weaker than a pinned content snapshot. Current records do not claim all external pages were archived immutably.

An editorial correction is complete when the document no longer overclaims. An empirical issue remains open until an experiment addresses it. Keep old records and add a new disposition instead of rewriting the historical audit as though it had always been correct.

## Limits

No formal exhaustive search database, deduplicated citation graph or search-saturation claim is supplied. Several new methods have only abstract/project-level coverage. No models, weights or robot experiments were executed. Numerical excerpts remain author-reported. Structural CI checks links, identifiers, schemas and frozen-version integrity; it does not validate external scientific facts or independently certify bilingual equivalence.
