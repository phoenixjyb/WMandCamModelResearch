# Slide 01 — Native spatial world models: the v4 research program

From camera-controlled video to spatial foundation modeling and executable cinematography.

Version 4.0 · 6 September 2026 · Research-source presentation.

Presenter note: No model or robot benchmark was executed for this revision. This is the revised argument and experiment program, not a results announcement. References resolve in [the source register](../SOURCE_REGISTRY.csv).

---

# Slide 02 — The scope correction

Spatial-model research must not collapse into robot shot ranking. Product validation must not disappear behind a foundation-model ambition.

Track A studies representation, geometry, generation, dynamics and memory. Track B studies prediction, planning and actual filming. Shared correctness tests connect them.

Presenter note: A foundation result can be valuable before full robot integration; a product feature can succeed with a simpler geometric system.

---

# Slide 03 — What changed from v3

The comparison set now includes Atlas's exact reconstruction specialists, keyframe-first generation, recurrent geometry, global optimization, explicit splats and missing world-model benchmarks.

Evidence coverage, numerical result extraction and our own experiments are separate records. V1–v3 remain intact.

Presenter note: The goal is not a longer model list; it is a stronger set of discriminating experiments.

---

# Slide 04 — Eight capability families

Camera control · reconstruction · novel views and explicit 3D · dynamics · memory · optics · world construction · embodiment.

Each needs its own input regime, metric and resource profile. There is no defensible universal SOTA winner in this review.

Presenter note: An accurate geometry predictor can lack video generation; a compelling video can lack metric control.

---

# Slide 05 — How the field evolved

Pose and rays established camera conditioning. Geometry transport reduced ambiguity. Dynamic refilming separated viewpoint from recorded time. Persistent state and joint modeling broadened the task.

These families coexist. Newer models do not make explicit geometry, retrieval or optimization obsolete [P03,P08,P11,P14,P15,P30–P33].

Presenter note: CogVideoX, AC3D and RealCam-I2V are historical controls, not the boundary of the research.

---

# Slide 06 — Atlas: what is actually disclosed

Posed multimodal sequences, autoregression and rectified flow; generation, reconstruction and explicit 3D products. Camera examples use authored trajectories [P01].

Undisclosed details must remain unknown: exact intrinsic interface, internal map, element granularity, metric tolerance and core-model contact physics.

Presenter note: Study a capability stack and several architecture hypotheses rather than copy an imagined monolith.

---

# Slide 07 — Atlas's five reconstruction comparators

Pi3X posed · Pi3 · VGGT-Omega 1B · Depth Anything 3 · MapAnything [P01–P06,P38].

The task supplies images and poses and predicts points for input pixels. This is not the same as camera-controlled video or held-out appearance generation.

Presenter note: Pi3X is not original Pi3; original VGGT in another paper is not VGGT-Omega.

---

# Slide 08 — A checkpoint warning changes evidence status

The VGGT-Omega model card warns that released-1B results in Tables 1 and 2 may be inflated because of ancestor-checkpoint contamination [P02].

Quarantine affected rows and check overlap. Do not infer that Atlas or all Omega variants are contaminated.

Presenter note: Model cards and corrections are part of literature review, not optional release housekeeping.

---

# Slide 09 — Reconstruction rankings depend on protocol

DA3 Table 3, with-pose regime [P05]:

| Model | ETH3D F1 ↑ | DTU Chamfer mm ↓ |
|---|---:|---:|
| DA3-Giant | 87.1 | 1.85 |
| DA3-Large | 75.2 | 1.23 |
| Original Pi3 | 80.6 | 1.72 |

Presenter note: Author-reported results, not Atlas scores. Dataset rankings differ and poses enter through different conditioning/fusion routes.

---

# Slide 10 — Offline quality is not causal readiness

SANA-WM Table 9, hard paths, same 2.6B/720p stage-1 backbone [P07]: bidirectional rotation error 3.17° versus autoregressive 10.02°; reported memory 49.2 versus 51.1 GB.

Recovered trajectories use Sim(3), including scale. These are particular configurations, not absolute-scale proof or universal serving minima.

Presenter note: The complete requested path is useful information for offline preview. Do not force one regime on both tasks.

---

# Slide 11 — Keyframe-first is a real architecture alternative

WorldStereo 2.0 motivates posed keyframes, spatial memory and temporal synthesis. Its ablations change latent design and trainable blocks [P08].

Test both factors explicitly. Count interpolation, geometry fusion and temporal synthesis—not just keyframe denoising.

Presenter note: A source table can motivate an experiment without isolating the cause of its gain.

---

# Slide 12 — Missing benchmarks and design families

WorldScore: camera/world controllability, quality and dynamics. PIVOT: unseen paths and calibration regimes. CUT3R: recurrent geometry. AnySplat: renderable explicit 3D. Glob3R: global optimization [P09–P13].

Presenter note: PIVOT's initial five drone scenes are useful but not a complete filming benchmark. Discovery is not reproduction.

---

# Slide 13 — Track A: the scientific questions

Can shared spatial learning improve multiple tasks? Can observations be order-robust without losing time? Can uncertain calibration be used correctly? Can memory revise rather than merely retain?

Matrix3D, Rays as Pixels, 4DiM and FantasyWorld are related but distinct precedents [P14,P15,P27,P29].

Presenter note: Added depth output in a video-camera method is a proposed extension, not an inherited paper result.

---

# Slide 14 — Four competing implementations

A0: specialists plus geometric rendering and generative residual.
A1: spatial keyframes plus temporal synthesis.
A2: shared spatial encoder with task-conditioned decoders.
A3: typed autoregressive spatial generation.

Presenter note: Begin with A0 and one alternative. Introduce complexity only to test a named hypothesis.

---

# Slide 15 — Stable interfaces, replaceable models

Evidence → revisable belief → context selection/compiler → spatial queries → geometry and observations → independent evaluation.

PhysicalWorldBelief, SpatialAnchor, SpatialContextPlan and StructuredRollout remain inspectable. Model boundaries may merge; evidence lineage must not disappear.

Presenter note: An interface is an engineering contract, not automatically a novel research contribution.

---

# Slide 16 — Camera correctness before model scale

Update K after image transforms: K' = AK. Distinguish axial depth from range, camera-to-world from its inverse, and frame time from latent time.

Separate arbitrary-scale, externally anchored and prior-only metric tracks. No free per-output scale fit on the anchored track.

Presenter note: Small convention errors can invalidate both conditioning and evaluation.

---

# Slide 17 — Memory must survive contradiction

A measured chair can move. A confident identity can be wrong. Reusing a generated frame does not create independent evidence.

Test stale observations, calibration drift, re-entry and correction latency. Measure persistent storage, selected context and total working memory separately.

Presenter note: Provenance is not calibrated probability; creative authorization is not uncertainty.

---

# Slide 18 — Dynamics and optical formation

Recorded-event refilming is different from future prediction. Camera-only interventions can preserve an event; actions that change the world cannot [P17–P20,P36,P37].

Focal changes, finite aperture, shutter and rolling shutter need explicit tests; pinhole rays alone do not model every optical effect [P22,P34,P35].

Presenter note: Smooth motion is not evidence of correct unseen state evolution.

---

# Slide 19 — Track B: reliable real filming

Intent → feasible camera/optics candidates → predictions → independent selection → local execution.

Shared world hypotheses should support candidate comparisons. A generated doorway must not make a real wall disappear. Cheap geometry/planning is a required baseline [P16,P21,P22].

Presenter note: Robot safety still depends on fresh sensing and local stop/replan authority, not merely deterministic code.

---

# Slide 20 — The experiment program

E0 validates contracts/evaluators. F1 compares geometry. F2 compares generation representations. F3 tests joint learning. F4 tests persistent dynamics and export.

E1 measures offline/causal systems. E2 tests evidence selection. E3 measures actual sensor and shot outcomes.

Presenter note: Track A can advance on F-series evidence; a robotic value claim specifically requires E3.

---

# Slide 21 — Fair comparisons need equal information

Pin checkpoints, inputs, calibration, data splits, refinement, sample counts and resources. Separate native conditioning from ground-truth fusion and future commands from future observations.

Report generation failure, verified error, evaluator failure and abstention separately. Use scene/session-level intervals and no undisclosed best-of-N selection.

Presenter note: Literature means from incompatible protocols cannot become a new aggregate leaderboard.

---

# Slide 22 — Resource and release gates

A 24 GB target requires a measured complete configuration. Include VAE, activations, caches, fusion, refinement, transfers and host RAM.

Code, weights, data, outputs, redistribution and teacher use have separate rights. Staged releases are not complete reproducibility [P23].

Presenter note: Replace broad calendar/GPU promises with a measured scenario budget.

---

# Slide 23 — What remains open

Atlas graphical scores and full benchmark metadata; Omega overlap; deeper shortlist review; actual model/robot runs; original v2 archival bytes; v4 rendered publication QA.

The current stack is bilingual Markdown papers, supporting records and these slide sources—not a claim of rebuilt PDF/DOCX/PPTX or reproduced SOTA.

Presenter note: A green documentation test proves structure and version integrity, not scientific correctness.

---

# Slide 24 — Decision: pursue both tracks, earn each claim

Build native spatial capability with explicit alternatives. Use Recomo to supply calibrated data and real outcome tests. Retain specialists where they win and unify where measured transfer justifies it.

An Atlas counterpart remains a legitimate ambition. The route is falsifiable spatial advances plus independent embodiment evidence—not imitation and not scope reduction.

Presenter note: Read the [white paper](../en/WHITE_PAPER.md), [Atlas dossier](../ATLAS_COMPARISON.md) and [experiment specification](../EXPERIMENTS.md) together.
