# 🤖 具身智能/机器人学术日报 (2026-04-10)

## 🏆 精选论文 (Top 5)

### 1. SafeMind: A Risk-Aware Differentiable Control Framework for Adaptive and Safe Quadruped Locomotion
- **Score:** 76
- **Categories:** cs.AI, cs.RO
- **Abstract:** Learning-based quadruped controllers achieve impressive agility but typically lack formal safety guarantees under model uncertainty, perception noise, and unstructured contact conditions. We introduce SafeMind, a differentiable stochastic safety-control framework that unifies probabilistic Control Barrier Functions with semantic context understanding and meta-adaptive risk calibration.
- **AI 点评:** SafeMind在四足机器人（Unitree A1/ANYmal C）上实现概率CBF安全控制，覆盖多地形、不确定性建模与实机200Hz部署，与研究核心高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2604.09474v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09474v1)

---

### 2. Incremental Semantics-Aided Meshing from LiDAR-Inertial Odometry and RGB Direct Label Transfer
- **Score:** 53
- **Categories:** cs.CV, cs.RO
- **Abstract:** Geometric high-fidelity mesh reconstruction from LiDAR-inertial scans remains challenging in large, complex indoor environments -- such as cultural buildings -- where point cloud sparsity, geometric drift, and fixed fusion parameters produce holes, over-smoothing, and spurious surfaces at structural boundaries. We propose a modular, incremental RGB+LiDAR pipeline that generates incremental semantics-aided high-quality meshes from indoor scans through scan frame-based direct label transfer.
- **AI 点评:** LiDAR-Inertial里程计结合语义网格重建，直接服务于移动机器人导航与建图，与SLAM/感知模块有较强相关性。
- 📄 [arXiv](https://arxiv.org/abs/2604.09478v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09478v1)

---

### 3. Sim-to-Real Transfer for Muscle-Actuated Robots via Generalized Actuator Networks
- **Score:** 40
- **Categories:** cs.LG, cs.RO
- **Abstract:** Tendon drives paired with soft muscle actuation enable faster and safer robots while potentially accelerating skill acquisition. Still, these systems are rarely used in practice due to inherent nonlinearities, friction, and hysteresis, which complicate modeling and control. So far, these challenges have hindered policy transfer from simulation to real systems.
- **AI 点评:** 肌腱驱动机械臂的sim-to-real方法（GeAN）有一定迁移学习参考价值，但属于manipulation领域而非足式运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2604.09487v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09487v1)

---

### 4. Physics-Informed Reinforcement Learning of Spatial Density Velocity Potentials for Map-Free Racing
- **Score:** 33
- **Categories:** cs.RO
- **Abstract:** Autonomous racing without prebuilt maps is a grand challenge for embedded robotics that requires kinodynamic planning from instantaneous sensor data at the acceleration and tire friction limits. Out-Of-Distribution (OOD) generalization to various racetrack configurations utilizes Machine Learning (ML) to encode the mathematical relation between sensor data and vehicle actuation for end-to-end control, with implicit localization.
- **AI 点评:** 自动驾驶赛车的sim-to-real迁移与物理信息RL有方法论参考价值，但聚焦轮式车辆而非足式机器人locomotion。
- 📄 [arXiv](https://arxiv.org/abs/2604.09499v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09499v1)

---

### 5. Towards Lifelong Aerial Autonomy: Geometric Memory Management for Continual Visual Place Recognition in Dynamic Environments
- **Score:** 30
- **Categories:** cs.CV, cs.LG, cs.RO
- **Abstract:** Robust geo-localization in changing environmental conditions is critical for long-term aerial autonomy. While visual place recognition (VPR) models perform well when airborne views match the training domain, adapting them to shifting distributions during sequential missions triggers catastrophic forgetting. Existing continual learning (CL) methods often fail here because geographic features exhibit severe intra-class variations.
- **AI 点评:** 面向无人机的视觉地点识别持续学习，与导航/定位有一定相关性，但聚焦空中平台而非地面/腿足机器人，相关性较低。
- 📄 [arXiv](https://arxiv.org/abs/2604.09038v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09038v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 271 篇 | 通过初筛: 45 篇 | 精选: 5 篇 (含 LLM 精筛)
