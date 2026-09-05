# V4.0 — Native spatial world models and executable cinematography

**Date / evidence cut-off:** 6 September 2026. **Status:** current research-source review edition; not an empirical or rendered-publication release.

V4 rebuilds the program around two connected tracks: native spatial foundation modeling and Recomo embodiment. It expands the task-specific literature comparison, names Atlas's actual reconstruction baselines, carries the VGGT-Omega checkpoint warning, and records numerical evidence with protocol qualifiers. Earlier v1/v2/v3 directories remain unchanged.

## Read the argument

- [English white paper — 18 main sections](en/WHITE_PAPER.md)
- [中文白皮书——18个对应章节](zh-CN/WHITE_PAPER.md)
- [English presentation source — 24 slides](slides/DECK_EN.md)
- [中文演示源稿——24页](slides/DECK_CN.md)

## Inspect the evidence and design

| Record | Purpose |
|---|---|
| [Atlas comparison dossier](ATLAS_COMPARISON.md) | Five named geometry comparators; benchmark caveats and unresolved graphical data |
| [Source registry](SOURCE_REGISTRY.csv) | 38 active records with actual review depth and reproduction status |
| [Literature coverage](LITERATURE_COVERAGE.csv) | Broader task-family shortlist; inherited and newly reviewed work distinguished |
| [Numerical results](RESULTS.csv) | 20 author-reported rows in three source-table protocols; no cross-paper ranking |
| [Review method](REVIEW_METHOD.md) | Search approach and limits of evidence coverage |
| [Architecture alternatives](ARCHITECTURE.md) | A0–A3 choices, contracts, uncertainty and physical boundary |
| [Experiment specification](EXPERIMENTS.md) | E0, F1–F4 and E1–E3 with controls and gates |
| [Roadmap](ROADMAP.md) | Parallel tracks and evidence-based scale/release decisions |
| [Open evidence gaps](OPEN_EVIDENCE_GAPS.csv) | Remaining chart, reproduction, archival, rights and publication work |
| [Reconciliation](RECONCILIATION.md) | Original-v2 discrepancy and frozen-version policy |
| [Version manifest](VERSION_MANIFEST.json) | Machine-readable scope and status |

The active 38 records overlap the [historical v3 index](../v3.0/SOURCE_REGISTRY.md); do not add the counts and call the sum fully reviewed unique papers. The earlier [38 audit dispositions](../v3.0/AUDIT_DISPOSITIONS.csv) remain preserved. Primary references are not our reproduced results.

## Validation

From a Git checkout, run:

```bash
python -m unittest discover -s tests -p 'test_research_v4.py' -v
python scripts/validate_research_v4.py --base ac2fbf5e354e439e0a31a9e425f433dcdc360555
```

Read-only CI checks bilingual section and slide counts, reference identities, source/result schemas, local paths, explicit incomplete statuses and frozen-directory integrity. It produces a review archive and validation record without changing repository content. These checks do not establish scientific truth, complete translation equivalence, model performance or robot safety.

## Publication boundary

Current deliverables are Markdown research and slide sources plus CSV/JSON evidence records. V4 PDF/DOCX/PPTX files are not claimed built or visually reviewed. Historical rendered files are not relabeled v4. Original conversation-v2 bytes remain a separately documented pending archive task. Model/robot experiments are not run. See the open-gap ledger before describing any of these activities as complete.
