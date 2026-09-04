# White Paper v2.0 — Current

**From Camera-Controlled Video to Spatial World Models**  
**从相机可控视频到空间世界模型**

V2.0 is the current Recomo research position. It preserves the field review in v1.0 and adds a close technical audit of World Labs Atlas, plus a revised counterpart architecture and gated R&D program.

## Read

- [English white paper](en/From_Camera_Controlled_Video_to_Spatial_World_Models_Recomo_White_Paper_v2.0_EN.md)
- [中文技术白皮书](zh-CN/从相机可控视频到空间世界模型_Recomo技术白皮书_v2.0_CN.md)
- [Atlas disclosure audit — English](source-audit/en/Atlas_Technical_Disclosure_Audit_and_Recomo_Implications_v2.0_EN.md)
- [Atlas 技术披露逐项审计——中文](source-audit/zh-CN/Atlas技术披露逐项审计与Recomo研发影响_v2.0_CN.md)
- [Version manifest](VERSION_MANIFEST_v2.0.md)

## Central conclusion

An Atlas-like model is a strong research direction because it makes camera pose, observation, geometry, and generation native parts of one spatial interface. For a filming robot, however, that learned interface must be combined with explicit 3D state, cinematographic intent, independent verification, and deterministic physical execution.

```text
Atlas-like learned spatial intelligence
+ explicit 3D-as-code state
+ Recomo cinematic planning
+ independent verification
+ deterministic robot execution
```

## Major additions over v1.0

- `SpatialAnchor`
- `SpatialContextPlan`
- `ContextCompiler`
- explicit observed/reconstructed/generated provenance
- context-size and cross-path tests
- preview-versus-actual-robot-capture embodiment gate
- disciplined separation of public Atlas disclosure, inference, and unverified claim

V1.0 remains frozen under `../v1.0/`.
