# 🤖 具身智能/机器人学术日报 (2026-09-18)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. FootQuery: Future-Touchdown-Guided Retrieval from Depth History for Perceptive Humanoid Locomotion
- **SOP Score:** 19
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, terrain
- **Zotero:** 待入库
- **Abstract:** Humanoid locomotion over complex terrain requires anticipating footholds that may no longer be visible at touchdown. Limited camera coverage and self-occlusion make it necessary to retrieve relevant terrain information from earlier observations. We present FootQuery, a perceptive locomotion framework that queries depth history using each foot's predicted next touchdown.
- 📄 [arXiv](https://arxiv.org/abs/2609.21447v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21447v1)

---

### 2. Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies
- **SOP Score:** 18
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies solve the same manipulation task through different action interfaces, but task success alone does not establish whether their physical executions agree. We study cross-policy end-effector geometry in 15,000 closed-loop LIBERO rollouts from four policies. The primary clean-condition analysis forms 3,600 configuration-matched, and therefore dependent, policy pairs. Both-success pairs have a median normalized dynamic time warping distance of 0.0120 m versus 0.
- 📄 [arXiv](https://arxiv.org/abs/2609.21659v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21659v1)

---

### 3. Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** world model
- **Zotero:** 待入库
- **Abstract:** Accurate neural world models are central to model-based robotics, where they enable robots to predict future states from previously observed trajectories. Multi-step autoregressive training improves long-horizon prediction, but fixed rollout horizons also increase computational cost and can amplify early training errors when the model is still inaccurate.
- 📄 [arXiv](https://arxiv.org/abs/2609.21482v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21482v1)

---

### 4. Robust Structureless Monocular Visual Inertial Initialization Exploiting Line Features and Vanishing Points
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +0 | Hardware +0 | Code +3 | cs.RO +2
- **Venue:** IROS
- **Zotero:** 待入库
- **Abstract:** Accurate initialization is essential for reliable visual-inertial odometry (VIO), but it is often ill-conditioned under degenerate motions. Existing methods typically require restrictive excitation motions to ensure sufficient observability or rely on computationally expensive 3D structure reconstruction, limiting efficient and practical deployment.
- 📄 [arXiv](https://arxiv.org/abs/2609.21186v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21186v1)

---

### 5. KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** sim-to-real, manipulation, motion planning, robot
- **Zotero:** 待入库
- **Abstract:** Learning robot manipulation policies typically requires substantial demonstration data, which are costly to collect on real robots. Recent methods generate robot demonstrations from human videos by adapting recovered motion and validating the resulting trajectories in simulation. However, methods centered on motion-reference adaptation can limit behavioral diversity by retaining the demonstrated contact strategies and subtask orders, while insufficient understanding of task requirements and scen...
- 📄 [arXiv](https://arxiv.org/abs/2609.21229v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21229v1)

---

### 6. From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** A pretrained robot foundation policy may execute most of a long-horizon task yet repeatedly fail at a few critical subtasks. Collecting additional full-task demonstrations for supervised fine-tuning (SFT) requires operators to repeat behaviors the policy already performs well. Reinforcement learning (RL) fine-tuning offers a promising path to bridge this gap, but existing approaches struggle to solve long-horizon tasks using only sparse rewards.
- 📄 [arXiv](https://arxiv.org/abs/2609.21788v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21788v1)

---

### 7. SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, reinforcement learning, robot, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Fine-tuning Vision-Language-Action (VLA) models commonly relies on human teleoperation demonstrations, while reinforcement learning (RL) with sparse binary rewards faces an exploration challenge when successful trajectories are rarely sampled. We propose SynthDemo-RL, a teacher-student framework in which an automated teacher converts simulator-privileged state into successful manipulation trajectories, a VLA student is distilled from them by supervised fine-tuning (SFT), and PPO with binary task...
- 📄 [arXiv](https://arxiv.org/abs/2609.21650v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21650v1)

---

### 8. Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** flow matching, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies based on flow matching generate action chunks through repeated evaluations of an action expert. Increasing the number of integration steps raises inference cost, but does not necessarily improve closed-loop success. We propose Coda, which reallocates part of this integration budget to a single learned endpoint correction.
- 📄 [arXiv](https://arxiv.org/abs/2609.21216v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21216v1)

---

### 9. ForceTwin: Physics-informed Digital Twins for Robotic Manipulation from Instrumented Human Interaction
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +3 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Manipulating objects requires understanding not only their motion, but also the physical properties that determine it. For articulated objects, these include inertia, friction, and mechanisms such as springs or door closers, whose effects can vary with configuration and velocity. Such properties are not directly observable from appearance: visually identical doors may require very different effort to manipulate.
- 📄 [arXiv](https://arxiv.org/abs/2609.21751v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21751v1)

---

### 10. ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** flow matching, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** World Action Models bring the predictive capabilities of video models into robot action generation, providing a rich foundation for modeling future visual states. Tactile sensing complements this foundation with direct measurements of physical interaction. Some existing methods use tactile features as conditioning inputs without jointly predicting future tactile states, visual observations, and actions.
- 📄 [arXiv](https://arxiv.org/abs/2609.21449v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21449v1)

---

### 11. Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Model-free reinforcement learning can acquire contact-rich robotic manipulation skills through trial-and-error interaction, but it often requires the policy to learn both task strategy and low-level motion generation. In this setting, the action representation is critical because it determines how policy outputs are converted into robot motion, shaping both exploration and physical execution.
- 📄 [arXiv](https://arxiv.org/abs/2609.21609v1) | 📥 [PDF](https://arxiv.org/pdf/2609.21609v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **Adaptive Color Grading** (SOP: 6) [Link](https://arxiv.org/abs/2609.21169v1)
- **FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision-Language-Action Models** (SOP: 6) [Link](https://arxiv.org/abs/2609.21228v1)
- **ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2609.21369v1)
- **A Scene Language Model for Open-Vocabulary Scene Mapping** (SOP: 5) [Link](https://arxiv.org/abs/2609.21400v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 332 篇 | 精选: 11 篇 | 关注: 4 篇 | 过滤: 184 篇
- 元数据不完整: 133 篇（不参与自动精选）
