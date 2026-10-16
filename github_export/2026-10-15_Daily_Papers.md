# 🤖 具身智能/机器人学术日报 (2026-10-15)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. An Agentic Framework for Proactive Robots with Procedural Assistance Memory
- **SOP Score:** 21
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** robot learning, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Proactive robots should anticipate user needs and provide assistance before being explicitly asked. A straightforward approach is to infer human intentions from commonsense knowledge, but the same observed behavior can imply different needs across users, potentially leading to unwanted assistance. We observe that everyday routines in the real world exhibit recurring patterns, so learning these patterns can reduce ambiguity in proactive decisions.
- 📄 [arXiv](https://arxiv.org/abs/2610.21211v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21211v1)

---

### 2. CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation
- **SOP Score:** 20
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** whole-body control, robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable quasi-dynamic simulator for batched model predictive control (MPC).
- 📄 [arXiv](https://arxiv.org/abs/2610.21349v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21349v1)

---

### 3. MR-MPCC: Model Predictive Contouring Control for Robotic Manipulator Tracking under Moving Reference Frames
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Maintaining small path-tracking errors under moving reference frames is essential for robotic manipulation tasks with tight execution tolerances, such as machining and surgical automation. Conventional time-indexed controllers, including tracking Model Predictive Control (MPC), rely on a fixed temporal correspondence with the reference trajectory and may therefore accumulate path-relative error under abrupt reference-frame motion or timing mismatch.
- 📄 [arXiv](https://arxiv.org/abs/2610.21292v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21292v1)

---

### 4. KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that still require robot data for adaptation or generate controller-specific commands that limit reuse.
- 📄 [arXiv](https://arxiv.org/abs/2610.21152v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21152v1)

---

### 5. CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable execution. First, executing an instruction like "make me a sandwich" requires grounding subtask decomposition in persistent user preferences rather than relying on a single generic solution.
- 📄 [arXiv](https://arxiv.org/abs/2610.21453v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21453v1)

---

### 6. Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation
- **Zotero:** 待入库
- **Abstract:** General-purpose dexterous manipulation requires policies to transfer knowledge from related tasks to new tasks with only a few target demonstrations. Existing benchmarks often provide too many target demonstrations. They also leave the differences between source and target tasks uncontrolled. As a result, they cannot clearly distinguish knowledge transfer from task memorization. Our key insight is the Core-Gen principle.
- 📄 [arXiv](https://arxiv.org/abs/2610.21180v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21180v1)

---

### 7. Manifold Generative Annealing for Contact Constraint-aware Impedance Control with Reinforcement Learning Prior
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Contact-rich robotic tasks require coordinated motion and impedance under uncertain interaction dynamics and physical constraints. While recent methods on learned policies provide useful interaction strategies, they may fail when contact conditions differ from those encountered during training. Model-based generative methods show promising receding-horizon trajectories optimization results, but often lack structured behavioral guidance and refinement that jointly accounts for constraint geometry...
- 📄 [arXiv](https://arxiv.org/abs/2610.21140v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21140v1)

---

### 8. Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +3 | Hardware +4 | Code +3 | cs.RO +0
- **Keywords:** reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Diffusion models (DMs) have steadily demonstrated outstanding performance in high-fidelity, controllable generation across diverse scenarios, following the "pretraining-finetuning" paradigm established in LLMs. Despite these advances, conventional DMs still face critical limitations in sophisticated reasoning, autonomous exploration of generation pathways, and adaptability to complex, human-aligned objectives.
- 📄 [arXiv](https://arxiv.org/abs/2610.21539v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21539v1)

---

### 9. Fast-VLA: You Only Think Once for Robot Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk. Yet task understanding changes far more slowly than the robot state. We introduce Fast-VLA, which invokes a frozen 4B VLM once per episode to contextualize the instruction and initial views as fixed, multi-layer key-value task memory.
- 📄 [arXiv](https://arxiv.org/abs/2610.21389v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21389v1)

---

### 10. RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** flow matching, robot navigation, robot
- **Zotero:** 待入库
- **Abstract:** Camera-to-robot pose estimation from a monocular image is significant for vision-based robot navigation and control. However, recovering 3D structural features from 2D observations remains a challenging task. Existing camera-to-robot pose estimation methods either rely on time-consuming iterative rendering or involve sophisticated 2D-3D registration which suffers from projection ambiguity, accumulated errors for distal joints and imbalanced learning for different joints.
- 📄 [arXiv](https://arxiv.org/abs/2610.21086v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21086v1)

---

### 11. Policy-Aligned Predictive Verification for Adaptive VLA Action-Chunk Execution
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies generate action sequences that reduce repeated inference, but deciding how much of each sequence to execute is critical to task success. Existing adaptive methods make this decision using generation stability or prediction agreement, yet these signals do not establish whether executing a candidate prefix preserves the ability to complete the task.
- 📄 [arXiv](https://arxiv.org/abs/2610.21434v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21434v1)

---

### 12. TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, robot
- **Zotero:** 待入库
- **Abstract:** Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language. The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 humanoid robot built around typed, measurable kinematic quantities.
- 📄 [arXiv](https://arxiv.org/abs/2610.21515v1) | 📥 [PDF](https://arxiv.org/pdf/2610.21515v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models** (SOP: 7) [Link](https://arxiv.org/abs/2610.21362v1)
- **VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models** (SOP: 7) [Link](https://arxiv.org/abs/2610.21306v1)
- **From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion** (SOP: 6) [Link](https://arxiv.org/abs/2610.21374v1)
- **LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation** (SOP: 6) [Link](https://arxiv.org/abs/2610.21199v1)
- **RLDF: A Region-Level Deepfake Dataset and Benchmark for Partial-Face Manipulation Detection** (SOP: 6) [Link](https://arxiv.org/abs/2610.21438v1)
- **AVALON: Zero-Shot Indoor Navigation with Human-Seeded Topological Memory** (SOP: 5) [Link](https://arxiv.org/abs/2610.21586v1)
- **CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay** (SOP: 5) [Link](https://arxiv.org/abs/2610.21239v1)
- **Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models** (SOP: 5) [Link](https://arxiv.org/abs/2610.21522v1)
- **MuSTMM: Learning Sound-Triggered Mobile Manipulation across Multiple Scenes** (SOP: 5) [Link](https://arxiv.org/abs/2610.21429v1)
- **Vision-Guided Closed-Loop Autonomous Navigation of Light-Driven Janus Microbots** (SOP: 5) [Link](https://arxiv.org/abs/2610.21222v1)
- **When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models** (SOP: 5) [Link](https://arxiv.org/abs/2610.21160v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 184 篇 | 精选: 12 篇 | 关注: 11 篇 | 过滤: 161 篇
