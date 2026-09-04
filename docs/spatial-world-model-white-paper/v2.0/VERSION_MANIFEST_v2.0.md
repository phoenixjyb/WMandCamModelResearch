# Recomo Spatial World Model White Paper — v2.0 Manifest

**Status:** Current research position  
**Date:** 2026-09-04  
**Predecessor:** v1.0 frozen baseline

## Canonical sources

- `en/From_Camera_Controlled_Video_to_Spatial_World_Models_Recomo_White_Paper_v2.0_EN.md`
- `zh-CN/从相机可控视频到空间世界模型_Recomo技术白皮书_v2.0_CN.md`
- `source-audit/en/Atlas_Technical_Disclosure_Audit_and_Recomo_Implications_v2.0_EN.md`
- `source-audit/zh-CN/Atlas技术披露逐项审计与Recomo研发影响_v2.0_CN.md`

## Derived artifacts

The repository build workflow renders editable DOCX/PPTX and reading PDFs from the canonical Markdown. The source documents, not a particular rendering, define the intellectual version.

## Scope of v2.0

V2.0 retains the field review and architecture developed in v1.0, while incorporating a close audit of the World Labs Atlas announcement. It introduces three architectural objects:

1. **SpatialAnchor** — a posed, timed, provenance-aware observation or reference attached to a region, subject, or scene hypothesis.
2. **SpatialContextPlan** — the evidence, coverage, memory, uncertainty, and imagination policy used for each camera-path segment.
3. **ContextCompiler** — the deterministic service that converts authoritative world state, references, camera paths, visibility, provenance, and uncertainty into the typed spatial sequence consumed by a model.

## Frozen decisions

- `CameraPlan` and `SpatialContextPlan` are separate contracts.
- The generative renderer is not the authority for metric pose, robot state, calibration, physical safety, or measured geometry.
- An Atlas-like model may implement several logical ports, but critical contracts must remain exportable and independently verifiable.
- Camera, RGB, depth, world time, provenance, and uncertainty are native research variables.
- External 3D state remains authoritative even when a learned spatial context is used.
- Scale-up is gated by measurable gains in camera accuracy, world consistency, cross-path reuse, and preview-to-reality prediction.

## v1.0 → v2.0 change summary

| Area | v1.0 | v2.0 |
|---|---|---|
| Atlas interpretation | Strategic native-spatial signal | Paragraph-level claim and architecture audit |
| Primary contracts | Camera/lens/time contract | Adds SpatialAnchor, SpatialContextPlan, ContextCompiler |
| Context | Persistent world state + model context | Explicit evidence scheduling and memory policy |
| Geometry | Authoritative external state | Adds observed/reconstructed/generated provenance by region |
| R&D plan | Modular counterpart then unified model | Five gated programs: interface, capability, architecture, embodiment, scale |
| Evaluation | Camera/world/cinema/system metrics | Adds context scaling, cross-path reuse, loop closure, claim-verification suite |

## Reproducibility policy

Every empirical result added after this version must record:

- code and configuration revision;
- model checkpoint and license;
- dataset version and provenance class;
- calibration and coordinate convention;
- whether translation was metrically evaluated or scale-aligned;
- failed pose-estimation samples rather than silently dropping them;
- inference hardware, peak memory, runtime, and failure rate.
