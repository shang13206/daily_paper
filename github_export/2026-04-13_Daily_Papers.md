# 🤖 具身智能/机器人学术日报 (2026-04-13)

## 🏆 精选论文 (Top 5)

### 1. SafeMind: A Risk-Aware Differentiable Control Framework for Adaptive and Safe Quadruped Locomotion
- **Score:** 72
- **Categories:** cs.AI, cs.RO
- **Abstract:** Learning-based quadruped controllers achieve impressive agility but typically lack formal safety guarantees under model uncertainty, perception noise, and unstructured contact conditions. We introduce SafeMind, a differentiable stochastic safety-control framework that unifies probabilistic Control Barrier Functions with semantic context understanding and meta-adaptive risk calibration.
- **AI 点评:** 为四足机器人（Unitree A1/ANYmal C）设计可微随机CBF安全控制框架，在12种地形上实现实机部署，与四足locomotion、terrain adaptation和安全控制高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.09474) | 📥 [PDF](https://arxiv.org/pdf/2604.09474.pdf)

---

### 2. Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning
- **Score:** 69
- **Categories:** cs.RO, cs.LG
- **Abstract:** World models promise a paradigm shift in robotics, where an agent learns the underlying physics of its environment once to enable efficient planning and behavior learning. However, current world models are often hardware-locked specialists: a model trained on a Boston Dynamics Spot robot fails catastrophically on a Unitree Go1 due to the mismatch in kinematic and dynamic properties, as the model overfits to specific embodiment constraints rather than capturing the universal locomotion dynamics.
- **AI 点评:** 提出跨形态四足机器人世界模型(QWM)，通过显式形态条件化实现零样本跨机器人泛化locomotion，与四足运动控制和sim-to-real核心研究方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2604.08780) | 📥 [PDF](https://arxiv.org/pdf/2604.08780.pdf)

---

### 3. Incremental Semantics-Aided Meshing from LiDAR-Inertial Odometry and RGB Direct Label Transfer
- **Score:** 45
- **Categories:** cs.CV, cs.RO
- **Abstract:** Geometric high-fidelity mesh reconstruction from LiDAR-inertial scans remains challenging in large, complex indoor environments -- such as cultural buildings -- where point cloud sparsity, geometric drift, and fixed fusion parameters produce holes, over-smoothing, and spurious surfaces at structural boundaries. We propose a modular, incremental RGB+LiDAR pipeline that generates incremental semantics-aided high-quality meshes from indoor scans through scan frame-based direct label transfer.
- **AI 点评:** 基于LiDAR-惯性里程计的增量语义网格重建pipeline，与SLAM和地图构建有关联，但主要面向室内场景重建而非机器人运动控制或导航部署。
- 📄 [arXiv](https://arxiv.org/abs/2604.09478) | 📥 [PDF](https://arxiv.org/pdf/2604.09478.pdf)

---

### 4. Sim-to-Real Transfer for Muscle-Actuated Robots via Generalized Actuator Networks
- **Score:** 42
- **Categories:** cs.RO, cs.LG
- **Abstract:** Tendon drives paired with soft muscle actuation enable faster and safer robots while potentially accelerating skill acquisition. Still, these systems are rarely used in practice due to inherent nonlinearities, friction, and hysteresis, which complicate modeling and control. So far, these challenges have hindered policy transfer from simulation to real systems.
- **AI 点评:** 肌肉驱动机械臂的sim-to-real迁移，提出广义执行器网络解决非线性建模问题，方法与系统辨识相关，但聚焦于机械臂manipulation而非移动/足式机器人。
- 📄 [arXiv](https://arxiv.org/abs/2604.09487) | 📥 [PDF](https://arxiv.org/pdf/2604.09487.pdf)

---

### 5. Accelerating Transformer-Based Monocular SLAM via Geometric Utility Scoring
- **Score:** 41
- **Categories:** cs.AI, cs.CV, cs.RO
- **Abstract:** Geometric Foundation Models (GFMs) have recently advanced monocular SLAM by providing robust, calibration-free 3D priors. However, deploying these models on dense video streams introduces significant computational redundancy. Current GFM-based SLAM systems typically rely on post hoc keyframe selection. Because of this, they must perform expensive dense geometric decoding simply to determine whether a frame contains novel geometry, resulting in late rejection and wasted computation.
- **AI 点评:** 面向单目SLAM的帧门控加速方法，提升SLAM吞吐量和效率，与移动机器人导航感知有一定关联，但非locomotion核心方向。
- 📄 [arXiv](https://arxiv.org/abs/2604.08718) | 📥 [PDF](https://arxiv.org/pdf/2604.08718.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Physics-Informed Reinforcement Learning of Spatial Density Velocity Potentials for Map-Free Racing** (Score: 36) [Link](https://arxiv.org/abs/2604.09499)

## 📊 今日统计
- 总抓取: 209 篇 | 通过初筛: 36 篇 | 精选: 5 篇 (含 LLM 精筛)
