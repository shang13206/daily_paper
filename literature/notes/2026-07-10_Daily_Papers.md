# 🤖 具身智能/机器人学术日报 (2026-07-10)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** RSS
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint.
- 📄 [arXiv](https://arxiv.org/abs/2607.09519v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09519v1)

---

### 2. One-Shot Multimodal Learning from Demonstration with Force-Constrained Elastic Maps
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Robotic manipulation tasks often require simultaneous reasoning over motion and contact forces, yet most Learning from Demonstration (LfD) methods model only spatial trajectories and neglect force interactions with the environment. This limitation reduces robustness and can lead to unsafe or inconsistent task reproduction in force-constrained settings. We propose a novel one-shot multimodal LfD framework for the segmentation, encoding, and reproduction of force-inclusive demonstrations.
- 📄 [arXiv](https://arxiv.org/abs/2607.09515v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09515v1)

---

### 3. Task-Adaptive Design of Modular Aerial Manipulators Under Airflow Exposure Constraints
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Aerial manipulation with multirotor platforms enables physical interaction in complex environments, but rotor-induced airflow remains a critical limitation for tasks involving airflow-sensitive targets or surroundings. This paper presents an optimization-based design framework for modular aerial manipulators that jointly considers task wrench feasibility, end-effector placement, and airflow exposure constraints.
- 📄 [arXiv](https://arxiv.org/abs/2607.09548v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09548v1)

---

### 4. Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
- **SOP Score:** 14
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** RSS
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-l...
- 📄 [arXiv](https://arxiv.org/abs/2607.09218v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09218v1)

---

### 5. Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** sim-to-real, robot
- **Zotero:** 待入库
- **Abstract:** Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing.
- 📄 [arXiv](https://arxiv.org/abs/2607.09060v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09060v1)

---

### 6. Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** locomotion, manipulation, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability.
- 📄 [arXiv](https://arxiv.org/abs/2607.09336v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09336v1)

---

### 7. TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting in motion imitation without physically grounded interaction.
- 📄 [arXiv](https://arxiv.org/abs/2607.09190v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09190v1)

---

### 8. Learning More from Less: Reinforcement Learning from Hindsight
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** manipulation, VLA, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, but every update consumes robot rollouts that are slow and costly to collect, making sample efficiency a central concern. Manipulation tasks typically provide only sparse rewards, so a weak policy fails almost every rollout early in training and has little to learn from, even when those failures execute coherent behavior. Such a failure, however, is a success at a different task.
- 📄 [arXiv](https://arxiv.org/abs/2607.09042v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09042v1)

---

### 9. Differential Analysis of Multispectral Images for Terrain Identification
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot navigation, terrain, robot
- **Zotero:** 待入库
- **Abstract:** Reliable terrain understanding is a prerequisite for autonomous robot navigation. Yet, the widespread RGB-based perception can fail under low illumination, shadows, and material ambiguities. In this work we propose DRIFT, a lightweight multispectral framework that combines raw spectral bands and illumination-tolerant band-ratio representations through a dual-stream residual architecture and a differential fusion branch.
- 📄 [arXiv](https://arxiv.org/abs/2607.09319v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09319v1)

---

### 10. Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, grasping, robot
- **Zotero:** 待入库
- **Abstract:** We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks.
- 📄 [arXiv](https://arxiv.org/abs/2607.09315v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09315v1)

---

### 11. Effects of Robotic Touch on Older Users During Walking Guidance by a Humanoid Robot
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, robot
- **Zotero:** 待入库
- **Abstract:** The shortage of healthcare staff is a challenge in geriatric care. To address this, robots can be integrated into care settings to provide assistance and emotional support. A promising application is walking guidance, particularly benefiting older adults as navigation skills deteriorate with aging. As walking guidance involves direct contact, the aim of this study is to understand how older adults perceive and respond to different touch modes during guided walking. 24 older adults (68 - 88 yrs.
- 📄 [arXiv](https://arxiv.org/abs/2607.09323v1) | 📥 [PDF](https://arxiv.org/pdf/2607.09323v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **BeyondSight: Object Permanence for End-to-End Autonomous Driving** (SOP: 7) [Link](https://arxiv.org/abs/2607.09138v1)
- **CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles** (SOP: 7) [Link](https://arxiv.org/abs/2607.09557v1)
- **GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency** (SOP: 7) [Link](https://arxiv.org/abs/2607.09191v1)
- **PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers** (SOP: 7) [Link](https://arxiv.org/abs/2607.09590v1)
- **B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations** (SOP: 6) [Link](https://arxiv.org/abs/2607.09648v1)
- **Empirical Pedestrian Safety Assessment in a Mobile Robot Using a Predictive Social Force Model** (SOP: 6) [Link](https://arxiv.org/abs/2607.09192v1)
- **PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2607.09365v1)
- **Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference** (SOP: 6) [Link](https://arxiv.org/abs/2607.09520v1)
- **Validating Virtual Reality for Studying Multimodal Human-Robot Interaction in Socially Aware Robot Navigation** (SOP: 6) [Link](https://arxiv.org/abs/2607.09261v1)
- **Vascular Geometry Characterization for AI-Based Endovascular Navigation** (SOP: 5) [Link](https://arxiv.org/abs/2607.09130v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 196 篇 | 精选: 11 篇 | 关注: 10 篇 | 过滤: 175 篇
