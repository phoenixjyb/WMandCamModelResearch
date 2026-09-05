# From Camera-Controlled Video to Evidence-Grounded Spatial World Models

## Technical foundations, an audit of current evidence, and a research program for executable cinematography

**Version:** 3.0 — proposed research revision  
**Date and evidence cut-off:** 5 September 2026  
**Prepared for:** Recomo Film Brain  
**Evidence status:** Primary-source review and architectural analysis; no model execution or benchmark reproduction  
**Predecessors:** Frozen repository v1.0/v2.0 and the separately identified original conversation v2.0  
**Reference convention:** R01–R36 retain the prior bibliography identifiers; N01–N35 identify the September audit additions. See [source registry](../SOURCE_REGISTRY.md).

## Abstract

Camera-controlled generation is developing along several intersecting lines: calibrated pose conditioning, ray-aligned attention, explicit geometry transport, synchronized video refilming, spatial memory, and joint visual-geometric modeling. None alone establishes that a generated sequence is a faithful prediction of a real camera or a useful basis for choosing a robot action. This paper reframes the Recomo program around evidence-grounded prediction and selection of executable camera trajectories under partial observability. Atlas remains a significant product-scale statement of native spatial modeling, but neither its disclosed architecture nor a visually compelling comparison establishes a necessary implementation or an absolute geometric tolerance.

Version 3 preserves calibrated camera contracts, revisable external world state, cinematic reasoning, and independent execution authority. It replaces a single capability ladder with a multidimensional profile, updates the comparison set, credits overlapping prior work, and separates offline preview from causal prediction. The proposed contribution is not the existence of a context compiler, memory cache, or director. It is a specific method whose predictions improve realized shot choice, remain compatible across candidate paths, respond correctly to new evidence, and know when observation is preferable to imagination. Four experimental gates test contract correctness, camera fidelity, memory revision, and real decision value before larger training commitments. The document also records a provenance discrepancy between the original v2 attachment and the shorter repository v2; historical sources are not silently rewritten.

## 1. Purpose, scope, and evidence discipline

The application has three different questions: what a shot should achieve, what a camera would observe, and how a physical robot can execute it. A language planner can express narrative intention without supplying valid geometry. A video model can follow a supplied trajectory without inventing that trajectory. A feasible camera path can still produce a poor shot. These responsibilities must be evaluated separately even when they share a learned backbone.

The scope covers camera-conditioned generation, reconstruction, dynamic refilming, spatial memory, action-conditioned observation prediction, and their use in cinematography. Generic visual quality is relevant but insufficient. Contact-rich manipulation and open-domain physical simulation remain related research, not assumed capabilities of the filming model.

Evidence is classified as disclosed architecture, author-reported experiment, released implementation, independently reproduced result, or proposed Recomo design. There are no independently reproduced model results in this revision. Bibliographic identity checks do not validate all numerical claims. A paper, code repository, model listing, accessible weights, usable training data, and permission for commercial deployment are distinct states.

The audit reviewed principal English v2 claims and references plus contemporary primary sources. It did not certify every historical translation, presentation, or rendered page. The 38 audit dispositions are not 38 factual errors: some retain earlier correct distinctions and some guard against interpretations the earlier document already rejected. Editorial incorporation closes a document action, not an empirical research question.

## 2. Camera awareness is a profile, not a total ordering

A camera-controlled generator approximates an observation process:

$$I_t = h(S_{\tau_w(t)}, C_t, K_t, \Pi_t, D_t, L_t) + \epsilon_t.$$

Here S is world state, C is camera pose, K is projective calibration, Pi is the projection family, D describes distortion, and L is the optical/photometric schedule. A world model additionally represents uncertainty about S and its evolution. The filming system chooses controls according to intent and embodiment constraints.

| Dimension | Distinctions that must remain visible |
|---|---|
| Camera | Semantic motion; relative pose; calibrated rays; externally anchored metric trajectory |
| Geometry | Observed surfaces; inferred depth; unseen completion; cross-view consistency |
| Dynamics | Plausible motion; synchronized refilming; out-of-sight evolution; action-dependent transition |
| Memory | Clip continuity; revisitation; cross-path agreement; conflict correction |
| Optics | Intrinsics/projection; distortion; focus/aperture; exposure/shutter |
| Systems | Offline quality; causal response; throughput; working and persistent memory |
| Decision | Visibility and framing prediction; ranking; realized footage; selective acceptance |
| Evidence | Disclosure; paper; usable release; matched reproduction |

There is consequently no single overall SOTA winner established by this review. Compare systems within a task, evidence regime, input budget, and deployment profile. A Pareto comparison is more useful than combining incompatible paper metrics into a league table.

## 3. Evolution: the ideas that remain useful

### 3.1 Pose, rays, and correspondence

MotionCtrl distinguishes camera and object controls; CameraCtrl makes pose information spatially aligned; CamCo and CamI2V introduce geometric correspondence constraints; VD3D brings calibrated control into a video-transformer adaptation [R01, R02, R03, R05, R07]. These are complementary mechanisms, not successive proofs that earlier representations should disappear.

For an undistorted pinhole camera with camera-to-world rotation R and origin o, a pixel p defines the direction d proportional to R K^{-1}p. A Plücker encoding (o cross d, d) identifies a line, not a surface depth. Rays can supply excellent geometry-aware indexing while leaving scale, occlusion, and unseen content uncertain.

AC3D studies where and when camera information enters a pretrained video transformer [R08, R32]. Its findings motivate conditioning ablations, not a universal rule that every new backbone must use identical layers or noise schedules. CogVideoX's 3D VAE compresses spatial and temporal video dimensions; it is not a metric scene model [R06]. The backbone, adapter, checkpoint, and experimental configuration must be named separately.

### 3.2 Geometry transport and dynamic refilming

RealCam-I2V uses estimated metric geometry to support interactive camera control. Its released exploratory CogVideoX implementation must not inherit results from its evaluated DynamiCrafter configuration [R10, R34]. A learned metric-depth prior is useful but is not independent scene metrology.

GEN3C, TrajectoryCrafter, and Uni3C exemplify geometric transport of visible content followed by learned completion [R11, R12, R15]. This decomposition reduces what generation must infer. It does not make estimated geometry infallible or static rendering sufficient for reflections, transparency, dynamics, and all optical settings.

ReCamMaster, CameraCtrl II, BulletTime, RealCam, Track2View, and CameraAnything address different combinations of motion, refilming, camera control, and temporal correspondence [R13, R14, R18, R22, R26, R28]. Refilming a recorded event is not predicting an unconstrained future event. Preserve the distinction between camera time and world time.

### 3.3 Memory and joint modeling

4DiM treats camera and time as core conditions; Matrix3D unifies image, pose, and depth tasks; Rays as Pixels studies joint video-camera modeling [R04, R09, R21]. Joint RGB-depth-camera generation is a proposed extension of the latter, not a result to attribute to it without evidence.

Persistent memory now includes explicit geometry, spatially indexed latent features, pose-based retrieval, and bounded local/global schemes. GEN3C is a historical anchor, not sufficient by itself as the leading contemporary comparison [R11, R25, R29, N06, N07, N08, N09, N10]. The scientific question is how memory trades accuracy, revision, latency, and storage—not whether memory exists.

## 4. Atlas: retain the disclosure, narrow the conclusions

World Labs describes Atlas as pretrained from scratch, with typed multimodal sequences, element-wise autoregression, rectified-flow generation, and posed image/depth inputs. Its published paths are authored, and its explicit 3D products do not establish native mesh or Gaussian tokenization [R30].

The camera comparison changes both the complete model and its control interface. It is a reported system-level preference comparison; it cannot isolate the causal effect of numeric camera inputs, prove metric tolerance, or establish superiority over all specialist systems under equal controls. The reconstruction protocol provides meaningful author-reported evidence, but not an independently reproduced universal ranking [R30].

For Recomo, native camera/world interfaces and reusable spatial context remain strong hypotheses. A hidden global map, complete intrinsic API, exact element granularity, deployed serving topology, and core-model contact physics remain undisclosed. The wider real-to-sim pipeline must be distinguished from the transformer itself [R30, R36].

The counterpart ambition remains legitimate at three levels: functional capability, architectural unification, and scale. They are not one milestone. A modular functional system can test the scientific proposition before a joint model or a large pretraining program is justified. Atlas-like architecture is one experimental branch, not the definition of success.

## 5. Contemporary comparison set and novelty boundaries

### 5.1 Camera fidelity, release maturity, and inference regime

SANA-WM is a relevant efficient contemporary baseline and provides bidirectional and causal configurations. Its recovered-camera evaluation uses Sim(3) alignment, including scale; aligned translation is not absolute metric evidence. Offline-versus-causal results must be associated with the exact configuration, sampling and refinement regime [N01, N02].

SolarWM is relevant to data organization and staged training. Its paper, repository, checkpoint stages, and underlying data access must be checked separately. Do not convert a staged release into a claim that every reported model and all raw training footage are obtainable [N03, N04, N05]. These remain author/release observations, not Recomo reproductions.

### 5.2 Memory and changing worlds

Compare at least an explicit geometry cache, a spatial latent memory, a pose-indexed retrieval method, and a bounded-memory method. WorldStereo, OctWorld, VMem, ReWorld and UCM provide relevant mechanisms [N06, N07, N08, N09, N10]. Mirage's cache reduction must not be described as an equal reduction of total model VRAM; selected attention size in Wonder is not equivalent to bounded historical storage [R25, R29].

LiveWorld explicitly studies out-of-sight dynamics; Flow Equivariant World Models provide another related representation direction [N13, N33]. Dynamic appearance alone is not persistent actor-state prediction. Test re-entry, moved objects, expired observations, and contradictory measurements. Memory that preserves an obsolete scene confidently is not a success.

### 5.3 Reconstruction, orchestration, and action selection

Retain MapAnything/VGGT-era references, but include Depth Anything 3, Pi3/Pi3X and VGGT-Omega in geometry selection; VGGT-World motivates compact predictive geometry features [R17, N19, N20, N21, N22]. The geometry estimator used to label training data must not be the sole evaluator of generated outputs.

GWM Worlds 2 adds director-level controls in a product disclosure. LingBot-World v2, HY-WorldPlay and Cosmos 3 are additional system references whose released configurations must be checked independently of demonstrations [N14, N15, N16, N17, N18]. GenDoP and CineMPC are relevant camera-planning and physical-cinematography precedents; CinemaTraj and ActCam belong in the broader comparison space [N23, N24, N25, N26].

AW4RE overlaps directly with evidence-grounded sensing queries, retrieval and generative completion [N30, N31]. CRONOS and CG-World provide intervention-based precedent; predictive action selection and ensemble futures have further prior work [N27, N28, N29, N34, N35]. Therefore, context selection, a director, counterfactual consistency, or scoring candidate actions is not a novelty claim by itself. A contribution must reside in a new method or a demonstrated capability under an appropriate comparison.

## 6. Research target: compare executable shots in the same uncertain world

Let O denote observations and telemetry, U the shot intent, and C_j a candidate camera/optics trajectory satisfying the current capability envelope. The proposed system predicts outcomes under uncertainty and chooses a candidate, acquires evidence, abstains, or replans.

A useful formulation is:

$$W^{(k)} \sim q(W\mid O), \qquad Y_j^{(k)} \sim p(Y\mid W^{(k)}, C_j).$$

The same world hypothesis k is queried across candidate paths j. Otherwise, independent previews may invent a doorway for one path and a wall for another, producing a biased comparison of invented environments. W may be explicit, latent, or hybrid; shared state and branch lineage must be testable. Reusing a random seed alone is not evidence that two paths share a world hypothesis.

For a camera-only intervention in a nonreactive scene, preserve the event and vary the observation. For physical actions that alter the world or elicit an actor response, share the initial state and exogenous variables while allowing subsequent dynamics to depend on action. Do not freeze an event that the intervention should change. CRONOS and CG-World motivate explicit intervention targets and invariants [N28, N29].

Define regret over a fixed, protocol-defined feasible candidate set:

$$\operatorname{Regret}=V_{\mathrm{real}}(C^*)-V_{\mathrm{real}}(\hat C).$$

C* is the best evaluated candidate, not an unknowable global optimum. Report framing, visibility, execution and blinded artistic preference separately. Any scalar value function and weights must be fixed before the test. Hard safety constraints cannot be traded for aesthetic reward. Uncertainty in measured preferences also belongs in the reported interval.

The non-generative baseline is essential: calibrated geometry, visibility/framing calculations and conventional optimization may already select a good shot. Generative prediction is justified where unseen appearance, identity, occlusion or actor evolution measurably changes the decision. A system that renders less but chooses better is an acceptable outcome.

Evidence acquisition should target expected reduction in decision risk per sensing, motion, latency and compute cost. Compare recent-frame, nearest-pose, coverage-based, uncertainty-based and learned selection under the same budget. Acquiring extra evidence and retrieving existing evidence are different costs. The proposed policy has prior art; its value must be demonstrated rather than inferred from the interface name [N30, N31].

## 7. Architecture: stable contracts, revisable state, replaceable models

The retained logical flow is:

```text
Observations + calibration + telemetry -> PhysicalWorldBelief
Intent + capability envelope -> ShotProgram -> feasible CameraPlan candidates
Belief + candidates -> evidence selection -> SpatialContextPlan
SpatialContextPlan -> ContextCompiler -> typed spatial evidence and queries
Shared world hypotheses -> candidate observations or compact predictions
Independent verification -> select / measure / abstain / revise
CinematicExecutionContract -> local robot checks and execution
```

`PhysicalWorldBelief` manages the best available physical evidence, uncertainty and revision history. Its authority is procedural, not a claim that all its fields are true. `CinematicContinuityState` records accepted narrative and visual decisions. `RendererLocalCache` is model-specific working state and cannot be the only recoverable world record.

`SpatialAnchor` binds an observation or authored reference to pose, world time, identity, calibration and provenance. A `SpatialContextPlan` selects what evidence supports a segment and which questions remain unresolved. The selection policy may be learned or optimized. `ContextCompiler` applies inspectable coordinate/time transformations, visibility calculations, budgeting and packaging. Deterministic serialization is not a substitute for good evidence selection.

Retain `StructuredRollout` as an exportable planning-future interface: predicted entities, visibility, occupancy, uncertainty, and camera/robot state should be inspectable independently of a rendered video. A shared backbone may implement several logical ports. It need not introduce a distinct foundation model for each port.

Two execution profiles are required. Offline preview can use the full proposed path and bidirectional context. Streaming prediction must respect causal information availability and measured response latency. Train or distill between them only where the accuracy/latency trade-off justifies it. A fair causal comparison must not leak future measurements.

Outputs may be RGB-D, point tracks, occupancy, framing, visibility, or latent task predictions. High-quality RGB is optional for decisions that can be made from geometry, but remains important for human review and appearance-sensitive judgments. Memory comparisons should separately measure persistent storage, active context, prefill, retrieval, working tensors and total device use.

## 8. Camera, optics, and temporal correctness

The camera contract carries camera-to-world transforms, K, projection family, distortion, sensor/world timestamps, exposure convention, optional rolling-shutter timing, calibration revision and uncertainty. Optical controls distinguish focal length, focus distance and aperture from gain, exposure and white balance. Sensor dimensions and pixel calibration must agree with any focal length in millimetres.

For a pinhole image-coordinate transform A, update K' = A K. Resize, crop, rotation and padding cannot silently preserve an incompatible K. Declare pixel-center conventions, normalized-coordinate conventions and the mapping between raw frames and temporal video latents. A nonlinear fisheye or distorted projection needs its actual inverse mapping rather than an unqualified K inverse.

Axial depth and range are different. If r is range and d is a unit world ray, X = o + r d. For axial depth z and camera-coordinate ray v = K^{-1}p normalized to v_z = 1, X = o + R(zv). A convention mismatch causes viewpoint-dependent geometric error. Invalid measurements and visibility masks must survive resampling and fusion.

The physical camera transform composes chassis, arm/lift, gimbal and fixed camera calibration. State conventions must specify axis orientation, handedness, transform direction, units, timestamp interpolation and the order of composition. Pure rotation, zoom and weak-parallax sequences need special scale-observability treatment.

Keep three scale tracks: arbitrary-scale reconstruction, externally anchored metric geometry, and learned metric prediction without an external anchor. Sim(3)-aligned results belong to the first track. A fixed calibration registration may be used in the anchored track if estimated independently and its uncertainty is declared. Per-test-output scale fitting must not erase metric error.

These are correctness requirements and proposed tests, not a claim of a complete robotics safety standard. E0 must establish evaluator behavior under known injected errors before model comparisons become credible.

## 9. Evidence, uncertainty, and mode boundaries

Provenance describes origin; it is not a probability. Store observation age, validity interval, calibration revision, source dependencies, association uncertainty and conflicting hypotheses. A measured chair may move. A generated forecast may correctly predict a moved chair, but it is still a hypothesis until independently corroborated. A static priority list cannot replace probabilistic and temporal reasoning.

Confidence must predict a specified event: for example, whether a visibility assertion is correct or whether depth error lies below a declared tolerance. Evaluate reliability, interval coverage and selective risk on held-out scenes. Sample diversity alone is not calibrated epistemic uncertainty. Generated observations derived from one measurement must not be counted as independent confirming measurements.

Creative mode authorizes scene invention. Observational mode predicts a real location and must not invent a passage to make the desired route feasible. Artistic permission and estimated probability of correctness are independent variables. In observational mode, insufficient evidence leads to conservative prediction, sensing, abstention or replanning; it cannot become fictional evidence of free space.

A deterministic optimizer can still act on a stale or incorrect map. Local checks need fresh sensing, conservative margins, actuator and balance constraints, dynamic-obstacle response and recovery. The generative model never has sole execution authority. No safety certification is claimed here.

## 10. Data, interventions, and training

Preserve four data regimes: exact synthetic geometry; Recomo captures with synchronized calibration and robot/lens telemetry; synchronized dynamic multiview capture; and licensed pseudo-calibrated footage. Record measured versus estimated labels and their uncertainty. Do not describe SfM scale or learned metric depth as independently measured truth.

A Recomo capture should link initial evidence, intended trajectory, executed trajectory, actual RGB/depth, lens state, timestamps and observed failure/recovery events. Keep planned-versus-executed deviations separate from prediction error. Dynamic sequential performances are not the same event: exact viewpoint comparisons need synchronized cameras, reproducible staged motion or simulation, with the regime declared.

Intervention samples require a parent-world identifier, branch type, intervention target, invariant state, changed variable and outcome. Observation-only branches differ from action and mechanism branches. Keep branches from one root in one split; otherwise held-out evaluation can leak the same underlying scene [N28, N29].

Use splits by scene, actor, asset family and session, not adjacent frame. Bootstrap intervals at scene/session level. Keep evaluator training separate from final tests. Log all seeds, rejected samples, retries and best-of-N policy. Test multiple levels of evidence coverage and conflicting/stale input, not only attractive camera trajectories.

Training begins with the cheapest experiment that identifies a failure. Camera encoders, geometry adapters, retrieval and uncertainty heads are options, not mandatory networks. Pose losses apply to a pose-prediction branch, not to a fixed supplied camera input. Reprojection supervision requires visibility, valid-depth and dynamic-state masks. Joint RGB/depth/pose learning must be compared with task-specific training for interference and compute cost [R09, R21].

If native spatial unification improves the task, pursue it. If analytic geometry or a compact feature predictor suffices, keep the product implementation small while reserving generative foundation research for capabilities that require it. Neither outcome should be forced by a predetermined parameter count.

## 11. Evaluation and E0–E3 gates

The detailed preregistration template is in [EXPERIMENTS.md](../EXPERIMENTS.md). The experiment outcomes below are proposed; none is reported as executed.

| Gate | Question | Essential controls | Go/no-go interpretation |
|---|---|---|---|
| E0 | Does the contract/evaluator detect known errors? | Scale, K/crop, transform reversal, time offset, depth/range, zoom/dolly, feature-poor negatives | No rankings before failure modes are calibrated |
| E1 | Which camera mechanism and inference regime help? | Same tasks, evidence, trajectories, frame count, seeds, refinement and resource accounting | Retain complexity only for held-out accuracy or useful efficiency |
| E2 | Does memory persist and revise correctly? | Loops, multiple paths, moved objects, stale calibration, dynamic re-entry, conflicts | Do not reward confident preservation of obsolete state |
| E3 | Does prediction improve actual shot choice? | Fixed feasible candidates; analytic, video-only and geometry-conditioned baselines; equal observation budget | Scale the responsible component only after real decision benefit |

Use independent scorecards for camera, world, cinema and robot outcomes. Add systems cost and evidence maturity instead of hiding them inside a single average. Report anchored translation, rotation, intrinsics, reprojection, static/dynamic correspondence, loop closure, cross-path agreement, framing and realized ranking/regret.

Every sample remains in the accounting. Separate generation failure, verified camera violation, evaluator nonconvergence and inconclusive/abstained cases. An operational policy may reject unevaluable output; a scientific analysis must not automatically call every estimator failure a generator error. Report conditional accuracy with its denominator and overall acceptance/failure coverage.

For memory and evidence policies, measure calibration, stale-state false acceptance, repair latency, context acquisition cost and total storage growth. For decision experiments, fix candidate generation or report its contribution separately. Otherwise a better candidate proposer can be incorrectly credited to a better renderer.

Choose metric tolerances and minimum useful decision gains from camera calibration, hardware margins and application needs before final evaluation. Do not invent centimetre-level targets as if the current system already achieves them. An E3 result should include uncertainty over scenes and resource-normalized comparisons, not a favorable demonstration.

## 12. Resources, licensing, and release discipline

Replace fixed GPU/team schedules with scenario budgets anchored in a chosen implementation, trainable parameters, tokens, sequence length, measured throughput, ablation count and evaluation cost. Distinguish inherited pretraining, data preparation, adapter training, causal conversion, distillation, VAE/refiner work and serving.

The 24 GB profile is a deployment target, not an established capability. Profile weights, activations, KV/recurrent state, 3D memory, VAE, temporary tensors, refinement, host RAM and transfer overhead. Denoising time is not total request latency; output frame rate is not interactive generation throughput. Pin precision, device, resolution, duration, sampler, steps, batch size, context policy and refiner status [N01, N02].

Record code, weights, data, redistribution, generated-output use and teacher-data permission separately. Pi3/Pi3X, LingBot-World v2 and SolarWM demonstrate why repository code terms must not be substituted for every upstream artifact's terms [N04, N15, N21]. This document is not legal advice or a license clearance. Recheck exact revisions before adopting a dependency.

A publication release needs a source digest, code/weight identifiers, dataset manifest, evaluator version, full configuration, failure counts and output provenance. The [release-card template](../RELEASE_CARD_TEMPLATE.json) leaves unmeasured values null. A document CI pass validates selected structural properties only; it cannot prove a scientific claim, legal permission, translation equivalence or robot safety.

## 13. Version reconciliation and audit disposition

The original English conversation v2 is 113,313 bytes with SHA-256 263c31369b11ac8bfadc9b7c7c47d229404e94e5db896b222b247eb683dbf530. The repository v2 at the pinned base is 45,171 bytes with Git blob 231186716ac0629dd92583cbbf21e0382c17db08. They differ in text, organization and research cut-off, not merely typography. The Chinese original is independently identified in the reconciliation record.

Version 3 is a new editorial synthesis informed by both the longer original and the audit; it is not an assertion that the shorter repository edition preserved all earlier material. The old repository directories remain unchanged. [RECONCILIATION.md](../RECONCILIATION.md) records source identities, retained ideas, revised claims and deferred archival work. It explicitly distinguishes editorial reconciliation from restoration of every original attachment byte.

All A01–A38 dispositions map to the present sections or supporting protocol. Their status is editorially incorporated with empirical gates still open. Historical model catalogues, old schedules and original claims remain discoverable in their versioned sources, but are not silently carried forward as current findings.

## 14. Final recommendation

Continue toward native spatial intelligence without defining success as imitation of a proprietary architecture. The capability program should preserve generation, reconstruction, refilming and exportable geometry as useful research goals. The Recomo acceptance program should ask a harder application question: do the predictions improve real executable cinematography under equal information and resources?

Keep calibrated interfaces and revisable state; compare geometry, latent and hybrid alternatives; make uncertainty and intervention semantics explicit; retain an offline renderer and a causal predictor where each is useful. Give existing memory, retrieval, counterfactual and camera-planning work proper credit. Measure what the new mechanism adds.

The first decisive result would be a held-out, calibrated study in which Recomo chooses better real shots, recognizes insufficient evidence, corrects stale beliefs, and refuses to invent physical feasibility. If that result holds, scale the responsible component. If it does not, revise the method rather than enlarging an untested assumption.
