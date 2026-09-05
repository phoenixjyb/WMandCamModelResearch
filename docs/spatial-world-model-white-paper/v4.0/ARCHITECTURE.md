# V4 architecture decision record

**Status:** Proposed alternatives and stable contracts; no winning architecture selected. Source references resolve in [SOURCE_REGISTRY.csv](SOURCE_REGISTRY.csv).

## 1. What stays stable

The public system contract is independent of whether one model or several models implement it. Preserve camera/optics/time semantics, evidence lineage, revisable state, explicit outputs, task-specific validation and a separate local execution boundary. Model modularity is an implementation choice; authority and provenance are system properties.

Track A exposes reconstruction, novel-view, dynamic, world-construction and explicit-3D tasks. Track B exposes predictive cinematography, evidence acquisition and execution. A Track B planner is a consumer of spatial predictions, not the definition of all spatial intelligence.

## 2. Alternatives to compare

| Design | Core mechanism | Strength to test | Principal risk | Initial experiment |
|---|---|---|---|---|
| A0: specialist hybrid | Geometry/reconstruction, explicit fusion, projection, generative residual | Diagnostic clarity and measured geometry | Error propagation across modules | F1/F2 |
| A1: spatial-keyframe-first | Posed keyframes, geometry fusion, temporal synthesis | Wide-baseline accuracy and context efficiency | Dynamic continuity and interpolation cost | F2/F4 |
| A2: shared spatial encoder | Joint evidence representation with task heads or decoders | Multi-task transfer and parameter reuse | Task interference and unequal data exposure | F3 |
| A3: typed autoregressive spatial generator | Interleaved evidence/query/output elements with continuous generation | Flexible continuation and reusable context | Error accumulation and serving complexity | F3/E1 |

HY-World 2.0 motivates A1, Matrix3D and related joint work motivate A2, and Atlas motivates one A3 hypothesis [P01,P08,P14]. None establishes that its paradigm is universally necessary. Pi3, DA3, MapAnything, CUT3R and Glob3R provide geometry mechanisms that can be tested inside or against any design [P03,P05,P06,P11,P13].

The first comparison should not train all alternatives at foundation scale. Establish A0 and one carefully chosen A1/A2 prototype. Introduce A3 when sequence flexibility or causal serving is the hypothesis, with an explicit matched alternative.

## 3. Evidence and query contracts

A minimal observation carries:

```yaml
observation:
  observation_id: immutable_capture_identifier
  scene_id: scene_identifier
  sensor_time: value_and_clock_domain
  world_time: value_and_mapping_revision
  camera_to_world: transform_and_uncertainty
  intrinsics: matrix_and_image_coordinate_convention
  projection: pinhole_or_declared_non_pinhole_model
  distortion: coefficients_and_convention
  geometry: optional_depth_or_point_map
  depth_semantics: axial_or_range_or_not_applicable
  optical_schedule: optional_focus_aperture_shutter_gain
  provenance: measured_reconstructed_estimated_generated_or_authored
  dependencies: source_observation_or_hypothesis_identifiers
  validity: time_interval_and_invalidation_reason
  calibration_revision: immutable_calibration_identifier
```

This is a design sketch, not a validated production schema. Unknown values must remain unknown rather than receive plausible defaults. Pose covariance requires a declared parameterization and frame; a matrix-shaped field alone is insufficient.

A query declares task, target cameras, world time, requested output types, supplied future commands, permissible creative changes, uncertainty target, resource budget and required evidence policy. Distinguish a future target camera from a future observed frame. A creative scene-completion query and a real-scene prediction query cannot share the same permissive default.

## 4. Logical ports and authority

PhysicalWorldBelief maintains the best available evidence and revision history. Its authority is procedural: it decides which evidence is accepted and how conflicts are represented, not that every accepted estimate is certain. CinematicContinuityState stores accepted artistic decisions. RendererLocalCache contains implementation-specific activations and may be discarded without destroying the only recoverable scene record.

SpatialAnchor binds evidence or authored reference to pose, identity and time. SpatialContextPlan selects support for a query under budget. ContextCompiler applies coordinate/time transforms, projection, masks, serialization and reproducible manifests. Selection may be learned; compilation must remain inspectable. A learned model can implement multiple ports without eliminating these contracts.

StructuredRollout exports predicted geometry, entities, tracks, visibility, occupancy and uncertainty for independent checking. RenderResult contains images or compact task outputs plus evidence lineage. Explicit3DExport identifies the representation, coordinate frame, scale status and observed/generated support. CinematicExecutionContract hands a validated path and monitoring requirements to local control.

## 5. Representation decisions that remain open

Camera input may combine numeric transforms, dense rays, rendered point/depth maps and track correspondences. The interface does not require every model to consume all of them. Test incremental utility with controlled data and compute. A ray identifies a line, not metric surface depth.

Observation encoding should be tested for order robustness while retaining timestamp semantics. Permuting complete observation tuples is different from changing the order of physical events. A set encoder with a time-conditioned output model is a research hypothesis, not a reverse-engineered Atlas architecture.

Geometry output may be depth, point maps, normals or a compact latent. A point cloud or Gaussian scene can be derived through explicit fusion; it need not be a native token. Conversely, explicit scene output does not certify collision geometry, dynamic identity or every optical effect [P12].

Do not introduce a new VAE, generative pose branch, uncertainty network or recurrent memory simply because a schema permits one. Each module must answer a hypothesis and beat an appropriate simpler control. Losses apply to predicted quantities, not already fixed inputs.

## 6. Uncertainty, freshness and correction

Provenance, creative authorization and predictive probability are different variables. A measured chair can move; a generated surface can later receive real support. Revision should preserve prior hypotheses and explain replacement or invalidation. Model-generated frames reinserted into context are dependent evidence, not independent confirmation.

Memory policies need tests for retention, retrieval, contradiction handling, eviction and recovery. Track persistent storage, selected context and peak working memory separately. Stable appearance that resists correct new measurements is a failure.

A query can return a prediction, request evidence, abstain or reject an incompatible plan. In real-scene mode, the model must not invent an opening to satisfy a desired trajectory. In creative mode, an authored opening is allowed only as an explicit scene edit, not retroactively labeled measured.

## 7. Dynamics and candidate branches

For observation-only queries on a nonreactive scene, multiple camera paths should share the same sampled world/event hypothesis. For action-dependent queries, share initial state and exogenous assumptions while allowing the transition to depend on the action. Shared random seeds alone do not certify common world state [P19,P20].

Track A evaluates world/query consistency even without a robot. Track B evaluates whether the consistent prediction improves actual selection. The latter may use compact visibility/framing predictions rather than render expensive RGB for every candidate.

## 8. Serving profiles and physical boundary

Offline preview can exploit a complete planned route and bidirectional computation. Streaming uses only causally available measurements and declares lookahead commands. Both profiles account for context prefill, retrieval, denoising, geometry fusion, VAE, transfer and refinement. Distillation is measured as an additional stage, not a free property of the initial model.

The physical camera path composes chassis, arm/lift, gimbal and fixed calibration. Feasibility includes joint and velocity limits, balance, collision, visibility, timing, clearance and recoverability. Deterministic code is not a safety proof when evidence is stale or wrong. Local sensing and stop/replan authority remain independent of the cloud model.

## 9. Promotion and rejection rules

Promote a shared representation when F3 establishes transfer or efficiency beyond equal-budget specialists. Promote keyframe generation when F2 controls VAE and trainable-block confounds and includes temporal synthesis costs. Promote a memory mechanism only after F4/E2 tests correction as well as retention. Promote a Recomo feature only after relevant E3 evidence and local execution validation.

A result may justify a different implementation for geometry, creative world construction and physical prediction. The architecture is allowed to conclude that a smaller specialist is sufficient for a function. This is not failure to build an Atlas counterpart; it is evidence-based scope and resource allocation.
