# Camera-Aware Video Generation and Spatial World Models

## Evolution, technical taxonomy, model comparison, and Recomo recommendations

**Version:** 1.0 — Frozen research report  
**Date:** 3 September 2026

---

## 1. Research question

How has video generation evolved from text-described camera movement to explicit camera extrinsics, intrinsics, metric geometry, persistent scene state, and native spatial world models? Which systems are relevant to Recomo, and which claims require stronger evidence?

The review includes systems that consume one or more of:

- numeric camera pose or trajectory;
- calibrated camera rays;
- intrinsics or projection parameters;
- epipolar correspondence;
- rendered depth, point clouds, or coordinate fields;
- 3D/4D point tracks;
- jointly modeled camera, RGB, depth, and time.

Text-only “pan left” control is treated as a weaker baseline rather than calibrated camera awareness.

---

## 2. Main finding

The direction evolved through four increasingly spatial formulations:

1. **Camera pose as an auxiliary condition** — MotionCtrl, CameraCtrl, VD3D, AC3D.
2. **Dense camera geometry and correspondence** — Plücker rays, epipolar attention, calibrated cross-view aggregation.
3. **Explicit scene transport** — metric depth, point clouds, rendered geometry, persistent 3D caches, 4D tracks.
4. **Native joint spatial modeling** — 4DiM, Matrix3D, Rays as Pixels, and the architecture direction represented by Atlas.

The strongest practical Recomo architecture is not a pure video generator. It is:

```text
explicit calibrated camera contract
+ persistent spatial state
+ deterministic rendering of known content
+ generative completion of uncertain content
+ cinematic planning and critique
+ robot feasibility and safe execution
```

---

## 3. Capability taxonomy

| Dimension | Weak interpretation | Strong interpretation |
|---|---|---|
| Camera language | Looks like a pan/orbit | Numeric trajectory follows a contract |
| Extrinsics | Relative motion direction | Metric \(SE(3)\) with frame convention and uncertainty |
| Intrinsics | Fixed approximate field of view | Per-frame \(K\), projection and distortion |
| Optics | Prompted “cinematic lens” | Focal, focus, aperture, shutter and exposure curves |
| Geometry | Temporally smooth pixels | Cross-view reprojection and metric depth consistency |
| Dynamics | Plausible local movement | Camera/world time separation and tracked identity |
| Memory | Long clip | Revisit and loop closure in a persistent scene |
| Robotics | Virtual trajectory | Feasible, stable and collision-checked embodied path |

A model should not be called metric merely because an evaluation aligns translation to an estimated depth scale. A no-scale-alignment camera score is required for physical use.

---

## 4. Dense ray representation

For a pixel \(\tilde p=[u,v,1]^T\):

\[
d_{tuv}=\frac{R_tK_t^{-1}\tilde p}{\|R_tK_t^{-1}\tilde p\|},
\]

and a Plücker ray may be represented as

\[
\mathcal P_{tuv}=(o_t\times d_{tuv},d_{tuv}).
\]

This gives each visual token a world-space line of sight. It does not provide scene depth. That missing variable explains the later movement toward depth-conditioned and cache-conditioned systems.

---

## 5. Evolution timeline

### MotionCtrl — separate camera and object motion

MotionCtrl established explicit conditioning for both camera and object trajectories. Its conceptual value is the separation of global viewpoint motion from local scene dynamics.

### CameraCtrl — spatialize the camera

CameraCtrl converted calibrated poses into pixel-aligned Plücker embeddings and injected them at multiple scales. It became a template for camera-control adapters.

### CamCo and CamI2V — constrain correspondence

Epipolar attention restricts cross-view feature retrieval to geometrically plausible locations, improving consistency and reducing the amount the network must discover from data.

### VD3D — camera control for video DiTs

VD3D transferred the calibrated-camera adapter concept into a transformer-based video diffusion model through a ControlNet-like branch.

### 4DiM — pose and time as model dimensions

4DiM jointly conditions on images, camera poses, and timestamps and uses metric-depth calibration. It is closer to a space-time world model than a simple camera adapter.

### AC3D — learn where and when to condition

AC3D reports that camera motion is low-frequency and established early in denoising. It restricts control to selected early layers and stages to preserve dynamic quality. AC3D on CogVideoX is an added camera branch; CogVideoX's 3D VAE is spatiotemporal compression, not a metric 3D world.

### RealCam-I2V — align camera scale to a reconstructed scene

RealCam-I2V predicts metric depth, backprojects a point cloud, aligns trajectory scale, and conditions generation using a geometric preview. Its metric claim remains dependent on depth and calibration quality; its released CogVideoX port is not identical to the evaluated paper implementation.

### GEN3C — persistent geometry cache

GEN3C builds and updates a 3D cache, renders it at target poses, and asks the video model to complete disoccluded and uncertain regions. It is the clearest open example of the principle that known view transformation should be computed rather than hallucinated.

### TrajectoryCrafter and Uni3C — geometry-guided redirection

These systems use point-cloud renderings or point-cloud conditions to alter camera paths, further validating explicit transport while exposing sensitivity to depth errors.

### ReCamMaster and CameraCtrl II — dynamic scenes and wider exploration

They focus on refilming an existing dynamic scene and expanding camera movement beyond restricted real-estate trajectories. Preserving actor timing while changing viewpoint makes world-time separation essential.

### RealCam — streaming refilming

The 2026 RealCam line uses a high-quality bidirectional teacher and a distilled causal student for lower-latency camera-controlled video-to-video operation.

### Track2View — explicit 4D correspondences

Projected 3D tracks say where source content should appear under the target camera. This can be more informative than pose alone, especially for dynamic refilming.

### AKiRa, UCPE, DeltaCam, CameraAnything — intrinsics and optics

These systems broaden control to focal length, distortion, gravity/orientation, focus, aperture, exposure, aspect ratio, and compound camera transitions.

### Rays as Pixels — jointly model camera and video

Camera rays are encoded as raxel images and processed through the same spatiotemporal latent machinery as video. The model supports camera estimation, camera-conditioned video, and joint camera/video generation. This is one of the clearest academic precursors to native spatial world models.

### Atlas — native spatial sequence direction

World Labs describes Atlas as a multimodal autoregressive diffusion transformer pretrained from scratch, with posed images, image sequences, depth, text, and camera-controlled generation in a shared spatial context. It also presents reconstruction and explicit 3D outputs. The system is closed early access and lacks a public specialist camera benchmark, model card, weights, and full architecture disclosure.

---

## 6. Focused comparison

### CogVideoX

A strong open video-DiT backbone. Its base input contract is not calibrated camera pose/intrinsics. “3D VAE” refers to spatiotemporal video compression.

### AC3D

Adds a lightweight calibrated ray-conditioned control branch and injects it selectively. Useful as a clean baseline for camera conditioning without persistent explicit geometry.

### RealCam-I2V

Adds approximate metric scene reconstruction and path authoring. More scene-aware than AC3D, but bounded by monocular depth and implementation differences.

### GEN3C

Adds rendered persistent geometry. Best open architectural reference for Recomo's geometry-authoritative/generation-replaceable principle.

### Atlas

Makes camera and depth native elements of a shared spatial model rather than retrofit conditions. Strategically important, but public evidence does not yet reveal metric tolerance, changing intrinsics, loop closure, dynamic memory, cost, or equal-condition specialist superiority.

---

## 7. Open problems

1. **Motion entanglement:** camera control may suppress subject dynamics; dynamic content may corrupt pose estimation.
2. **Metric integrity:** normalized translation hides physical-distance error.
3. **Disocclusion:** unseen truth cannot be recovered from one view; provenance must distinguish inference from measurement.
4. **Loop closure:** temporal smoothness does not imply a stable revisitable world.
5. **Gravity and optics:** non-level mounts, roll/pitch, dolly-vs-zoom and shutter are under-tested.
6. **Dynamic 4D state:** static geometry caches are insufficient for people and moving objects.
7. **Executability:** virtual paths may violate robot kinematics, collision, visibility, stability, acceleration, or safety.

---

## 8. Recomo reference architecture

```text
User intent (precise or vague)
    ↓
Cinematic planner — shot grammar and aesthetics
    ↓
Camera contract — pose, optics, and time
    ↓
Robot feasibility — chassis, arm/lift, wrist, gimbal
    ↓
Executable trajectory — PNC/MPC/safety

Persistent spatial state — RGB-D, SLAM, 3DGS, semantics, tracks
    ↓
Geometry preview — render known content at target camera
    ↓
Camera-aware generator — complete unknown content and dynamics
    ↓
Geometric + cinematic critic
    ↺ feedback to planning and selection
```

The video model consumes a final camera trajectory. It does not decide how the physical degrees of freedom share the movement.

### Canonical contract

\[
\mathcal C(t)=\{T^W_C(t),K(t),\Pi(t),D(t),focus(t),aperture(t),shutter(t),exposure(t),\tau_t\}.
\]

Physical composition:

\[
T^W_C(t)=T^W_B(t)T^B_A(q_t)T^A_G(\theta_t)T^G_C.
\]

Coordinate frames, units, timestamps, shutter model, uncertainty, and calibration source must be versioned.

---

## 9. Benchmark proposal

### Test regimes

- calibrated synthetic scenes;
- static repeated Recomo robot captures;
- dynamic synchronized real scenes.

### Trajectories

Pan, tilt, roll, dolly, truck, crane, orbit/look-at, compound paths, dolly zoom, large parallax, non-level base, yaw lock/unlock, return loop, aggressive out-of-distribution paths, and decoupled world time.

### Scores

- **Camera:** rotation, metric translation, ATE/RPE, intrinsics, optics, smoothness.
- **World:** reprojection, depth, tracks, identity, cross-path consistency, loop closure.
- **Cinema:** composition, shot scale, screen direction, motion character, visual quality, human preference.
- **Robot/system:** reachability, collision, stability, execution margin, VRAM, runtime, failure rate, and preview-versus-real capture.

Rules include no scale alignment for the metric track, separate reporting of aligned trajectory shape, counting estimator failures, and separate scores for observed and generated regions.

---

## 10. Recommended experiments

| Priority | System | Question |
|---|---|---|
| A | AC3D-CogVideoX | What does ray conditioning achieve without explicit geometry? |
| B | RealCam-I2V | How much does depth-aligned metric authoring help? |
| C | GEN3C | Does rendered external geometry improve camera/world consistency? |
| D | ReCamMaster/TrajectoryCrafter | Can an existing dynamic performance be refilmed? |
| E | UCPE/CameraAnything | Can optics, orientation, and compound edits be controlled? |
| F | Track2View | Do explicit correspondences outperform pose/render-only control? |
| Reference | Atlas | What native spatial capabilities can be verified when access becomes available? |

---

## 11. Counterpart strategy

1. **Functional counterpart:** modular reconstruction, persistent 3D cache, explicit trajectory, RGB-D completion, 3D export, and independent validation.
2. **Architectural counterpart:** a joint camera/RGB/depth/time model with several inference directions.
3. **Scale counterpart:** long-duration, high-resolution, open-domain product parity.

Build the first before the second, and validate the second before scaling toward the third.

---

## 12. Final recommendation

The central architectural recommendation is:

\[
\boxed{
\text{camera contract}
+\text{explicit world state}
+\text{geometry-conditioned generation}
+\text{cinematic intelligence}
+\text{deterministic execution}
}.
\]

Atlas is a meaningful confirmation that camera geometry is becoming part of the foundation-model interface. Recomo should be compatible with that future while retaining the structures required for metric truth, editability, verification, and real robot motion.

---

## Core sources

- Atlas: https://www.worldlabs.ai/blog/atlas
- MotionCtrl: https://arxiv.org/abs/2312.03641
- CameraCtrl: https://hehao13.github.io/projects-CameraCtrl/
- CamCo: https://arxiv.org/abs/2406.02509
- CamI2V: https://arxiv.org/abs/2410.15957
- VD3D: https://arxiv.org/abs/2407.12781
- 4DiM: https://arxiv.org/abs/2407.07860
- AC3D: https://arxiv.org/abs/2411.18673
- CogVideoX: https://arxiv.org/abs/2408.06072
- RealCam-I2V: https://arxiv.org/abs/2502.10059
- GEN3C: https://arxiv.org/abs/2503.03751
- TrajectoryCrafter: https://arxiv.org/abs/2503.05638
- Uni3C: https://arxiv.org/abs/2504.14899
- ReCamMaster: https://arxiv.org/abs/2503.11647
- CameraCtrl II: https://arxiv.org/abs/2503.10592
- RealCam: https://arxiv.org/abs/2605.06051
- Track2View: https://arxiv.org/abs/2606.15534
- AKiRa: https://arxiv.org/abs/2412.14158
- UCPE: https://github.com/chengzhag/UCPE
- DeltaCam: https://arxiv.org/abs/2605.25266
- CameraAnything: https://arxiv.org/abs/2607.24591
- Rays as Pixels: https://arxiv.org/abs/2604.09429
