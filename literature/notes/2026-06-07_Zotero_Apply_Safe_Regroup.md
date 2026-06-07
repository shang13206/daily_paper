# Zotero apply-safe regrouping — 2026-06-07

原则：只追加高置信 collection；不删除任何现有 collection；`RSL` 只用于 ETH Zurich Robotic Systems Lab。

## 执行结果

- 写回 Zotero：已执行
- 追加 collection 的论文数：99
- 失败数：0
- 最终复查候选数：0
- 本地 index stale 条目清理：1 条

清理的 stale 条目：

- `Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection` — 本地 index key 为 `FAT26KPX`，但 Zotero API 返回 404，说明该 Zotero 条目已不存在；已从本地 `~/Zotero/zotero_index.json` 删除。

## 最终本地索引分布

- 真实论文数：119
- 未分组论文数：0
- RSL：17
- Terrain & Parkour：55
- Humanoid：47
- Quadruped：33
- Gait & Style：31
- Perception：30
- Navigation：29
- Sim2Real：24
- Teacher-Student：17
- Memory & Representation：17
- Mimic & Motion Prior：16
- MPC：15
- Whole-Body Control：11
- VLA：9
- State Estimation：8
- RAL：8
- Koopman：8
- Aerial：7
- IROS：7
- ICRA：6
- RSS：6
- Science Robotics：6
- Wheeled-Legged：5
- TRO：5
- CoRL：5
- Theory：4
- Locomotion：3
- Blind Locomotion：2
- Flow Policy：1
- Vision：1
- IJRR：1
- book：1

## 验证

执行后重新 dry-run：

```text
candidates: 0
failures: 0
skipped_missing_key: 0
```

说明当前高置信可追加的 collection 已全部写回；剩下如果要继续调整，应进入人工/二次审阅阶段，而不是继续自动批量追加。
