# V4 experiment specification

**Status:** Proposed protocols, not completed experiments. **Date:** 2026-09-06. References resolve in [SOURCE_REGISTRY.csv](SOURCE_REGISTRY.csv). The numerical literature excerpts in [RESULTS.csv](RESULTS.csv) are not acceptance thresholds and not our results.

## 1. Shared rules

Track A studies spatial-model capability and learning. Track B studies Recomo prediction and execution. Both require E0. Neither track may silently borrow privileged information from the other. The matrix below defines experiments rather than model-name shopping lists.

| ID | Track | Main question | Principal comparisons |
|---|---|---|---|
| E0 | Shared | Are contracts and evaluators correct? | Exact renders and injected negative controls |
| F1 | A | Which geometry representation uses evidence best? | Atlas-named specialists; recurrent and optimization alternatives |
| F2 | A | Which representation improves calibrated generation? | Ray-only; geometry-conditioned; keyframe-first; video-latent |
| F3 | A | Does joint learning improve multiple tasks? | Matched specialists versus shared representation |
| F4 | A | Does the model retain and revise a dynamic world? | Explicit cache; recurrent/latent memory; retrieval; joint model |
| E1 | Shared | What are offline and causal performance frontiers? | Full-trajectory preview versus causal prediction |
| E2 | B/A | When should the system retrieve, measure or abstain? | Budget-matched evidence-selection methods |
| E3 | B | Does prediction improve actual sensor and shot outcomes? | Conventional geometry/planning versus learned predictors |

Every run card must identify code revision, weight digest, base model, adaptation stage, dataset split, camera and depth conventions, input privileges, precision, frame count, resolution, sampling steps, sample count, refinement, hardware, persistent memory and evaluator version. An unavailable system is recorded as unavailable, not assigned a zero score. Distinct checkpoints never inherit a family-level result.

Before observing test outcomes, freeze primary metrics, acceptance margins, sampling policy and statistical unit. Choose margins from product requirements, evaluator noise and a pilot calibration set; do not invent universal centimetre or degree thresholds in a research proposal. Separate hard feasibility constraints from artistic rewards.

## 2. E0 — contracts and evaluator validation

Construct a small exact-render suite with known camera-to-world transforms, K, lens projection, axial depth and range, static geometry, world time and shutter timing. Include texture-rich and feature-poor surfaces, pure rotation, pure dolly, pure zoom, dolly zoom, close parallax, occlusion, extreme pitch/roll and crop/resize operations.

Inject a known scale factor, transposed/inverted transforms, axis flips, stale intrinsics after cropping, swapped axial-depth/range conventions, timestamp offsets and malformed sequences. Check analytic projection and geometry metrics before testing learned camera recovery. Calibrate the recovery pipeline on valid feature-poor cases so that its own nonconvergence is identifiable.

Primary outcomes are detection of known errors, false rejection, evaluator nonconvergence and numerical agreement with exact projection. A failed estimator may make a sample operationally unacceptable, but does not by itself prove generator error. Preserve all outcomes as separate categories.

**Gate:** no camera or geometry model ranking is accepted until the evaluator distinguishes the injected faults. This does not claim complete real-world coverage; it establishes basic identifiability of the metric pipeline.

## 3. F1 — reconstruction and evidence-conditioned geometry

Required specialist configurations are Pi3X posed, original Pi3, VGGT-Omega 1B where evidence permits, DA3 variants and MapAnything [P01–P06,P38]. Add CUT3R for recurrent state, Glob3R for global optimization and a conventional calibrated reconstruction pipeline [P11,P13]. Do not substitute one Pi3 family member or original VGGT for another.

Run separate input regimes: (a) images only with arbitrary-scale evaluation; (b) supplied K and accurate poses; (c) supplied but corrupted poses/K; (d) calibrated metric scale anchors such as stereo baseline or measured depth. Preserve the actual noise distribution and calibration covariance. Ground-truth poses used only in fusion must be distinguished from native pose conditioning.

Measure observed-region point/depth accuracy, held-out reprojection, completeness, scale error where observable, input-order sensitivity, robustness to erroneous priors, time and memory. Evaluate 2/4/8/16 views as initial operating points, then expand only when supported by the method and hardware. These counts are proposed design points, not claimed model limits.

Omega's affected 1B paper rows remain quarantined until the checkpoint notice and benchmark overlap are resolved [P02]. It can be tested on a genuinely independent set with its exact checkpoint recorded; that does not retroactively validate contaminated paper numbers.

**Gate:** choose the strongest practical geometry baseline for each input regime. The selected model need not be generative. Do not select solely on a literature average over incompatible datasets.

## 4. F2 — calibrated generation and representation factorial

Compare A0 geometry-conditioned generation, a current efficient camera model such as a reproducible SANA-WM variant, and one keyframe-first implementation informed by WorldStereo 2.0 [P07,P08,P30]. Retain a historical ray-conditioned adapter as a diagnostic control, not the sole competitor.

The representation experiment crosses (i) keyframe image versus temporal-video latent and (ii) camera-only adaptation versus broader backbone adaptation. Where exact parameter matching is impossible, report trainable parameters, optimizer steps, training tokens and compute. Otherwise the VAE and adaptation schedule remain confounded. Include a temporal synthesis cost when evaluating keyframe pipelines; keyframes alone cannot claim video throughput.

Use matched scene evidence, target paths, timestamps, image preprocessing, output dimensions, frame rate, seeds, number of samples and refinement policies. Score novel views at requested times, not only interpolated easy frames. Include dynamic clips to detect suppression of actor motion.

Primary outcomes: anchored metric camera error where independently measurable; aligned relative error as a different track; observed-region geometry; disocclusion behavior; identity and dynamic timing; visual preference; total runtime and memory. Report each source metric with its units and alignment. Do not mix SANA's aligned camera errors with an unaligned metre-scale claim.

**Gate:** retain a new representation only if its advantage survives the factorial controls and held-out path families. A failure is informative about task fit; it does not prove the representation universally inferior.

## 5. F3 — native spatial learning and task transfer

Compare specialists linked by a contract against a shared evidence encoder and against a typed multimodal generator when its added sequence flexibility is being tested. Matrix3D, Rays as Pixels, 4DiM and FantasyWorld are distinct precedents, not interchangeable claims of RGB-depth-camera output [P14,P15,P27,P29].

Tasks include image-to-geometry, pose-conditioned novel views, multi-view completion, camera estimation when cameras are actually unknown, and optional RGB-D generation. Match initialization, data exposure and training budget. A shared model seeing more modalities must not be credited for architectural benefit without a corresponding data-controlled baseline.

Ablate order-sensitive versus order-equivariant observation encoding. Shuffle whole evidence tuples with their timestamps and poses attached; preserve the query and output order. Repeat with dynamic observations to detect a representation that gains order robustness by discarding necessary temporal information.

Measure each task individually, task interference, transfer to unseen scenes, context-size scaling, parameter reuse and total serving cost. Use camera-output losses only on predicted camera branches. Reprojection losses must be masked for correspondence, visibility and dynamic state. Test whether a metric prior is learned rather than recovered from supplied anchors.

**Gate:** a joint model advances Track A when it offers measurable multi-task or efficiency benefit beyond the controlled specialist system. It need not already improve complete robot shot selection. This is the explicit correction to an application-only scaling rule.

## 6. F4 — persistence, dynamics and explicit products

Compare an explicit geometry cache, a spatial latent/recurrent memory, pose-indexed frame retrieval and a budgeted memory. Include static revisits, two independent paths through one scene, actor disappearance/re-entry, object relocation, contradictory observations and stale calibration. CUT3R and HY-World 2.0 provide relevant state mechanisms; LiveWorld and CAT4D provide different dynamic task precedents [P08,P11,P17,P18]. The inherited v3 memory families require exact implementation review before inclusion.

Separate three regimes: recorded-event refilming, unobserved future evolution and action-dependent changes. A frozen event is valid only for observation interventions on a nonreactive scene. For action-dependent evolution, share initial state/exogenous assumptions, not an invariant future that the action changes [P19,P20].

Explicit-output tests compare point maps, point clouds, splats and optional meshes. Evaluate both input-view geometry and genuinely held-out appearance. AnySplat is relevant to renderable outputs, not a substitute for dynamic-state prediction [P12]. Collision geometry needs a separate validation contract.

Primary outcomes are loop/cross-path point and identity disagreement, stale-state error, correction latency, coverage and calibration of uncertain regions, dynamic timing, storage growth and render quality. Record dependencies between reused generated views to avoid counting one hypothesis as many observations.

**Gate:** persistence must not improve by refusing correct new evidence. Export quality, dynamic fidelity and memory cost remain separate scores.

## 7. E1 — offline and streaming systems profiles

Offline generation may use the entire requested camera path. Causal generation may use future target commands only when supplied by the application, but never future sensor observations unavailable at that decision time. Report this information budget explicitly.

Measure time to first usable preview, total completion time, prefill, retrieval, denoising, VAE, fusion, host/device transfers and refinement. Count persistent world memory separately from active attention and peak device memory. A high playback frame rate is not a generation speed measurement. A cache compression ratio is not a total-VRAM ratio.

For the 24 GB profile, run an exact declared configuration and record peak usage and out-of-memory failures. Offload may trade device memory for host RAM and latency. No fit or service-level claim is made until measured.

**Gate:** select different implementations for offline and streaming if their measured frontiers differ. Autoregression is not a prerequisite for Track A, and bidirectional quality is not proof of interactive readiness.

## 8. E2 — evidence acquisition, freshness and selective prediction

Compare recent frames, nearest poses, coverage heuristics, uncertainty heuristics and a learned/optimized policy. AW4RE is a required related formulation [P16]. Separate retrieval of stored data from physically acquiring a new view: the latter incurs movement, time and safety costs.

At equal budgets, evaluate whether selected evidence reduces task error or decision risk. Include a pose-near but stale observation, a pose-far but informative view, redundant views, corrupted calibration and conflicting identity evidence. An extra view should not automatically receive credit merely because more data was supplied.

Calibrate a specified probability target such as visibility failure, depth-error threshold or forecast interval. Evaluate selective risk versus accepted coverage, not only confidence averages. Creative authorization and epistemic uncertainty remain independent fields.

**Gate:** evidence policy improvements must survive matched data/compute/sensing budgets and out-of-distribution calibration noise. The compiler must expose which evidence was used and why it was admissible even when retrieval itself is learned.

## 9. E3 — real camera prediction and realized cinematography

Use synchronized camera/robot telemetry with planned and executed paths stored separately. For static scenes, repeat a bounded candidate set. For dynamic scenes, use synchronized multiview capture, controlled repeatable motion or simulated branches; do not call separate actor performances exact counterfactuals.

Compare analytic geometry/framing with conventional optimization, a video-only predictor, a geometry-conditioned predictor and the proposed shared-belief method. Keep candidate trajectories fixed for the prediction/ranking test. A separate free-planning test may compare trajectory invention, but it must account for different candidate search budgets. GenDoP and CineMPC are relevant planning references [P21,P22].

Primary measures: observed RGB-D/feature agreement, subject framing, visibility false acceptance, trajectory execution deviation, blinded artistic preference, latency, observation cost and regret relative to the best evaluated feasible candidate. Report objective and human outcomes separately. Aesthetic weights must not trade away hard physical constraints.

**Gate:** Track B scaling requires useful real outcomes beyond cheaper baselines. Track A can independently advance on F1–F4, but claimed robotic value specifically requires E3 evidence.

## 10. Statistical design and benchmark roles

Use scene/session-level uncertainty intervals and hold out actor/asset families. Keep same-root branches within one partition. Register all retries and samples. Bootstrap clustered units, not frames as independent observations. Compare paired cases where possible and report effect sizes with uncertainty, not only a winning mean.

WorldScore supplies camera/world quality and dynamics coverage; PIVOT isolates trajectory/calibration conditions; CRONOS and CG-World clarify interventions; CamWorldQA, WorldExam and WorldArena provide complementary perception/reactivity/function questions [P09,P10,P19,P20,P25,P26,P28]. A learned WorldReward-like evaluator is an optional diagnostic or training signal, never the sole external judge or robot safety authority [P24].

The experimental output is a task-specific performance frontier and failure taxonomy. The review does not pre-register an overall winner and does not certify a proprietary comparison without access.
