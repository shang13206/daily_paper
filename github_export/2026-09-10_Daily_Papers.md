# 🤖 具身智能/机器人学术日报 (2026-09-10)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising
- **SOP Score:** 35
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +19 | Hardware +4 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** humanoid, locomotion, robot learning, terrain, robot
- **Zotero:** 待入库
- **Abstract:** Humanoid locomotion across complex terrain demands forward-looking exteroception to anticipate obstacles, yet this signal is unreliable in real-world deployment, failing partially and intermittently. Existing perceptive policies often assume that depth observations remain clean and in-distribution, while recent attempts to unify perceptive and blind control typically route or switch between separate sub-policies, leaving recoverable information in partially corrupted depth unexploited.
- 📄 [arXiv](https://arxiv.org/abs/2609.11553v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11553v1)

---

### 2. ObstaDiff: Generalizable Diffusion Policy Learning via Obstacle-aware Representations
- **SOP Score:** 27
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +17 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** CoRL
- **Keywords:** robot learning, diffusion policy, manipulation, imitation learning, robot
- **Zotero:** 待入库
- **Abstract:** Imitation learning has achieved impressive results in robotic manipulation, yet most existing approaches assume clean backgrounds and lack explicit mechanisms for obstacle-aware motion generation. Extending such policies to cluttered, real-world scenes with unstructured obstacles remains a key generalization challenge. We present ObstaDiff, a decomposed diffusion-policy framework with a lightweight obstacle-aware visual encoder.
- 📄 [arXiv](https://arxiv.org/abs/2609.10918v1) | 📥 [PDF](https://arxiv.org/pdf/2609.10918v1)

---

### 3. IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies
- **SOP Score:** 23
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +9 | Hardware +4 | Code +0 | cs.RO +0
- **Venue:** IROS
- **Keywords:** flow matching, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) policies leverage pretrained vision-language backbones to achieve strong cross-task generalization. A leading design couples this backbone with a dedicated continuous action head trained via diffusion or flow matching. However, such heads rely on iterative multi-step sampling, for example 10 Euler steps in $π_{0.5}$. This creates an inference bottleneck that produces stop-and-go movement in the robot and slower task completion.
- 📄 [arXiv](https://arxiv.org/abs/2609.10915v1) | 📥 [PDF](https://arxiv.org/pdf/2609.10915v1)

---

### 4. Beyond Noise Steering: Dual-Latent Space Reinforcement Learning for Generative Robot Policy
- **SOP Score:** 17
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** robot policy, manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Pretrained generative robot policies learn expressive action priors from demonstrations. However, existing reinforcement learning methods only steer the noisy space but fail to modulate intermediate action representations during the generation process, resulting in performance degradation and inefficiency.
- 📄 [arXiv](https://arxiv.org/abs/2609.11270v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11270v1)

---

### 5. Morphology-Aware Human Motion Retargeting for Wheeled-Humanoid Loco-Manipulation
- **SOP Score:** 17
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +15 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, locomotion, manipulation, robot, Isaac Lab
- **Zotero:** 待入库
- **Abstract:** Human-to-humanoid retargeting has largely been studied on legged platforms, while comparatively few wheeled-humanoid systems support coupled locomotion and manipulation from general human motion. Building on GMR's configurable general-motion retargeting and BeyondMimic's physically simulated R1 Pro learning framework, we present a reproducible pipeline that converts multi-dataset SMPLX motion into executable loco-manipulation behavior for the Galaxea R1 Pro wheeled humanoid.
- 📄 [arXiv](https://arxiv.org/abs/2609.11357v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11357v1)

---

### 6. Gait-Dependent Effects on Quadruped Locomotion for Load-Carrying using Passive Mechanism
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, locomotion
- **Zotero:** 待入库
- **Abstract:** Passive mechanical interfaces offer a lightweight alternative to actuated manipulators for quadruped payload carrying, but their impedance directly couples the payload dynamics with the locomotion pattern. This paper analyzes how passive-arm stiffness-damping selection affects payload-carrying locomotion under different gait and payload conditions. We compare damped and underdamped passive-arm impedance configurations in simulation during flat-ground locomotion.
- 📄 [arXiv](https://arxiv.org/abs/2609.11059v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11059v1)

---

### 7. Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, robot navigation, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult.
- 📄 [arXiv](https://arxiv.org/abs/2609.11225v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11225v1)

---

### 8. 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Long-horizon robot manipulation requires memory, but not necessarily inside the action policy. To address such tasks, current agentic systems often combine VLAs with planners and geometric tools, sometimes using additional depth or calibrated geometry. These systems confound attribution: gains may come from richer observations or alternative motor tools, while failures may stem from either the policy or an under-specified language interface.
- 📄 [arXiv](https://arxiv.org/abs/2609.11308v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11308v1)

---

### 9. BridgeMatch: Conditional Transport Bridges in Matching Matrix Space for 3D Deformable Registration
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** flow matching, manipulation, embodied
- **Zotero:** 待入库
- **Abstract:** Reliable non-rigid point cloud correspondences are important for deformable anatomical registration, embodied perception and manipulation, and dynamic 3D reconstruction. Coarse-to-fine methods reduce computational cost by selecting the top-\(K\) coarse regions. However, this pruning may remove weak but correct hypotheses and restrict fine matching to an incomplete search space.
- 📄 [arXiv](https://arxiv.org/abs/2609.11472v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11472v1)

---

### 10. FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** VLA, world model, robot
- **Zotero:** 待入库
- **Abstract:** Reliable robot deployment requires online failure monitoring, yet existing monitors mainly derive risk from proxy signals or train dedicated monitoring components. We ask whether the internal predictive states of a frozen pretrained robotic world model already contain directly decodable failure information.
- 📄 [arXiv](https://arxiv.org/abs/2609.11445v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11445v1)

---

### 11. Safety-aware Skill Adaptation for Reinforcement Learning in Dynamic Environments
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Skill adaptation frameworks based on reinforcement learning often require restrictive assumptions to maintain stability, such as fixed observations or tightly controlled exploration schedules. In cluttered and dynamic environments, however, unrestricted exploration can lead to unsafe behaviour and unstable learning, particularly when task-relevant observations lie near obstacles or involve moving objects.
- 📄 [arXiv](https://arxiv.org/abs/2609.11433v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11433v1)

---

### 12. Topological Necessities: Mechanism-Invariant Strategic Subgoals for Cross-Embodiment Goal-Conditioned Control
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** humanoid, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Long-horizon goal-conditioned reinforcement learning delegates control to a high-level module that proposes subgoals, but existing subgoals are implicit byproducts of value functions or latent actions, tied to the executor that produced them. We study a different object: a route-conditioned order of unavoidable stages that every successful executor must traverse, recoverable from offline trajectories and belonging to none of them.
- 📄 [arXiv](https://arxiv.org/abs/2609.11014v1) | 📥 [PDF](https://arxiv.org/pdf/2609.11014v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **GeoTrussRover: Morphological Computation with Contact-Semantic Control Primitives** (SOP: 7) [Link](https://arxiv.org/abs/2609.11361v1)
- **A Mathematical Theory of Pragmatic Information** (SOP: 6) [Link](https://arxiv.org/abs/2609.10986v1)
- **Memory as Plans: World-Action Modeling with Memory-Grounded Planning** (SOP: 6) [Link](https://arxiv.org/abs/2609.11561v1)
- **SwarmNxt: Open-source Software-Hardware Platform for Fast and Agile Aerial Swarms** (SOP: 6) [Link](https://arxiv.org/abs/2609.11382v1)
- **LTLDiff: Finite Linear Temporal Logic-Guided Data Generation and Diffusion Policies for Multi-agent Robotic Manipulation** (SOP: 5) [Link](https://arxiv.org/abs/2609.11043v1)
- **Quasi-static analysis of passive stability in a novel underactuated multi-finger hand** (SOP: 5) [Link](https://arxiv.org/abs/2609.11579v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 148 篇 | 精选: 12 篇 | 关注: 6 篇 | 过滤: 130 篇
