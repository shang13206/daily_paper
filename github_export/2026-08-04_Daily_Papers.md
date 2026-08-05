# 🤖 具身智能/机器人学术日报 (2026-08-04)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. Unified Visuomotor Targets: Supervising VLAs Beyond Physical Actions
- **SOP Score:** 19
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** VLA models are trained to predict robot actions from visual and language observations. This is a natural choice, but it creates a mismatch: VLMs encode rich, high-level representations of scenes and goals, while robot actions are low-level signals with limited task structure. We ask whether changing what the policy is trained to predict, rather than how it is architecturally designed, can yield better and more efficiently trained policies.
- 📄 [arXiv](https://arxiv.org/abs/2608.03563v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03563v1)

---

### 2. Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking
- **SOP Score:** 16
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +6 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** IROS
- **Keywords:** manipulation, VLA
- **Zotero:** 待入库
- **Abstract:** Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned attention is diverted from task-relevant regions to a localized patch.
- 📄 [arXiv](https://arxiv.org/abs/2608.03231v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03231v1)

---

### 3. PFM-HR: Pose Flow Matching for Humanoid Robots
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, flow matching, reinforcement learning
- **Zotero:** 待入库
- **Abstract:** Motion priors improve reinforcement learning for physics-based humanoid tracking, but temporal priors require ordered motion clips, while pose priors provide limited guidance for policy-induced pose transitions. We present Pose Flow Matching for Humanoid Robots (PFM-HR), a reusable flow matching prior trained directly on large scale unordered pose data.
- 📄 [arXiv](https://arxiv.org/abs/2608.03227v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03227v1)

---

### 4. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation
- **SOP Score:** 15
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +13 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, dexterous manipulation, manipulation
- **Zotero:** 待入库
- **Abstract:** Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations, but transferring such imagined behaviors into executable whole-body humanoid skills remains largely unexplored.
- 📄 [arXiv](https://arxiv.org/abs/2608.03387v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03387v1)

---

### 5. EmbodiedVAE: Disentangled Video VAE for Efficient and Controllable Embodied Manipulation
- **SOP Score:** 12
- **SOP 评分证据:** Venue +5 | Institution +0 | Keywords +5 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** ECCV
- **Keywords:** manipulation, robot, embodied
- **Zotero:** 待入库
- **Abstract:** Latent diffusion models (LDMs) have recently significantly advanced embodied learning in constructing powerful embodied manipulation world models. However, despite the remarkable performance, existing LDMs predominantly rely on Variational Autoencoders (VAEs) optimized for natural scenes while failing to account for the unique characteristics of embodied manipulation scenarios, yielding latent representations that are neither compact nor controllable, thereby hindering efficient training of LDMs...
- 📄 [arXiv](https://arxiv.org/abs/2608.02990v1) | 📥 [PDF](https://arxiv.org/pdf/2608.02990v1)

---

### 6. POMDPs for Autonomous Science Exploration
- **SOP Score:** 12
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +0 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Zotero:** 待入库
- **Abstract:** Autonomous exploration missions require decision-making under sensor uncertainty and computational constraints, yet integrating scientific representations into POMDP planning has remained intractable due to high-dimensional observation spaces. Information-theoretic planners overcome this by assuming deterministic observations, sacrificing the principled uncertainty quantification that POMDPs provide.
- 📄 [arXiv](https://arxiv.org/abs/2608.03155v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03155v1)

---

### 7. A Hierarchical Approach to Imitation Learning for Manipulation Tasks Requiring Time Varying Forces
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +11 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** diffusion policy, manipulation, imitation learning
- **Zotero:** 待入库
- **Abstract:** Diffusion policies have shown strong performance in learning complex, multi-modal behaviors for robotic manipulation. However, their application to contact-rich disassembly tasks remains limited by a key trade-off: the iterative denoising process introduces inference latencies that makes high frequency control difficult, which is essential for realizing dynamic interactions such as chiseling and prying.
- 📄 [arXiv](https://arxiv.org/abs/2608.03103v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03103v1)

---

### 8. PLS-Calib: A Partial Least Squares Framework for Event Camera and Odometry Calibration under Ground Motion Constraints
- **SOP Score:** 11
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +1 | Hardware +0 | Code +0 | cs.RO +0
- **Venue:** IROS
- **Keywords:** robot
- **Zotero:** 待入库
- **Abstract:** Accurate extrinsic rotation calibration between sensors is fundamental to the performance of robotic perception systems. However, most existing calibration techniques rely on full 6-DoF motion to excite all degrees of freedom, which is often infeasible for ground-constrained robots with limited motion capabilities.
- 📄 [arXiv](https://arxiv.org/abs/2608.03296v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03296v1)

---

### 9. Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +10 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** manipulation, VLA, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Existing chunk-based Vision-Language-Action (VLA) models execute a fixed number of actions (i.e., execution horizon) before replanning, turning replanning into a task-agnostic periodic schedule that is independent of task progress. As a result, when no replanning boundary falls before a critical manipulation stage, it is executed from a stale chunk rather than a freshly replanned one.
- 📄 [arXiv](https://arxiv.org/abs/2608.03483v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03483v1)

---

### 10. PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud
- **SOP Score:** 10
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +3 | cs.RO +0
- **Keywords:** VLA, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Physical AI policies require inference throughout their lifecycle, including model evaluation, cloud reinforcement learning rollout, edge GPU serving, and onboard deployment. Although these settings share the same checkpoint and action semantics, they often rely on separate inference programs. To unify them, we build PhyAI, a Physical AI inference engine with a single runtime that keeps architecture-specific conditioning, solver, cache, and output logic in model adapters while sharing graph exec...
- 📄 [arXiv](https://arxiv.org/abs/2608.03682v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03682v1)

---

### 11. GORDON: Graph-based Object-centric Rewards for Decomposition of Long-Horizon Manipulation
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, reinforcement learning, robot
- **Zotero:** 待入库
- **Abstract:** Learning long-horizon manipulation skills with reinforcement learning remains challenging due to the complexity of reward design, the limited guidance of sparse rewards, and the high cost of manual subtask annotation. Visual demonstrations can provide supervision for reward learning, but rewards learned from raw pixels can be brittle and sensitive to visual variation, background appearance, and robot motion.
- 📄 [arXiv](https://arxiv.org/abs/2608.03753v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03753v1)

---

### 12. Human Centric Embodied Intelligence for Soft Wearable Robotics
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +2 | Hardware +4 | Code +0 | cs.RO +2
- **Keywords:** robot, embodied
- **Zotero:** 待入库
- **Abstract:** Soft wearable robots have evolved rapidly from proof-of-concept devices into promising platforms for rehabilitation, occupational assistance, and human augmentation. As the field matures, its central challenge extends beyond the development of softer materials and more capable actuators to the integration of sensing, intelligence, and human adaptation into systems that users can wear comfortably, trust, and benefit from over extended periods.
- 📄 [arXiv](https://arxiv.org/abs/2608.03556v1) | 📥 [PDF](https://arxiv.org/pdf/2608.03556v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **Learning Context-Aware Motion Priors for Humanoid Control** (SOP: 7) [Link](https://arxiv.org/abs/2608.03234v1)
- **Shooting for Contact: Contact-Implicit Multiple Shooting for Dynamic Motion Retargeting** (SOP: 7) [Link](https://arxiv.org/abs/2608.03116v1)
- **Accelerating Human-Aware Robot Trajectory Generation via Diffusion and Consistency Distillation** (SOP: 6) [Link](https://arxiv.org/abs/2608.03159v1)
- **DigitCode: Symbolic Tokenization of Hand Motion by Anatomical Units** (SOP: 6) [Link](https://arxiv.org/abs/2608.03127v1)
- **How Should Vision-Language-Action Models Use Proprioceptive State?** (SOP: 6) [Link](https://arxiv.org/abs/2608.03052v1)
- **Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning** (SOP: 6) [Link](https://arxiv.org/abs/2608.02993v1)
- **Track4Action: Distilling World-Centric 3D Tracker into Vision-Language-Action Policies** (SOP: 6) [Link](https://arxiv.org/abs/2608.03727v1)
- **A Wearable Stiffness-Rendering Haptic Device with a Honeycomb Jamming Mechanism for Bilateral Teleoperation** (SOP: 5) [Link](https://arxiv.org/abs/2608.03002v1)
- **Bridging Online and Offline Handwriting via Differentiable Physical Rendering** (SOP: 5) [Link](https://arxiv.org/abs/2608.03198v1)
- **GraspMeanFlow: SE(3)-Equivariant MeanFlow for Few-Step 6-DoF Grasp Generation** (SOP: 5) [Link](https://arxiv.org/abs/2608.03295v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 319 篇 | 精选: 12 篇 | 关注: 10 篇 | 过滤: 297 篇
