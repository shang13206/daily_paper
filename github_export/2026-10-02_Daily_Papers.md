# 🤖 具身智能/机器人学术日报 (2026-10-02)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. Safe Streaming Flow Planning by Aligning Sampling Dynamics with Execution Dynamics
- **SOP Score:** 32
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +16 | Hardware +4 | Code +0 | cs.RO +2
- **Venue:** CoRL
- **Keywords:** locomotion, robot learning, flow matching, robot
- **Zotero:** 待入库
- **Abstract:** Generative planners based on diffusion/flow matching can learn to synthesize long-horizon trajectories from demonstrations. However, real-world deployment requires (i) enforcing safety constraints during execution and (ii) tight online replanning at fast execution rates. Prior safe diffusion/flow planners generate the agent's full trajectory at once, while repeatedly perturbing intermediate states to satisfy safety constraints.
- 📄 [arXiv](https://arxiv.org/abs/2610.03132v1) | 📥 [PDF](https://arxiv.org/pdf/2610.03132v1)

---

### 2. CrowdOcc: Monocular Semantic Scene Completion for Quadruped Robots in Crowded Indoor Environments
- **SOP Score:** 15
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +5 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** ICRA
- **Keywords:** quadruped
- **Zotero:** 待入库
- **Abstract:** Monocular semantic scene completion (SSC) for quadruped robots remains underexplored in real crowded indoor environments, where human-scene occlusion disrupts static geometry and human occupancy predictions are often incomplete or spatially misplaced. We present CrowdOcc, an RGB-D dataset and monocular SSC framework for this setting. CrowdOcc contains 25.1K frames from 11 indoor scenes, with semantic occupancy annotations constructed through static dynamic decoupling.
- 📄 [arXiv](https://arxiv.org/abs/2610.03031v1) | 📥 [PDF](https://arxiv.org/pdf/2610.03031v1)

---

### 3. Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** sim-to-real, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Transferring robotic skills from simulation to reality requires task knowledge that remains usable across differences in perception, dynamics, and embodiment. We introduce Skill2Real, an agentic policy framework that learns executable skills through a shared application programming interface (API). A Proposer-Verifier-Governor (PVG) loop uses privileged simulation evidence to diagnose outcomes and validate updates, while keeping learned skills grounded in public observations and API semantics.
- 📄 [arXiv](https://arxiv.org/abs/2610.02788v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02788v1)

---

### 4. AdaTempo: Learning Shared Relative Tempo from Demonstrations for Faster Robot Manipulation
- **SOP Score:** 14
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +12 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** diffusion policy, manipulation, imitation learning, robot
- **Zotero:** 待入库
- **Abstract:** Visuomotor policies trained via imitation learning often inherit the unnecessarily slow timing of teleoperated demonstrations. Yet uniform speedup is unreliable because different phases of a manipulation task tolerate acceleration differently. In this work, we introduce AdaTempo, a self-supervised method that accelerates visuomotor policies by exploiting shared relative-tempo structure in demonstrations.
- 📄 [arXiv](https://arxiv.org/abs/2610.02706v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02706v1)

---

### 5. Beyond Reward Hacking: Proxy Divergence Across Four Layers of a Staged Humanoid Learning Pipeline
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, legged robot, robot
- **Zotero:** 待入库
- **Abstract:** A reinforcement-learning (RL) pipeline for a legged robot is assembled from proxies. A reward stands in for intended behaviour, a curriculum gate stands in for competence, an evaluation statistic stands in for robustness, and a reference motion stands in for an achievable skill. The traditional view treats only the first of these as optimised against, and so locates specification failure (reward hacking) in the reward alone.
- 📄 [arXiv](https://arxiv.org/abs/2610.03196v1) | 📥 [PDF](https://arxiv.org/pdf/2610.03196v1)

---

### 6. FastOPD: On-Policy Distillation for Lightweight VLA Deployment
- **SOP Score:** 13
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-Language-Action (VLA) foundation models have scaled rapidly to enhance manipulation performance and generalizability, but this scaling incurs high computational costs that render real-world deployment increasingly challenging. Existing approaches typically mitigate this issue by designing smaller architectures or reducing the iterative denoising steps in flow-based policies.
- 📄 [arXiv](https://arxiv.org/abs/2610.02832v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02832v1)

---

### 7. Around the World: Unified Learned Locomotion on a 270 g Continuous-Rotation Quadruped
- **SOP Score:** 12
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** quadruped, locomotion
- **Zotero:** 待入库
- **Abstract:** Closed-loop learned locomotion is established on commercial quadrupeds but remains uncommon at the sub-kilogram scale. Continuous-rotation legs give MiNI-Q, a 270 g quadruped, access to supporting configurations on either side of the body. We exploit this range with a single posture-conditioned reinforcement-learning policy that runs entirely onboard.
- 📄 [arXiv](https://arxiv.org/abs/2610.02728v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02728v1)

---

### 8. PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** World action models jointly learn to forecast world dynamics and predict robot actions, such that the learned internal world dynamics guide accurate actions. Existing approaches typically represent the world as RGB frames or latent counterparts while predicting actions as end-effector poses or joint angles, but they often struggle to capture the 3D spatial structure and contact geometry central to dexterous manipulation.
- 📄 [arXiv](https://arxiv.org/abs/2610.02840v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02840v1)

---

### 9. RoboBridge: A Self-Evolving Embodied Agent Framework for Sim-to-Real Transfer
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** sim-to-real, manipulation, embodied
- **Zotero:** 待入库
- **Abstract:** A key challenge in bringing embodied intelligence into the real world is transferring capabilities from simulation to reality and enabling agents to continually adapt after deployment. End-to-end vision-language-action policies provide strong manipulation capabilities, but their transfer to physical environments typically relies on calibrating simulated visual and dynamical conditions, collecting additional target-domain demonstrations, and optimizing the policy through further training.
- 📄 [arXiv](https://arxiv.org/abs/2610.02717v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02717v1)

---

### 10. DexJoCo-X: Benchmarking Action Representations for Multi-Hand Dexterous Manipulation
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** dexterous manipulation, manipulation
- **Zotero:** 待入库
- **Abstract:** As dexterous hands proliferate, collecting data and training policies separately for every morphology becomes increasingly impractical. Scalable cross-embodiment learning therefore requires a unified representation that captures shared manipulation structure while preserving morphology-specific control. Differences in hands, tasks, datasets, and control interfaces prevent existing studies from isolating the effects of representation, pretraining, and architecture.
- 📄 [arXiv](https://arxiv.org/abs/2610.03278v1) | 📥 [PDF](https://arxiv.org/pdf/2610.03278v1)

---

### 11. EmbPASS: Towards Cross-Embodiment Open Panoramic Segmentation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** quadruped, embodied
- **Zotero:** 待入库
- **Abstract:** Panoramic images provide a complete 360-degree field of view, enabling comprehensive scene understanding for embodied perception. However, heterogeneous embodied platforms exhibit substantial differences in observation viewpoints and spatial layouts, giving rise to cross-embodiment observation shifts that pose additional challenges to consistent and reliable panoramic perception, while systematic studies of this problem remain limited.
- 📄 [arXiv](https://arxiv.org/abs/2610.03248v1) | 📥 [PDF](https://arxiv.org/pdf/2610.03248v1)

---

### 12. SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Tactile sensing provides essential contact information for robotic manipulation, yet incorporating it into pretrained vision-language-action (VLA) models remains challenging. A common concern is that simply introducing touch during task-specific fine-tuning may fail to bridge the cross-modal gap, yielding limited gains or even reduced success.
- 📄 [arXiv](https://arxiv.org/abs/2610.02784v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02784v1)

---

### 13. ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models aim to perform diverse manipulation tasks, but task success in existing rigid-body benchmarks does not indicate whether they preserve objects. We introduce ManiPhysicsZoo, which consolidates literature-supported material properties, 3D meshes, and supporting references into reusable object assets.
- 📄 [arXiv](https://arxiv.org/abs/2610.02802v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02802v1)

---

### 14. MixVLA: Adaptive Mixing of Non-Invariant Information for Generalizable Vision-Language-Action Models
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-Language-Action (VLA) models have achieved remarkable advances in robotic manipulation, yet their zero-shot generalization under out-of-distribution (OOD) conditions remains limited. These models often entangle task-relevant invariant structure with environment-specific non-invariant factors, causing policies to rely on spurious appearance cues during action prediction.
- 📄 [arXiv](https://arxiv.org/abs/2610.02898v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02898v1)

---

### 15. Permutation Robustness Is Not Enough: Action Collapse in Multi-Agent Transformer Policies
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** robot learning, robot
- **Zotero:** 待入库
- **Abstract:** Transformer policies are attractive for multi-agent robot learning because self-attention can model interactions among agents. However, multi-agent teams are unordered, while transformers typically process agents as ordered token sequences. We study how this mismatch affects cooperative navigation policies under agent-order permutations. Our results show that low permutation error alone can be misleading: policies may appear robust simply because all agents choose the same action.
- 📄 [arXiv](https://arxiv.org/abs/2610.02848v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02848v1)

---

### 16. SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models often require costly real-world demonstrations to adapt to contact-rich manipulation tasks, particularly when generalization across object placements is needed. We propose SARI (Simulated Approach, Real Interaction), a phase-split sim-and-real co-training framework built on a simple insight: spatial coverage and contact physics should be acquired from the domains best suited to them.
- 📄 [arXiv](https://arxiv.org/abs/2610.02804v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02804v1)

---

### 17. SceneFactory-3D: Lifting 2D Traffic Scenes into 3D Physical Counterfactuals for Scalable Physically Grounded Safety Evaluation
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +3 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** terrain
- **Zotero:** 待入库
- **Abstract:** Scalable driving simulators typically execute vehicle commands using prescribed behavioral or kinematic rules, overlooking the physics of tire-road interfaces, thereby limiting their ability to capture how adverse road and environmental conditions alter vehicle execution and propagate through traffic. To address this limitation, we present SceneFactory-3D, a GPU-batched, physics-grounded multi-agent driving simulator.
- 📄 [arXiv](https://arxiv.org/abs/2610.02874v1) | 📥 [PDF](https://arxiv.org/pdf/2610.02874v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **CSIR: Contextually and Socially Informed Robots for Efficient Person Goal Navigation** (SOP: 7) [Link](https://arxiv.org/abs/2610.02750v1)
- **DeltaWorld: Physically Consistent Interactive World Simulators via Action-Conditioned Latent Increment Learning** (SOP: 6) [Link](https://arxiv.org/abs/2610.02691v1)
- **Learning Reflexive Behavior for Contact-Rich Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.02811v1)
- **RoboChemGym: A Protocol-Driven Generative Simulation Framework for Long-Horizon Chemical Manipulation** (SOP: 6) [Link](https://arxiv.org/abs/2610.02708v1)
- **LOCUS: Landmark-Oriented Container Discrimination Using Spatial Graphs** (SOP: 5) [Link](https://arxiv.org/abs/2610.02803v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 39 篇 | 精选: 17 篇 | 关注: 5 篇 | 过滤: 17 篇
