# 🤖 具身智能/机器人学术日报 (2026-10-06)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. QF3: Fast Flow RL with Filtered Q-Gradients
- **SOP Score:** 29
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +27 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, flow matching, flow policy, manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Flow policies have become a standard policy class for learning robot behaviors from demonstrations, but reinforcement learning is still critical for improving pre-trained flow policies or learning them from scratch through interaction. We introduce QF3 (Fast Flow RL with Filtered Q-Gradients), an online off-policy RL algorithm that trains a flow policy with flow matching plus the critic's action gradient, backpropagated through a one-step prediction of the flow's output.
- 📄 [arXiv](https://arxiv.org/abs/2610.08789v1) | 📥 [PDF](https://arxiv.org/pdf/2610.08789v1)

---

### 2. DepthWorld: 3D World Model for Robot Manipulation
- **SOP Score:** 24
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** robot learning, manipulation, world model, robot
- **Zotero:** 待入库
- **Abstract:** World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world.
- 📄 [arXiv](https://arxiv.org/abs/2610.08780v1) | 📥 [PDF](https://arxiv.org/pdf/2610.08780v1)

---

### 3. I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning
- **SOP Score:** 23
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +17 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** humanoid, whole-body control, manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Behavioral foundation models (BFMs) have recently shown that a single humanoid policy can support diverse whole-body control, but extending such generality to physical interaction remains challenging. We introduce I-BFM, to our knowledge the first BFM for humanoid-object interaction. Rather than relying on task-specific policies or reference tracking, I-BFM learns a shared representation of the coupled dynamics among the humanoid, objects, and their contacts using forward-backward representation...
- 📄 [arXiv](https://arxiv.org/abs/2610.06129) | 📥 [PDF](https://arxiv.org/pdf/2610.06129.pdf)

---

### 4. EigenDEXplore: Structured Exploration for Dexterous Manipulation with Human Priors
- **SOP Score:** 22
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +20 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, sim-to-real, manipulation, grasping, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Dexterous manipulation poses a challenging high-dimensional optimization problem, as useful behaviors require coordinated motion across many hand joints. In reinforcement learning (RL) and sampling-based trajectory optimization, exploration commonly relies on independent robot joint perturbations, making coordinated behaviors difficult to discover.
- 📄 [arXiv](https://arxiv.org/abs/2610.07681v1) | 📥 [PDF](https://arxiv.org/pdf/2610.07681v1)

---

### 5. BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation
- **SOP Score:** 19
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** humanoid, manipulation, imitation learning, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchronised multi-camera views and full-body execution records.
- 📄 [arXiv](https://arxiv.org/abs/2610.07594v1) | 📥 [PDF](https://arxiv.org/pdf/2610.07594v1)

---

### 6. Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI
- **SOP Score:** 18
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** embodied AI, embodied
- **Zotero:** 待入库
- **Abstract:** General purpose language models are increasingly able to control robotic hardware. Understanding the capabilities and safety of these models when embodied is therefore increasingly important for understanding their societal impact and risks. To this end, we introduce Inspect Robots, a modular, open-source framework for developing and running evaluations of embodied agents.
- 📄 [arXiv](https://arxiv.org/abs/2610.06306) | 📥 [PDF](https://arxiv.org/pdf/2610.06306.pdf)

---

### 7. Propagating Elevation-Map Uncertainty Through the Contact Maximum in Closed Form
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** terrain
- **Zotero:** 待入库
- **Abstract:** Risk-aware planners score paths on uncertain elevation maps using the path cost's mean and standard deviation. Modeling rigid contact, however, requires computing a maximum over several uncertain cells. First-order propagation loses accuracy here by differentiating at only a single cell, while Monte Carlo sampling requires a full path evaluation per draw. We compute the moments of that contact maximum in closed form using Clark's pairwise recursion.
- 📄 [arXiv](https://arxiv.org/abs/2610.06103) | 📥 [PDF](https://arxiv.org/pdf/2610.06103.pdf)

---

### 8. Robotizing Human Videos with Physically Consistent Interactions
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** diffusion policy, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Human videos offer scalable manipulation data, but the embodiment gap between human hands and robot manipulators limits their direct use. Existing video-editing methods replace hands with rendered robots, yet inaccurate interaction reconstruction and compositing can produce inconsistent grasps and implausible robot-object occlusions. We address these failures from two complementary physical aspects: interaction geometry and scene visibility.
- 📄 [arXiv](https://arxiv.org/abs/2610.06137) | 📥 [PDF](https://arxiv.org/pdf/2610.06137.pdf)

---

### 9. SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** sim-to-real, manipulation, VLA, robot, embodied
- **Zotero:** 待入库
- **Abstract:** The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limited articulated-object categories, while general-purpose synthesis pipelines lack explicit designs for part-level semantics and articulation c...
- 📄 [arXiv](https://arxiv.org/abs/2610.07652v1) | 📥 [PDF](https://arxiv.org/pdf/2610.07652v1)

---

### 10. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** humanoid, robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other.
- 📄 [arXiv](https://arxiv.org/abs/2610.06850) | 📥 [PDF](https://arxiv.org/pdf/2610.06850.pdf)

---

### 11. DexForge: High-Fidelity Physics-Informed Dexterous Retargeting
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, robot, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Human demonstrations offer rich examples of precise dexterous manipulation and a promising source of robot training data. However, high-fidelity reproduction of demonstrated motions and hand-object interactions across robot embodiments remains challenging under physical constraints. We present DexForge, a differentiable physics-grounded framework for converting human video demonstrations into high-fidelity robot trajectories.
- 📄 [arXiv](https://arxiv.org/abs/2610.06331) | 📥 [PDF](https://arxiv.org/pdf/2610.06331.pdf)

---

### 12. EgoLAP: Learning from Egocentric Human Data through Language-Action Reasoning
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Egocentric human data offer a path to scaling robot learning beyond costly robot demonstrations, yet the embodiment gap makes raw human trajectories a poor supervisory target for control. Our key insight is that, although low-level actions are embodiment-specific, their underlying motion intent can capture task-relevant structure that transfers across humans and robots.
- 📄 [arXiv](https://arxiv.org/abs/2610.08726v1) | 📥 [PDF](https://arxiv.org/pdf/2610.08726v1)

---

### 13. Talk, Render, Act: Integrating Social Gesture and Digital Face with Synchronized Speech for Conversational Humanoid Robot
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, motion planning, robot
- **Zotero:** 待入库
- **Abstract:** Expressive humanoid interaction requires speech, facial animation, and body gestures to form a coherent response. However, many full-body humanoid robots produce speech and gestures without a visually expressive face, while talking-face animation and robot gesture generation are typically developed separately. We present Talk, Render, Act (TRABot), an agent-based framework comprising specialized agents for motion-atom construction, dialogue generation, motion planning, and facial animation.
- 📄 [arXiv](https://arxiv.org/abs/2610.06153) | 📥 [PDF](https://arxiv.org/pdf/2610.06153.pdf)

---

### 14. Dual Variational Autoencoders for Efficient Sim-to-Real Transfer in Low-Cost Robotic Navigation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +4 | Code +0 | cs.RO +0
- **Keywords:** sim-to-real, robot
- **Zotero:** 待入库
- **Abstract:** Vision-based autonomous navigation for low-cost robots remains a fundamental challenge, primarily due to the significant gap between simulated training environments and real-world operational conditions. Direct policy transfer from simulation is often ineffective, while training exclusively on real data is impractical. We propose a hybrid transfer learning framework that effectively bridges the sim-to-real gap by combining domain randomization with feature-level domain adaptation.
- 📄 [arXiv](https://arxiv.org/abs/2610.06327) | 📥 [PDF](https://arxiv.org/pdf/2610.06327.pdf)

---

### 15. VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Portable mobile-manipulation demonstrations can help alleviate data scarcity for embodied intelligence, but obtaining reliable, low-cost, and robot-free motion supervision from RGB observations remains challenging. Existing approaches often rely on teleoperation or specialized devices equipped with additional sensing hardware, while directly using estimated visual odometry (VO) trajectories can introduce inconsistencies due to accumulated drift and imperfect motion supervision.
- 📄 [arXiv](https://arxiv.org/abs/2610.08220v1) | 📥 [PDF](https://arxiv.org/pdf/2610.08220v1)

---

### 16. AffordCraft: Scalable Construction of Task-Ready Simulation Assets from Single Images
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Robot learning in simulation depends on the objects the simulator offers. Many tasks need objects with separate parts, joints that allow the required motion, and physical properties that remain valid under contact. Existing methods recover this structure anew for every image: generative models predict parts and joints that mostly fail to settle or move in simulation, and general-purpose agents need a long session of model calls for each photograph.
- 📄 [arXiv](https://arxiv.org/abs/2610.06643) | 📥 [PDF](https://arxiv.org/pdf/2610.06643.pdf)

---

### 17. GAMBIT: Learning to Plan Continuous Multi-Robot Trajectories
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** imitation learning, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** GAMBIT is an opening chess move in which a player sacrifices a piece, typically a pawn, to gain a positional advantage later in the game. Analogously, in multi-robot coordination, individual robots may need to forgo locally reward-maximising behaviours to improve overall team performance. Such self-sacrificial behaviours are difficult to capture with manually designed heuristics, particularly in dense, interaction-rich environments.
- 📄 [arXiv](https://arxiv.org/abs/2610.06290) | 📥 [PDF](https://arxiv.org/pdf/2610.06290.pdf)

---

### 18. WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** embodied AI, embodied
- **Zotero:** 待入库
- **Abstract:** LLM-based agents are increasingly advancing scientific and engineering problem solving, with physics simulation emerging as a challenging yet practical testbed for reproducing complex physical phenomena with application in embodied AI, games and films. As the workhorse of such simulation, a solver computes how the state of a dynamic system evolves over time.
- 📄 [arXiv](https://arxiv.org/abs/2610.08720v1) | 📥 [PDF](https://arxiv.org/pdf/2610.08720v1)

---

### 19. Physics Residual Dynamics and Reduced Order Whole-Body Planning for Obstacle Aware Human Robot Cloth CoTransportation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** whole-body control, robot
- **Zotero:** 待入库
- **Abstract:** Human--robot co-transportation of deformable objects requires predicting object deformation during motion, since obstacle clearance depends on both the grasp points and the unactuated interior. We present a hierarchical planning framework that combines a learned cloth model with a reduced-order whole-body model of a dual-arm mobile manipulator.
- 📄 [arXiv](https://arxiv.org/abs/2610.06641) | 📥 [PDF](https://arxiv.org/pdf/2610.06641.pdf)

---

### 20. SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +5 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** world model, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Simulation offers structured motion supervision, but appearance differences hinder direct transfer, and inaccurate simulation predictions can misguide real-video generation.
- 📄 [arXiv](https://arxiv.org/abs/2610.06598) | 📥 [PDF](https://arxiv.org/pdf/2610.06598.pdf)

---

### 21. Towards Quadruped-Provided Localization and Active Tracking for Micro-UAVs
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, robot
- **Zotero:** 待入库
- **Abstract:** Micro unmanned aerial vehicles (micro-UAVs) are small enough to reach confined spaces that larger robots cannot access, but too small to carry the sensing and computing power required for autonomous flight. We move the localization stack entirely off the aerial platform onto a quadruped robot with a 7-degree-of-freedom (DOF) arm, which supplies the micro-UAV (27 g bare, 42 g with fiducial markers) its full 6-DOF pose.
- 📄 [arXiv](https://arxiv.org/abs/2610.06215) | 📥 [PDF](https://arxiv.org/pdf/2610.06215.pdf)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **Micro Neural Policies for Safe Real-Time Robotic Control** (SOP: 7) [Link](https://arxiv.org/abs/2610.08541v1)
- **Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution** (SOP: 6) [Link](https://arxiv.org/abs/2610.07946v1)
- **CETUS: How Far Do Representations Trained on Earth Transfer to Cassini SAR of Titan?** (SOP: 6) [Link](https://arxiv.org/abs/2610.07576v1)
- **Encoded but Not in Control: Revealing the Grounding Gap in Vision-Language Robot Policies** (SOP: 6) [Link](https://arxiv.org/abs/2610.06235)
- **Recursive Video In-Context Learning for Agentic Robot** (SOP: 6) [Link](https://arxiv.org/abs/2610.06843)
- **Traversability-Aware Cooperative Path Planning for Human-UGV Casualty Evacuation** (SOP: 6) [Link](https://arxiv.org/abs/2610.06487)
- **Arm-wise Compositional Generalization in Dual-Arm Vision-Language-Action Models** (SOP: 5) [Link](https://arxiv.org/abs/2610.06184)
- **Conditional Trajectory Peaks: Single-Pass Multimodal Policies over Action Chunks** (SOP: 5) [Link](https://arxiv.org/abs/2610.06104)
- **Future Anchored Verification and Online Recovery for World Action Models** (SOP: 5) [Link](https://arxiv.org/abs/2610.06280)
- **Learning Grasp Targeting from Point Clouds for Log Pile Clearing on a Hydraulic Crane** (SOP: 5) [Link](https://arxiv.org/abs/2610.07613v1)
- **Odyssey: A Closed-Loop Benchmark for Long-Horizon Real-World Driving with Explicit Navigation Routes** (SOP: 5) [Link](https://arxiv.org/abs/2610.06469)
- **Towards Robust Prehensile Manipulation in Open-Ended Environments** (SOP: 5) [Link](https://arxiv.org/abs/2610.06376)
- **VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning** (SOP: 5) [Link](https://arxiv.org/abs/2610.08761v1)
- **Visual Swarm Navigation via Deep Reinforcement Learning and Evolutionary Hybrid Design** (SOP: 5) [Link](https://arxiv.org/abs/2610.06400)
- **VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models** (SOP: 5) [Link](https://arxiv.org/abs/2610.06271)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 784 篇 | 精选: 21 篇 | 关注: 15 篇 | 过滤: 351 篇
- 元数据不完整: 397 篇（不参与自动精选）
