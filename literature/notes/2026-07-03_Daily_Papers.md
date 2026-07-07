# 🤖 具身智能/机器人学术日报 (2026-07-03)

## 🏆 精选论文 (Top 5)

### 1. ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion
- **Score:** 73
- **Categories:** cs.LG, cs.RO
- **Abstract:** In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states.
- **AI 点评:** 直接研究人形 locomotion 的扰动鲁棒控制、接触与动力学先验，和核心 locomotion policy learning 高度匹配。
- 📄 [arXiv](https://arxiv.org/abs/2607.03454v1) | 📥 [PDF](https://arxiv.org/pdf/2607.03454v1)

---

### 2. E-TraMamba: A New Paradigm for Efficient Long-Term 3D Feature Tracking with Event Cameras
- **Score:** 64
- **Categories:** cs.CV, cs.RO
- **Abstract:** Event-based 3D tracking enables low-latency and high-speed perception, while existing CNN- and Transformer-based trackers struggle to capture long-range spatiotemporal dependencies in sparse, noisy event streams, especially under real-time and efficiency constraints. To address these challenges, we present E-TraMamba, the first Mamba-based framework for 3D feature tracking on event data.
- **AI 点评:** 事件相机3D特征跟踪明确服务低延迟视觉里程计、SLAM和机器人感知，和导航状态估计较契合。
- 📄 [arXiv](https://arxiv.org/abs/2607.02866v1) | 📥 [PDF](https://arxiv.org/pdf/2607.02866v1)

---

### 3. Derivations of Error-State Kalman Filter Kinematics for Globally Applicable Aided Inertial Navigation Systems
- **Score:** 49
- **Categories:** cs.RO, eess.SY
- **Abstract:** Global navigation systems require state estimation algorithms that handle Earth's curvature, Earth's rotation, and gravitational variations. These factors can typically be neglected in local navigation algorithms for robots, drones, etc. In classical error-state Kalman Filtering (ESKF) the error state dynamics are trajectory-dependent. Invariant ESKFs utilize Lie Group symmetries to represent the error, which can render error propagation trajectory-independent for group-affine systems.
- **AI 点评:** 惯性导航与ESKF状态估计对机器人定位有较强参考价值，但偏公式综述且非移动机器人部署导向。
- 📄 [arXiv](https://arxiv.org/abs/2607.03211v1) | 📥 [PDF](https://arxiv.org/pdf/2607.03211v1)

---

### 4. High-Precision Formation Control for Heterogeneous Multi-Robot Systems via Hierarchical Hybrid Physics-Informed Deep Reinforcement Learning
- **Score:** 49
- **Categories:** cs.RO
- **Abstract:** Existing classical control methods commonly require precise models and struggle to cope with model uncertainties and external disturbances, while end-to-end reinforcement learning (RL) approaches suffer from low sample efficiency and poor convergence. To overcome these challenges, this paper proposes a hierarchical hybrid physics-informed deep reinforcement learning (HHy-PIDRL) framework, aiming to realize high-precision, highly responsive formation control for heterogeneous multi-robot systems...
- **AI 点评:** 异构多机器人编队控制结合导航、DRL 和物理控制，和机器人运动控制较相关但非足式 locomotion 核心。
- 📄 [arXiv](https://arxiv.org/abs/2607.03512v1) | 📥 [PDF](https://arxiv.org/pdf/2607.03512v1)

---

### 5. Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion
- **Score:** 44
- **Categories:** cs.RO
- **Abstract:** Efficient flapping propulsion hinges on operating within a narrow Strouhal number window, a principle nature has converged upon for maximum thrust-to-power ratio. We translate this bioinspired empirical rule into real-time control, demonstrating it on an autonomous underwater vehicle driven by four soft fins.
- **AI 点评:** 涉及真实机器人MPC与高效运动控制，但平台是水下多鳍机器人，和轮足/四足locomotion有方法相关性但不直接。
- 📄 [arXiv](https://arxiv.org/abs/2607.03216v1) | 📥 [PDF](https://arxiv.org/pdf/2607.03216v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Continuous-Time Gaussian Belief Trees for Motion Planning** (Score: 43) [Link](https://arxiv.org/abs/2607.02884v1)
- **Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations** (Score: 40) [Link](https://arxiv.org/abs/2607.03146v1)
- **iVISION-2DCD: A Long-Term Change Detection Dataset for Large-Scale Outdoor Construction Monitoring** (Score: 38) [ICRA] [Link](https://arxiv.org/abs/2607.03553v1)

## 📊 今日统计
- 总抓取: 276 篇 | 通过初筛: 46 篇 | 精选: 5 篇 (含 LLM 精筛)
