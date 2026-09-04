# Changelog

All notable changes to this research repository are recorded here. The intellectual versions are immutable once marked **Frozen**; packaging and link repairs are recorded separately.

## v2.0 — Current — 2026-09-04

### Added

- Paragraph-by-paragraph technical audit of World Labs' Atlas announcement.
- A stricter distinction between Atlas' publicly disclosed native element types—text, posed images, image sequences, camera poses, and depth maps—and downstream fused products such as point clouds or Gaussian splats.
- `SpatialAnchor`, `SpatialContextPlan`, and a deterministic `ContextCompiler` as first-class Recomo interfaces.
- Explicit separation between `CameraPlan` (where/how the camera observes) and `SpatialContextPlan` (which evidence constrains each observation).
- Provenance and uncertainty classes for measured, reconstructed, estimated, generated, unknown, and invalidated world regions.
- Interface, capability, architecture, embodiment, and scale gates for an Atlas-counterpart program.
- Tests for metric trajectory following, context-size scaling, cross-path consistency, loop closure, observed-versus-generated regions, and predicted-preview-versus-actual-robot capture.

### Changed

- Reframed Atlas as evidence for a native spatial sequence interface rather than proof that one closed model has solved metric world modeling, cinematographic planning, or robot execution.
- Strengthened the role of an external, authoritative 3D world state even when an Atlas-like neural spatial context is used.
- Clarified that the camera-controlled Atlas demonstrations use supplied/manual camera paths; they do not publicly establish automatic director-level trajectory planning.
- Revised the Recomo counterpart strategy from "copy a monolithic omni model" to a staged progression: functional counterpart → joint RGB-depth-camera model → native spatial omni model.

## v1.0 — Frozen baseline — 2026-09-03

### Added

- First integrated bilingual white-paper stack on camera-aware video generation and spatial world models.
- Technical taxonomy spanning semantic camera prompting, explicit pose conditioning, dense rays, epipolar constraints, metric depth, rendered 3D caches, 4D correspondence, and joint camera-video modeling.
- Comparative analysis of MotionCtrl, CameraCtrl, CamCo, CamI2V, VD3D, 4DiM, AC3D, RealCam-I2V, GEN3C, TrajectoryCrafter, Uni3C, ReCamMaster, CameraCtrl II, RealCam, Track2View, AKiRa, UCPE, DeltaCam, CameraAnything, Rays as Pixels, and Atlas.
- Recomo reference architecture based on a calibrated camera contract, persistent world state, geometry-conditioned generation, independent verification, and deterministic robot execution.
- Unified benchmark separating camera, world, cinema, and systems/robot metrics.

## Research report v1.0 — Frozen — 2026-09-03

- Initial English and Chinese research reports and a bilingual presentation source covering the evolution of camera-aware video generation and the implications for Recomo.

## Repository packaging notes

- Markdown is the canonical version-controlled source.
- PDF, DOCX, and PPTX files are derived artifacts built from the canonical sources.
- Re-rendering a frozen version does not alter its intellectual version, but any source-content correction requires a new version or an explicit erratum.
