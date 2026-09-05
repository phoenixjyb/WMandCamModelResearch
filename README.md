# World Models and Camera-Aware Video Generation Research

Versioned Recomo research on camera-aware generation, spatial world models and executable cinematography.

## Current research-source review — v4.0

V4 pursues two connected tracks: **native spatial foundation-model research** and **Recomo embodied validation**. It compares reconstruction, generation, novel views, dynamics, memory, optics and world construction without reducing the whole program to robot shot ranking or copying an undisclosed Atlas architecture.

- [V4 overview and complete source stack](docs/spatial-world-model-white-paper/v4.0/README.md)
- [English technical white paper](docs/spatial-world-model-white-paper/v4.0/en/WHITE_PAPER.md)
- [中文技术白皮书](docs/spatial-world-model-white-paper/v4.0/zh-CN/WHITE_PAPER.md)
- [Atlas and its five reconstruction comparators](docs/spatial-world-model-white-paper/v4.0/ATLAS_COMPARISON.md)
- [Task-family literature coverage](docs/spatial-world-model-white-paper/v4.0/LITERATURE_COVERAGE.csv)
- [Protocol-qualified result excerpts](docs/spatial-world-model-white-paper/v4.0/RESULTS.csv)
- [Foundation and embodiment experiments](docs/spatial-world-model-white-paper/v4.0/EXPERIMENTS.md)
- [English slide source](docs/spatial-world-model-white-paper/v4.0/slides/DECK_EN.md) / [中文演示源稿](docs/spatial-world-model-white-paper/v4.0/slides/DECK_CN.md)

## Version lineage

| Stack | Status | Role |
|---|---|---|
| Research report v1.0 | Preserved repository edition | Historical review and bilingual presentations |
| White paper v1.0 | Preserved repository edition | Initial integrated research position |
| White paper v2.0 | Preserved repository edition | Atlas audit and spatial-context contracts; differs from longer original attachment |
| White paper v3.0 | Preserved audit revision | Evidence correction, decision-consistent prediction and safeguards |
| White paper v4.0 | Current research-source review | Dual-track scope, deeper comparator records, alternative architectures and expanded experiments |

The original conversation v2 and repository v2 are not identical texts. Their provenance and remaining restoration work are recorded in [v4 reconciliation](docs/spatial-world-model-white-paper/v4.0/RECONCILIATION.md). No historical directory is silently rewritten by this update.

## Historical materials

[Research report and presentations v1.0](docs/camera-aware-video-generation/research-report/v1.0/README.md) · [White paper v1.0](docs/spatial-world-model-white-paper/v1.0/README.md) · [White paper v2.0](docs/spatial-world-model-white-paper/v2.0/README.md) · [V3 audit stack](docs/spatial-world-model-white-paper/v3.0/README.md)

[Historical changelog](CHANGELOG.md) · [V3 changes](CHANGELOG_v3.0.md) · [V4 changes](CHANGELOG_v4.0.md)

## Evidence and publication status

The 38 active v4 source records overlap the 71 historical v3 entries. Neither source count is a count of independently reproduced methods. V4 contains 20 explicitly author-reported numerical rows from three source-table protocols. The exact numeric Atlas graphical panels remain untranscribed from a verified primary artifact.

Current v4 deliverables are bilingual Markdown papers and slide sources, supporting technical documents and CSV/JSON records. No v4 PDF/DOCX/PPTX rendering or page/slide visual certification is claimed. Model/robot experiments, 24 GB performance claims and original-v2 byte restoration remain separate work. See [open gaps](docs/spatial-world-model-white-paper/v4.0/OPEN_EVIDENCE_GAPS.csv).

## Validation

```bash
python -m unittest discover -s tests -p 'test_research_v4.py' -v
python scripts/validate_research_v4.py --base ac2fbf5e354e439e0a31a9e425f433dcdc360555
```

Read-only documentation CI validates source/result records, links, bilingual structure and frozen-version integrity. It uploads review artifacts without committing generated files. A green check is not certification of scientific truth, translation equivalence, licensing, model performance or robot safety. Existing v3 validators remain available for that historical revision.

## License

No new reuse license is selected by this update. Repository publication does not itself grant a separate license beyond applicable GitHub terms. External code, weights, data, outputs, redistribution and teacher uses require separate checks.
