# 🤖 具身智能/机器人学术日报 (2026-07-16)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation
- **SOP Score:** 27
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +11 | Hardware +4 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** sim-to-real, behavior cloning, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** End-to-end diffusion-based policies have demonstrated strong performance in mapless visual navigation, but their iterative denoising process introduces substantial inference latency, while behavior cloning limits performance to the quality of expert demonstrations. We present NavCMPO, a two-stage adaptive navigation framework that combines few-step MeanFlow trajectory generation, critic-guided refinement, and reinforcement learning fine-tuning.
- 📄 [arXiv](https://arxiv.org/abs/2607.14643v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14643v1)

---

### 2. Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments
- **SOP Score:** 24
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +8 | Hardware +4 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** humanoid, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Reinforcement Learning (RL) has demonstrated remarkable capabilities for solving complex robotic control problems, but its lack of safety guarantees severely limits deployment on hardware. In particular, as legged robots and manipulators often operate near safety-critical boundaries, out-of-distribution states can lead to failure upon deployment.
- 📄 [arXiv](https://arxiv.org/abs/2607.14488v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14488v1)

---

### 3. BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching
- **SOP Score:** 20
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** flow matching, motion planning
- **Zotero:** 待入库
- **Abstract:** In robotic motion planning, equivariance to rigid body transformations is crucial for robust spatial generalization. However, current learning-based planners face a critical dilemma: they either lack inherent equivariance, treating transformed tasks as novel scenarios, or enforce it via computationally expensive specialized architectures that bottleneck real-time inference. To break this trade-off, we propose BridgeFlow, a fast and strictly SE(2)-equivariant generative motion planning framework.
- 📄 [arXiv](https://arxiv.org/abs/2607.14725v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14725v1)

---

### 4. Learning Agile Navigation in Crowded Environments for Quadruped Robots
- **SOP Score:** 20
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** quadruped, locomotion, agile, robot
- **Zotero:** 待入库
- **Abstract:** Navigating dynamic and crowded environments presents significant challenges for quadruped robots due to severe sensor occlusion and unpredictable human motion. Existing approaches face a trade-off: model-based methods, such as Velocity Obstacles (VO), theoretically guarantee safety but rely on accurate obstacle motion estimates that often fail in dense crowds, while end-to-end learning methods offer robustness but lack motion prediction capability of obstacles, leading to collisions or conservat...
- 📄 [arXiv](https://arxiv.org/abs/2607.15036v1) | 📥 [PDF](https://arxiv.org/pdf/2607.15036v1)

---

### 5. Reinforcement Learning for the Full Strawberry Harvesting Process: Obstacle Separation, Detachment, and Placement
- **SOP Score:** 20
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** sim-to-real, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Severe occlusions and deformable plant structures introduce complex contact dynamics that challenge robotic strawberry harvesting. A policy-driven reinforcement learning (RL) framework with heuristic phase coordination was developed, in which obstacle separation, fruit detachment, and placement were formulated as a sequential decision-making task.
- 📄 [arXiv](https://arxiv.org/abs/2607.14708v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14708v1)

---

### 6. Hybrid Rigid-Soft Robotic Gripper with Shape Adaptation, Uniform Force Distribution, and Self-Locking Capabilities
- **SOP Score:** 18
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** manipulation, grasping
- **Zotero:** 待入库
- **Abstract:** Conventional robotic grippers face a significant challenge in agricultural automation: the trade-off between compliant, adaptive grasping, pressure balancing among all joints, and high load capacity, often at the cost of high energy consumption. This paper presents a novel hybrid rigid-soft gripper that integrated low-cost, membrane-based pneumatic actuators with 3D-printed dual ratchet-pawl mechanisms to simultaneously achieve shape adaptation, uniform force distribution, and energy-free self-l...
- 📄 [arXiv](https://arxiv.org/abs/2607.14730v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14730v1)

---

### 7. Catch, Throw, Repeat: Planning for Human-Robot Partner Juggling
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** motion planning, robot
- **Zotero:** 待入库
- **Abstract:** Dynamic object exchange between humans and robots remains a challenging problem due to uncertainty in perception, timing, and contact-rich interaction. Human-robot juggling represents a particularly demanding instance of this problem, requiring precise real-time coordination, predictive motion planning with feedback control, and robustness to variability in human motion. Enabling such skills is of interest for advancing physical human-robot interaction and shared autonomy.
- 📄 [arXiv](https://arxiv.org/abs/2607.15129v1) | 📥 [PDF](https://arxiv.org/pdf/2607.15129v1)

---

### 8. Beyond Implicit Force: Evaluating Explicit Force-Torque Proxies in Action Chunking with Transformers
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Contact-rich manipulation requires policies to infer interaction state from signals that are often weakly observable through vision and kinematics alone. Action Chunking with Transformers (ACT) has shown strong performance in fine-grained manipulation, but many deployments collect demonstrations through leader-follower teleoperation, where tracking error between commanded leader motion and executed follower motion implicitly encodes contact, resistance, and constraint violation.
- 📄 [arXiv](https://arxiv.org/abs/2607.14578v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14578v1)

---

### 9. KineFuse: Kinematic-Aware Haptic Fusion for In-Hand Occluded-Object Pose Tracking
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Dexterous in-hand manipulation requires continuous 6D pose tracking, yet the manipulating fingers inevitably occlude the object from the camera. We study how to structure the sparse haptic signals already available on multi-fingered hands, including proprioception, proximal force/torque, and binary contact, to complement a pretrained visual pose tracker under occlusion.
- 📄 [arXiv](https://arxiv.org/abs/2607.14842v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14842v1)

---

### 10. SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation
- **SOP Score:** 14
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +2 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** robot, embodied
- **Zotero:** 待入库
- **Abstract:** In goal-directed embodied navigation, where an agent must locate a specified target in an unseen environment, 3D scene understanding and navigation reasoning must work in concert. Current approaches transmit 3D scene information to vision-language models (VLMs) through text, suggesting a representation gap in our tested configurations; a controlled ablation confirms that direct embedding-level transfer significantly outperforms the evaluated text serialization formats.
- 📄 [arXiv](https://arxiv.org/abs/2607.14586v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14586v1)

---

### 11. Curvature-Constrained and Constant-Speed Distributed Simultaneous Arrival Control for Multi-Robot Systems
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +1 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** robot
- **Zotero:** 待入库
- **Abstract:** The simultaneous arrival of multiple mobile robots at a target point is crucial for cooperation tasks such as cooperative encirclement, disaster relief, and environmental monitoring. Although the simultaneous arrival problem itself is already complex, the problem becomes more challenging when there are constraints on the robot trajectory curvatures and the speeds are required to be constant (possibly different for different robots), and the control law for robots needs to be distributed.
- 📄 [arXiv](https://arxiv.org/abs/2607.14781v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14781v1)

---

### 12. Mixed-Agent Museum Tour Guide Design Improves Gendered Learning Outcomes and Visitor Preferences
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +1 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** robot
- **Zotero:** 待入库
- **Abstract:** Robots are increasingly integrated into everyday contexts, including museums, where they can both entertain and educate visitors. To enhance visitor experience and engagement, we present a novel mixed-agent tour guide system that combines a physical robot with a projected virtual agent that actively participates in the tour through conversation and interaction, achieving the interaction richness of two mobile agents from a single platform.
- 📄 [arXiv](https://arxiv.org/abs/2607.14468v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14468v1)

---

### 13. Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA) models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models.
- 📄 [arXiv](https://arxiv.org/abs/2607.14852v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14852v1)

---

### 14. MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Dexterous manipulation is limited not only by algorithms but by a shortage of accessible hand hardware that combines human-scale morphology, ease of manufacturing or maintenance, tactile sensing, and practical cost. Existing dexterous hands tend to optimize some of these properties at the expense of others. We present MIDAS Hand, a low-cost, open-source, human-scale dexterous hand with integrated tactile sensing for manipulation research.
- 📄 [arXiv](https://arxiv.org/abs/2607.14487v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14487v1)

---

### 15. Reflex: Real-Time VLA Control through Streaming Inference
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** flow matching, VLA
- **Zotero:** 待入库
- **Abstract:** Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse.
- 📄 [arXiv](https://arxiv.org/abs/2607.14695v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14695v1)

---

### 16. Scaling Behavior Foundation Model for Humanoid Robots
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** humanoid, embodied
- **Zotero:** 待入库
- **Abstract:** Humanoid control requires natural whole-body coordination, precise real-time responses to control signals, and robust generalization across diverse environmental contexts, making it a cornerstone for generalist embodied agents. Behavior Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale behavioral data to achieve superior expressiveness, versatility and generalization.
- 📄 [arXiv](https://arxiv.org/abs/2607.15163v1) | 📥 [PDF](https://arxiv.org/pdf/2607.15163v1)

---

### 17. Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals.
- 📄 [arXiv](https://arxiv.org/abs/2607.14698v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14698v1)

---

### 18. Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** sim-to-real, VLA
- **Zotero:** 待入库
- **Abstract:** Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision is applied too directly to the inherited multimodal pathway, it can also destabilize representations that support language-side process...
- 📄 [arXiv](https://arxiv.org/abs/2607.14635v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14635v1)

---

### 19. Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-rich manipulation, where critical interaction states are often hidden from vision. Future tactile prediction is a promising way to use touch because it turns tactile outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain representations with different roles, from perceptual encoding to motor prediction, making it unclear where this supervision should be applied.
- 📄 [arXiv](https://arxiv.org/abs/2607.14609v1) | 📥 [PDF](https://arxiv.org/pdf/2607.14609v1)

---

### 20. SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +5 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** sim-to-real
- **Zotero:** 待入库
- **Abstract:** CAD-to-image alignment aims to estimate an object's 9D pose (rotation, translation, and anisotropic scale) from a single RGB image, enabling applications in robotics and augmented reality. Recent zero-shot methods use visual foundation models to match image regions to CAD models, yet typically their correspondences are appearance-driven and degrade under occlusion or sim-to-real domain shift.
- 📄 [arXiv](https://arxiv.org/abs/2607.15058v1) | 📥 [PDF](https://arxiv.org/pdf/2607.15058v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **DriftWorld: Fast World Modeling through Drifting** (SOP: 7) [Link](https://arxiv.org/abs/2607.15065v1)
- **An LLM-Based Automatic Sportscast Solution for Robot Soccer Matches** (SOP: 6) [Link](https://arxiv.org/abs/2607.14809v1)
- **Motion Planning with Model-Based Diffusion via Constraint Optimization and Adaptive Scheduling** (SOP: 6) [Link](https://arxiv.org/abs/2607.14455v1)
- **CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking** (SOP: 5) [Link](https://arxiv.org/abs/2607.15004v1)
- **DRIFT: Drift and Aggregation for Motion Planning** (SOP: 5) [Link](https://arxiv.org/abs/2607.14507v1)
- **Knowing You at First Glance: Inferring Apparent Personality from Faces** (SOP: 5) [Link](https://arxiv.org/abs/2607.14631v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 244 篇 | 精选: 20 篇 | 关注: 6 篇 | 过滤: 218 篇
