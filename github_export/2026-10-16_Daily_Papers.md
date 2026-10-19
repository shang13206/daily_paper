# 🤖 具身智能/机器人学术日报 (2026-10-16)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. Pedicel-Targeted Strawberry Harvesting via Imitation Learning on a Low-Cost Teleoperated Robotic Arm
- **SOP Score:** 27
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +12 | Hardware +0 | Code +3 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation, grasping, imitation learning, motion planning
- **Zotero:** 待入库
- **Abstract:** Precise pedicel-targeted grasping in strawberry harvesting remains a critical bottleneck due to the pedicel's small diameter (1.3-3 mm), color similarity with surrounding foliage, and precise force control required for clean abscission zone detachment. As a market-grade crop, strawberry aesthetic value makes bruise-free pedicel detachment essential over direct fruit grasping.
- 📄 [arXiv](https://arxiv.org/abs/2610.22765v1) | 📥 [PDF](https://arxiv.org/pdf/2610.22765v1)

---

### 2. CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots
- **SOP Score:** 19
- **SOP 评分证据:** Venue +5 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ICLR
- **Keywords:** humanoid, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation.
- 📄 [arXiv](https://arxiv.org/abs/2610.23288v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23288v1)

---

### 3. Structured Perception Representations for Off-road Dynamics Learning
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** terrain, robot
- **Zotero:** 待入库
- **Abstract:** Autonomously navigating off-road terrain at high speed demands accurate control, which often relies on dynamics models that capture complex interactions between the robot and terrain. In off-road regimes, terrain interaction is a major component of the vehicle's dynamics. Prior work attempts to capture this effect by training learned models of the vehicle's dynamics, conditioned on its perception of the local environment.
- 📄 [arXiv](https://arxiv.org/abs/2610.22900v1) | 📥 [PDF](https://arxiv.org/pdf/2610.22900v1)

---

### 4. BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, world model, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Humanoid control requires coordinating whole-body posture with position and heading in the world frame. Mainstream controllers imitate trajectories in the root frame, but struggle to regain the target world pose after displacement. We introduce BeJEPA, a goal-conditioned Behavior World Model learned through unsupervised reinforcement learning from human motion priors and robot interaction.
- 📄 [arXiv](https://arxiv.org/abs/2610.23127v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23127v1)

---

### 5. Ego2Contact: Predicting Touch from Egocentric Human Video for Contact-Rich Robot Manipulation
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot policy, manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Contact locations and interaction forces are critical for contact-rich robot manipulation but are often ambiguous from vision alone. Measuring them on robots requires specialized tactile hardware and platform-specific data collection, which keeps robot tactile data scarce. Human egocentric video is far easier to scale but lacks touch. Recent predictors trained on egocentric recordings paired with tactile-glove measurements can predict this missing signal from video alone.
- 📄 [arXiv](https://arxiv.org/abs/2610.22932v1) | 📥 [PDF](https://arxiv.org/pdf/2610.22932v1)

---

### 6. GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** flow policy, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-Language-Action (VLA) models that directly regress joint-space actions avoid the deployment-time cost of inverse kinematics. However, their training objectives remain misaligned with task success, as joint-space losses ignore the unequal physical consequences of joint errors and visual conditioning lacks explicit focus on hand-object interaction regions. To address these issues, we propose a training-phase prior injection framework for fine-grained bimanual manipulation.
- 📄 [arXiv](https://arxiv.org/abs/2610.23123v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23123v1)

---

### 7. Simultaneous Force and Motion Control in Generalised Coordinates
- **SOP Score:** 14
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +2 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** robot, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Robot manipulators often come into contact with rigid objects when performing work. This imposes physical constraints on their motion. Simultaneous force & motion control was developed to regulate contact forces commensurate with these constraints, whilst projecting motion control in to the orthogonal, unconstrained directions. This is typically formulated in the task coordinates, i.e. operational space, then mapped to joint torques to command the robot.
- 📄 [arXiv](https://arxiv.org/abs/2610.22813v1) | 📥 [PDF](https://arxiv.org/pdf/2610.22813v1)

---

### 8. MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +4 | Code +3 | cs.RO +0
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models have shown strong promise for generalist robotic manipulation, but their inference cost remains a major bottleneck for real-time control. This limitation is especially pronounced in flow-matching VLAs such as $π_{0.5}$, where the action expert is evaluated repeatedly during iterative denoising. We introduce MambaAct, an efficient Mamba action expert for flow-matching VLA policies. MambaAct retains the pretrained visual-language prefix encoder of $π_{0.
- 📄 [arXiv](https://arxiv.org/abs/2610.22951v1) | 📥 [PDF](https://arxiv.org/pdf/2610.22951v1)

---

### 9. NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models
- **SOP Score:** 11
- **SOP 评分证据:** Venue +5 | Institution +0 | Keywords +3 | Hardware +0 | Code +3 | cs.RO +0
- **Venue:** NeurIPS
- **Keywords:** VLA
- **Zotero:** 待入库
- **Abstract:** Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes. We instead advocate a paradigm in which skills are first learned independently and then consolidated post hoc.
- 📄 [arXiv](https://arxiv.org/abs/2610.23271v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23271v1)

---

### 10. Unifying Embodied Foundation Models via a Model-to-Policy Formulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** robot learning, VLA, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models and world-action models (WAMs) have emerged as promising approaches to robot learning and control. These models integrate multimodal perception and action generation, but differ in their architectures, output representations, and learning objectives. In this paper, we present a unified, architecture-agnostic probabilistic formulation for embodied foundation models based on stochastic kernels.
- 📄 [arXiv](https://arxiv.org/abs/2610.23053v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23053v1)

---

### 11. VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, embodied
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models are rapidly expanding what individual robots can accomplish, yet many real-world manipulation settings require multiple arms to operate as a coordinated system. Existing approaches organize multi-arm coordination in different ways, including centralized joint policies, high-level task or role assignment, and locally executed policies that react to teammates.
- 📄 [arXiv](https://arxiv.org/abs/2610.23018v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23018v1)

---

### 12. I2V-DETACH: Source Grounding Detachment for Unauthorized Image-to-Video Generation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +5 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** NeurIPS
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Recent diffusion models have advanced image-conditioned video generation, but their accessibility raises risks of unauthorized manipulation. Image immunization has emerged as a promising defense for Image-to-Video (I2V) protection, yet existing methods often rely on degrading visual quality or temporal coherence. In this work, we revisit I2V immunization as reducing source-content preservation, shifting the focus from output degradation to weakening source-conditioned content propagation.
- 📄 [arXiv](https://arxiv.org/abs/2610.23287v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23287v1)

---

### 13. ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, world model
- **Zotero:** 待入库
- **Abstract:** World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks. However, existing image-based and dense 3D world models do not explicitly impose object-level rigid motion, leaving rigid-object geometry preservation to be learned implicitly and making multi-step rollouts susceptible to shape drift or object-level motion inconsistency.
- 📄 [arXiv](https://arxiv.org/abs/2610.23156v1) | 📥 [PDF](https://arxiv.org/pdf/2610.23156v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence** (SOP: 7) [Link](https://arxiv.org/abs/2610.23334v1)
- **PASS-VLN: Passability-Aware Local-Command Vision-and-Language Navigation** (SOP: 7) [Link](https://arxiv.org/abs/2610.22812v1)
- **PASS: A Trustworthy Precision Approach Simulation System for CAT III Integrity Algorithm Development** (SOP: 7) [Link](https://arxiv.org/abs/2610.23019v1)
- **Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors** (SOP: 7) [Link](https://arxiv.org/abs/2610.22852v1)
- **DefFlow: Goal-Conditioned Deformable Object Manipulation using 3D Point Flows** (SOP: 6) [Link](https://arxiv.org/abs/2610.22827v1)
- **From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models** (SOP: 6) [Link](https://arxiv.org/abs/2610.23319v1)
- **HAPACT: A Benchmark For Human-Centric Physical Impact Localization in Movies** (SOP: 6) [Link](https://arxiv.org/abs/2610.22895v1)
- **InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration** (SOP: 6) [Link](https://arxiv.org/abs/2610.23098v1)
- **LY-GWM-RoboCasa-Human300: Prediction-Guided Action Selection with a Graph Dynamics Model** (SOP: 6) [Link](https://arxiv.org/abs/2610.23274v1)
- **Robotic Spatiotemporal Editing: A Unified Interface for Controllable Action Generation via Masked Action Reconstruction** (SOP: 6) [Link](https://arxiv.org/abs/2610.23002v1)
- **SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning** (SOP: 6) [Link](https://arxiv.org/abs/2610.23128v1)
- **Shape-Aware Neural Time Fields for Rigid-Body Motion and Manipulation Planning** (SOP: 6) [Link](https://arxiv.org/abs/2610.22762v1)
- **SimpleVLN: Towards Simple and Frontier Vision-Language Navigation** (SOP: 6) [Link](https://arxiv.org/abs/2610.23203v1)
- **Foundation Models for Autonomous Space Robotics: Architectures, Physical Adaptation, and Validation** (SOP: 5) [Link](https://arxiv.org/abs/2610.23068v1)
- **Hardware-as-Regularization: Enhancing Data Consistency in Imitation Learning via an Adjustable Passive Compliant Leader Arm** (SOP: 5) [Link](https://arxiv.org/abs/2610.22977v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 209 篇 | 精选: 13 篇 | 关注: 15 篇 | 过滤: 181 篇
