# Version reconciliation and provenance

**Prepared:** 2026-09-05. **Pinned repository baseline:** `e88e67e3880b94823f1496093706d25952678465`.

## 1. What is established

The original conversation English v2 and repository English v2 are different textual editions, not merely different renderings. The original contains 1,996 lines and declares 2026-09-04 as its research cut-off; the repository edition declares 2026-09-03. The historical assurance of complete unchanged import was too strong.

| Source | Size in bytes | Identity | Repository restoration status |
|---|---:|---|---|
| Original conversation v2 English Markdown | 113313 | SHA-256 `263c31369b11ac8bfadc9b7c7c47d229404e94e5db896b222b247eb683dbf530` | Original attachment bytes checked; not imported in this PR |
| Original conversation v2 Chinese Markdown | 98249 | SHA-256 `18863b6004b48938d67e256a217d2a5b7d194858cb400c7fcde5977650f69089` | Original attachment bytes checked; not imported in this PR |
| Repository v2 English Markdown | 45171 | Git blob `231186716ac0629dd92583cbbf21e0382c17db08` at the pinned base | Retained unchanged in its existing directory |

SHA-256 content hashes and Git blob SHA-1 identifiers are different digests; they must not be compared as though they were the same algorithm.

Original source attachment identities, for provenance rather than public download:

- English: `file_0000000049b882309333901bc65110a9`
- Chinese: `file_000000004b2082309cc138012195fcd4`
- English September audit: `file_00000000bfc881fda4feb907add74250`, SHA-256 `85b159f923b793237d0e5dd054d341428a3040da383c61c9394fae23769b8a3b`
- Audit claim ledger: SHA-256 `bd0817fdc27a6b40c1ffb475f0fb83ace46c13e15cb9dda5cdac3fd86bb27848`
- Audit source registry: SHA-256 `fe04707992707216d3129ca840f616e5ed03db1f7ccf9d16085cabb4760cb11f`

These identifiers are not GitHub-accessible file links. No unavailable link is presented as a complete archival copy.

## 2. Editorial reconciliation

The original longer source's section inventory and the audit informed v3. This table records the treatment of substantive topic groups; it is not a machine proof of sentence-by-sentence semantic equivalence.

| Original v2 topic group | v3 treatment | Reason |
|---|---|---|
| Scope and observation/action distinctions | Sections 1–2 | Retained with empirical-status and evidence-scope limits |
| Capability ladder | Section 2 | Revised to independent capability dimensions |
| Historical evolution and design space | Section 3; source registry | Condensed in current argument; frozen historical editions remain separate |
| CogVideoX/AC3D/RealCam-I2V category corrections | Section 3 | Retained with configuration-specific attribution |
| Atlas close reading and system decomposition | Section 4 | Retained; causal interface claim narrowed; architecture not assumed necessary |
| Functional/architectural/scale counterpart | Sections 4 and 14 | Preserved as distinct ambitions rather than one milestone |
| Authority ports and three state classes | Section 7 | Retained; procedural authority does not imply infallible truth |
| Camera and optical contract | Section 8 | Expanded with K transformation, range/depth and temporal semantics |
| SpatialAnchor/SpatialContextPlan/ContextCompiler | Sections 5–7 | Retained; novelty qualified and learned selection separated from validation |
| StructuredRollout | Section 7 | Explicitly retained as exportable planning-critical future state |
| Joint model/VAEs/objectives | Sections 3, 7 and 10 | Recast as alternatives and ablations, not mandatory modules |
| External 3D state and provenance | Sections 7–9 | Expanded to freshness, conflicts, dependencies and calibrated reliability |
| Data curriculum and real captures | Section 10 | Retained with branch lineage and leakage controls |
| Four scorecards and baseline list | Sections 5 and 11 | Updated; no incompatible headline leaderboard |
| Estimator failure handling | Section 11 | Replaced unconditional attribution with failure taxonomy |
| Team/GPU schedules and 24 GB profile | Section 12 | Replaced procurement-like numbers with measured scenario cards |
| Licensing | Section 12 | Per-code/weight/data/output rights, no blanket clearance |
| Risks, ablations and roadmap | Sections 9–12; EXPERIMENTS.md | E0–E3 gates; outcomes remain unrun |
| Original references and audit additions | SOURCE_REGISTRY.md | All 71 audit identifiers retained with review-scope qualification |
| Old hypotheses and version chronology | This record and AUDIT_DISPOSITIONS.csv | Superseded claims remain historical, not overwritten |

## 3. What this PR does not claim

It does not restore all original PDF, DOCX, PPTX, figure or Markdown attachment bytes to GitHub. It does not certify all historical renderings or translations. It does not label the shorter repository v2 a faithful full copy. It does not close empirical gates by editing prose.

The new v3 papers are an independent editorial synthesis. Existing v1/v2 repository paths are frozen. Complete lossless import of the two original v2 Markdown attachments is a remaining archival task, not concealed by a green documentation check. The accompanying recovery utility verifies both original SHA-256 digests before writing new files under `archives/conversation-v2.0/`; it never overwrites the frozen v2 directory.

## 4. Recovery procedure

With the original two Markdown attachments downloaded locally:

```sh
python scripts/restore_original_v2_sources.py --en /path/to/original_EN.md --zh /path/to/original_CN.md
python scripts/restore_original_v2_sources.py --en /path/to/original_EN.md --zh /path/to/original_CN.md --write
```

The first command only verifies. The second preserves the exact bytes in a separate provenance directory, refusing differing existing copies. Commit those recovered files in a distinct archival commit and update this status only after checking their hashes from GitHub. Do not substitute a generated summary, rerendering or manually reconstructed text.
