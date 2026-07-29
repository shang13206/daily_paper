# 🤖 具身智能/机器人学术日报 (2026-07-28)

## 🏆 SOP 精选论文 (≥ 8 分)

### 1. P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning
- **SOP Score:** 24
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +19 | Hardware +0 | Code +3 | cs.RO +2
- **Keywords:** humanoid, parkour, robot learning, parkour, robot
- **Zotero:** 待入库
- **Abstract:** Variational Autoencoders are widely used to encode high-dimensional and noisy observations in robotics. However, their stochastic latent creates a mismatch with Proximal Policy Optimization (PPO): an effective policy marginalizes over the latent distribution, whereas former implementations estimate its probability ratio and KL divergence using only one latent sample.
- 📄 [arXiv](https://arxiv.org/abs/2607.25541v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25541v1)

---

### 2. When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning
- **SOP Score:** 16
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +14 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** humanoid, robot learning, manipulation, robot
- **Zotero:** 待入库
- **Abstract:** Robotic hardware evolves over time, but demonstration data is often tied to a specific sensor and actuator configuration. This raises a practical and underexplored question: when does legacy data begin to benefit an upgraded robot? We study this question on a wheeled humanoid platform across two hardware generations, where both the camera and gripper are changed while the overall morphology remains fixed.
- 📄 [arXiv](https://arxiv.org/abs/2607.25593v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25593v1)

---

### 3. Decentralized Scalable Exploration via Emergent Adaptive Lévy Walks on Minimal-Sensing Platforms
- **SOP Score:** 13
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +1 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Keywords:** robot
- **Zotero:** 待入库
- **Abstract:** Efficient autonomous exploration with palm-sized nano-UAVs remains challenging due to severe limitations in sensing, computation, and flight endurance. We present a lightweight sensor-driven Lévy walk (SDLW) controller for aerial robots weighing under 50 grams and equipped with sparse local sensing. The method combines discrete Lévy step-length sampling with a sensor-reactive heading policy using directional range measurements.
- 📄 [arXiv](https://arxiv.org/abs/2607.25195v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25195v1)

---

### 4. Room-Mediated Co-occurrence for Zero-Shot Object-Centric Semantic Navigation via Frontier Scoring
- **SOP Score:** 12
- **SOP 评分证据:** Venue +10 | Institution +0 | Keywords +0 | Hardware +0 | Code +0 | cs.RO +2
- **Venue:** IROS
- **Zotero:** 待入库
- **Abstract:** Zero-shot ObjectNav methods increasingly use vision-language priors, but direct object-object similarity in the latent space is often a weak proxy for spatial co-occurrence. We present an analytical, training-free semantic navigation pipeline that mediates object relationships through a compact room lexicon. Each object label is mapped to a CLIP-derived Room Probability Vector (RPV), and object-target co-occurrence is computed from RPV distribution overlap.
- 📄 [arXiv](https://arxiv.org/abs/2607.25448v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25448v1)

---

### 5. Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations
- **SOP Score:** 11
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +9 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, imitation learning, motion planning
- **Zotero:** 待入库
- **Abstract:** Successfully automating dexterous, long-horizon robotic manipulation requires frameworks capable of both high-level reasoning and fine-grained execution. Traditional task and motion planning (TAMP), while excellent at symbolic planning, is often brittle in contact-rich operations. Simultaneously, imitation learning (IL), while effective in manipulation tasks with visual feedback, is limited by its low capability in spatial generalization and multi-stage operation.
- 📄 [arXiv](https://arxiv.org/abs/2607.25397v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25397v1)

---

### 6. A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models
- **SOP Score:** 9
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +7 | Hardware +0 | Code +0 | cs.RO +2
- **Keywords:** manipulation, VLA, robot
- **Zotero:** 待入库
- **Abstract:** Vision-language-action (VLA) models predict sequential actions to execute tasks specified by language instructions, conditioned on visual observations and proprioceptive states. However, how to fuse modalities in VLA models remains an open problem, since robot manipulation involves dynamic phases, such as long-distance movements and close-range interactions, in which the importance of visual observations may vary over time.
- 📄 [arXiv](https://arxiv.org/abs/2607.25516v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25516v1)

---

### 7. Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller
- **SOP Score:** 8
- **SOP 评分证据:** Venue +0 | Institution +0 | Keywords +8 | Hardware +0 | Code +0 | cs.RO +0
- **Keywords:** sim-to-real, world model
- **Zotero:** 待入库
- **Abstract:** This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop.
- 📄 [arXiv](https://arxiv.org/abs/2607.25728v1) | 📥 [PDF](https://arxiv.org/pdf/2607.25728v1)

---

## 👀 SOP 关注论文 (5–7.99 分)

- **CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model** (SOP: 7) [Link](https://arxiv.org/abs/2607.25487v1)
- **Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design** (SOP: 6) [Link](https://arxiv.org/abs/2607.25798v1)
- **Tri-Manual Visuomotor Imitation Learning of Robot Policies** (SOP: 6) [Link](https://arxiv.org/abs/2607.25731v1)
- **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** (SOP: 6) [Link](https://arxiv.org/abs/2607.25236v1)
- **Cooperative Multi-UAV Navigation in Complex Environments via Systematic Multi-Agent Deep Reinforcement Learning** (SOP: 5) [Link](https://arxiv.org/abs/2607.25754v1)

## 📊 今日统计
- 评分机制: `paper-evaluation-sop-v1`
- 总抓取: 144 篇 | 精选: 7 篇 | 关注: 5 篇 | 过滤: 132 篇
