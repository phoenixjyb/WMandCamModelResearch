# World Models and Camera-Aware Video Generation Research

This repository preserves the Recomo research stack on **camera-aware video generation, spatial world models, World Labs Atlas, and executable cinematic robotics**.

The central thesis is:

> A useful filming world model needs a calibrated camera contract, persistent and provenance-aware spatial state, geometry-conditioned generation, cinematic planning, independent verification, and deterministic robot execution.

## Start here

### Current white paper — v2.0

- [English Markdown](docs/spatial-world-model-white-paper/v2.0/en/From_Camera_Controlled_Video_to_Spatial_World_Models_Recomo_White_Paper_v2.0_EN.md)
- [English PDF](docs/spatial-world-model-white-paper/v2.0/en/From_Camera_Controlled_Video_to_Spatial_World_Models_Recomo_White_Paper_v2.0_EN.pdf)
- [中文 Markdown](docs/spatial-world-model-white-paper/v2.0/zh-CN/从相机可控视频到空间世界模型_Recomo技术白皮书_v2.0_CN.md)
- [中文 PDF](docs/spatial-world-model-white-paper/v2.0/zh-CN/从相机可控视频到空间世界模型_Recomo技术白皮书_v2.0_CN.pdf)
- [Atlas disclosure audit — English](docs/spatial-world-model-white-paper/v2.0/source-audit/en/Atlas_Technical_Disclosure_Audit_and_Recomo_Implications_v2.0_EN.md)
- [Atlas 技术披露逐项审计——中文](docs/spatial-world-model-white-paper/v2.0/source-audit/zh-CN/Atlas技术披露逐项审计与Recomo研发影响_v2.0_CN.md)

### Foundational research report and presentation

- [English research report](docs/camera-aware-video-generation/research-report/v1.0/en/camera_aware_video_generation_research_v1.0_EN.md)
- [中文研究报告](docs/camera-aware-video-generation/research-report/v1.0/zh-CN/相机感知视频生成与世界模型研究_v1.0_CN.md)
- [English slide deck](docs/camera-aware-video-generation/research-report/v1.0/slides/camera_aware_video_generation_evolution_recommendations_v1.0_EN.pptx)
- [中文演示文稿](docs/camera-aware-video-generation/research-report/v1.0/slides/相机感知视频生成演进与Recomo建议_v1.0_CN.pptx)

## Version lineage

| Stack | Status | Main contribution |
|---|---|---|
| Research report v1.0 | Frozen | Evolution from pose conditioning through rays, geometry caches, 4D correspondence, and native spatial models. |
| White paper v1.0 | Frozen baseline | First integrated technical white paper and Recomo counterpart proposal. |
| White paper v2.0 | Current | Paragraph-by-paragraph Atlas disclosure audit; adds `SpatialAnchor`, `SpatialContextPlan`, and the context compiler; revises the R&D gates. |

See [CHANGELOG.md](CHANGELOG.md) and the [v2.0 version manifest](docs/spatial-world-model-white-paper/v2.0/VERSION_MANIFEST_v2.0.md).

## Repository layout

```text
docs/
├── camera-aware-video-generation/
│   └── research-report/v1.0/
└── spatial-world-model-white-paper/
    ├── v1.0/
    └── v2.0/
        ├── source-audit/
        └── assets/
```

Each white-paper version includes editable Markdown and Word sources, rendered PDFs, and the figures required for GitHub Markdown rendering. Convenience ZIP bundles are intentionally omitted because Git already provides versioned archival; release bundles can be attached to formal GitHub releases later.

## Version policy

- `v1.0` is frozen as the original baseline.
- `v2.0` is the current research position.
- Future changes should create a new version directory rather than silently rewriting a frozen version.
- Corrections to packaging, broken links, or checksums may be made without changing the intellectual content, but must be recorded in the changelog.

## License

No reuse license has yet been selected for this research stack. Publication in this repository does not itself grant a separate content or software license beyond GitHub's applicable terms.
