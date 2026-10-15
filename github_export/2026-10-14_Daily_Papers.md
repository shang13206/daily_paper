# 🤖 具身智能/机器人学术日报 (2026-10-14)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. E2DRL: End-to-End Differentiable Reinforcement Learning for 3D Obstacle Avoidance in Quadruped Robots
- **SOP Score:** 33
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +27 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** quadruped, locomotion, robot policy, sim-to-real, reinforcement learning, terrain, robot
- **Zotero:** 待入库
- **Abstract:** Differentiable reinforcement learning shows strong promise for robot policy learning, but its application to legged locomotion has remained limited to blind walking or simulated 2D tasks. Extending it to end-to-end visual obstacle avoidance is challenging because hard collision constraints and early termination upon contact corrupt first-order gradients, trapping optimizers in local minima.
- 📄 [arXiv](https://arxiv.org/abs/2610.19627v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19627v1)

---

### 2. PolyMorph: Learning Locomotion Policy for Cross-Embodiment Adaptation
- **SOP Score:** 26
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +24 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, bipedal, locomotion, robot policy, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Reinforcement learning has enabled robust locomotion for legged robots, but learned policies are typically tied to a specific robot morphology and require additional engineering when the number of legs, actuators, or mechanical properties change. We present PolyMorph, a morphology-conditioned framework that learns a single locomotion policy for heterogeneous legged robots.
- 📄 [arXiv](https://arxiv.org/abs/2610.19615v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19615v1)

---

### 3. Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training
- **SOP Score:** 24
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** robot learning, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data. However, existing approaches typically treat simulators as fixed data sources, relying on uniform generation, offline retrieval, or manual parameter alignment by domain experts. We formulate \textit{Active Generative Simulation}: optimizing a simulator's data-generation distribution to maximize downstream real-world performance.
- 📄 [arXiv](https://arxiv.org/abs/2610.19479v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19479v1)

---

### 4. VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** manipulation, VLA, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation. However, conventional pretrained VLA policies lack a mechanism for gradual adaptation through accumulated interaction experience during deployment. We therefore propose VLRLA, a general framework that equips existing VLA models with \textit{in-context reinforcement learning} capabilities for deployment-time adaptation.
- 📄 [arXiv](https://arxiv.org/abs/2610.19517v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19517v1)

---

### 5. Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models have shown strong potential for general-purpose robotic manipulation, but extending them to bimanual dexterous manipulation introduces a high-dimensional and structured action space. Existing bimanual VLA policies commonly concatenate right- and left-side arm--hand actions at each control timestep, leaving cross-hand interactions implicit within a single action vector.
- 📄 [arXiv](https://arxiv.org/abs/2610.19753v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19753v1)

---

### 6. Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, whole-body control
- **Zotero:** 待入库
- **Abstract:** Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessarily prioritize the expressive characteristics of each action.
- 📄 [arXiv](https://arxiv.org/abs/2610.19393v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19393v1)

---

### 7. Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation. In our experiments, a pretrained subtask VLA achieves 80% success rate on atomic manipulation tasks but only 19% when these skills are composed into mobile manipulation. We argue that this gap stems from failures across the execution process rather than from local manipulation capability alone.
- 📄 [arXiv](https://arxiv.org/abs/2610.19600v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19600v1)

---

### 8. RoboSpan: Learning Modular Coordination Policies for High-DoF Whole-Body Mobile Manipulation with Teleoperation
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** locomotion, manipulation, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Whole-body mobile manipulation suffers from two fundamental challenges: inherent motion heterogeneity across locomotion, arm, and hand modules, and progressive error accumulation over long-horizon multi-stage tasks. Existing teleoperation platforms also lack integrated dexterous tactile sensing to support coordinated whole-body decision-making.
- 📄 [arXiv](https://arxiv.org/abs/2610.19594v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19594v1)

---

### 9. HiFun: a Hierarchical Framework for Efficient Functional Dexterous Manipulation Learning
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** While multi-fingered dexterous robot hands have the potential to provide human-level dexterity, using them for functional manipulation remains difficult because task success depends on precise contact, coordinated arm-hand motion, and reactive recovery from execution errors. Precise contact depends on complex contact dynamics that are difficult to model accurately in simulation, motivating real-world learning.
- 📄 [arXiv](https://arxiv.org/abs/2610.19518v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19518v1)

---

### 10. Back on Track: Deployment-time Policy Improvement via World Model Planning
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** diffusion policy, world model
- **Zotero:** 待入库
- **Abstract:** State-of-the-art visuomotor policies are increasingly capable of executing complex tasks, yet can fail during deployment in ways they cannot predict or recover from on their own. Improving their performance and robustness typically requires collecting more data, retraining, or modifying the policy architecture, all of which are time- and resource-intensive in practice.
- 📄 [arXiv](https://arxiv.org/abs/2610.19579v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19579v1)

---

### 11. Accelerating VLA Inference with Perturbation Informed Execution
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Action-chunking vision-language-action (VLA) models predict sequences of future robot actions. Under fixed-horizon execution, the robot executes a fixedlength prefix of each predicted chunk before invoking the policy again, leaving the remaining predictions unused. For a given number of executed actions, short execution horizons require more policy calls. Extending the execution horizon amortizes policy inference cost over more actions.
- 📄 [arXiv](https://arxiv.org/abs/2610.19656v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19656v1)

---

### 12. ACRO: Actor-Critic Rollout Orchestration
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Executing a vision-language-action (VLA) policy involves deciding when to continue an attempt and when to intervene to improve its chances of success. We introduce ACRO, an Actor--Critic rollout orchestration layer that makes these decisions for a fixed VLA. ACRO seeks interventions that offer a more promising continuation, are physically feasible, and leave sufficient time to complete the task.
- 📄 [arXiv](https://arxiv.org/abs/2610.19677v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19677v1)

---

### 13. One-shot Human Video-Guided Adaptation for Vision-Language-Action Models
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation. However, their ability to rapidly adapt to novel manipulation tasks beyond the training distribution remains limited. Existing approaches often require task-specific robot demonstrations and additional training, which are labor- and compute-intensive, limiting the scalability of VLA adaptation to open-world scenarios...
- 📄 [arXiv](https://arxiv.org/abs/2610.19746v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19746v1)

---

### 14. ForceBench: Benchmarking Force Integration for Robotic Manipulation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Force feedback provides vision-language-action (VLA) policies with physical observations that can guide action selection and execution. However, differences in tasks, demonstrations, and control settings across existing systems hinder reliable comparisons of force integration designs. We introduce ForceBench, a simulation benchmark for evaluating six-axis wrist-force integration under a unified protocol.
- 📄 [arXiv](https://arxiv.org/abs/2610.19604v1) | 📥 [PDF](https://arxiv.org/pdf/2610.19604v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **$S^3$-Nav: Structured Spatial-Semantic Decision Making for Language-Guided Robot Navigation** (SOP: 6) [Link](https://arxiv.org/abs/2610.19431v1)
- **A Master-to-Simulation Interface with Demonstration-Trajectory Guidance for Vascular Intervention** (SOP: 6) [Link](https://arxiv.org/abs/2610.19395v1)
- **A VR Training System for Robot-Assisted Vascular Intervention with Dual-Mode Control and Model-Based Interaction Response** (SOP: 6) [Link](https://arxiv.org/abs/2610.19413v1)
- **Design and Characterization of a Unified Continuum Robot Actuation Platform** (SOP: 6) [Link](https://arxiv.org/abs/2610.19798v1)
- **Eye, Robot: Learning Expressive Gaze Dynamics via a VLM-Guided Transformer-VAE** (SOP: 6) [Link](https://arxiv.org/abs/2610.19635v1)
- **FOMI: A Force-Feedback Manipulation Interface for Teaching Contact-Rich Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.19839v1)
- **Refine Actions If Needed: Adaptive Action Chunk Refinement for Robot Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.19765v1)
- **Dual-arm Cooperation for Tabletop Wiping with Temporal Object Removal** (SOP: 5) [Link](https://arxiv.org/abs/2610.19527v1)
- **Instruction-Conditioned Motion Control for Robotic Arms: Language-to-Code Decomposition and Reinforcement Learning** (SOP: 5) [Link](https://arxiv.org/abs/2610.19617v1)
- **Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies** (SOP: 5) [Link](https://arxiv.org/abs/2610.19438v1)
- **Runtime Monitoring of Supermartingale Certificates** (SOP: 5) [Link](https://arxiv.org/abs/2610.19701v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 250 篇 | 精选: 14 篇 | 关注: 11 篇 | 过滤: 225 篇
