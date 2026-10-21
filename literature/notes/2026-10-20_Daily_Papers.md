# 🤖 具身智能/机器人学术日报 (2026-10-20)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. Adaptive Traversal Tubes for Posture-Aware Navigation of Bipedal Humanoids
- **SOP Score:** 19
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +17 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, bipedal, locomotion, robot, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Bipedal humanoids can change their effective footprint by adjusting body yaw, enabling both narrow-passage traversal and socially aware yielding. This paper presents a posture-aware navigation framework centered on \emph{Adaptive Traversal Tubes} (ATT), \emph{Interval Velocity--Heading} (IVH) control, and a sidestep-enhanced AMP locomotion prior.
- 📄 [arXiv](https://arxiv.org/abs/2610.27688v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27688v1)

---

### 2. HATCH: Hardware-Attested Task Chains for Verifiable Manipulation
- **SOP Score:** 19
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +3 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Capability claims in robot manipulation are unverifiable, and existing leaderboards are each closed, simulated, or gameable. We propose HATCH, a robot escape room: an openly specified, physically replicable, sensor-scored, and unrehearsable benchmark. Tasks span five skill categories at three difficulty levels and are chained so that the sensor confirming one task's completion unlocks the next, turning a room into a single long-horizon evaluation.
- 📄 [arXiv](https://arxiv.org/abs/2610.27485v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27485v1)

---

### 3. AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies
- **SOP Score:** 18
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** manipulation, behavior cloning
- **Zotero:** 待入库
- **Abstract:** Human-collected real-world robotic manipulation demonstrations often contain mixed-quality trajectories, including hesitant, indirect, or inefficient action segments. While diffusion- and flow-based policies can model such multimodal data, standard behavior cloning (BC) assigns equal likelihood to all demonstrated actions and may therefore reproduce suboptimal modes.
- 📄 [arXiv](https://arxiv.org/abs/2610.27736v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27736v1)

---

### 4. Evaluating Social Reasoning in Embodied Vision-Language Models
- **SOP Score:** 14
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +2 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** robot, embodied
- **Zotero:** 待入库
- **Abstract:** Foundation models now serve as reasoning layers for robot teams, but it remains unclear whether embodiment-specialized vision-language models (VLMs) preserve the social-reasoning capabilities of general-purpose VLMs. We evaluate Gemini Robotics-ER on SHREC, a benchmark of real human-robot social interactions, and compare it with published general-purpose VLM baselines.
- 📄 [arXiv](https://arxiv.org/abs/2610.27496v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27496v1)

---

### 5. EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, quadruped, robot
- **Zotero:** 待入库
- **Abstract:** Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega features and combines historical residual proposals using cellwise weights and a learned no-update option.
- 📄 [arXiv](https://arxiv.org/abs/2610.27616v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27616v1)

---

### 6. Multi-View Latent Action Pretraining for Cross-Embodiment Robot Learning from Videos
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, flow matching, robot
- **Zotero:** 待入库
- **Abstract:** Action-free videos are an appealing substitute for costly teleoperated data. Latent action models (LAMs) turn videos into a supervision signal by inferring abstract actions between frames. Existing LAMs observe a single camera view, which resolves 6D robot actions only ambiguously missing out-of-plane movements and potential occlusions. We propose a LAM that ingests synchronized multi-camera views using cross-attention to resolve depth and occlusions before compressing them into latent actions.
- 📄 [arXiv](https://arxiv.org/abs/2610.27794v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27794v1)

---

### 7. Robot-Task Suitability in Heterogeneous Multi-Robot Task Allocation
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +1 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** robot
- **Zotero:** 待入库
- **Abstract:** Heterogeneous multi-robot task allocation depends on estimates of how suitable individual robots are for candidate tasks, yet suitability can be defined in substantially different ways. We compare ten deterministic methods and two LLM-based variants spanning rule-based, similarity-based, requirement-oriented, fuzzy, and semantic approaches.
- 📄 [arXiv](https://arxiv.org/abs/2610.27504v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27504v1)

---

### 8. RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks. We introduce \textbf{RoboCasa-Shift}, a diagnostic robustness benchmark built on RoboCasa365 that combines controlled single-factor shifts, matched clean-perturbed rollouts in which each pair shares the same underlying settings and differs only in the target shift, and simulator-grounde...
- 📄 [arXiv](https://arxiv.org/abs/2610.27861v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27861v1)

---

### 9. World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** embodied AI, manipulation, embodied
- **Zotero:** 待入库
- **Abstract:** Long-horizon human-object-scene interaction (HOSI) is central to embodied AI, animation, and game development. Existing human-object interaction (HOI) and human-scene interaction (HSI) models excel in their respective domains, but none alone covers tasks requiring multiple interaction skills. Training unified HOSI models is hindered by scarce and costly data.
- 📄 [arXiv](https://arxiv.org/abs/2610.27725v1) | 📥 [PDF](https://arxiv.org/pdf/2610.27725v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning** (SOP: 7) [Link](https://arxiv.org/abs/2610.27613v1)
- **Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum** (SOP: 7) [Link](https://arxiv.org/abs/2610.27865v1)
- **LaLa-World: Scaling Latent World Models with Natural Language Actions** (SOP: 7) [Link](https://arxiv.org/abs/2610.27851v1)
- **PLaCA: Learning Patch-Level Future Latent Change for Action Generation** (SOP: 7) [Link](https://arxiv.org/abs/2610.27657v1)
- **VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs** (SOP: 7) [Link](https://arxiv.org/abs/2610.27698v1)
- **EventSync: Event-Driven Memory Updates for History-Dependent Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.27917v1)
- **Towards Autonomous Bricklaying Using Boston Dynamics Spot** (SOP: 6) [Link](https://arxiv.org/abs/2610.27472v1)
- **What Novice Operators See Changes What the Policy Learns: A User Study of Keypoint Hand Visual Representation for Teleoperated Demonstration** (SOP: 6) [Link](https://arxiv.org/abs/2610.27907v1)
- **Prescribed Performance Guided Safe Reinforcement Learning for Roundabout Navigation of Autonomous Vehicles** (SOP: 5) [Link](https://arxiv.org/abs/2610.27732v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 169 篇 | 精选: 9 篇 | 关注: 9 篇 | 过滤: 151 篇
