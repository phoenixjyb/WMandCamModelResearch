# From Camera-Controlled Video to Spatial World Models

## Technical foundations, a close assessment of World Labs Atlas, and a development blueprint for Recomo

**Version:** 2.0  
**Status:** Current Recomo research position  
**Research cut-off:** 3 September 2026  
**Predecessor:** v1.0 frozen baseline

---

## Abstract

Camera-aware video generation has evolved from semantic motion prompts into a family of increasingly geometric systems. Early methods added pose sequences to pretrained video generators. Later systems converted calibrated cameras into dense ray fields, introduced epipolar attention, aligned translation with metric depth, rendered point clouds or persistent 3D caches along target trajectories, or represented source-to-target 4D correspondence explicitly. A newer line treats camera, RGB, depth, and time as jointly modeled modalities rather than side-channel controls. World Labs' Atlas is the most visible product-scale expression of this latter direction: it is publicly described as a multimodal autoregressive diffusion transformer pretrained from scratch to operate over text, posed images, image sequences, and depth maps in a shared spatial context.

This white paper asks three questions. First, what does camera awareness actually require beyond a visually plausible pan or orbit? Second, what does Atlas genuinely disclose, and what remains unverified? Third, how should Recomo build a functional and eventually architectural counterpart while retaining metric geometry, cinematographic intent, inspectability, and robot safety?

The report concludes that Atlas is a strong research direction but not a complete engineering blueprint. Recomo should adopt the native spatial interface—camera pose, RGB, depth, time, provenance, and uncertainty as first-class variables—while preserving an external authoritative world state and deterministic execution boundary. V2.0 introduces `SpatialAnchor`, `SpatialContextPlan`, and a `ContextCompiler`, separating where the camera moves from what evidence constrains each generated observation. The proposed program progresses through five gates: interface, functional capability, joint-model architecture, physical embodiment, and scale.

---

## Executive summary

The field is moving through four broad paradigms:

1. **Pose as an added condition.** Extrinsics or camera trajectories are injected into an existing video model.
2. **Camera geometry as a dense condition.** Intrinsics and extrinsics are converted into pixel-aligned rays; epipolar or multi-view operators improve correspondence.
3. **Explicit scene geometry as an intermediate representation.** Depth, point clouds, point tracks, or a persistent 3D cache deterministically transport known content to the target camera; diffusion fills disocclusions and uncertain appearance.
4. **Camera, image, depth, and world state as native jointly modeled modalities.** The model learns several inference directions inside one typed spatial context: reconstruct, estimate camera, synthesize a view, generate RGB-D, or jointly propose camera and video.

These paradigms should not be read as a simple replacement sequence. Dense rays remain useful inside explicit-geometry systems; modular geometry remains valuable around a native spatial model. The strongest architecture for a physical filming robot is therefore hybrid:

```text
calibrated camera and optics contract
+ persistent provenance-aware spatial state
+ spatial-context compiler
+ geometry-conditioned generative model
+ cinematic planner and critic
+ independent verification
+ deterministic robot feasibility and execution
```

Atlas strengthens the case for native camera and depth modalities, but its public material does not yet establish centimetre- or metre-level trajectory accuracy, variable per-frame intrinsics, lens distortion control, dynamic loop closure, contact-physics fidelity, reproducible model scale, inference cost, or superiority to specialist explicit-camera systems under a shared calibrated benchmark.

For Recomo, the key differentiation is not merely generating a world along a camera path. It is deciding which path is cinematographically desirable, compiling it into chassis/arm-or-lift/gimbal motion, predicting the resulting observation, and executing it safely.

---

# Part I — Problem definition

## 1. Why camera movement is a special control variable

A normal video generator can treat camera motion as one component of apparent pixel motion. That is insufficient for a filming system. In Recomo, camera movement is simultaneously:

- the principal creative action;
- a calibrated observation operator over a three-dimensional scene;
- a source of parallax, occlusion, and disocclusion;
- a trajectory that must respect time, lens settings, and target framing;
- a physical path allocated across the chassis, arm or lift, wrist, and gimbal;
- a safety-critical command that must be checked before execution.

A useful model must therefore distinguish at least three questions:

1. **What should the shot achieve?** Narrative purpose, subject, composition, motion character, optics, and temporal arc.
2. **What camera observation should occur?** A continuous calibrated camera-and-lens trajectory in a world and time frame.
3. **How can the robot realize it?** A feasible, stable, collision-free motion of the platform and its joints.

Most camera-controlled video papers address only the second question after a trajectory has already been supplied. Atlas' disclosed camera-generation examples likewise use designed camera paths. The Recomo film brain must span all three while preserving their different authorities.

## 2. A capability ladder for camera awareness

The term *camera-aware* is often used too broadly. We use the following ladder.

| Level | Capability | Required evidence | What it does not prove |
|---|---|---|---|
| L0 | Semantic camera language | Correctly responds to phrases such as pan, orbit, crane, handheld | Numeric pose following |
| L1 | Relative extrinsic control | Accepts a sequence of rotations and translations | Metric scale or intrinsics |
| L2 | Calibrated ray control | Uses pose and intrinsics to define a viewing ray for each pixel/token | Surface depth or correct occlusion |
| L3 | Metric scene-aware control | Translation is tied to a metric scene representation | Complete unseen geometry |
| L4 | Cross-view and 4D consistency | Static and dynamic points remain coherent across viewpoint and time | Long-term world memory |
| L5 | Optical camera control | Focal length, projection, distortion, focus, aperture, shutter, exposure | Robot feasibility |
| L6 | Persistent spatial world modeling | Multiple observations, paths, revisits, reconstruction, and generation share a stable scene hypothesis | Guaranteed physical truth or safety |
| L7 | Executable cinematic intelligence | Intent becomes a feasible camera/lens path and verified robot action | Fully autonomous artistic judgment in every domain |

A system may be strong on one level and weak on another. A model can follow an orbit perceptually while translating the wrong metric distance. It can generate smooth footage while changing the room during loop closure. It can estimate internally consistent camera and depth while both disagree with the real world.

## 3. Camera terminology

The standard projective intrinsic matrix is

\[
K_t=
\begin{bmatrix}
f_{x,t}&s_t&c_{x,t}\\0&f_{y,t}&c_{y,t}\\0&0&1\end{bmatrix}.
\]

This is different from:

- **projection and lens calibration:** pinhole, fisheye, equirectangular, radial and tangential distortion;
- **focus and aperture:** focus distance, f-number, depth of field, bokeh;
- **photometric controls:** shutter, ISO/gain, exposure compensation, white balance, response curve.

A counterpart to Atlas should not collapse all of these into an ambiguous field called *intrinsics*. Recomo's camera contract versions them separately.

---

# Part II — How the field evolved

## 4. Stage A: pose-conditioned video generation

### MotionCtrl

MotionCtrl separated camera motion from object motion and conditioned a pretrained video generator on camera poses and object trajectories. Its lasting contribution was conceptual: global viewpoint change and local scene dynamics need distinct controls. A model trained only on ordinary videos can easily entangle them because similar optical flow may arise from a moving camera, moving subject, or both.

### CameraCtrl

CameraCtrl made the condition spatial. Rather than using only a frame-level pose vector, it generated a per-pixel Plücker-ray embedding and injected multiscale camera features into a video U-Net. This representation became a common interface because it aligns camera geometry with image or latent tokens.

For pixel \(\tilde p=[u,v,1]^T\), camera-to-world rotation \(R_t\), camera centre \(o_t\), and intrinsics \(K_t\), the world-space ray direction is

\[
d_{tuv}=\frac{R_tK_t^{-1}\tilde p}{\|R_tK_t^{-1}\tilde p\|}.
\]

A Plücker representation can be written as

\[
\mathcal P_{tuv}=(o_t\times d_{tuv},d_{tuv}).
\]

This says which 3D line a token observes. It does not say where a surface lies on that line.

## 5. Stage B: epipolar geometry and transformer adapters

CamCo and CamI2V introduced epipolar feature aggregation so that cross-view search is restricted by calibrated geometry. VD3D moved calibrated camera conditioning into a video diffusion transformer through a ControlNet-like branch. These systems improved trajectory following and view consistency, but their success remained tied to the pose and motion distribution of training data such as RealEstate10K.

This stage established three lessons:

- dense camera encoding is usually more useful than a global pose token;
- explicit correspondence constraints reduce the burden on learned attention;
- training-data camera distributions strongly determine out-of-distribution performance.

## 6. Stage C: understanding where camera control enters a video DiT

AC3D analysed camera representations inside a pretrained video diffusion transformer. It reported that camera-induced movement is dominated by low spatial frequencies, becomes established early in denoising, and is already linearly recoverable from intermediate representations. It therefore injects camera conditioning only into selected early layers and the earlier portion of reverse diffusion.

The broader design principle is useful beyond AC3D:

> Establish the global coordinate transformation early; preserve later network capacity for local dynamics, identity, appearance, and detail.

AC3D on CogVideoX must be described precisely. The original CogVideoX is a text/video foundation model. Its 3D VAE compresses spatial and temporal video dimensions; it is not a metrically calibrated 3D scene representation. AC3D adds a camera branch to the backbone. Therefore:

\[
\text{AC3D-CogVideoX}=\text{CogVideoX visual prior}+\text{calibrated camera adapter}.
\]

It is not evidence that the base CogVideoX architecture natively models camera calibration or a persistent world.

## 7. Stage D: metric depth and explicit geometry

### RealCam-I2V

RealCam-I2V estimates metric depth from a reference image, backprojects it into a point cloud, aligns relative pose annotations to that estimated metric scene, lets the user design a camera path in the reconstructed space, and uses a rendered geometric preview to shape generation. It is an important bridge from relative camera control toward scene-aware metric control.

The term *metric* still needs care. Accuracy is bounded by the monocular depth model, calibration, scale alignment, and unobserved content. The public CogVideoX1.5 port is also an exploratory implementation rather than the exact DynamiCrafter configuration used for the paper's reported numbers.

### GEN3C

GEN3C makes the geometric/generative split clearer. It maintains a depth-derived 3D cache from the seed and preceding generated frames, renders the cache along the target trajectory, and gives these renderings to the video generator. Known content is transported geometrically; diffusion concentrates on disocclusion, uncertain regions, appearance restoration, and dynamics.

For Recomo, this is a foundational pattern:

\[
\boxed{\text{compute known viewpoint change geometrically; generate what geometry cannot determine}.}
\]

TrajectoryCrafter and Uni3C explore related decompositions using rendered point clouds or point-cloud conditions. They reinforce that a ray field alone is not a scene.

## 8. Stage E: refilming dynamic worlds

When the input is an existing performance video, a target output must preserve not only appearance but world time: actor motion, cloth, liquids, object timing, and lighting changes. ReCamMaster frames this as generative re-rendering with synchronized dynamic multi-view training data. CameraCtrl II broadens spatial exploration and addresses the suppression of object motion under strong camera conditioning. The 2026 RealCam line distils a bidirectional teacher into a causal streaming student for interactive camera-controlled video-to-video operation.

Track2View uses projected 3D point tracks to specify where source content should move in the target view. This progresses from an ambiguous pose condition to explicit 4D correspondence:

\[
\text{pose}\rightarrow\text{rendered geometry}\rightarrow\text{source-target tracks}.
\]

These systems expose a crucial separation:

\[
I=I(T^W_C,\tau_{world}),
\]

where viewpoint and world time are independent. Changing the camera while holding world time fixed yields a bullet-time or novel-view query; advancing world time with a fixed camera yields scene evolution; ordinary video changes both.

## 9. Stage F: the complete camera model

AKiRa, UCPE, DeltaCam, CameraAnything, and related work extend beyond extrinsics. They investigate focal length, field of view, distortion, pitch/roll, gravity, focus, aperture, exposure, native resolution, and compound camera transitions.

This matters because a dolly and a zoom may produce similar framing but different parallax. Recomo must explicitly separate:

\[
T^W_C(t),\quad K(t),\quad \Pi(t),\quad D(t),\quad \mathcal O(t),
\]

where \(\Pi\) is the projection family, \(D\) lens calibration, and \(\mathcal O\) the focus/aperture/shutter/exposure schedule.

## 10. Stage G: cameras as a jointly modeled modality

4DiM already treated images, poses, and timestamps as core variables in a space-time diffusion model. Rays as Pixels advances the idea by encoding camera rays as image-like *raxel* tensors through the same spatiotemporal VAE as video. A single model can infer camera from video, generate video from a specified camera, or jointly generate a synchronized camera/video hypothesis.

This is qualitatively different from a fixed camera adapter. It learns a joint distribution such as

\[
p(I,D,C,t,\text{text}),
\]

rather than only

\[
p(I_{1:T}\mid I_0,C_{1:T}).
\]

The joint formulation supports several directions of inference, but self-consistency is not the same as physical correctness. Training distributions dominated by static scenes and smooth trajectories remain a limitation.

---

# Part III — Atlas: close technical reading

## 11. What World Labs publicly discloses

World Labs describes Atlas as an omni model pretrained from scratch to operate on text, images, video, and 3D. The technical description is more specific: the disclosed native elements include text, images, camera poses, and depth maps; video is represented as sequences of images; each image and depth map is associated with an explicit camera pose. Inputs are arranged in a shared spatial context, and the model generates the next requested element while remaining conditioned on preceding elements.

Atlas is described as a **multimodal autoregressive diffusion transformer**. A useful high-level factorization is

\[
p(E_1,\ldots,E_N)=\prod_i p(E_i\mid E_{<i}),
\]

where a high-dimensional element such as an image or depth map is produced through rectified-flow denoising rather than discrete token sampling.

The public demonstrations include:

- camera-controlled video from one to six images and a supplied trajectory;
- longer generation, including a one-minute 1440p example, using designed camera movement and spatial-context management;
- construction of a spatial scene from images placed at selected positions;
- sparse-view reconstruction and depth prediction;
- point-cloud and 3D Gaussian-splat products derived from posed image/depth output;
- multiple trajectories through a common scene;
- RGB/depth generation along simulated body-camera paths for navigation-oriented real-to-sim work;
- broader real-to-sim-to-real pipelines in which spatial environments are combined with task-specific simulation and representations.

## 12. What the wording does not establish

The public material does not disclose enough to infer a particular hidden 3D representation. *Shared spatial context* could involve posed token conditioning, implicit scene tokens, external geometry, or a combination. It should not be paraphrased as proof of a persistent global voxel map, object-centric scene graph, internal Gaussian field, or bundle-adjusted metric reconstruction unless World Labs publishes that detail.

Likewise, point clouds and Gaussian splats should be described as explicit products constructed from predicted posed geometry, not automatically as native token modalities.

The announcement does not yet provide a reproducible account of:

- model parameter count or active parameter count;
- training-data mixture and calibration quality;
- exact camera encoding;
- explicit per-frame intrinsic interface;
- support for varying focal length or distortion during a shot;
- metric translation tolerance;
- gravity and coordinate conventions;
- loop-closure drift;
- dynamic-scene world memory;
- runtime, peak memory, throughput, and serving cost;
- checkpoint, model card, public API contract, or training code.

## 13. Camera-control benchmark interpretation

The disclosed camera benchmark gives Atlas the desired trajectory through its native camera representation. Selected general video models that lack such an interface receive textual camera descriptions. Human raters judge which output better follows the intended movement.

This is useful evidence for

\[
\text{native geometric camera input}>\text{text-only camera prompting}.
\]

It is not an apples-to-apples comparison against AC3D, RealCam-I2V, GEN3C, UCPE, Track2View, or other specialist systems receiving the same calibrated camera and intrinsic sequence. It also does not report degree-level rotation, metre-level translation, reprojection, focal-length, depth, loop-closure, or object-track errors.

Accordingly, phrases such as *pixel-perfect camera control* remain vendor claims until tested under a metric specialist benchmark.

## 14. The important architectural signal

Despite those limitations, Atlas makes a strong strategic proposition:

> Camera pose, image observation, depth, generation, and reconstruction should share a native spatial sequence interface rather than being assembled only through a late camera adapter.

That proposition is consistent with independent research in 4DiM, Matrix3D, Rays as Pixels, RGB-D world generation, and masked multimodal reconstruction. It is scientifically valuable even before every Atlas product claim is independently verified.

## 15. The overlooked role of context planning

Atlas' examples do not only specify a camera path. They also decide which input images occupy which locations in spatial context, and the long-video description explicitly couples camera movement with spatial-context management. This implies two different plans:

\[
\boxed{\text{CameraPlan}=\text{where and how the camera observes}}
\]

\[
\boxed{\text{SpatialContextPlan}=\text{what evidence constrains each observation}}
\]

The second determines which posed images, depth maps, reference appearances, prior generated frames, world-time slices, and geometric previews should be visible to the model at each segment. This becomes critical when context is finite, observations conflict, multiple references are placed in one scene, or a long trajectory crosses regions with different evidence coverage.

## 16. More views, less imagination

World Labs describes a continuum: with sparse observations Atlas imagines unseen content; with more observations it is increasingly constrained by the actual scene. Recomo should turn this into an explicit engineering contract rather than an informal model property.

Every world region or spatial primitive should record provenance, for example:

```text
MEASURED
MULTI_VIEW_RECONSTRUCTED
DEPTH_ESTIMATED
GENERATED_CONSTRAINED
GENERATED_UNCONSTRAINED
USER_EDITED
UNKNOWN
INVALIDATED
```

It should also record geometry, appearance, metric-scale, and temporal confidence. Evaluation must score observed and generated regions separately.

## 17. Atlas and robotics

For navigation, the disclosed path is concrete: reconstruct or condition a world, simulate a body-mounted camera path, and generate expected RGB/depth observations. This is closely aligned with a Recomo capability target.

For manipulation and interaction, the public claim is broader. World Labs' real-to-sim-to-real framing combines world-model environments with task-specific simulation and may use different representations for different tasks. It should not be interpreted as proof that the same generative checkpoint alone supplies deterministic contact physics.

Recomo should therefore stage embodiment:

1. predict calibrated filming-camera RGB-D along a proposed robot path;
2. validate navigation and visibility consequences;
3. add dynamic actors and object tracks;
4. integrate task-specific simulation;
5. study learned contact dynamics only after matched simulation/reality tests.

---

# Part IV — Recomo architecture v2.0

## 18. Architectural principle

The recommended system is

\[
\boxed{
\text{camera contract}
+\text{persistent world state}
+\text{spatial-context planning}
+\text{geometry-conditioned generation}
+\text{cinematic intelligence}
+\text{independent verification}
+\text{deterministic execution}
}.
\]

The latest model may replace or merge several implementation modules. It must not erase authority boundaries.

## 19. Authoritative states

### 19.1 PhysicalWorldBelief

Contains metric geometry, posed observations, dynamic entities, identities, visibility, camera and robot state, uncertainty, provenance, and calibration. It is authoritative for planning evidence, not because every field is certain but because uncertainty and source are explicit.

### 19.2 CinematicContinuityState

Contains shot phase, narrative and aesthetic arc, composition motif, screen direction, palette, lens character, and accepted continuity decisions. It guides artistic coherence but is not a metric map.

### 19.3 RendererLocalCache

Contains video latents, key/value caches, denoising state, and model-specific memory. It may improve generation but is disposable and must never be the sole world memory.

## 20. Stable logical ports

```text
UserIntentEnvelope
    ↓
CinematicIntentContract + CinematicAestheticSpecification
    ↓
ShotProgram
    ↓
CameraPlan Synthesizer
    ↓
Deterministic Constraint Authority
    ↓
Validated CameraPlan

PhysicalWorldBelief + References + CameraPlan
    ↓
SpatialAnchor construction
    ↓
SpatialContextPlan
    ↓
ContextCompiler
    ↓
Typed SpatialElement sequence
    ↓
Spatial film/world model
    ↓
RGB / depth / camera / confidence / explicit-3D candidates
    ↓
Independent factorized verification
    ↓
CinematicExecutionContract
    ↓
Robot feasibility compiler and PNC/MPC/safety
```

A unified model may implement several ports, but each contract must remain exportable, inspectable, and testable.

## 21. Canonical camera and optics contract

For frame or query time \(t\):

\[
\mathcal C_t=\{T^W_C(t),K(t),\Pi(t),D(t),\tau_s(t),\tau_w(t),\Sigma_t\},
\]

with optional imaging schedule

\[
\mathcal O_t=\{f(t),d_{focus}(t),N(t),s_{shutter}(t),ISO(t),E(t),WB(t)\}.
\]

The contract must version:

- coordinate-frame handedness and axis convention;
- camera-to-world versus world-to-camera transform;
- metric units;
- timestamp and shutter convention;
- rolling-shutter model where relevant;
- projection family and distortion coefficients;
- covariance or confidence;
- calibration provenance.

For the physical platform,

\[
T^W_C(t)=T^W_B(t)T^B_A(q_t)T^A_G(\theta_t)T^G_C,
\]

where \(B\) is the chassis, \(A\) the arm/lift chain, \(G\) the gimbal, and \(C\) the calibrated film camera.

The generative model consumes the resulting camera path. It does not decide, by itself, how yaw, translation, lift, wrist pitch, and gimbal motion are allocated.

## 22. SpatialAnchor

A `SpatialAnchor` binds evidence to a world hypothesis:

```yaml
spatial_anchor:
  scene_id: scene_042
  anchor_id: cam03_t012
  modality: RGBD
  T_world_camera: [...]
  intrinsics: [...]
  projection: pinhole
  distortion: [...]
  sensor_time: 12.040
  world_time: 12.000
  region_or_entity: room_A/person_1
  provenance: MEASURED
  geometry_confidence: 0.97
  appearance_confidence: 0.99
  metric_scale_confidence: 0.96
  validity_interval: [11.95, 12.10]
```

An anchor can also be a user-supplied style/identity reference, a reconstructed keyframe, a generated but validated view, a point map, or a dynamic track set. The type and provenance determine how strongly it may constrain generation and planning.

## 23. SpatialContextPlan

A `SpatialContextPlan` is segment-specific:

```yaml
spatial_context_plan:
  segment: shot_03/segment_02
  camera_interval: [6.0, 10.0]
  world_time_policy: advance
  required_anchors: [cam03_t012, subject_identity_ref]
  optional_anchors: [room_A_reconstruction]
  rendered_geometry: point_map_with_visibility
  observed_coverage_target: 0.72
  imagination_budget:
    unseen_background: medium
    subject_identity: none
    object_layout: low
  memory:
    retain: [subject_tokens, loop_closure_keyframes]
    evict: [low_confidence_generated_views]
  conflicts:
    authority_order: [MEASURED, RECONSTRUCTED, ESTIMATED, GENERATED]
  requested_outputs: [RGB, DEPTH, CONFIDENCE]
```

This plan makes long-horizon context a controllable system component rather than an accidental sequence of prompts.

## 24. ContextCompiler

The compiler is deterministic where possible. It:

1. resolves coordinate and time conventions;
2. transforms anchors into a shared world frame;
3. selects evidence relevant to the target camera frustum and world-time interval;
4. computes ray maps, rendered depth/point maps, visibility, and disocclusion masks;
5. applies provenance and conflict rules;
6. packages typed spatial elements in the model's required ordering;
7. enforces context budget and memory policy;
8. emits a manifest allowing exact replay and evaluation.

The model may learn retrieval suggestions, but the final compiled context should remain inspectable.

## 25. Typed SpatialElement interface

```text
SpatialElement {
    scene_id
    element_id
    modality
    world_timestamp
    sensor_timestamp
    T_world_camera
    intrinsics
    projection_and_distortion
    optical_schedule
    payload_or_latent
    validity_mask
    visibility_mask
    provenance
    confidence
    uncertainty
}
```

Candidate modalities include text, RGB, depth, normals, point maps, ray maps, pose, camera query, video, segmentation, object tracks, scene tokens, and robot actions. Images are one-frame videos at the interface level, but the model may use modality-specific tokenizers.

---

# Part V — Building an Atlas counterpart

## 26. Three meanings of counterpart

### Functional counterpart

A modular system that accepts sparse posed or unposed images/video, reconstructs a scene, follows an explicit camera trajectory, generates RGB-D, reuses the scene across paths, and exports editable 3D.

### Architectural counterpart

A model that jointly represents text, RGB, depth, pose, time, and spatial context; supports multiple inference directions; and autoregressively generates typed high-dimensional elements.

### Scale counterpart

A system matching Atlas' open-domain quality, context capacity, long-duration high-resolution output, broad world knowledge, serving performance, and product reliability.

The first is a credible near-term program. The second is a serious research program. The third requires undisclosed foundation-scale data and compute and should not be used as the first milestone.

## 27. RSFM — Recomo Spatial Film Model

The proposed model combines five ideas:

1. Atlas-like typed spatial sequences;
2. Matrix3D-style masked multimodal training;
3. Rays-as-Pixels-style joint camera/video latent modeling;
4. GEN3C-style external geometric memory and rendering;
5. Recomo-specific cinematic and executable-camera contracts.

A useful architecture is autoregressive over elements and rectified-flow-based within an element:

\[
p(E_i\mid E_{<i},S_{external},P_{context}),
\]

where \(S_{external}\) is the authoritative external spatial state and \(P_{context}\) the compiled context plan.

### Tokenizers

- RGB/video VAE with careful preservation of low-frequency camera motion;
- metric depth/geometry VAE using log depth or inverse depth, invalid masks, and confidence;
- deterministic ray/pose encoder;
- optional generative raxel/camera latent;
- text or VLM encoder;
- later, action and dynamic-object tokenizers.

### Attention hierarchy

- local within-frame attention;
- cross-view and space-time correspondence attention;
- compact scene-memory attention over keyframes, entities, tracks, 3D cells or Gaussian clusters, camera history, and provenance.

The model should not attend to every pixel from every prior observation indefinitely.

## 28. Keep several camera representations

No single representation is sufficient. RSFM should compare and combine:

- authoritative numeric pose/intrinsics;
- dense ray or Plücker fields;
- a generative raxel latent;
- rendered metric coordinates/depth/point maps;
- visibility and disocclusion masks;
- source-target tracks for dynamic refilming.

A key ablation is whether joint camera latent modeling adds value after explicit rendered geometry is already supplied.

## 29. Explicit 3D outside the neural context

RSFM should estimate or generate depth, normals, point maps, tracks, camera poses, and uncertainty. A deterministic fusion service should construct point clouds, surfels, 3D Gaussian splats, optional meshes, collision proxies, and semantic/dynamic graphs.

Generated state must not silently overwrite measured state. Conflicts should be retained, scored, and resolved through authority and uncertainty rules.

## 30. Reuse before rebuilding

A functional prototype should initially integrate strong open components rather than train every module from scratch:

- MapAnything, VGGT, or another feed-forward geometry model;
- classical SLAM, bundle adjustment, and metric calibration for verification;
- AC3D as a ray-conditioned video baseline;
- RealCam-I2V as a metric-depth-conditioned baseline;
- GEN3C as an explicit 3D-cache baseline;
- a joint RGB-D world-generation baseline such as HunyuanWorld-Voyager where licensing permits;
- 3DGS or point-cloud fusion;
- a selected open video/world backbone for RSFM continuation pretraining.

Licensing is a research gate. Outputs from a model whose license prohibits training another model must not be used as teacher data.

---

# Part VI — Data and training

## 31. Data tiers

### Tier A: exact synthetic geometry

Use Blender, Unreal Engine, and Isaac Sim to generate RGB, metric depth, normals, optical flow, segmentation, object poses, exact camera calibration, lens parameters, world time, visibility, and dynamic trajectories. Deliberately cover extreme pitch/roll, non-level mounts, rapid translation, close parallax, compound motion, dolly zoom, loop closure, and dynamic actors.

### Tier B: Recomo-native captures

Synchronize the filming camera with robot odometry, IMU, chassis pose, arm/lift encoders, gimbal angles, RGB-D or stereo reference, lens metadata, and timestamps. The unique proprietary tuple is

\[
\{\text{initial observations},\text{planned path},\text{executed path},\text{actual footage}\}.
\]

This enables a product-relevant question: can the model predict what the Recomo camera will actually observe before the robot executes the shot?

### Tier C: synchronized dynamic capture

Use several synchronized ordinary cameras to capture people, articulated objects, cloth, screens, mirrors, reflections, changing illumination, entries/exits, and heavy occlusion. This data is required to separate world time from camera time.

### Tier D: pseudo-calibrated licensed video

Run shot detection, pose/depth estimation, SfM/SLAM refinement, tracking, dynamic/static decomposition, reprojection checks, and licensing filters. Retain data quality classes:

```text
A — exact calibrated
B — high-confidence pseudo-calibrated
C — unposed video
```

Pseudo-poses and monocular metric depth must never be labelled ground truth.

## 32. Curriculum

### Stage 1 — camera and geometry literacy

At low resolution and 4–8 views, train masked directions such as RGB→depth, RGB→camera, RGB+camera→novel RGB, RGB+camera→depth, and sparse RGB-D completion.

### Stage 2 — wider sparse-view context

Increase baseline, intrinsics variation, indoor/outdoor diversity, and partial modality combinations. Measure whether unified training harms specialist camera or depth accuracy.

### Stage 3 — short RGB-D video

Train fixed-camera dynamics, moving-camera static scenes, both moving, metric trajectories, and separate world/camera time.

### Stage 4 — spatial continuation

Generate chunks, validate them, update the external map, recompile context, and continue. Render the external map into each new segment so that neural history is not the only memory.

### Stage 5 — joint camera/video hypotheses

Only after reliable camera-conditioned generation should the model jointly propose video and a camera path. The cinematic planner and feasibility layer still select and validate the proposal.

### Stage 6 — explicit world and action output

Add point maps, normals, tracks, confidence, Gaussian attributes, and eventually robot-action-conditioned predictions.

## 33. Objective design

A plausible loss is

\[
\mathcal L=\lambda_{rgb}\mathcal L_{flow}^{RGB}+\lambda_d\mathcal L_{flow}^{D}+\lambda_R\mathcal L_R+\lambda_t\mathcal L_t+\lambda_K\mathcal L_K+\lambda_{repr}\mathcal L_{reproj}+\lambda_{cycle}\mathcal L_{cycle}+\lambda_{track}\mathcal L_{track}+\lambda_{unc}\mathcal L_{unc}.
\]

Do not optimize only visual diffusion loss. Camera, metric geometry, dynamic correspondence, and confidence calibration require explicit supervision and evaluation.

---

# Part VII — Evaluation

## 34. Test regimes

1. **Calibrated synthetic scenes:** exact geometry, optics, object motion, and world time.
2. **Static Recomo captures:** repeated paths with VIO/odometry, calibration, depth, and reconstruction.
3. **Dynamic real scenes:** people, cloth, reflections, screens, lighting changes, and loop closure.

Every model should receive the same trajectory, calibration, context, frame count, resolution, and evaluator.

## 35. Trajectory suite

- pan, tilt, and roll;
- dolly, truck, pedestal, and crane;
- orbit with a fixed look-at target;
- simultaneous rotation and translation;
- dolly zoom and independent focal changes;
- close-subject parallax and large disocclusion;
- non-level gimbal base with a level world camera;
- chassis yaw locked and unlocked;
- return-to-start loop closure;
- aggressive out-of-distribution motion;
- camera-time and world-time decoupling.

## 36. Four scorecards

### Camera score

- rotation error;
- metric translation ATE/RPE without per-clip scale alignment;
- separately reported scale-aligned path shape;
- focal length, field of view, principal point, and distortion;
- look-at and subject-relative pose;
- smoothness, acceleration, and jerk.

### World score

- metric depth and point-map error;
- reprojection and static-track consistency;
- point-cloud/3DGS accuracy and completeness;
- cross-trajectory consistency;
- loop-closure drift;
- observed versus generated region quality;
- uncertainty calibration.

### Cinema score

- shot size and composition;
- subject screen position and visibility;
- headroom, lead room, screen direction, and continuity;
- lens and depth-of-field strategy;
- motion character and temporal arc;
- visual quality and human cinematographic preference.

### Robot/system score

- reachability, collision, clearance, balance, and stability;
- chassis/arm/lift/gimbal limits;
- execution margin and recoverability;
- peak VRAM, runtime, model-loading overhead, throughput, and failure rate;
- predicted preview versus actual robot-captured footage.

Camera-estimator failure counts as a failed sample, not a row to drop. A beautiful video with the wrong 1.2 m translation is a camera failure; an accurate but badly composed video is a cinema failure.

## 37. Atlas-claim verification suite

A fair evaluation of an Atlas-like model should test:

- the same numeric camera and intrinsic sequence across all compatible models;
- context sizes from 1 to more than 100 observations;
- adding evidence versus adding contradictory evidence;
- multiple paths through one scene;
- loop closure after leaving and revisiting a region;
- observed versus imagined areas;
- metric translation and scale;
- varying focal length and distortion;
- dynamic actors under independent world time;
- RGB-depth-camera mutual consistency;
- export and re-render quality of explicit 3D;
- inference cost and latency.

---

# Part VIII — Program plan

## 38. Five gates

### Gate 1 — Interface

Freeze coordinate, camera, optics, time, provenance, `SpatialAnchor`, `SpatialContextPlan`, typed element, and replay-manifest contracts.

### Gate 2 — Functional capability

Build a modular counterpart: observations → geometry → external 3D cache → target-camera rendering → RGB-D completion → 3D fusion → verification. Demonstrate multiple paths through one scene.

### Gate 3 — Architecture

Train a 1–3B RSFM research model and test joint camera/RGB/depth modeling, element autoregression, context compilation, and external-memory conditioning against modular baselines.

### Gate 4 — Embodiment

Compare predicted camera observations with actual Recomo captures under planned and executed paths. A counterpart that cannot predict the platform's own footage has not crossed the embodiment gate.

### Gate 5 — Scale

Increase model and data scale only after measurable gains in metric camera following, world consistency, cross-path reuse, dynamic time separation, and prediction of physical capture.

## 39. Suggested milestones

### Months 0–2

- contracts and coordinate conventions;
- common benchmark and trajectories;
- AC3D, RealCam-I2V, GEN3C, reconstruction, and RGB-D baselines;
- licensing register;
- robot-capture schema.

### Months 2–5

- modular functional counterpart;
- one to six observations;
- 5–10 second 512p/720p RGB-D output;
- point-cloud/3DGS export;
- multiple camera paths through one scene;
- context compiler v1.

### Months 4–10

- RSFM-S, roughly 1–3B parameters;
- 4–16 context views and short video;
- masked multimodal tasks;
- camera, depth, and view-generation directions;
- external spatial memory and provenance.

### Months 9–18

- element-level autoregressive context;
- longer RGB-D continuation;
- joint camera/video hypotheses;
- dynamic world time;
- refilming;
- context-size scaling;
- Recomo embodiment evaluation.

## 40. Deployment profile

A 24 GB GPU is an inference and adapter target, not a plausible foundation pretraining target. The v0.10 deployment profile should use sequential model residency:

1. intent and shot planning;
2. geometry/reconstruction and context compilation;
3. unload heavy geometry models;
4. load the video/world generator;
5. generate and cache candidates;
6. unload and run critics/evaluators;
7. retain only compact camera paths, RGB-D, point maps, scene tokens, tracks, uncertainty, and selected latents.

Teacher models may run on larger cloud hardware; distilled students, quantization, offload, tiled decoding, and low-step generation can target the 24 GB environment.

## 41. Team and compute planning assumptions

A credible first-year core team is approximately 10–14 people spanning video/world models, 3D geometry and SLAM, data engineering, distributed training, graphics/3DGS, evaluation, and robotics/cinematography integration.

Rough planning envelopes—not Atlas disclosures—are:

| Program | Illustrative compute |
|---|---|
| Baselines and adapters | 8–16 high-memory GPUs |
| RSFM-S continued pretraining | 32–64 H100-class GPUs for several weeks |
| RSFM-M architectural counterpart | 128–256 H100-class GPUs for several months |
| Product-scale open-domain parity | Unknown and likely substantially larger |

Scaling should follow evidence, not precede it.

## 42. Principal risks

- multi-task interference between generation, pose, and depth;
- camera-data bias toward smooth, level trajectories;
- pseudo-calibration and metric-scale corruption;
- generated-memory contamination;
- long-horizon drift and false loop closure;
- weak dynamic-scene representation;
- optical control conflated with extrinsic movement;
- model licenses that restrict teacher-data use or distribution;
- benchmarks that hide metric failure behind alignment or dropped samples;
- premature monolithic training before interfaces and baselines are stable.

Mitigations include staged curriculum, exact synthetic data, Recomo-native metric capture, external state and provenance, independent evaluators, frozen test sets, and go/no-go gates.

---

# Conclusion

Atlas is a compelling research direction because it treats camera pose, image observation, depth, reconstruction, and generation as parts of a native spatial interface. That direction is independently supported by the evolution from pose adapters to rays, epipolar geometry, metric caches, 4D tracks, masked multimodal models, and joint camera-video latents.

Atlas should nevertheless be treated as a North Star rather than copied literally. Its public announcement does not yet establish a complete camera/optics contract, metric tolerances, long-term dynamic memory, deterministic physics, reproducible architecture, or equal-condition superiority over specialist systems.

For Recomo, the correct program is

\[
\boxed{
\text{Atlas-like learned spatial intelligence}
+\text{explicit 3D-as-code state}
+\text{cinematic planning}
+\text{independent verification}
+\text{deterministic robot execution}
}.
\]

The distinctive research question is not simply whether a model can render a world along a camera path. It is whether a spatial model can help choose a cinematographically meaningful and physically feasible path, predict the observation produced by the real filming robot, preserve metric and temporal truth where measured, quantify imagination where evidence is absent, and hand the result to a safe execution system.

That is a defensible counterpart to Atlas and a stronger foundation for a camera-centric embodied product.

---

# Primary sources and project references

1. World Labs, **Atlas: A World Model for Spatial Intelligence**, 1 September 2026: https://www.worldlabs.ai/blog/atlas
2. World Labs, **3D as Code**: https://www.worldlabs.ai/blog/3d-as-code
3. World Labs, **Real-to-Sim-to-Real**: https://www.worldlabs.ai/blog/real-to-sim-to-real
4. MotionCtrl: https://arxiv.org/abs/2312.03641
5. CameraCtrl: https://hehao13.github.io/projects-CameraCtrl/
6. CamCo: https://arxiv.org/abs/2406.02509
7. CamI2V: https://arxiv.org/abs/2410.15957
8. VD3D: https://arxiv.org/abs/2407.12781
9. 4DiM: https://arxiv.org/abs/2407.07860
10. AC3D: https://arxiv.org/abs/2411.18673
11. CogVideoX: https://arxiv.org/abs/2408.06072
12. RealCam-I2V: https://arxiv.org/abs/2502.10059
13. GEN3C: https://arxiv.org/abs/2503.03751
14. GEN3C implementation: https://github.com/nv-tlabs/GEN3C
15. TrajectoryCrafter: https://arxiv.org/abs/2503.05638
16. Uni3C: https://arxiv.org/abs/2504.14899
17. ReCamMaster: https://arxiv.org/abs/2503.11647
18. CameraCtrl II: https://arxiv.org/abs/2503.10592
19. RealCam: https://arxiv.org/abs/2605.06051
20. Track2View: https://arxiv.org/abs/2606.15534
21. AKiRa: https://arxiv.org/abs/2412.14158
22. UCPE: https://github.com/chengzhag/UCPE
23. DeltaCam: https://arxiv.org/abs/2605.25266
24. CameraAnything: https://arxiv.org/abs/2607.24591
25. Rays as Pixels: https://arxiv.org/abs/2604.09429
26. Matrix3D: https://arxiv.org/abs/2502.07685
27. MapAnything: https://arxiv.org/abs/2509.13414
28. HunyuanWorld-Voyager: https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager
29. iWorld-Bench: https://arxiv.org/abs/2605.03941
30. Recomo v1.0 white paper and v2.0 Atlas disclosure audits in this repository.
