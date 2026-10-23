# 🤖 具身智能/机器人学术日报 (2026-10-22)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation
- **SOP Score:** 28
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +12 | Hardware +4 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** quadruped, robot navigation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Autonomous mobile robots operating in dense crowds and cluttered sites require $360^\circ$ perception to react to surrounding hazards. While panoramic LiDAR offers full-surround coverage, learning representations within reinforcement learning (RL) is sample-inefficient under sparse rewards, and existing 3D pretrained point-cloud encoders are too memory-heavy for massively parallel RL simulation.
- 📄 [arXiv](https://arxiv.org/abs/2610.29845) | 📥 [PDF](https://arxiv.org/pdf/2610.29845.pdf)

---

### 2. SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation
- **SOP Score:** 19
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +17 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, whole-body control, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-pose-driven interface.
- 📄 [arXiv](https://arxiv.org/abs/2610.30044) | 📥 [PDF](https://arxiv.org/pdf/2610.30044.pdf)

---

### 3. AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** manipulation, imitation learning, VLA, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies. However, existing VLA-RL methods typically suffer from delayed and biased credit assignment due to trajectory-level sparse rewards, while imbalanced subtask mastery creates bottlenecks that limit overall performance.
- 📄 [arXiv](https://arxiv.org/abs/2610.30097) | 📥 [PDF](https://arxiv.org/pdf/2610.30097.pdf)

---

### 4. Watch Your Step: Anticipated Perception for Humanoid Locomotion
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, terrain, robot
- **Zotero:** 待入库
- **Abstract:** Perceptive locomotion policies typically observe a dense robot-centric elevation map, although only the terrain beneath and around the next footsteps informs the control decision. Learned encoders compress the whole visual input, leaving the policy to work out which inputs matter while learning the baseline locomotion task. Learning both at once slows training and, without computationally expensive attention mechanisms, makes generalization to new terrain harder.
- 📄 [arXiv](https://arxiv.org/abs/2610.29612) | 📥 [PDF](https://arxiv.org/pdf/2610.29612.pdf)

---

### 5. Do Earth-Trained Humanoid Controllers Walk on the Moon? Gravity, Terrain, and Soil Transfer
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, terrain
- **Zotero:** 待入库
- **Abstract:** The Moon changes gravity, terrain, and soil at once. Learned locomotion has studied reduced gravity on rigid ground and granular terrain mostly at Earth gravity, but not humanoids under both, generalist-controller transfer, or the Earth cost of lunar adaptation. On a simulated Unitree G1, we train 12 policies with one recipe, varying gravity, terrain geometry, and ground contact (rigid or three-dimensional resistive force theory, 3D RFT), and including Earth-to-Moon fine-tuning and gravity rando...
- 📄 [arXiv](https://arxiv.org/abs/2610.30080) | 📥 [PDF](https://arxiv.org/pdf/2610.30080.pdf)

---

### 6. Test-Time Motion Steering for Perceptive Humanoid Fall Recovery
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** humanoid, terrain, robot
- **Zotero:** 待入库
- **Abstract:** Humanoid fall recovery requires selecting a motion that suits both the surrounding scene and the task. The same fallen pose can admit several ways to stand, with different routes, support transitions, and final headings. Yet reliable recovery alone does not provide control over which of these alternatives the robot executes. Steering this choice requires anticipating the physical consequences of a requested movement.
- 📄 [arXiv](https://arxiv.org/abs/2610.30061) | 📥 [PDF](https://arxiv.org/pdf/2610.30061.pdf)

---

### 7. Agentic World Action Models
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, world model, robot
- **Zotero:** 待入库
- **Abstract:** Recent world action models provide visual foresight and future prediction for robot manipulation, but lack explicit mechanisms for compositional skill reuse. Agentic robotics combines code-based planning and reasoning with reusable skills, but often lacks predictive grounding in physical dynamics. We introduce AW-0, an agentic world action model framework that integrates code-based planning with joint video and action prediction.
- 📄 [arXiv](https://arxiv.org/abs/2610.30136) | 📥 [PDF](https://arxiv.org/pdf/2610.30136.pdf)

---

### 8. Joint-Angle Invariance of Jacobian-Based Performance Indices for Serial Robotic Manipulators
- **SOP Score:** 12
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +0 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Zotero:** 待入库
- **Abstract:** This article investigates the joint-angle invariance (JAI) of Jacobian-based performance indices for serial robotic manipulators. We identify kinematic conditions under which representative performance indices, including manipulability, stiffness, and other Jacobian-derived indices, remain independent of the first and last joint angles. This property allows a systematic reduction in the effective configuration-space dimensionality, thereby simplifying the performance evaluation.
- 📄 [arXiv](https://arxiv.org/abs/2610.29570) | 📥 [PDF](https://arxiv.org/pdf/2610.29570.pdf)

---

### 9. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use
- **SOP Score:** 12
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +2 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** RSS
- **Keywords:** robot, embodied
- **Zotero:** 待入库
- **Abstract:** Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed systems that couple multimodal task reasoning with physical action and revise decisions from the resulting feedback.
- 📄 [arXiv](https://arxiv.org/abs/2610.30108) | 📥 [PDF](https://arxiv.org/pdf/2610.30108.pdf)

---

### 10. Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly. Disagreement within an ensemble of independently trained policies can guide these decisions, but requires training and running multiple policies. We propose post-hoc kernel-variance heads that estimate epistemic uncertainty from the embeddings of a single policy.
- 📄 [arXiv](https://arxiv.org/abs/2610.29730) | 📥 [PDF](https://arxiv.org/pdf/2610.29730.pdf)

---

### 11. Toward Recursive Self-Improvement in Physical AI
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Recursive self-improvement (RSI) describes a system that improves not only its behavior but also the process by which it improves. Recent digital agents test this idea by rewriting their own code and checking each version with executable tests. Bringing these mechanisms into the physical world requires learning from partial observations through costly trials, while accounting for changing operating conditions and potentially irreversible consequences.
- 📄 [arXiv](https://arxiv.org/abs/2610.29677) | 📥 [PDF](https://arxiv.org/pdf/2610.29677.pdf)

---

### 12. End-to-End Reinforcement Learning for Quadrupedal Jumping in Lunar Gravity
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** reinforcement learning, terrain, robot, control policy
- **Zotero:** 待入库
- **Abstract:** Legged robots can extend planetary exploration to rugged and discontinuous terrain that is inaccessible to conventional rovers. In lunar gravity, jumping further expands this mobility by enabling robots to cross obstacles and gaps that cannot be traversed by walking alone. We present a multistage reinforcement-learning approach that produces a single end-to-end control policy for commanded point-to-point jumping under lunar gravity.
- 📄 [arXiv](https://arxiv.org/abs/2610.29586) | 📥 [PDF](https://arxiv.org/pdf/2610.29586.pdf)

---

### 13. HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, manipulation
- **Zotero:** 待入库
- **Abstract:** Real-time whole-body humanoid teleoperation remains challenging due to the computational latency introduced by optimization-based retargeting pipelines and future-frame conditioning. Existing motion tracking policies typically require dense reference targets including full joint positions, body-part transformations, and even future frames, which tightly couples the controller to expensive upstream modules.
- 📄 [arXiv](https://arxiv.org/abs/2610.29903) | 📥 [PDF](https://arxiv.org/pdf/2610.29903.pdf)

---

### 14. Asymmetric On-Policy Distillation Learns In-Context Exploration
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Sequential decision-making under partial observability is difficult because agents must explore to infer hidden, task-relevant information before acting effectively. Learning such information-gathering behaviors tabula rasa via online reinforcement learning is sample-inefficient, whereas offline imitation averages expert actions across hidden states and fails to learn exploration.
- 📄 [arXiv](https://arxiv.org/abs/2610.30105) | 📥 [PDF](https://arxiv.org/pdf/2610.30105.pdf)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **CausGround: Causal Interaction Grounding for Adaptive Embodied Planning** (SOP: 7) [Link](https://arxiv.org/abs/2610.29702)
- **FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring** (SOP: 6) [Link](https://arxiv.org/abs/2610.29692)
- **From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks** (SOP: 6) [Link](https://arxiv.org/abs/2610.30051)
- **CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation** (SOP: 5) [Link](https://arxiv.org/abs/2610.30117)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 204 篇 | 精选: 14 篇 | 关注: 4 篇 | 过滤: 12 篇
- 元数据不完整: 174 篇（不参与自动精选）
