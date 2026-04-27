# 🤖 具身智能/机器人学术日报 (2026-04-24)

## 🏆 精选论文 (Top 5)

### 1. X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation
- **Score:** 79
- **Categories:** cs.RO
- **Abstract:** Wheel-legged robots combine the efficiency of wheeled locomotion with the versatility of legged systems, enabling rapid traversal over both continuous and discrete terrains. However, conventional designs typically employ fixed wheels as feet and limited degrees of freedom (DoFs) at the hips, resulting in reduced stability and mobility during legged locomotion compared to humanoids with flat feet.
- **AI 点评:** X2-N轮足人形机器人结合RL全身控制框架，实现双模式运动与操作，覆盖轮足locomotion、地形适应和实机部署，与OmniBot研究高度契合。
- 📄 [arXiv](https://arxiv.org/abs/2604.21541) | 📥 [PDF](https://arxiv.org/pdf/2604.21541.pdf)

---

### 2. Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
- **Score:** 73
- **Categories:** cs.RO, cs.AI
- **Abstract:** Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging due to the conflicting requirements of stability and dynamic expressiveness across different gaits. We present a multi-gait learning approach that enables a humanoid robot to master five distinct gaits -- walking, goose-stepping, running, stair climbing, and jumping -- using a consistent policy structure, action space, and reward formulation.
- **AI 点评:** 人形机器人多步态RL学习（含楼梯攀爬），采用选择性AMP+PPO+域随机化实现zero-shot sim-to-real，与locomotion policy learning和sim-to-real方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2604.19102) | 📥 [PDF](https://arxiv.org/pdf/2604.19102.pdf)

---

### 3. SLAM as a Stochastic Control Problem with Partial Information: Optimal Solutions and Rigorous Approximations
- **Score:** 70
- **Categories:** cs.RO, math.OC
- **Abstract:** Simultaneous localization and mapping (SLAM) is a foundational state estimation problem in robotics in which a robot accurately constructs a map of its environment while also localizing itself within this construction. We study the active SLAM problem through the lens of optimal stochastic control, thereby recasting it as a decision-making problem under partial information.
- **AI 点评:** 将主动SLAM建模为随机最优控制问题，直接服务于移动机器人定位建图与导航决策，与导航感知方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.21693) | 📥 [PDF](https://arxiv.org/pdf/2604.21693.pdf)

---

### 4. A Survey of Legged Robotics in Non-Inertial Environments: Past, Present, and Future
- **Score:** 66
- **Categories:** cs.RO, eess.SY
- **Abstract:** Legged robots have demonstrated remarkable agility on rigid, stationary ground, but their locomotion reliability remains limited in non-inertial environments, where the supporting ground moves, tilts, or accelerates. Such conditions arise in ground transportation, maritime platforms, and aerospace settings, and they introduce persistent time-varying disturbances that break the stationary-ground assumptions underlying conventional legged locomotion.
- **AI 点评:** 综述非惯性环境下腿足机器人的状态估计与控制，与四足机器人locomotion和terrain adaptation高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.20990) | 📥 [PDF](https://arxiv.org/pdf/2604.20990.pdf)

---

### 5. Quadruped Parkour Learning: Sparsely Gated Mixture of Experts with Visual Input
- **Score:** 59
- **Categories:** cs.RO
- **Abstract:** Robotic parkour provides a compelling benchmark for advancing locomotion over highly challenging terrain, including large discontinuities such as elevated steps. Recent approaches have demonstrated impressive capabilities, including dynamic climbing and jumping, but typically rely on sequential multilayer perceptron (MLP) architectures with densely activated layers.
- **AI 点评:** 四足机器人视觉跑酷，基于稀疏MoE架构的运动控制策略，在真实Unitree Go2上验证，直接对应足式运动学习与复杂地形适应。
- 📄 [arXiv](https://arxiv.org/abs/2604.19344) | 📥 [PDF](https://arxiv.org/pdf/2604.19344.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Radar Odometry Subject to High Tilt Dynamics of Subarctic Environments** (Score: 59) [Link](https://arxiv.org/abs/2604.19962)
- **HALO: Hybrid Auto-encoded Locomotion with Learned Latent Dynamics, Poincar\'e Maps, and Regions of Attraction** (Score: 53) [Link](https://arxiv.org/abs/2604.18887)
- **RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting** (Score: 53) [Link](https://arxiv.org/abs/2604.21355)
- **Efficient Reinforcement Learning using Linear Koopman Dynamics for Nonlinear Robotic Systems** (Score: 46) [Link](https://arxiv.org/abs/2604.19980)
- **Multimodal embodiment-aware navigation transformer** (Score: 46) [Link](https://arxiv.org/abs/2604.19267)
- **Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot** (Score: 44) [Link](https://arxiv.org/abs/2604.21351)
- **SL(C)AMma: Simultaneous Localisation, (Calibration) and Mapping With a Magnetometer Array** (Score: 42) [Link](https://arxiv.org/abs/2604.19946)
- **Reinforcement Learning Enabled Adaptive Multi-Task Control for Bipedal Soccer Robots** (Score: 41) [Link](https://arxiv.org/abs/2604.19104)
- **Feasibility of Indoor Frame-Wise Lidar Semantic Segmentation via Distillation from Visual Foundation Model** (Score: 38) [Link](https://arxiv.org/abs/2604.18831)

## 📊 今日统计
- 总抓取: 666 篇 | 通过初筛: 145 篇 | 精选: 5 篇 (含 LLM 精筛)
