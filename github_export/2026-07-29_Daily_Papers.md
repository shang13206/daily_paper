# 🤖 具身智能/机器人学术日报 (2026-07-29)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. Reinforcement Learning on Cost-Constrained Quadrupedal Hardware
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** locomotion, sim-to-real, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Deploying learned control policies on low-cost robotic platforms introduces transport latencies and noisy motor feedback that systematically widens the sim-to-real gap. The chasm of simulation to deployment in hardware lies in the delay of the actuator reaching the commanded position. On platforms such as the Mini Pupper 2, a measured > $50 ms transport delay transforms the locomotion task from a standard Markov decision process into a partially observable one.
- 📄 [arXiv](https://arxiv.org/abs/2607.26434v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26434v1)

---

### 2. RLMM-Flow: A Flow-based Mobile Manipulation Framework with Latent-Space Reinforcement Learning
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** flow policy, manipulation, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Mobile manipulation requires generating whole-body action chunks that jointly satisfy goal reaching, collision avoidance, base kinematic constraints, manipulator joint limits, and trajectory smoothness. Flow-based generative policies provide an efficient paradigm for learning multimodal and temporally consistent motion priors from expert demonstrations, but imitation-only training cannot improve policy quality beyond the demonstration distribution.
- 📄 [arXiv](https://arxiv.org/abs/2607.26460v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26460v1)

---

### 3. CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, world model
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores l...
- 📄 [arXiv](https://arxiv.org/abs/2607.26789v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26789v1)

---

### 4. Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world. This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation. To bridge this crucial gap, we construct a Concept Expert module for VLA to build executable Analytic Concepts that represent objects as explicit, programmatic blueprints.
- 📄 [arXiv](https://arxiv.org/abs/2607.26513v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26513v1)

---

### 5. From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** embodied AI, manipulation, robot, embodied
- **Zotero:** 待入库
- **Abstract:** The key bottleneck in embodied AI is not model architecture but data. Although billions of human manipulation videos exist online, robots cannot directly learn from them due to the embodiment gap between human morphology and robot hardware. We introduce Pegasus, a low-resource framework that bridges this gap by translating human demonstrations into robot-learnable data through structured knowledge transfer.
- 📄 [arXiv](https://arxiv.org/abs/2607.26903v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26903v1)

---

### 6. Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions across manipulation tasks and, even worse, the unavailability of the kinematic signals at inference time. In this work, we first observe that most semantically distinct manipulation tasks reduce to multiple kinematic archetypes.
- 📄 [arXiv](https://arxiv.org/abs/2607.26807v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26807v1)

---

### 7. SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Deep reinforcement policy learning directly in physical robots (on-robot learning) remains bottlenecked by slow wall-clock training times. We present SymmGrid, a trajectory level augmentation framework inspired by parallelized symmetries that super-scales group transformations to significantly accelerate on-robot learning in both egocentric and exocentric visual setups.
- 📄 [arXiv](https://arxiv.org/abs/2607.26985v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26985v1)

---

### 8. RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** imitation learning, VLA
- **Zotero:** 待入库
- **Abstract:** Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore inherit correlated failure modes.
- 📄 [arXiv](https://arxiv.org/abs/2607.26991v1) | 📥 [PDF](https://arxiv.org/pdf/2607.26991v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **ContactFlow: A video action conditioning that transfers across embodiments** (SOP: 7) [Link](https://arxiv.org/abs/2607.26579v1)
- **Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation** (SOP: 6) [Link](https://arxiv.org/abs/2607.26646v1)
- **Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations** (SOP: 6) [Link](https://arxiv.org/abs/2607.26809v1)
- **SCOUT: Per-Context Reset Curricula for Sparse-Reward Reinforcement Learning** (SOP: 6) [Link](https://arxiv.org/abs/2607.26417v1)
- **Speech2Grasp: Data-Efficient Transfer of Text-Conditioned Grasp Detection to Speech in Humanoid Robots** (SOP: 6) [Link](https://arxiv.org/abs/2607.26567v1)
- **Vision-TL-Action: Neuro-Symbolic Trajectory Generation from Visual Observations and Temporal Logic** (SOP: 6) [Link](https://arxiv.org/abs/2607.26770v1)
- **ActSWM: Action-Sensitive World Models for Long-Horizon Planning in Open-World Games** (SOP: 5) [Link](https://arxiv.org/abs/2607.26712v1)
- **Risk-Aware Motion Planning with Learned Trajectory Primitives and Probabilistic Safety Assessment** (SOP: 5) [Link](https://arxiv.org/abs/2607.26802v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 239 篇 | 精选: 8 篇 | 关注: 8 篇 | 过滤: 223 篇
