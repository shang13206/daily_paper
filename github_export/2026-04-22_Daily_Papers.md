# 🤖 具身智能/机器人学术日报 (2026-04-22)

## 🏆 精选论文 (Top 5)

### 1. Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
- **Score:** 69
- **Categories:** cs.AI, cs.RO
- **Abstract:** Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging due to the conflicting requirements of stability and dynamic expressiveness across different gaits. We present a multi-gait learning approach that enables a humanoid robot to master five distinct gaits -- walking, goose-stepping, running, stair climbing, and jumping -- using a consistent policy structure, action space, and reward formulation.
- **AI 点评:** 人形机器人多步态RL学习，含零样本sim-to-real迁移和域随机化，方法（AMP+PPO）与四足locomotion policy learning高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.19102v1) | 📥 [PDF](https://arxiv.org/pdf/2604.19102v1)

---

### 2. HALO: Hybrid Auto-encoded Locomotion with Learned Latent Dynamics, Poincaré Maps, and Regions of Attraction
- **Score:** 59
- **Categories:** cs.RO, eess.SY
- **Abstract:** Reduced-order models are powerful for analyzing and controlling high-dimensional dynamical systems. Yet constructing these models for complex hybrid systems such as legged robots remains challenging. Classical approaches rely on hand-designed template models (e.g., LIP, SLIP), which, though insightful, only approximate the underlying dynamics.
- **AI 点评:** 提出用自编码器学习腿式机器人混合动力系统的降阶模型并分析吸引域，直接针对人形/跳跃机器人步态稳定性分析，与locomotion policy研究高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.18887v1) | 📥 [PDF](https://arxiv.org/pdf/2604.18887v1)

---

### 3. Quadruped Parkour Learning: Sparsely Gated Mixture of Experts with Visual Input
- **Score:** 59
- **Categories:** cs.RO
- **Abstract:** Robotic parkour provides a compelling benchmark for advancing locomotion over highly challenging terrain, including large discontinuities such as elevated steps. Recent approaches have demonstrated impressive capabilities, including dynamic climbing and jumping, but typically rely on sequential multilayer perceptron (MLP) architectures with densely activated layers.
- **AI 点评:** 四足机器人视觉parkour学习，使用MoE策略在真实Unitree Go2上实现复杂地形穿越，高度契合locomotion policy learning与sim-to-real核心方向。
- 📄 [arXiv](https://arxiv.org/abs/2604.19344v1) | 📥 [PDF](https://arxiv.org/pdf/2604.19344v1)

---

### 4. Multimodal embodiment-aware navigation transformer
- **Score:** 52
- **Categories:** cs.RO
- **Abstract:** Goal-conditioned navigation models for ground robots trained using supervised learning show promising zero-shot transfer, but their collision-avoidance capability nevertheless degrades under distribution shift, i.e. environmental, robot or sensor configuration changes. We propose ViLiNT a multimodal, attention-based policy for goal navigation, trained on heterogeneous data from multiple platforms and environments, which improves robustness with two key features.
- **AI 点评:** 融合RGB+LiDAR+embodiment描述符的多模态导航Transformer，在真实机器人上验证越野导航，与感知-导航一体化方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.19267v1) | 📥 [PDF](https://arxiv.org/pdf/2604.19267v1)

---

### 5. Enhancing Glass Surface Reconstruction via Depth Prior for Robot Navigation
- **Score:** 46
- **Categories:** cs.CV, cs.RO
- **Abstract:** Indoor robot navigation is often compromised by glass surfaces, which severely corrupt depth sensor measurements. While foundation models like Depth Anything 3 provide excellent geometric priors, they lack an absolute metric scale. We propose a training-free framework that leverages depth foundation models as a structural prior, employing a robust local RANSAC-based alignment to fuse it with raw sensor depth.
- **AI 点评:** 针对玻璃表面深度传感器失效问题提出训练无关的深度融合框架，直接服务于室内机器人导航，与导航感知方向相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.18336v1) | 📥 [PDF](https://arxiv.org/pdf/2604.18336v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Relative State Estimation using Event-Based Propeller Sensing** (Score: 43) [Link](https://arxiv.org/abs/2604.18289v1)
- **Feasibility of Indoor Frame-Wise Lidar Semantic Segmentation via Distillation from Visual Foundation Model** (Score: 42) [Link](https://arxiv.org/abs/2604.18831v1)
- **Bounded Ratio Reinforcement Learning** (Score: 41) [Link](https://arxiv.org/abs/2604.18578v1)
- **A Hamilton-Jacobi Reachability-Guided Search Framework for Efficient and Safe Indoor Planar Robot Navigation** (Score: 40) [Link](https://arxiv.org/abs/2604.17679v1)
- **GenerativeMPC: VLM-RAG-guided Whole-Body MPC with Virtual Impedance for Bimanual Mobile Manipulation** (Score: 40) [Link](https://arxiv.org/abs/2604.19522v1)
- **Reinforcement Learning Enabled Adaptive Multi-Task Control for Bipedal Soccer Robots** (Score: 40) [Link](https://arxiv.org/abs/2604.19104v1)

## 📊 今日统计
- 总抓取: 702 篇 | 通过初筛: 91 篇 | 精选: 5 篇 (含 LLM 精筛)
