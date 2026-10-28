# 🤖 具身智能/机器人学术日报 (2026-10-27)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour
- **SOP Score:** 23
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +21 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, parkour, parkour, terrain
- **Zotero:** 待入库
- **Abstract:** Humanoid parkour requires robots to reason about future footholds and whole-body motions over highly discontinuous terrain. We revisit the information asymmetry in asymmetric actor-critic learning for perceptive humanoid locomotion: the critic exploits privileged simulator signals during training, whereas the deployable actor operates solely from onboard perception.
- 📄 [arXiv](https://arxiv.org/abs/2610.36825v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36825v1)

---

### 2. GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers
- **SOP Score:** 22
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +16 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, VLA, terrain
- **Zotero:** 待入库
- **Abstract:** Humanoid behavior foundation models (BFMs) provide reusable whole-body motion priors: given a kinematic reference, they generate coordinated joint commands for motion replay, teleoperation, and VLA control. However, trained primarily on flat-ground motion, BFMs lack an explicit mechanism to adapt foot placement, swing clearance, and contact timing to local terrain.
- 📄 [arXiv](https://arxiv.org/abs/2610.36507v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36507v1)

---

### 3. REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal
- **SOP Score:** 22
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +18 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** humanoid, bipedal, locomotion, terrain
- **Zotero:** 待入库
- **Abstract:** Humanoid locomotion in confined spaces requires continuous height adaptation across multiple locomotion modes, yet most existing approaches remain limited to height-adjustable bipedal walking. We present REACH, an RL-based hierarchical framework that enables a Unitree G1 humanoid to traverse height-constrained environments through variable-height bipedal walking and crawling. The learned policies regulate body height over complementary command ranges of 1.27--0.50m in bipedal locomotion and 0.
- 📄 [arXiv](https://arxiv.org/abs/2610.36546v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36546v1)

---

### 4. A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation
- **SOP Score:** 20
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +18 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, dexterous manipulation, manipulation, grasping, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous manipulation in unstructured environments.
- 📄 [arXiv](https://arxiv.org/abs/2610.36789v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36789v1)

---

### 5. When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate
- **SOP Score:** 17
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** locomotion, robot learning, robot
- **Zotero:** 待入库
- **Abstract:** Robot foundation models may generalize across tasks and embodiments, but their actions still depend on sensors that can fail. When the policy is frozen or inaccessible, can an external monitor diagnose and repair corrupted inputs without access to its internals? We test a structured surrogate that separates periodic gait from sensor-dependent corrections to guide input repair around a frozen locomotion policy.
- 📄 [arXiv](https://arxiv.org/abs/2610.36852v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36852v1)

---

### 6. A Trainable CPG Framework for Quadruped Locomotion
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** quadruped, locomotion
- **Zotero:** 待入库
- **Abstract:** We present CPG-ENN, a trainable quadruped locomotion framework that combines explicit neural coordination with learned motion realization. A symmetry-based eight-neuron central pattern generator (CPG) supplies gait rhythms, while a pretrained, leg-shared execution neural network (ENN) maps rhythmic signals and trajectory parameters to joint-angle references without online inverse kinematics. A single feedback policy modulates six physically interpretable trajectory variables.
- 📄 [arXiv](https://arxiv.org/abs/2610.36537v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36537v1)

---

### 7. SO-101 Bench: Accessible Spatial Manipulation
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** robot learning, manipulation, grasping, robot, Isaac Lab
- **Zotero:** 待入库
- **Abstract:** Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup.
- 📄 [arXiv](https://arxiv.org/abs/2610.36420v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36420v1)

---

### 8. TAPESTRY: A Single Backbone for Video Generation and Robot Control
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** CoRL
- **Keywords:** robot learning, robot
- **Zotero:** 待入库
- **Abstract:** Pretrained video generation models encode rich priors about physical interactions, but leveraging them for robot control typically requires either resource-intensive video generation at test time or action heads trained from scratch that do not fully utilize the pretrained backbone. We introduce Tokenizing Actions as Video Patches in a Shared Transformer Policy (TAPESTRY), a world action model that repurposes a pretrained video diffusion transformer into a robotic policy without requiring video...
- 📄 [arXiv](https://arxiv.org/abs/2610.36823v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36823v1)

---

### 9. Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** CoRL
- **Keywords:** grasping
- **Zotero:** 待入库
- **Abstract:** We fine-tuned a separate $π_{0.5}$ policy for each of the five tasks in the MetaFine Open Competition, with a task-specific training mixture and number of actions executed per prediction. Training started from the official demonstrations and expert procedures. Local evaluation exposed recurring grasping, pushing, and insertion failures.
- 📄 [arXiv](https://arxiv.org/abs/2610.36765v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36765v1)

---

### 10. Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** humanoid, robot
- **Zotero:** 待入库
- **Abstract:** Enabling a humanoid to interact naturally with human partners requires preserving not only individual motions but also the spatial, semantic, and contact relationships underlying the interaction (i.e., hugging, dancing, hand-shaking, etc.). Furthermore, a practical solution should generalize across various humanoid embodiments with distinct morphologies and kinematic constraints.
- 📄 [arXiv](https://arxiv.org/abs/2610.36615v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36615v1)

---

### 11. SVIn+: Multi-Modal Framework for Robust Underwater State Estimation using 3D Sonar, Visual-Inertial, Water-Pressure, and DVL
- **SOP Score:** 12
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +0 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Zotero:** 待入库
- **Abstract:** As expansion and scalability in underwater oper- ations becomes more important and challenging, autonomous underwater vehicles (AUVs) become more relevant and the necessity for reliable autonomy more critical. A fundamental challenge in any autonomous underwater operation, from control to safe navigation and mapping, is state estimation; a notorious hard problem to address, especially in low visibility conditions.
- 📄 [arXiv](https://arxiv.org/abs/2610.36454v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36454v1)

---

### 12. CARD: Contact-Anchored Retargeting for Dexterous Manipulation
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Humans are dexterous, but traditional data collection paradigms such as teleoperation, kinesthetic teaching, and wearable exoskeletons force humans to act through the robot embodiment, bottlenecking their dexterity. Retargeting can avoid this. However, existing methods purely translate kinematics and ignore the real-world contact dynamics essential for task success.
- 📄 [arXiv](https://arxiv.org/abs/2610.36539v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36539v1)

---

### 13. RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Bimanual robot manipulation plays an important role in real-world robotic applications, but the high cost of collecting bimanual demonstrations limits the scalable development of bimanual policy learning. Meanwhile, existing single-arm manipulation data are difficult to directly transfer to bimanual systems due to the Single-to-Dual gap in action spaces, coordination requirements, and arm-side spatial preference.
- 📄 [arXiv](https://arxiv.org/abs/2610.36685v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36685v1)

---

### 14. OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +4 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Handheld data-collection interfaces such as the Universal Manipulation Interface (UMI) allow manipulation demonstrations to be gathered in the wild without a robot in the loop, but the quality of the resulting action labels is bounded by the accuracy of vision-based localization. Existing systems recover end-effector pose from monocular visual-inertial odometry, which is subject to scale ambiguity and drift, or delegate tracking to closed-source modules and external infrastructure that reintrodu...
- 📄 [arXiv](https://arxiv.org/abs/2610.36598v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36598v1)

---

### 15. Whole-Body Humanoid Control via Stochastic Motion Tokenization
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** humanoid, robot
- **Zotero:** 待入库
- **Abstract:** While velocity-commanded RL policies are effective for controlling quadrupeds, they are a limited interface for humanoids that need to perform complex whole-body motions. Furthermore, RL tracking policies for whole-body motions typically have limited information about the desired future motion, preventing them from performing controlled deviations to achieve long-term task success; such information is particularly relevant when a controller must prepare for transitions between behaviors.
- 📄 [arXiv](https://arxiv.org/abs/2610.36452v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36452v1)

---

### 16. ActiveAlign: Aligning Egocentric Manipulation via Active Perception
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** sim-to-real, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Real-to-Sim-to-Real (Real2Sim2Real) enables structured world representations for planning, interpretability, and safe execution. Most existing approaches rely on passive perception, which creates real2sim gaps due to imperfect observation. Inspired by how humans perceive actively through actions, we propose ActiveAlign, a framework that leverages active perception to align the Real2Sim2Real gap from interactions.
- 📄 [arXiv](https://arxiv.org/abs/2610.36859v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36859v1)

---

### 17. RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +4 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** world model, robot
- **Zotero:** 待入库
- **Abstract:** Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface.
- 📄 [arXiv](https://arxiv.org/abs/2610.36791v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36791v1)

---

### 18. TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** flow matching, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Flow-based policies for language-conditioned multi-task manipulation commonly share a single $\textit{Gaussian}$ source prior and a common linear transport path across tasks. However, reliably executing multiple tasks with distinct motion requirements remains challenging for a shared policy. We introduce $\textbf{TOPS}$ ($\textbf{T}$ask-$\textbf{O}$riented $\textbf{P}$riors and $\textbf{S}$chedules), which adapts the flow source prior and interpolation schedule to each task without modifying the...
- 📄 [arXiv](https://arxiv.org/abs/2610.36694v1) | 📥 [PDF](https://arxiv.org/pdf/2610.36694v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **Evolving Agent Teams** (SOP: 7) [Link](https://arxiv.org/abs/2610.36848v1)
- **Camera-to-Quadruped Robot Pose Estimation from Sequential Images** (SOP: 6) [Link](https://arxiv.org/abs/2610.36599v1)
- **On Shaky Ground: Characterising Non-Rigid Base Effects in Mobile Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.36725v1)
- **SWIM: Learning What Matters from Behaviors for JEPA World Models** (SOP: 6) [Link](https://arxiv.org/abs/2610.36662v1)
- **Trace-WAM: Learning to Act via 3D Motion Prediction for World Action Models** (SOP: 6) [Link](https://arxiv.org/abs/2610.36840v1)
- **From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement** (SOP: 5) [Link](https://arxiv.org/abs/2610.36681v1)
- **Learning Side-by-Side Navigation for Personal Mobility Vehicles from Human Drivers** (SOP: 5) [Link](https://arxiv.org/abs/2610.36726v1)
- **RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding** (SOP: 5) [Link](https://arxiv.org/abs/2610.36533v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 195 篇 | 精选: 18 篇 | 关注: 8 篇 | 过滤: 169 篇
