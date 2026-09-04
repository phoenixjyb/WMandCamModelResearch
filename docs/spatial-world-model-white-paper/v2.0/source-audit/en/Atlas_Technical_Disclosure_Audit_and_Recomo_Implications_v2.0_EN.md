# Atlas Technical Disclosure Audit and Recomo Implications

**Companion to the Recomo white paper v2.0**  
**Audit date:** 3 September 2026  
**Primary source:** World Labs, “Atlas: A World Model for Spatial Intelligence,” 1 September 2026

## Purpose and evidence policy

This document records a close reading of the Atlas announcement. It separates four categories:

- **D — directly disclosed:** stated or visibly demonstrated by World Labs;
- **I — reasonable inference:** a conclusion supported by the disclosure but not stated as an implementation fact;
- **U — undisclosed:** required for engineering assessment but absent from the public material;
- **V — vendor claim requiring independent verification.**

The audit does not assume that a product blog is a peer-reviewed architecture paper, nor does it dismiss the blog: it is currently the primary disclosure of a strategically important system.

---

## 1. Product-level claim: an omni spatial model

### Disclosure

Atlas is described as pretrained from scratch to operate on text, images, video, and 3D, and as a multimodal autoregressive diffusion transformer. Inputs are combined into a shared spatial context; the model generates what comes next while maintaining three-dimensional consistency with prior context and imagining beyond observed content.

### Classification

- Pretraining from scratch: **D**
- Multimodal autoregressive diffusion transformer: **D**
- Shared spatial context: **D**, at the level of the product description
- Consistency and imagination claims: **V** unless tied to a defined benchmark
- Exact hidden scene representation: **U**

### Recomo implication

Research camera, image, depth, and time as native co-modelled variables. Do not infer a particular hidden 3D data structure or remove external spatial state.

---

## 2. Native element types

### Disclosure

The technical section is more specific than the opening description. It identifies text, images, camera poses, and 3D depth maps; video is represented as a sequence of images. Images and depth are associated with explicit camera poses.

### Classification

- Text, images, pose, depth as disclosed native types: **D**
- Video as image sequence: **D**
- Point cloud and Gaussian splat as native token types: **not disclosed**
- Mesh as a native token type: **not disclosed**

### Recomo implication

Represent point clouds and 3DGS as fused or exported products unless an implementation explicitly models them as native elements. Define `SpatialElement` around posed RGB/depth first, then extend through ablation.

---

## 3. Autoregression and rectified flow

### Disclosure

Atlas processes a sequence of multimodal elements and generates outputs one at a time. High-dimensional continuous outputs are generated through rectified flow.

### Classification

- Element-level autoregressive ordering: **D**
- Rectified-flow generation: **D**
- Exact transformer blocks, token layout, VAE, attention topology, and schedule: **U**
- Whether all modalities share one VAE: **U**

### Recomo implication

Implement an architecture hypothesis that is autoregressive over typed elements and flow-based within a continuous element, but treat it as one design to test—not a dogma. Compare with masked bidirectional and non-autoregressive alternatives.

---

## 4. Camera-controlled generation

### Disclosure

The camera-control section shows generation from one to six input images along designed camera paths. The path is supplied; the model renders the scene along that path.

### Classification

- Explicit camera-path input: **D**
- One-to-six reference examples: **D**
- Automatic cinematographic path planning: **not demonstrated**
- Metric trajectory accuracy: **U/V**
- Per-frame variable intrinsics and distortion: **U**

### Recomo implication

Keep the Recomo `ShotProgram`, CameraPlan synthesizer, constraint authority, and robot compiler. Atlas-like generation belongs downstream of a camera path; it does not replace director-level reasoning or physical feasibility.

---

## 5. Long video

### Disclosure

World Labs presents a one-minute 1440p example and attributes longer controlled generation to the combination of camera movement and spatial-context management.

### Classification

- Demonstrated output length/resolution for a selected example: **D**
- General success rate at that length/resolution: **U**
- Runtime and serving cost: **U**
- Long-horizon loop closure and dynamic identity metrics: **U**

### Recomo implication

Long generation requires two plans, not one: `CameraPlan` and `SpatialContextPlan`. Build a context compiler, keyframe/evidence retention, external spatial memory, and loop-closure tests before optimizing raw duration.

---

## 6. Placing references in space

### Disclosure

The blog shows input images located at selected positions in 3D and Atlas constructing content or transitions between them.

### Classification

- Posed/spatially placed input observations: **D**
- Ability to use unrelated references as spatial anchors in examples: **D**
- Guarantee that contradictory anchors are resolved correctly: **U**
- Metric correctness of the constructed transition: **U**

### Recomo implication

Add `SpatialAnchor`, including pose, time, subject/region binding, provenance, confidence, and validity. Separate user references from measured observations in authority rules.

---

## 7. Sparse-view reconstruction and 3D output

### Disclosure

Atlas predicts depth and uses posed image/depth output to create explicit products such as point clouds and Gaussian splats. Sparse-view reconstruction is part of the demonstrated capability surface.

### Classification

- RGB/depth generation or prediction: **D**
- Point-cloud and 3DGS products: **D**
- Native internal 3DGS representation: **U**
- Metric accuracy, completeness, and benchmark protocol: **U**

### Recomo implication

Keep explicit 3D as an output and system interface. Fuse measured, reconstructed, estimated, and generated geometry with provenance; use it for replay, editing, visibility, collision proxies, and independent rendering.

---

## 8. More context reduces imagination

### Disclosure

World Labs describes a continuum from sparse evidence, where the model imagines unseen regions, to many observations, where it is more constrained by the scene. The post discusses contexts extending beyond a few images and demonstrates repeated scene use.

### Classification

- Qualitative evidence-imagination trade-off: **D/V**
- Exact context capacity and degradation curve: **U**
- Calibration under conflicting or low-quality observations: **U**

### Recomo implication

Make the trade-off explicit through provenance, coverage, uncertainty, and an `imagination_budget`. Benchmark 1, 2, 4, 8, 16, 32, 64, and 100+ observations; add conflicts and stale dynamic observations.

---

## 9. Multiple paths through one scene

### Disclosure

Atlas demonstrates different camera paths through a common scene or context.

### Classification

- Reuse across selected paths: **D**
- Cross-path identity and geometric consistency under a metric benchmark: **U**
- Persistent state between independent sessions: **U**

### Recomo implication

Cross-path consistency is a primary metric. Generate paths independently, reconstruct their outputs, compare static landmarks, depth, identities, and loop closure, and distinguish shared external map state from model-local latent cache.

---

## 10. Camera benchmark

### Disclosure

Atlas receives its native camera trajectory. General video comparators that lack such a native input receive textual descriptions. Human raters select the output that better follows the desired camera movement.

### Classification

- Human preference under the published protocol: **D**
- Evidence that native camera control is better than text-only prompts: **I**, strongly supported
- Specialist superiority over AC3D/GEN3C/RealCam-I2V under equal input: **not established**
- “Pixel-perfect” metric tolerance: **V**

### Recomo implication

Run an equal-input specialist benchmark: identical \(SE(3)\), intrinsics, frame times, references, and resolution; report rotation, metric translation, focal error, reprojection, camera-estimator failure, and visual quality separately.

---

## 11. Navigation simulation

### Disclosure

The post describes reconstructing environments and generating RGB/depth observations along simulated body-camera paths for navigation-oriented workflows.

### Classification

- Camera-sensor simulation capability surface: **D**
- Policy success and sim-to-real performance attributable solely to Atlas: **U**
- Deterministic geometry and collision fidelity: **U**

### Recomo implication

Adopt an embodiment gate: given initial observations and a proposed robot camera trajectory, predict RGB-D and compare against the real capture. Use measured geometry and robot state as authority.

---

## 12. Manipulation and interaction

### Disclosure

Atlas is said to aid the construction of simulations involving object motion and interaction. Related World Labs material describes a broader real-to-sim-to-real stack combining spatially coherent environments with task-aligned simulation and different representations.

### Classification

- Participation in a broader simulation pipeline: **D**
- One model providing all contact physics: **not disclosed**
- Reliable manipulation dynamics and contact transfer: **U/V**

### Recomo implication

Do not collapse learned rendering, object dynamics, and contact physics. Stage navigation/camera prediction first, then dynamic tracks, hybrid simulators, and finally matched sim-real contact tests.

---

## 13. Architecture facts still needed

A reproducible counterpart requires answers to:

1. How are camera poses represented and normalized?
2. Are intrinsics explicit, inferred, fixed, or encoded through rays?
3. How are depth scale and camera translation calibrated?
4. What are the image/depth/video tokenizers and compression ratios?
5. Is the context causally autoregressive for all inputs or selectively masked?
6. How is context selected or evicted at long horizons?
7. Is there an external reconstruction/fusion loop?
8. How are generated elements prevented from contaminating measured evidence?
9. What is the model size, data mixture, training compute, and sampling schedule?
10. What is the failure distribution across scene dynamics, parallax, reflective surfaces, and extreme lenses?

Until disclosed, these remain design variables for RSFM rather than facts about Atlas.

---

## 14. Resulting Recomo architecture change

V1.0 already contained the calibrated camera contract, persistent world state, geometry-conditioned renderer, cinematic planner, verifier, and deterministic execution. The Atlas close reading adds:

```text
SpatialAnchor
    ↓
SpatialContextPlan
    ↓
ContextCompiler
    ↓
Typed posed RGB/depth/camera/time elements
    ↓
Atlas-like spatial model
```

This change is substantive because long-horizon spatial generation depends not only on the path but also on evidence scheduling and memory authority.

---

## 15. Research hypotheses generated by the audit

- **H1:** A compiled context selected by visibility, provenance, and world time outperforms naive recency-based context at equal token budget.
- **H2:** Rendered metric point maps plus rays outperform either representation alone on large-parallax metric trajectories.
- **H3:** A joint camera latent improves inverse camera estimation and cycle consistency, but may add little to forward rendering when explicit geometry is already supplied.
- **H4:** External validated 3D memory reduces cross-path and loop-closure drift more than simply increasing neural context length.
- **H5:** Separating measured and generated map layers improves safety and calibration without materially reducing visual quality.
- **H6:** Recomo-native planned/executed/captured tuples provide more product value per sample than additional uncalibrated web video.
- **H7:** Camera accuracy and cinematographic quality remain sufficiently independent that a factorized verifier outperforms a single video preference score.

---

## Final assessment

Atlas is a high-quality strategic direction because it places cameras and geometry inside the foundation-model interface. The strongest lesson is not that a single proprietary checkpoint should replace every component. It is that spatial evidence should be typed, posed, timed, and jointly usable for generation and reconstruction.

Recomo should adopt that interface while being stricter about metric truth, provenance, context planning, cinematographic intent, and physical execution. This produces an Atlas-compatible research trajectory without depending on undisclosed internals or unverified product claims.
