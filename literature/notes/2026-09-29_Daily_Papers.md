# 🤖 具身智能/机器人学术日报 (2026-09-29)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. EquivDP3: A SIM(3)-Invariant Point-Cloud Encoder for Data-Efficient Humanoid Loco-Manipulation
- **SOP Score:** 23
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +21 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, diffusion policy, manipulation, behavior cloning
- **Zotero:** 待入库
- **Abstract:** Visuomotor policies for humanoid loco-manipulation must generalize across object poses and lighting from only a handful of demonstrations. 3D Diffusion Policy (DP3) conditions a diffusion-based action generator on point-cloud features, but its PointNet-style encoder has no built-in equivariance to the rotations, translations, and scalings (SIM(3)) that manipulation tasks respect. EquiBot closed this gap for wheeled manipulators with a SIM(3)-equivariant Vector Neuron Network (VNN) encoder.
- 📄 [arXiv](https://arxiv.org/abs/2609.36575v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36575v1)

---

### 2. AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations
- **SOP Score:** 21
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +15 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation, grasping, imitation learning, VLA, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Aerial manipulators extend robotic manipulation into 3D workspaces that are difficult for ground-based robots to access, creating new opportunities for general-purpose manipulation. However, extending Vision-Language-Action (VLA) models to aerial robots introduces distinct challenges due to the tight coupling between manipulation and flight, continuously changing observations, and safety-critical physical interactions.
- 📄 [arXiv](https://arxiv.org/abs/2609.36915v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36915v1)

---

### 3. PreferenceFlow: Test-Time Guidance of Flow-Matching Robot Policies from Human Interventions
- **SOP Score:** 18
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** flow policy, manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Flow-matching policies can represent complex robot behaviors but remain susceptible to local errors under distribution shift at deployment. Many reinforcement learning approaches to policy improvement require reward signals that are difficult to specify or obtain in real-world manipulation. We present PreferenceFlow, a framework for improving a pretrained flow policy at test time without environment rewards or updates to the base policy.
- 📄 [arXiv](https://arxiv.org/abs/2609.36872v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36872v1)

---

### 4. Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** We study reinforcement learning (RL) methods for cooperative multi-agent Vision-Language-Action (VLA) models. This problem is challenging because VLAs are pretrained on large-scale single-agent data and therefore lack the fine-grained coordination skills required for inter-robot collaboration. Supervised fine-tuning (SFT) on multi-robot demonstrations partially bridges this gap, but its performance is bounded by the demonstration data and cannot improve from its own experience.
- 📄 [arXiv](https://arxiv.org/abs/2609.36588v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36588v1)

---

### 5. Riemannian Splat Regression Models for Learning Time Fields on Arbitrary Riemannian Manifolds
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** motion planning
- **Zotero:** 待入库
- **Abstract:** Motion planning on arbitrary Riemannian manifolds is an important and difficult problem that frustrates typical planning methods for Euclidean spaces. In particular, motion planning methods that approximate optimal time-to-go functions with neural networks, e.g., Neural Time Fields (NTFields), cannot be directly applied without using ad-hoc coordinate projections into higher dimensions.
- 📄 [arXiv](https://arxiv.org/abs/2609.36561v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36561v1)

---

### 6. RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +4 | Code +3 | cs.RO +0
- **Keywords:** sim-to-real, imitation learning
- **Zotero:** 待入库
- **Abstract:** End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-world deployment. To address this issue, reinforcement learning (RL) post-training offers a promising alternative by leveraging world models as interactive training environments to enable future scene generation for policy improvement.
- 📄 [arXiv](https://arxiv.org/abs/2609.36851v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36851v1)

---

### 7. VidAct: Learning Manipulation from In-the-Wild Videos with Object-Centric 3D Awareness
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** sim-to-real, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Video demonstrations offer a scalable alternative to costly robot data for learning manipulation, yet existing reconstruction-based approaches often rely on constrained camera viewpoints or human-to-robot retargeting, while the reconstructed trajectories are difficult to adapt to new objects configurations without distorting the trajectory shape.
- 📄 [arXiv](https://arxiv.org/abs/2609.36870v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36870v1)

---

### 8. OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Transferring human motion to humanoid robots requires adapting the demonstrated motion to the robot morphology while preserving interactions with the environment. This is particularly challenging for loco-manipulation tasks, where contacts with the ground and manipulated objects must remain consistent despite differences in body proportions. Yet, skeletal motion alone does not fully describe these interactions, and fixing object trajectories limits the adaptation to a new embodiment.
- 📄 [arXiv](https://arxiv.org/abs/2609.36602v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36602v1)

---

### 9. All Roads Lead to Rome: Flow-driven Multi-Anchor Exploration for Open-Environment Active 3D Mapping
- **SOP Score:** 13
- **SOP 评分证据:** Venue +5 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** NeurIPS
- **Keywords:** flow matching, embodied
- **Zotero:** 待入库
- **Abstract:** To advance the development of embodied intelligence, Open-Environment Active 3D Mapping has attracted increasing attention, aiming to perform a long-horizon and shortest trajectory exploration for reconstructing unseen scenarios. Since only limited information about unseen environments is available, methods built on the closed-set assumption, i.e., assuming that the test environments are similar to those seen during training, cannot generalize satisfactorily.
- 📄 [arXiv](https://arxiv.org/abs/2609.36889v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36889v1)

---

### 10. GlassFormer: Learning Real-time Glass Segmentation using Radar-Depth Fusion
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +0 | Hardware +0 | Code +3 | cs.RO +0
- **Venue:** IROS
- **Zotero:** 待入库
- **Abstract:** Transparent surfaces are ubiquitous in built environments, yet they remain a persistent failure case for robotic perception. RGB cameras perceive the background behind glass rather than the surface itself, while depth sensors such as LiDAR, time-of-flight, and RGB-D often return invalid or background measurements in transparent regions.
- 📄 [arXiv](https://arxiv.org/abs/2609.36844v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36844v1)

---

### 11. NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +1 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** robot
- **Zotero:** 待入库
- **Abstract:** LiDAR return intensity provides complementary surface-response cues for robotic perception and state estimation, yet many simulation pipelines omit it or reproduce it using reconstruction methods that require real intensity supervision and per-scene optimization. These requirements increase data-collection and fitting costs and limit reuse across simulated scenes.
- 📄 [arXiv](https://arxiv.org/abs/2609.36878v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36878v1)

---

### 12. Inferring Soil Friction Angle from Robot Foot-Ground Force Histories: A Bayesian Inverse Approach to Proprioceptive Soil Sensing
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, terrain, robot
- **Zotero:** 待入库
- **Abstract:** Foot-ground interaction signals recorded by quadruped robots may enable spatially distributed, in situ characterization of soil strength. As a first step, we test whether the internal friction angle $φ$ of cohesionless soil can be identified from the force history of a simplified rotating leg. A two-dimensional continuum model implemented with the material point method, benchmarked against measured rotating-leg force histories, generates the training data, and two Gaussian-process surrogates sup...
- 📄 [arXiv](https://arxiv.org/abs/2609.36582v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36582v1)

---

### 13. One from Infinity: Actualizing Futures from Pretrained World Models into Robot Actions
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** flow matching, world model, robot
- **Zotero:** 待入库
- **Abstract:** A pretrained video world model admits many plausible futures for a scene, but a robot must realize the exact task-conditioned one. To turn world models into executable robot policies, existing methods fine-tune the heavy world model backbone using large-scale robot data and computational resources. Challenging this status quo, we argue that the expensive part has already been paid in the world model pretraining since the representation space of a video world model lays out the diverse potential...
- 📄 [arXiv](https://arxiv.org/abs/2609.36413v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36413v1)

---

### 14. Track-and-Complete: Learning Humanoid Skills from a Single Failed Human Video
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** humanoid, robot learning, robot
- **Zotero:** 待入库
- **Abstract:** Learning humanoid skills from videos typically requires a successful human demonstration, which often demands custom data collection. Although failures have traditionally been treated only as negative examples in robot learning, they can still reveal a usable trajectory prefix before the task fails, as well as the intended outcome.
- 📄 [arXiv](https://arxiv.org/abs/2609.36924v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36924v1)

---

### 15. FineART: Fine-grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Robots operating in real-world environments must execute complex, multi-step bimanual tasks over long horizons rather than single, isolated actions. Current manipulation datasets struggle to support this capability: although single-arm datasets reach hundreds of thousands of trajectories, they typically provide only one high-level instruction per episode while the rare bimanual effort that does label subtasks annotates only a fraction of its hours.
- 📄 [arXiv](https://arxiv.org/abs/2609.36416v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36416v1)

---

### 16. HACo: Learning Haptic Active Compliance for Force-Aware Dexterous Manipulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation
- **Zotero:** 待入库
- **Abstract:** Contact-rich dexterous manipulation requires policies that translate physical feedback into motion commands while regulating interaction loads across evolving multi-contact interactions. This requires haptic observations of contact state and action supervision showing how commands should adapt. Existing policies often overlook complementary fingertip tactile and joint-torque feedback, while common action targets either encode excessive loading or omit motion constrained by the object.
- 📄 [arXiv](https://arxiv.org/abs/2609.36596v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36596v1)

---

### 17. Kinematic Nonlinear Spatio-Temporal Trajectory Warping for Contact-Rich Dexterous Manipulation Demonstrations
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation
- **Zotero:** 待入库
- **Abstract:** We present a straightforward but effective method for repurposing existing contact-rich dexterous manipulation demonstrations. Starting from inputs of hand and object trajectories, our method outputs high-quality nonlinear trajectory warps that account for intermediate waypoints, environmental barriers, temporal shifts, and varied start/end configurations.
- 📄 [arXiv](https://arxiv.org/abs/2609.36676v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36676v1)

---

### 18. Foundation-Model-Guided Topology-Aware Semantic Risk Fields for Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, motion planning, robot
- **Zotero:** 待入库
- **Abstract:** Robot motion planning in everyday environments must satisfy hard geometric constraints while accounting for context-dependent semantic risk. We present a foundation-model-guided, topology-aware semantic risk field that extends manipulation safety beyond collision avoidance. For each manipulated-object/scene-object pair, a foundation model provides six directional risk weights and a pair-specific spatial decay scale.
- 📄 [arXiv](https://arxiv.org/abs/2609.36640v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36640v1)

---

### 19. RoboChrono: A Real Robot Benchmark for Streaming Task Understanding
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +4 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Understanding ongoing robot manipulation requires models to interpret visual observations in relation to interaction history and task progress. We introduce RoboChrono, a benchmark for streaming task understanding comprising 39 scenarios and 34,713 evaluation instances, constructed from real robot executions and complementary bare-hand human recordings.
- 📄 [arXiv](https://arxiv.org/abs/2609.36605v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36605v1)

---

### 20. TaRL: Learning General and Physical Rewards from Tactile Demonstrations
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Contact-rich manipulation requires robots to sequence precise contacts, maintain stable grasps, and apply directed forces. Reinforcement learning (RL) can acquire such behaviors automatically, but its performance hinges on reward design: sparse rewards reduce the learning efficiency, while dense rewards are hard to specify. Visual reward learning addresses this by inferring rewards from action-free demonstrations.
- 📄 [arXiv](https://arxiv.org/abs/2609.36785v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36785v1)

---

### 21. Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Existing VLA pruning strategies primarily select individual visual tokens according to task-level semantic relevance, while overlooking the spatial information required for robotic manipulation. To examine this limitation, we construct a simple Stride baseline that uniformly samples tokens along the flattened one-dimensional visual sequence, representing a purely geometric pruning strategy.
- 📄 [arXiv](https://arxiv.org/abs/2609.36967v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36967v1)

---

### 22. Learning to Explore Hidden Kinematics for Articulated Object Manipulation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** The kinematics of an articulated object is often ambiguous from vision alone. Interaction resolves the ambiguity, and active perception methods exploit this by searching for the single action that most sharpens a belief over the kinematic parameters at each step. Such greedy search cannot be extended over a horizon without forward models of the contact and inertial dynamics, which are themselves unknown. We instead amortize action selection into training.
- 📄 [arXiv](https://arxiv.org/abs/2609.36553v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36553v1)

---

### 23. World4Scorer: Outcome-Grounded World Modeling for Autonomous Driving
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, world model
- **Zotero:** 待入库
- **Abstract:** Autonomous driving requires choosing a safe and efficient plan as surrounding traffic evolves. Generate-and-select planners propose multiple trajectories and score them for execution, and they have outperformed representative direct-prediction baselines on NAVSIM. Their scorer must compare plans that were never executed.
- 📄 [arXiv](https://arxiv.org/abs/2609.36438v1) | 📥 [PDF](https://arxiv.org/pdf/2609.36438v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **A robust single-sensing-element tactile sensor for concurrent pressure and tackiness detection with real-time signal decoupling capability** (SOP: 7) [Link](https://arxiv.org/abs/2609.36558v1)
- **DQ-MPCC: Dual-Quaternion MPCC for Quadrotor Racing** (SOP: 7) [Link](https://arxiv.org/abs/2609.36482v1)
- **Spotter: Let the Embodied Model Lead, and the VLM Reflect for It** (SOP: 7) [Link](https://arxiv.org/abs/2609.36808v1)
- **Staircase Policy: Streaming Inference for World-Action Models with Large Action Chunks** (SOP: 7) [Link](https://arxiv.org/abs/2609.36471v1)
- **Asymmetric Scout-Worker Reconnaissance for Route Validation in Unknown Environments** (SOP: 6) [Link](https://arxiv.org/abs/2609.36537v1)
- **ComManip: Overfitting Manipulation Policies to Comfortable Regions** (SOP: 6) [Link](https://arxiv.org/abs/2609.36928v1)
- **Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM** (SOP: 6) [Link](https://arxiv.org/abs/2609.36753v1)
- **DRHeC: Differentiable Rendering for Hand-Eye Calibration with RGB-Based Gradients** (SOP: 6) [Link](https://arxiv.org/abs/2609.36779v1)
- **Executor-aware Candidate Selection via a Feasibility Certificate** (SOP: 6) [Link](https://arxiv.org/abs/2609.36597v1)
- **LexiconVLA: Learning Reusable Atomic Action Codebooks for Unseen Tasks** (SOP: 6) [Link](https://arxiv.org/abs/2609.36774v1)
- **LIBERO-MAX: Do Robot Policies Adapt When the World Changes?** (SOP: 6) [Link](https://arxiv.org/abs/2609.36518v1)
- **Reactive Real-Time Flow Policies via Asynchronous Distribution Alignment** (SOP: 6) [Link](https://arxiv.org/abs/2609.36540v1)
- **Scene Retargeting: Learning Object Placement with Analogical Transfer** (SOP: 6) [Link](https://arxiv.org/abs/2609.36801v1)
- **Simple Agentic Memory for Generalist Robot Policies** (SOP: 6) [Link](https://arxiv.org/abs/2609.36595v1)
- **Trajectory-Level Mode Guidance for Controllable Diffusion-Based Multi-Robot Motion Planning** (SOP: 6) [Link](https://arxiv.org/abs/2609.36530v1)
- **T$^2$Mem: Learning Test-Time Memory for Robotics** (SOP: 5) [Link](https://arxiv.org/abs/2609.36720v1)
- **Where Predictive Supervision Goes Shapes What VLA Policies Learn** (SOP: 5) [Link](https://arxiv.org/abs/2609.36645v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 114 篇 | 精选: 23 篇 | 关注: 17 篇 | 过滤: 74 篇
