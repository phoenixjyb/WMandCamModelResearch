---
title: Camera-Aware Video Generation and Spatial World Models
subtitle: Evolution, Atlas assessment, and Recomo recommendations
version: v1.0
language: en
format: 16:9
---

# 1. Camera-aware video generation

**Evolution, Atlas assessment, and Recomo recommendations**

- From camera prompts to calibrated spatial models
- Recomo Research · 3 September 2026

---

# 2. Research question

How did the field move from “pan left” to explicit camera pose, intrinsics, geometry, world memory, and executable filming trajectories?

- What is actually controlled?
- What is metrically verifiable?
- What belongs inside a world model?
- What should remain explicit and deterministic?

---

# 3. Main conclusion

The winning direction is not a better motion prompt.

```text
camera contract
+ persistent spatial state
+ geometry-conditioned generation
+ cinematic intelligence
+ deterministic execution
```

A video model is a renderer and predictor—not the sole authority for geometry or robot safety.

---

# 4. Capability ladder

1. Semantic camera language
2. Relative extrinsic control
3. Calibrated ray control
4. Metric scene-aware control
5. Cross-view and 4D consistency
6. Optical camera control
7. Persistent spatial world modeling
8. Executable cinematic intelligence

---

# 5. Camera terminology matters

- **Extrinsics:** rotation and translation in a defined world frame
- **Intrinsics:** focal parameters and principal point
- **Projection/distortion:** pinhole, fisheye, radial/tangential terms
- **Optics:** focus, aperture, shutter, exposure
- **Time:** camera time is not always world time

Dolly and zoom can preserve framing while producing different parallax.

---

# 6. From pose matrices to dense rays

For each pixel, pose and intrinsics define a world-space viewing ray.

- Pixel-aligned geometry is richer than a frame-level pose token
- Plücker rays became a common conditioning representation
- A ray identifies a line of sight—not the surface depth

That missing depth drives the next stage of the field.

---

# 7. Stage 1 — MotionCtrl and CameraCtrl

**MotionCtrl**

- Separates object and camera motion
- Adds explicit camera trajectories to a pretrained generator

**CameraCtrl**

- Converts calibration into pixel-wise Plücker embeddings
- Injects camera features into video-generation layers

---

# 8. Stage 2 — Epipolar geometry

**CamCo · CamI2V**

- Restrict cross-view feature retrieval using epipolar lines
- Reduce correspondence ambiguity
- Improve multi-view consistency

Remaining problem: training data is dominated by smooth, mostly static camera paths.

---

# 9. Stage 3 — Video-DiT camera adapters

**VD3D** brings calibrated control to transformer video diffusion.

**AC3D** asks where and when camera control should enter:

- camera motion is mostly low-frequency
- global movement is established early in denoising
- selective early conditioning preserves dynamics and appearance

---

# 10. CogVideoX correction

CogVideoX is a strong video-DiT backbone.

Its “3D VAE” means spatial-temporal video compression—not a metric 3D scene.

```text
AC3D-CogVideoX
= CogVideoX visual prior
+ calibrated camera adapter
```

---

# 11. Stage 4 — Metric depth

**RealCam-I2V**

- predicts metric depth
- backprojects the source into a point cloud
- aligns trajectory scale
- lets users author a path in the estimated scene
- conditions generation with a geometric preview

Caveat: metric quality remains bounded by monocular depth and calibration.

---

# 12. Stage 5 — Explicit 3D cache

**GEN3C**

- maintains a depth-derived cache
- renders known content at the target camera
- asks the video model to complete disocclusion and uncertainty

```text
compute the known viewpoint change
+ generate what geometry cannot determine
```

---

# 13. Stage 6 — Refilming and 4D correspondence

**ReCamMaster · CameraCtrl II · RealCam**

- change viewpoint while preserving a dynamic performance
- broaden exploration and support streaming operation

**Track2View**

- projected 3D tracks specify source-to-target content motion

World time and camera time must be separable.

---

# 14. Stage 7 — Intrinsics and optics

**AKiRa · UCPE · DeltaCam · CameraAnything**

- focal length and field of view
- lens distortion and projection
- pitch, roll, and gravity
- focus and aperture
- shutter and exposure
- native resolution and compound transitions

---

# 15. Cameras become a modeled modality

**4DiM · Rays as Pixels**

A single model can support:

- video → camera
- camera → video
- camera + video joint generation
- pose/time-conditioned novel views

The target changes from a side condition to a joint spatial distribution.

---

# 16. What Atlas genuinely changes

World Labs describes Atlas as:

- pretrained from scratch as spatial
- a multimodal autoregressive diffusion transformer
- using text, posed images, image sequences, and depth in shared context
- generating camera-controlled video and geometry-related outputs
- supporting longer designed paths and scene reuse

Strategic signal: camera geometry is becoming a foundation-model interface.

---

# 17. What Atlas does not yet establish

Publicly undisclosed or unverified:

- per-frame intrinsics and changing focal length
- metric translation tolerance
- distortion and gravity conventions
- loop-closure drift and dynamic-world memory
- latency, VRAM, model size, weights, and API
- equal-input comparison with specialist camera models

Treat Atlas as validation of direction, not a reproducible dependency.

---

# 18. Open problems

1. Camera/object-motion entanglement
2. Metric-scale integrity
3. Disocclusion and unknown truth
4. Loop closure and revisitation
5. Gravity, roll/pitch, and optics
6. Dynamic 4D state
7. Physical executability

Measured ≠ reconstructed ≠ generated.

---

# 19. Recomo architectural principle

1. **Camera contract** — calibrated and model-independent
2. **Persistent world state** — measured, reconstructed, generated, dynamic
3. **Generative renderer** — completes unknown appearance and motion
4. **Robot compiler** — deterministic feasibility and safety

Do not replace the spatial stack with the newest video model.

---

# 20. Recomo reference pipeline

```text
User intent
→ Cinematic planner
→ Camera contract
→ Robot feasibility
→ Executable trajectory

Persistent spatial state
→ Geometry preview
→ Camera-aware generator
→ Geometric + cinematic critic
↺ planning feedback
```

---

# 21. Canonical camera contract

```text
C(t) = {
  T_world_camera(t), K(t), projection(t), distortion(t),
  focus(t), aperture(t), shutter(t), exposure(t), time(t)
}
```

Physical chain:

```text
World → Chassis → Arm/Lift → Gimbal → Camera
```

Version frames, units, timebase, calibration, and uncertainty.

---

# 22. Benchmark design

Three regimes:

- calibrated synthetic scenes
- repeated static Recomo captures
- dynamic synchronized real scenes

Trajectory suite:

- pan/tilt/roll
- dolly/truck/crane
- orbit/look-at and dolly zoom
- large parallax
- non-level gimbal base
- yaw lock/unlock
- loop closure
- aggressive OOD paths

---

# 23. Four independent scorecards

**Camera** — rotation, metric translation, ATE/RPE, intrinsics

**World** — reprojection, depth, tracks, identity, loop closure

**Cinema** — composition, dynamics, continuity, human preference

**Robot/system** — reachability, collision, stability, VRAM, runtime, failures

A beautiful video with a wrong camera is still a camera failure.

---

# 24. Experimental shortlist

- AC3D-CogVideoX — ray-conditioning baseline
- RealCam-I2V — depth-aligned metric control
- GEN3C — explicit 3D-cache generation
- ReCamMaster / TrajectoryCrafter — dynamic refilming
- UCPE / CameraAnything — optics and orientation
- Track2View — explicit correspondence
- Atlas — reference when access and fair evaluation become available

---

# 25. Final recommendation

```text
Atlas-like learned spatial intelligence
+ explicit 3D state
+ Recomo cinematic planning
+ independent verification
+ deterministic robot execution
```

Build a functional counterpart first, then a joint RGB-depth-camera model, and scale only after metric and embodiment gains are demonstrated.
