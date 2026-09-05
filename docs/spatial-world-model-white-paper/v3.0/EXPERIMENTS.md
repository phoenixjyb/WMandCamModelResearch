# Preregisterable evaluation protocol — E0 to E3

**Status:** Specification, not experiment results. All gates are unrun.  
**Evidence and prior art:** See SOURCE_REGISTRY.md, particularly N01, N13, N24, N28, N29, N30 and N32.

## 1. Before collecting final test results

Freeze the task, model/checkpoint revision, calibration version, candidate set policy, camera/lens sampling, scene split, seeds, refinement, alignment convention and maximum input/compute budget. Declare primary outcomes and the minimum useful improvement. Derive tolerances from calibration and application needs; do not choose them after seeing a model's results. Log all generations and retries.

Provide three scale tracks: arbitrary-scale reconstruction, externally anchored metric prediction, and predicted metric scale without an anchor. Report any fixed independent registration and its uncertainty. Do not fit test-output scale for the anchored track. Camera time, world time, exposure time and video-latent time must be explicit.

The observation budget counts new physical sensing separately from retrieval of existing evidence. Compute includes prefill, depth/reconstruction, candidate selection, generation, refinement, evaluation and transfers. Report both initial request cost and amortized multi-candidate cost.

## 2. E0 — contract and evaluator validation

Produce synthetic sequences with known geometry, camera, intrinsics, depth semantics and timebase. Include calibrated real sequences as a separate later check. Inject known transform reversal, translation scale, crop/intrinsic mismatch, timing offset and depth/range mismatch. Include pure zoom, pure dolly, pure rotation, weak texture, occlusion and malformed outputs.

Measure detection of known errors and evaluator nonconvergence. A low-texture valid sequence and a malformed generation are different negative controls. Report detection curves and evaluator uncertainty; no generator ranking is accepted until evaluator behavior is understood.

Required outputs: contract test cases, calibration manifest, all injected perturbations, recovered values, failure taxonomy, and an explicit statement of cases outside the evaluator's observability.

## 3. E1 — camera mechanism and offline/streaming trade-off

Compare a historical ray-conditioned model, an efficient contemporary camera model and a geometry-conditioned model. A same-backbone bidirectional/causal comparison is preferred when available. Match conditioning, frames, resolution, camera schedule, seed policy and refinement. Do not give streaming methods future sensor observations.

Primary measures: rotation; anchored metric translation; separately aligned path shape; intrinsic following; observed-region depth/reprojection; dynamics preservation; end-to-end time and total peak memory. Measure raw-frame versus latent-rate control behavior. A refiner's cost and effect belong to the configuration, not an unreported postprocessing advantage.

Ablations: rays alone; rendered geometry plus masks; tracks where supported; joint camera latent where supported; offline versus causal; refinement on/off. Keep additional mechanisms only if they produce held-out accuracy or useful efficiency gains.

## 4. E2 — persistence, revision and dynamic re-entry

Compare explicit metric memory, spatial latent memory, nearest-pose retrieval and a bounded cache. Keep identical observations and trajectories. Include loop closure, two paths through one world, object relocation, stale calibration, identity ambiguity, actor disappearance/re-entry and conflicting evidence.

Measure cross-path geometry/identity disagreement, observed-region retention, stale-state false acceptance, uncertainty calibration, repair latency, active context and total storage growth. Static revisitation and unseen-event evolution must be separate results. Add a relevant out-of-sight protocol/baseline such as LiveWorld where usable; do not rename that existing task as novel.

A generated view must keep dependency links to the observations from which it was inferred. Multiple generated descendants are not independent evidence. A cache that refuses to revise a wrong scene is not successful memory.

## 5. E3 — realized shot choice and value of information

Hold feasible candidate camera/optics trajectories fixed across methods. Compare analytic geometry/framing and optimization; video-only prediction; geometry-conditioned prediction; and shared-hypothesis/evidence-selection variants. Also report candidate-proposer improvements separately if the proposal policy is varied.

For each scene define the intended subject, framing requirements, visibility objectives, hard constraints and evaluation procedure. Measure actual resulting footage when possible. Separate deviations between planned and executed camera motion from predictive error.

Report ranking agreement, regret relative to the best evaluated feasible candidate, false acceptance of poor visibility, selective risk/abstention, extra sensing cost and decision latency. Blinded human preference complements objective geometry and execution metrics. Safety constraints cannot be offset by an aesthetic score.

Static scenes can support repeated paths. Dynamic counterfactual truth requires synchronized views, reproducible staged motion, or simulation; repeated unsynchronized actor performances are not exact alternatives of the same event. Disclose which regime supports every result.

## 6. Intervention record

```json
{
  "root_world_id": "example-root",
  "branch_id": "example-branch",
  "intervention_type": "observation_only",
  "initial_state_id": "initial-state",
  "exogenous_trajectory_id": "shared-event",
  "camera_plan_id": "candidate-left",
  "changed_variables": ["camera_pose"],
  "invariants": ["world_geometry", "event_trajectory"],
  "evidence_ids": ["measured-frame-001"],
  "ground_truth_regime": "synthetic_exact",
  "split_group": "root-world-and-asset-family"
}
```

For action or mechanism interventions, change the branch type and invariants. Camera-only changes preserve a nonreactive event; physical actions may legitimately change its subsequent state. Sharing a seed is not sufficient validation of shared branch semantics.

## 7. Statistics and accounting

Split by scene, actor, asset family and capture session. Keep all same-root branches within one split. Bootstrap over scenes or sessions, not correlated frames. Keep evaluator training and test calibration separate from final outcomes. Predeclare sample selection and best-of-N policy.

Every trial receives an outcome: valid/evaluable, verified control violation, generation failure, evaluator nonconvergence, or inconclusive/abstained. Report conditional errors with denominators and unconditional coverage. Operational rejection and scientific attribution are different decisions.

Report uncertainty in calibrated predictions and preference measurements. Do not declare a win from one aggregate score while hiding a safety violation, a larger observation budget or a substantial latency increase. A negative result should identify whether failure originates in proposal, geometry, dynamics, retrieval, rendering, evaluation or execution.

## 8. Acceptance and scaling

E0 validates the measurement process, not a model. E1 and E2 establish capability/efficiency trade-offs. E3 establishes application value. The first scale decision requires a held-out gain beyond the non-generative baseline that is not explained by extra observations or compute. An independent generative-research branch may pursue other capability hypotheses, but must state its own measurable objective rather than claiming Recomo execution value by association.

No numerical acceptance thresholds, dataset counts, measured improvements or hardware service levels are populated in this protocol. They require a selected implementation and an approved preregistration. Documentation CI does not execute these experiments.
