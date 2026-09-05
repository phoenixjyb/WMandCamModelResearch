# World Models and Camera-Aware Video Generation Research

Versioned Recomo research on camera-aware video generation, spatial world models and executable cinematography.

## Current review: v3.0

The audit-driven revision is proposed for review; it has not been empirically validated. It preserves the camera/world interface while shifting acceptance toward evidence-grounded prediction and selection of real executable shots.

- [V3.0 overview](docs/spatial-world-model-white-paper/v3.0/README.md)
- [English white paper](docs/spatial-world-model-white-paper/v3.0/en/WHITE_PAPER.md)
- [中文白皮书](docs/spatial-world-model-white-paper/v3.0/zh-CN/WHITE_PAPER.md)
- [38 audit dispositions](docs/spatial-world-model-white-paper/v3.0/AUDIT_DISPOSITIONS.csv)
- [71 primary-source identifiers and review scope](docs/spatial-world-model-white-paper/v3.0/SOURCE_REGISTRY.md)
- [E0–E3 experimental protocol](docs/spatial-world-model-white-paper/v3.0/EXPERIMENTS.md)
- [Version reconciliation and outstanding archive work](docs/spatial-world-model-white-paper/v3.0/RECONCILIATION.md)

## Version lineage

| Stack | Status | Role |
|---|---|---|
| Camera-aware video research report v1.0 | Frozen repository edition | Historical review and bilingual presentations |
| Spatial world-model white paper v1.0 | Frozen repository edition | Initial integrated research position |
| Spatial world-model white paper v2.0 | Frozen repository edition | Atlas audit and spatial-context contracts; differs from the longer original attachment |
| Spatial world-model white paper v3.0 | Proposed research revision | Audit incorporation, current comparisons, shared-belief decision objective and experimental gates |

The original conversation v2 and repository v2 are not identical sources. The reconciliation record identifies their hashes and treatment. A valid generated PDF does not prove unchanged import of its original source. Existing historical directories are not rewritten by this revision.

## Historical documents

- [Research reports and slide decks v1.0](docs/camera-aware-video-generation/research-report/v1.0/README.md)
- [White paper v1.0](docs/spatial-world-model-white-paper/v1.0/README.md)
- [White paper v2.0](docs/spatial-world-model-white-paper/v2.0/README.md)
- [Historical changelog](CHANGELOG.md)
- [V3.0 changes](CHANGELOG_v3.0.md)

## Validation and publication

Run `python scripts/validate_research_v3.py --base e88e67e3880b94823f1496093706d25952678465` and `python -m unittest discover -s tests -p 'test_research_v3.py' -v` from a Git checkout.

Documentation checks validate references, local links, section numbering, disposition coverage, explicit empirical status and frozen-path integrity. They do not validate model performance or prove factual completeness. V3 is submitted as Markdown review source; no new rendered editions are certified in this PR. The legacy artifact builder is manual and read-only so publication cannot silently rewrite frozen files.

## Research position

A shared model may implement multiple ports, but physical belief must remain revisable, predictions must expose uncertainty, and local execution must retain fresh safety checks. A visually convincing imagined scene is not evidence that a real robot path is feasible. Additional model complexity must earn its place through matched capability or real decision gains.

## License

No new reuse license is selected by this PR. Repository publication does not itself grant a separate license beyond applicable GitHub terms. External code, weights, datasets, generated outputs and teacher-data uses require separate checks.
