# Spatial world models for executable cinematography — v3.0

**Status:** Proposed audit-driven research revision, pending PR review.  
**Evidence cut-off:** 2026-09-05.  
**Empirical status:** Literature/disclosure analysis and proposed experiments; no models or robot benchmarks have been reproduced for this revision.

## Read

- [English technical white paper](en/WHITE_PAPER.md)
- [中文技术白皮书](zh-CN/WHITE_PAPER.md)
- [Primary-source registry](SOURCE_REGISTRY.md)
- [Audit disposition matrix](AUDIT_DISPOSITIONS.csv)
- [Version reconciliation and provenance](RECONCILIATION.md)
- [Experiment protocol](EXPERIMENTS.md)
- [Release and resource card](RELEASE_CARD_TEMPLATE.json)

The English and Chinese papers follow the same 14-section argument. Neither is presented as a byte-preserving translation of the older editions. The historical survey remains in v1/v2; v3 reorganizes the research program rather than appending a model list.

## Changes that matter

1. Replace an overall capability ladder with independent capability and evidence dimensions.
2. Keep Atlas as an important reference, not the unique architecture or a causal camera-interface ablation.
3. Add task-specific contemporary comparison families and explicitly credit related retrieval, counterfactual, memory, and cinematography work.
4. Define shared-world candidate prediction, calibrated uncertainty, evidence acquisition, and realized shot-selection value as testable research objectives.
5. Separate offline preview and causal streaming; allow compact geometry/task predictions instead of always rendering video.
6. Make metric scale, crop/intrinsic transformations, depth semantics, temporal validity, evaluator failure, and local safety explicit.
7. Replace speculative scale commitments with E0–E3 gates and measured release cards.
8. Preserve existing v1/v2 repository files. Record the original-attachment/repository discrepancy rather than silently calling the shorter v2 an exact import.

## Publication policy

Markdown is the review source. This PR does not certify new PDF/DOCX/PPTX rendering or model performance. Legacy files stay frozen. Version-specific publication builds must write outside frozen directories and must be reviewed before being called final editions.

The reconciliation record distinguishes verified hashes, editorial disposition, and byte-archive restoration. A successful documentation CI check is not evidence of complete archival restoration, external factual correctness, or empirical model validation.
