# 🤖 具身智能/机器人学术日报 (2026-04-21)

## 🏆 精选论文 (Top 5)

### 1. Iterated Invariant EKF for Quadruped Robot Odometry
- **Score:** 80
- **Categories:** cs.RO
- **Abstract:** Kalman filter-based algorithms are fundamental for mobile robots, as they provide a computationally efficient solution to the challenging problem of state estimation. However, they rely on two main assumptions that are difficult to satisfy in practice: (a) the system dynamics must be linear with Gaussian process noise, and (b) the measurement model must also be linear with Gaussian measurement noise.
- **AI 点评:** 提出基于IterIEKF的四足机器人里程计状态估计算法，利用本体感知和运动学约束，直接对应四足机器人状态估计核心需求。
- 📄 [arXiv](https://arxiv.org/abs/2604.15449) | 📥 [PDF](https://arxiv.org/pdf/2604.15449.pdf)

---

### 2. LatentMimic: Terrain-Adaptive Locomotion via Latent Space Imitation
- **Score:** 76
- **Categories:** cs.RO, cs.AI
- **Abstract:** Developing natural and diverse locomotion controllers for quadruped robots that can adapt to complex terrains while preserving motion style remains a significant challenge. Existing imitation-based methods face a fundamental optimization trade-off: strict adherence to motion capture (mocap) references penalizes the geometric deviations required for terrain adaptability, whereas terrain-centric policies often compromise stylistic fidelity.
- **AI 点评:** 四足机器人地形自适应locomotion学习，解耦风格保真与地形适应，直接对应核心研究方向。
- 📄 [arXiv](https://arxiv.org/abs/2604.16440) | 📥 [PDF](https://arxiv.org/pdf/2604.16440.pdf)

---

### 3. Environment-Adaptive Solid-State LiDAR-Inertial Odometry
- **Score:** 75
- **Categories:** cs.RO
- **Abstract:** Solid-state LiDAR-inertial SLAM has attracted significant attention due to its advantages in speed and robustness. However, achieving accurate mapping in extreme environments remains challenging due to severe geometric degeneracy and unreliable observations, which often lead to ill-conditioned optimization and map inconsistencies.
- **AI 点评:** 固态LiDAR-惯性里程计，针对极端退化环境的状态估计与建图，直接支持移动机器人导航与状态估计需求。
- 📄 [arXiv](https://arxiv.org/abs/2604.15864) | 📥 [PDF](https://arxiv.org/pdf/2604.15864.pdf)

---

### 4. Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
- **Score:** 67
- **Categories:** cs.RO
- **Abstract:** Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from...
- **AI 点评:** 全身人形机器人运动控制框架，结合扩散模型运动生成与RL追踪器实现地形感知适应，在Unitree G1上成功部署，与研究方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2604.17335) | 📥 [PDF](https://arxiv.org/pdf/2604.17335.pdf)

---

### 5. GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow
- **Score:** 54
- **Categories:** cs.RO, cs.CV
- **Venue:** RA-L
- **Abstract:** Gaussian splatting has recently gained traction as a compelling map representation for SLAM systems, enabling dense and photo-realistic scene modeling. However, its application to monocular SLAM remains challenging due to the lack of reliable geometric cues from monocular input. Without geometric supervision, mapping or tracking could fall in local-minima, resulting in structural degeneracies and inaccuracies.
- **AI 点评:** 单目GaussianSplatting SLAM系统，光流引导的位姿估计与建图，对移动机器人导航感知有一定参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2604.15612) | 📥 [PDF](https://arxiv.org/pdf/2604.15612.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **A Survey of Spatial Memory Representations for Efficient Robot Navigation** (Score: 49) [CVPR] [Link](https://arxiv.org/abs/2604.16482)
- **A Hamilton-Jacobi Reachability-Guided Search Framework for Efficient and Safe Indoor Planar Robot Navigation** (Score: 46) [Link](https://arxiv.org/abs/2604.17679)
- **Enhancing Glass Surface Reconstruction via Depth Prior for Robot Navigation** (Score: 46) [Link](https://arxiv.org/abs/2604.18336)
- **Enhancing Glass Surface Reconstruction via Depth Prior for Robot Navigation** (Score: 46) [Link](https://arxiv.org/abs/2604.18336v1)
- **Relative State Estimation using Event-Based Propeller Sensing** (Score: 43) [Link](https://arxiv.org/abs/2604.18289)
- **Relative State Estimation using Event-Based Propeller Sensing** (Score: 41) [Link](https://arxiv.org/abs/2604.18289v1)
- **LiDAR-based Crowd Navigation with Visible Edge Group Representation** (Score: 39) [Link](https://arxiv.org/abs/2604.16741)
- **Bounded Ratio Reinforcement Learning** (Score: 35) [Link](https://arxiv.org/abs/2604.18578v1)
- **From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation** (Score: 35) [Link](https://arxiv.org/abs/2604.15805)
- **Novel Algorithms for Smoothly Differentiable and Efficiently Vectorizable Contact Manifold Construction** (Score: 35) [ICRA] [Link](https://arxiv.org/abs/2604.17538)

## 📊 今日统计
- 总抓取: 636 篇 | 通过初筛: 131 篇 | 精选: 5 篇 (含 LLM 精筛)
