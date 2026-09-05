# V4 roadmap and research gates

**Status:** Proposed work allocation, not a time estimate or compute commitment. See [EXPERIMENTS.md](EXPERIMENTS.md) and [ARCHITECTURE.md](ARCHITECTURE.md).

## Dual-track objective

Track A pursues native spatial learning, multi-task generalization, geometry/generation coupling, persistent dynamics and explicit 3D. Track B pursues calibrated prediction, useful evidence acquisition, cinematography and real execution. Shared infrastructure should reduce duplication without making robot shot ranking the sole acceptance criterion for foundation research.

| Gate | Required output | Advance criterion | Failure response |
|---|---|---|---|
| G0: correctness and evidence | Versioned task/camera contracts; E0 negative controls; source and release cards | Evaluator detects known faults; source claims carry scope | Repair contracts/evaluator before ranking models |
| G1: strong specialists | F1 geometry and one F2 generation reproduction | Exact variant/data/protocol and failure accounting recorded | Reduce implementation ambiguity; no scale-up |
| G2: alternative design | A0 plus one A1/A2 comparison; A3 only for an explicit question | Controlled mechanism or efficiency benefit | Retain simpler baseline or revise hypothesis |
| G3: joint spatial capability | F3 task transfer, context scaling and order robustness | Gains not explained only by more data/compute | Decouple harmful shared components |
| G4: persistent dynamic world | F4 revision, refilming and explicit-export evidence | Correct re-entry and correction without stale confidence | Improve data/state semantics before longer continuation |
| G5: embodiment | E2/E3 evidence selection, sensor prediction and actual filming | Measurable real benefit over conventional controls | Use simpler product stack while Track A continues |
| G6: scale or deployment | Measured resource model and capability-specific release package | Evidence identifies the responsible bottleneck and permitted use | Do not equate model growth with progress |

G3 and G5 are not a strict serial dependency. A publishable Track A contribution can advance without complete robot integration. A product Track B function can be accepted with classical geometry while model research continues. Both must satisfy shared correctness and provenance requirements.

## Initial priority portfolio

Start with a calibrated geometry comparison covering DA3, Pi3X posed and MapAnything, with additional Pi3 and Omega rows handled according to variant and contamination status. Pair a historical ray-only control with SANA-WM or another reproducible efficient camera model and a geometry-conditioned baseline. Evaluate keyframe-first WorldStereo-style mechanisms without assuming the entire HY-World pipeline must be adopted.

Prioritize WorldScore and PIVOT protocol mapping, because they expose task and calibration distinctions missing from a video-quality-only evaluation. Include CUT3R and a global-optimization alternative when studying persistent geometry. Add CAT4D/LiveWorld-type dynamic tests before claiming a general 4D model. AW4RE and existing camera planners define novelty and comparison obligations for evidence selection and cinematography.

Exact dependencies require release and rights inspection. The plan does not certify that every named checkpoint or training set is available. Sources, roles and review depths are in [LITERATURE_COVERAGE.csv](LITERATURE_COVERAGE.csv).

## Scaling ledger

For each candidate run, record: initialized and newly trained parameters; tokens/views/frames; image and temporal compression; training stages; optimizer states; activation checkpointing; devices and utilization; elapsed training; retries; preprocessing and latent-cache cost; evaluation and refinement cost. Inference records separately include peak device memory, host RAM, persistent state, time to first useful output and total completion.

Use these measurements to produce scenario budgets. The earlier broad GPU/team estimates remain historical planning assumptions, not necessary requirements or Atlas disclosures. A 24 GB profile is accepted only after the complete declared configuration fits and meets useful latency; offload is a trade-off, not a proof.

## Release and rights card

Pin code revision, weight digest, checkpoint stage, data snapshot, camera/optics/time conventions, sampler, precision, refinement, hardware and memory strategy. Separate rights for code, weights, data, outputs, redistribution and teacher training. A repository license alone does not settle all six. Benchmark contamination notices are part of the evidence card and must be checked again at experiment start.

## Publication sequence

The present deliverable is the bilingual v4 research-source stack, revised slide sources and machine-readable evidence/experiment records. It does not declare model results, rebuilt PDF/DOCX/PPTX publications or independent translation certification. A publication release requires rendering and visual review, frozen build dependencies and an artifact manifest. Archive recovery of original v2 attachment bytes is separately tracked and must not be confused with editorial reconciliation.

The first scientific paper should be scoped to the mechanism actually demonstrated by F1–F4, not claim every capability of an Atlas-scale product. The first application report should distinguish prediction, selection and execution, and include a successful cheap baseline even when it weakens the case for generation.
