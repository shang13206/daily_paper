# 🤖 具身智能/机器人学术日报 (2026-10-23)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot
- **SOP Score:** 21
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +15 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** quadruped, manipulation, grasping, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame.
- 📄 [arXiv](https://arxiv.org/abs/2610.32271v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32271v1)

---

### 2. CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying
- **SOP Score:** 19
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** humanoid, whole-body control, terrain
- **Zotero:** 待入库
- **Abstract:** Recent advances in large-scale human motion data, motion retargeting, and motion imitation have enabled increasingly capable whole-body control for individual humanoids. Cooperative carrying is more challenging because successful coordination requires not only plausible individual motions, but also consistent cross-agent and agent-object relations, including shared grasp, relative configuration, and whole-body support.
- 📄 [arXiv](https://arxiv.org/abs/2610.32460v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32460v1)

---

### 3. MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation
- **SOP Score:** 19
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Generalist robot manipulation requires a single vision-language-action (VLA) policy to execute diverse skills across scenes and instructions. However, current multi-skill VLA policies often leave two aspects of an instruction insufficiently modeled: which primitive skill to execute and where/how to contact and move objects. We propose MAST-VLA (Multi-skill Adaptation with Skill-conditioned experts and Trajectory-affordance priors), a dual-conditioning framework for robot manipulation.
- 📄 [arXiv](https://arxiv.org/abs/2610.32312v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32312v1)

---

### 4. Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies
- **SOP Score:** 18
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** robot learning, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Flow-matching Vision-Language-Action (VLA) models generate expressive continuous trajectories for robotic manipulation, yet balancing real-time responsiveness with execution stability remains a persistent challenge. Standard deployment workflows typically treat numerical solver depth and execution horizon as decoupled choices. The horizon amortizes inference latency, while solver depth is kept high to preserve integration fidelity.
- 📄 [arXiv](https://arxiv.org/abs/2610.32102v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32102v1)

---

### 5. DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning
- **SOP Score:** 18
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +16 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, imitation learning, behavior cloning, VLA, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Behavior cloning for robotic manipulation is highly sensitive to the coverage of its training data, yet collecting diverse successful demonstrations remains costly. We study reinforcement learning (RL) not as a deployable controller, but as a data generator for downstream visuomotor imitation learning. Our key premise is that multiple successful solution modes cover a broader range of successful trajectories than repeatedly collecting a single narrow solution.
- 📄 [arXiv](https://arxiv.org/abs/2610.32093v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32093v1)

---

### 6. Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, robot, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Learned humanoid controllers are usually trained in one simulator and then checked in a second one before they go near hardware. We ask what that check says about command delay. We train motion-tracking policies for a 24-joint humanoid on five motions taken from monocular video and test them in an independent CPU MuJoCo harness, which we first verify against the training model. Every policy completes its motion in at least 26 of 30 episodes under the training randomization.
- 📄 [arXiv](https://arxiv.org/abs/2610.32277v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32277v1)

---

### 7. Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems
- **SOP Score:** 14
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** CoRL
- **Keywords:** VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-Language-Action (VLA) models have emerged as powerful general-purpose robot policies, but their successes and failures remain difficult to diagnose and understand. In this work, we show that sparse autoencoder (SAE) representations of OpenVLA activations contain outcome-predictive information and can be used to predict task failure before the robot reaches an unrecoverable state.
- 📄 [arXiv](https://arxiv.org/abs/2610.32208v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32208v1)

---

### 8. RoboCode: Learning Reusable Action Primitives for Robot Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** diffusion policy, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Recent robot manipulation policies commonly predict continuous action chunks directly from observations, without explicitly modeling reusable structure in the action space. However, manipulation demonstrations often contain recurring short-horizon motion patterns that are shared across tasks. We introduce \textsc{RoboCode}, which learns these patterns through a shared soft-gated primitive action interface.
- 📄 [arXiv](https://arxiv.org/abs/2610.32225v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32225v1)

---

### 9. TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** reinforcement learning, terrain
- **Zotero:** 已完成入库
- **Abstract:** Traversability analysis in off-road settings remains a fundamental challenge for mobile robots. Key difficulties include constructing an accurate and expressive local map from multimodal sensor data, and using the map to design traversability rules that yield desirable navigation behavior. Importantly, this system must be resilient to the limited sensing regime brought about by complex environments and high speeds.
- 📄 [arXiv](https://arxiv.org/abs/2610.32130v1) | 📥 [PDF](https://arxiv.org/pdf/2610.32130v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.32330v1)
- **From Freehand Demonstrations to Autonomous Robotic Ultrasound: An Anatomy-Anchored Learning Framework** (SOP: 6) [Link](https://arxiv.org/abs/2610.32525v1)
- **Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion** (SOP: 6) [Link](https://arxiv.org/abs/2610.32143v1)
- **HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching** (SOP: 6) [Link](https://arxiv.org/abs/2610.32554v1)
- **LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners** (SOP: 6) [Link](https://arxiv.org/abs/2610.32348v1)
- **PPO vs. SAC: A Comparative Study for Cooperative Motion Control of Dual-Arm Space Robots** (SOP: 6) [Link](https://arxiv.org/abs/2610.32034v1)
- **$R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design** (SOP: 5) [Link](https://arxiv.org/abs/2610.32439v1)
- **Graphs of Trajectory Bundles for Nonlinear Motion Planning** (SOP: 5) [Link](https://arxiv.org/abs/2610.32365v1)
- **OWLS: Open-world Language-conditioned Speed Fields for Zero-Shot Rover Navigation** (SOP: 5) [Link](https://arxiv.org/abs/2610.32596v1)
- **SKG in Practice: OOD Generalization Cases Across FourDomains** (SOP: 5) [Link](https://arxiv.org/abs/2610.32314v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 188 篇 | 精选: 9 篇 | 关注: 10 篇 | 过滤: 169 篇
