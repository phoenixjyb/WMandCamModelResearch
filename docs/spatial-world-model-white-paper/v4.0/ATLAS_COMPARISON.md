# Atlas and the specialist comparison set — v4.0

**Checked:** 6 September 2026. **Status:** source audit and proposed comparison protocol; no model execution. Source identifiers resolve in [SOURCE_REGISTRY.csv](SOURCE_REGISTRY.csv). Numerical excerpts are in [RESULTS.csv](RESULTS.csv).

## 1. Evidence boundary

Atlas's official article describes posed text/image/depth sequences, element-wise autoregression and rectified-flow generation. It presents controlled video, reconstruction, explicit 3D products, reframing, sensor simulation and image/panorama generation. Its examples use authored camera paths. The camera study changes both the model and the camera interface; it therefore supports a system-level preference result, not a causal estimate of the numeric interface. Its reconstruction task supplies images and poses and predicts a point per input pixel [P01].

V4 does not infer native mesh or Gaussian tokens, a particular persistent internal map, a variable-intrinsics API, a metric tolerance, or core-model contact physics from that description. Absence of public evidence is not proof that a capability is absent. Atlas is an important reference, not the name of our entire research problem.

## 2. Exact reconstruction competitors

The official labels are Pi3X (posed), Pi3, VGGT-Omega 1B, Depth Anything 3 and MapAnything [P01]. These are five distinct comparison targets. Pi3X must not inherit the original Pi3 paper's results; original VGGT in DA3's table must not be relabeled VGGT-Omega.

| Comparator | Checked evidence | Required replication decision |
|---|---|---|
| Pi3X posed | Official release supports conditional pose/intrinsics/depth injection and approximate scale [P04] | Exact weights, supplied fields, confidence mask and preprocessing |
| Pi3 | Permutation-equivariant local point and relative pose formulation [P03] | Reference-order test, gauge alignment and posed-fusion path |
| VGGT-Omega 1B | Paper identity and explicit checkpoint warning [P02,P38] | Check benchmark overlap before using affected results |
| Depth Anything 3 | Depth-ray formulation and Table 3 [P05] | Giant/Large variants, native pose conditioning versus fusion |
| MapAnything | Flexible geometric inputs and factored prediction [P06] | Exact, noisy and missing-prior conditions |

## 3. The contamination notice is narrow but material

The August 18, 2026 model-card notice says an ancestor checkpoint may have contaminated the released 1B model's benchmark results in Tables 1 and 2. The authors advise against relying on those affected results pending investigation [P02].

This does not establish contamination in Atlas. It does not invalidate every VGGT-Omega variant or every downstream use. Our result registry must instead quarantine the affected rows, record exact checkpoint identity, and establish whether Atlas's evaluation overlaps the warned benchmarks. A newer model-card revision could alter the disposition; record the checked date and inspect the notice again before experiments.

## 4. Numerical comparisons that are actually extracted

### DA3 Table 3: posed reconstruction, reported by DA3 authors

| Model | ETH3D F1, higher | DTU Chamfer mm, lower |
|---|---:|---:|
| MapAnything | 71.9 | 3.97 |
| Pi3 | 80.6 | 1.72 |
| Original VGGT | 66.7 | 1.44 |
| DA3-Giant | 87.1 | 1.85 |
| DA3-Large | 75.2 | 1.23 |

These columns use the source's with-pose reconstruction regime. Methods consume poses differently, including conditioning and fusion. They are not Atlas measurements. Dataset rankings differ; no average over these incompatible units is meaningful [P05].

### SANA-WM Table 9: same-backbone inference regimes

On the hard 60-second split, the 2.6B/720p bidirectional and autoregressive stage-1 variants report rotation errors of 3.17 and 10.02 degrees, and memory of 49.2 and 51.1 GB respectively. Recovered trajectories are Sim(3)-aligned. This is motivation for an offline/causal comparison, not proof of absolute metric control or a universal minimum memory requirement [P07].

### HY-World 2.0 Table 6: camera-only configurations

The source reports RotErr values of 1.690 for SEVA, 0.944 for GEN3C, 3.481 for WorldPlay, 3.452 for WorldCompass, 0.762 for WorldStereo and 0.492 for WorldStereo 2.0. The last two are starred camera-only configurations without memory. The excerpt preserves the source-native unit rather than guessing a metric interpretation. Table 7 changes VAE design and trainable network blocks: it motivates a factorial experiment, not a claim that the VAE alone caused the gain [P08].

## 5. The unresolved Atlas graphical panel

Exact numeric values and complete model/version labels from the graphical camera-comparison panel have not been transcribed from a verified primary artifact in this revision. No secondary site's numbers are promoted into RESULTS.csv. Exact reconstruction chart scores are likewise not reconstructed from secondary summaries. Missing values are missing, not zero and not inferred rankings.

Required closure: obtain a primary chart/data artifact; record axis, units, aggregation, competitor versions, trial count, motion strata, ties, uncertainty intervals and sampling policy. Then distinguish the vendor protocol from a matched specialist experiment. This is a tracked evidence gap, not an experimental result.

## 6. Full capability comparison protocol

Use separate tasks for input-view geometry, held-out novel views, calibrated trajectory generation, synchronized refilming, future dynamics, persistence, explicit 3D export, panorama/world construction and embodied sensor prediction. Shared input names do not guarantee equal privilege: ground-truth target depth, optimized poses, future frames, or additional source views change the task.

A fair study has two views. The capability view gives each system its best declared supported interface. The causal ablation holds initialization, data, training budget, sampling and interface constant while changing a single mechanism. The former compares systems; only the latter supports a mechanism-level explanation.

Include a traditional calibrated reconstruction/rendering pipeline and a compact geometry predictor. A generative system must demonstrate why its added ambiguity and cost are useful. Conversely, conventional reconstruction cannot claim recovery of truly unseen surfaces, and static rendering cannot replace dynamic or optical image formation.

The study must publish scene-level confidence intervals, failed generations, evaluator failures, retry policies and all candidate samples. A proprietary system lacking access can remain a disclosed comparator without fabricating a run. The practical target is a reproducible capability profile, not a single aggregate Atlas-versus-everyone score.
