# 🤖 具身智能/机器人学术日报 (2026-10-09)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. Sampling-based Kinodynamic Planning with World Models
- **SOP Score:** 23
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +7 | Hardware +4 | Code +0 | cs.RO +2
- **Venue:** ICRA
- **Keywords:** world model, motion planning, robot
- **Zotero:** 待入库
- **Abstract:** Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI. However, these optimizers stall on long-horizon tasks where progress requires motion the objective does not reward, such as moving around a block before pushing it. This paper revisits kinodynamic sampling-based motion planning for world models, using the learned model as the propagator of a tree search in latent space.
- 📄 [arXiv](https://arxiv.org/abs/2610.12910v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12910v1)

---

### 2. TAME-Nav: Temporal Asymmetric Mixture-of-Experts Distillation for Agile and Versatile Robot Navigation
- **SOP Score:** 20
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +18 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, sim-to-real, robot navigation, agile, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Agile and reliable navigation is a core capability for embodied robots navigating complex spatial constraints and dynamic interactions. However, a single policy often struggles to accommodate the distinct decision-making demands of diverse scenarios. We present TAME-Nav, an asymmetric Teacher-Student navigation framework built around a temporal soft mixture of experts (Soft-MoE).
- 📄 [arXiv](https://arxiv.org/abs/2610.12877v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12877v1)

---

### 3. Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, whole-body control, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop, creating a tension: replacing the plan whenever the belief shifts disrupts the maneuver under way, while keeping it strands the robot on a pat...
- 📄 [arXiv](https://arxiv.org/abs/2610.13087v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13087v1)

---

### 4. Human2Dex: Dexterous Robot Learning from Wrist-Centric Human Demonstrations
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Collecting dexterous manipulation demonstrations for each robot hand requires repeated task-specific data acquisition. We ask whether one shared corpus of natural human demonstrations can instead serve as a reusable data interface for different dexterous hands, without collecting task demonstrations on each target robot. We present Human2Dex, a wrist-centric human demonstration interface that separates shared human observation and motion semantics from embodiment-specific execution.
- 📄 [arXiv](https://arxiv.org/abs/2610.13119v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13119v1)

---

### 5. Robot-WATCHDOG : failure detection through object-centric graph representation
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Reliable real-time failure detection is critical for deploying learned robotic policies, yet defining failures explicitly is infeasible in open-world settings. This motivates failure detection from nominal demonstrations alone. Existing methods, however, struggle to balance robustness to benign variations with the ability to capture semantic and interaction-level errors.
- 📄 [arXiv](https://arxiv.org/abs/2610.13403v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13403v1)

---

### 6. Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, whole-body control, grasping
- **Zotero:** 待入库
- **Abstract:** Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads. However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predictive controller (MPC) that generates dynamically feasible reference motions, (ii) an adaptive fuzzy balance controller that compensates for pa...
- 📄 [arXiv](https://arxiv.org/abs/2610.12972v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12972v1)

---

### 7. EgoReveal: Learning Active Vision and Object Manipulation under Partial Occlusions from Egocentric Demonstrations
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +3 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation
- **Zotero:** 待入库
- **Abstract:** Learning from Demonstrations (LfD) enables robots to learn object manipulation directly from human demonstrations. In contrast to resource-intensive and labor-intensive teleoperation, egocentric demonstrations are easy to collect, enabling scalable data collection. Manipulated objects are often partially occluded in everyday environments, yet prior egocentric demonstration-based methods that require no robots or specialized teaching devices do not explicitly address occlusions.
- 📄 [arXiv](https://arxiv.org/abs/2610.12999v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12999v1)

---

### 8. AlphaNIST: Emergent Assembly Skills from Binary Task Rewards
- **SOP Score:** 14
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +4 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** ICRA
- **Keywords:** manipulation, robot
- **Zotero:** 待入库
- **Abstract:** The NIST Assembly Task Board #1 remains a challenging benchmark for learning-based methods in robotic manipulation. Over short horizons, it demands precise, contact-rich control of small, tight-fitting parts. Over long horizons, it requires recovery and coordination across extended action sequences. Demonstrations, task decomposition, and dense progress rewards have enabled research advances by providing guidance on how to assemble.
- 📄 [arXiv](https://arxiv.org/abs/2610.13354v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13354v1)

---

### 9. Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Actions specify what a robot should execute, but do not describe what those commands will achieve. Vision-language-action (VLA) policies nevertheless learn primarily by predicting action chunks from images, language, and state. We introduce Action--Future Coupled Effect Learning (AFCE), which makes a future-grounded physical Effect the policy's primary prediction target.
- 📄 [arXiv](https://arxiv.org/abs/2610.13212v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13212v1)

---

### 10. Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, manipulation, world model, robot
- **Zotero:** 待入库
- **Abstract:** Scaling robot manipulation policies requires large amounts of diverse, action-labeled data, yet collecting such data in the real world remains expensive and difficult to scale. Existing methods either depend on human teleoperation, rely on simulation with limited visual realism, or use human videos that lack embodiment-specific annotations.
- 📄 [arXiv](https://arxiv.org/abs/2610.13164v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13164v1)

---

### 11. Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot policy, VLA, robot
- **Zotero:** 待入库
- **Abstract:** In the practical deployment of vision--language--action policies, handling long-tailed task distributions is a common challenge due to the highly imbalanced composition of robot demonstration datasets. To investigate this issue, we study the head-task action bias in shared robot policies, particularly focusing on its relationship with task-specific visual evidence.
- 📄 [arXiv](https://arxiv.org/abs/2610.12861v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12861v1)

---

### 12. JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, reinforcement learning, embodied
- **Zotero:** 待入库
- **Abstract:** Embodied agents must translate multimodal observations and user requests into executable actions while adapting to product constraints, changing goals, and execution feedback. We present JoyInside-VLM-Agent, a ReAct-style multimodal agent developed through product-conditioned trajectory construction and staged policy learning for robotic platforms and smart hardware.
- 📄 [arXiv](https://arxiv.org/abs/2610.12957v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12957v1)

---

### 13. PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, motion planning
- **Zotero:** 待入库
- **Abstract:** Fast whole-body motion planning enables continuous replanning for humanoid robots in dynamic environments while satisfying collision avoidance and kinematic constraints. However, constrained motion planning incurs substantial computational cost due to repeated constraint projection in addition to collision checking and nearest-neighbor search. Recently, GPU-based massively parallel planners have been proposed to reduce computational cost.
- 📄 [arXiv](https://arxiv.org/abs/2610.13195v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13195v1)

---

### 14. VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, manipulation
- **Zotero:** 待入库
- **Abstract:** Third-person human videos offer a scalable alternative to task-specific reward engineering, teleoperation, and manually scripted demonstrations for humanoid loco-manipulation. Recent video-to-humanoid systems have shown that noisy human motion, object trajectories, and contacts can be extracted from unstructured videos and refined into deployable skills.
- 📄 [arXiv](https://arxiv.org/abs/2610.13079v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13079v1)

---

### 15. Evo-RL: Iterative Robot Reinforcement Learning from Selective Experience
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Existing real-world reinforcement learning methods improve robot policies by combining human corrections with autonomous rollouts. However, accumulated experience varies in its value for policy improvement, and even successful trajectories can contain inefficient or redundant behavior, motivating more selective experience reuse. To this end, we propose Evo-RL, an iterative reinforcement learning method that combines human interventions with advantage-guided experience selection.
- 📄 [arXiv](https://arxiv.org/abs/2610.13345v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13345v1)

---

### 16. Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models provide a unified framework for visual understanding, language grounding, and robot control, yet anticipating how the scene will evolve beyond the current observation can provide additional information for control. Action supervision alone does not explicitly encourage such anticipation, while future-image prediction entangles task-relevant motion with largely static appearance.
- 📄 [arXiv](https://arxiv.org/abs/2610.12936v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12936v1)

---

### 17. PartiGen: Part-Aware Representations for Language-Conditioned Humanoid Motion Generation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, robot, MuJoCo
- **Zotero:** 待入库
- **Abstract:** Translating language into humanoid motion requires coordinating body parts, determining motion duration, and producing references suitable for robot execution. We introduce PartiGen, a part-aware latent diffusion framework that incorporates anatomical structure into a shared whole-body motion representation. Part-specific attention processes anatomically masked frame features, and its outputs are fused to combine local limb information with whole-body context.
- 📄 [arXiv](https://arxiv.org/abs/2610.13373v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13373v1)

---

### 18. VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation. The key challenge in turning pretrained VLMs into generalist manipulation policies is to expose these capabilities through an appropriate action interface. Vision-language-action (VLA) models provide a unified trainable policy, but typically introduce learned action tokens, action heads, or action experts whose semantics must be learned from robot data pret...
- 📄 [arXiv](https://arxiv.org/abs/2610.12832v1) | 📥 [PDF](https://arxiv.org/pdf/2610.12832v1)

---

### 19. EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot policy, robot
- **Zotero:** 待入库
- **Abstract:** Artificial intelligence is beginning to automate scientific discovery, yet physical robot-policy research still relies on scientists and engineers to interpret experimental failures and decide how controllers should be revised. We present EndoRSI (Endoscopic Recursive Self-Improvement), a human-governed, self-improving robotic research system in which the embedded EndoForge coding agent iteratively develops and refines endoscopic robot policies using evidence from physical experiments.
- 📄 [arXiv](https://arxiv.org/abs/2610.13376v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13376v1)

---

### 20. ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +3 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** world model
- **Zotero:** 待入库
- **Abstract:** End-to-end planning in complex scenes must model diverse driving intentions and select the most appropriate trajectory using scene context and future risks. However, multi-query regression may collapse to one mode, while anchor-based and generative planners share a scaling bottleneck: small candidate sets limit maneuver coverage or discovery of high-quality trajectories, whereas large sets increase generation and scoring costs.
- 📄 [arXiv](https://arxiv.org/abs/2610.13409v1) | 📥 [PDF](https://arxiv.org/pdf/2610.13409v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **CeDR-Nav: Cross-Embodiment Mapless Navigation via Offline Demonstration Recasting** (SOP: 6) [Link](https://arxiv.org/abs/2610.13007v1)
- **ReAT: Residual Action Tokenization for Autoregressive Robot Policies** (SOP: 6) [Link](https://arxiv.org/abs/2610.13093v1)
- **RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors** (SOP: 6) [Link](https://arxiv.org/abs/2610.13516v1)
- **The value of information and the emergence of communication in evolved e-puck robots** (SOP: 6) [Link](https://arxiv.org/abs/2610.13118v1)
- **Forward Dynamics Models** (SOP: 5) [Link](https://arxiv.org/abs/2610.13117v1)
- **Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving** (SOP: 5) [Link](https://arxiv.org/abs/2610.13453v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 118 篇 | 精选: 20 篇 | 关注: 6 篇 | 过滤: 92 篇
