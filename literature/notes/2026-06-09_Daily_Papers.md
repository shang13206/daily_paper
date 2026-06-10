# 🤖 具身智能/机器人学术日报 (2026-06-09)

## 🏆 精选论文 (Top 5)

### 1. Safe Polytope-in-Polytope Motion Planning and Control with Control Barrier Functions
- **Score:** 74
- **Categories:** cs.RO
- **Abstract:** Autonomous mobile robots operating in tight environments require motion planning frameworks that account for the physical footprint of the robot. Simplifying the geometry to a point or a circle is conservative and discards information needed to successfully and safely traverse narrow passages. This work proposes a safe local motion planning and control method that guarantees that a polytopic robot footprint stays inside a continuously updated convex free-space region.
- **AI 点评:** 面向移动机器人的实时局部规划与CBF控制，含LiDAR/栅格感知和硬件验证，和导航避障部署高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.09719v1) | 📥 [PDF](https://arxiv.org/pdf/2606.09719v1)

---

### 2. VGP-Nav: Metric-Aware Visual Geometric Perception for Robot Navigation
- **Score:** 69
- **Categories:** cs.RO
- **Abstract:** Reliable robotic navigation necessitates the seamless integration of accurate global localization and dense, metric-consistent obstacle perception. A common strategy to achieve these capabilities involves integrating diverse sensing modalities: cameras offer rich visual features for localization, while active sensors like LiDAR provide direct metric measurements. However, such multi-sensor configurations necessitate complex spatial-temporal calibration and increase deployment overhead.
- **AI 点评:** 单目视觉同时支持尺度一致定位和障碍感知并部署到移动机器人，直接契合导航、感知-规划耦合与实机部署方向。
- 📄 [arXiv](https://arxiv.org/abs/2606.09268v1) | 📥 [PDF](https://arxiv.org/pdf/2606.09268v1)

---

### 3. PTDL:Multi-Terrain Fall Recovery via Phase-Terrain Decoupled Learning
- **Score:** 60
- **Categories:** cs.RO
- **Abstract:** Humanoid robots can fall on slopes, gravel, and uneven ground in unstructured environments. We target integrated fall recovery and locomotion: rebuilding balance from a fallen state using proprioception alone and resuming velocity-commanded walking at the fall site. Prior methods often stop at quasi-static rise, neglect the post-fall ground-contact phase, or, when trained on mixed terrains without separating recovery and locomotion phases or per-surface constraints, collapse to a single compromi...
- **AI 点评:** 直接针对人形机器人多地形跌倒恢复到行走的端到端本体感知策略，涵盖地形适应、硬件部署和locomotion学习，相关性很高。
- 📄 [arXiv](https://arxiv.org/abs/2606.08922v1) | 📥 [PDF](https://arxiv.org/pdf/2606.08922v1)

---

### 4. Dual Quaternion-Based Unscented Kalman Filter with Visual Inertial Odometry for Navigation in GPS-Denied Environments
- **Score:** 59
- **Categories:** cs.RO, eess.SY
- **Abstract:** Reliable navigation in GPS-denied environments remains a fundamental challenge in robotics, aerospace, and autonomous vehicle applications. This paper presents a Dual Quaternion-Based Unscented Kalman Filter (DQUKF) equipped with a Visual Inertial Odometry (VIO) algorithm for accurate state estimation enabling navigation in GPS denied locations.
- **AI 点评:** VIO与UKF状态估计直接服务GPS拒止导航，虽非腿足 locomotion，但与机器人导航/部署状态估计高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.09292v1) | 📥 [PDF](https://arxiv.org/pdf/2606.09292v1)

---

### 5. VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands
- **Score:** 58
- **Categories:** cs.RO
- **Abstract:** Humanoid robots hold immense potential for real-world assistance, yet agile interaction with objects in unstructured environments demands tightly coupled whole-body coordination. Despite recent advancements, current controllers face a critical deployment gap. They rely heavily on dense reference trajectories and perfect state observability, which inherently limits physical generalization.
- **AI 点评:** 面向人形机器人的视觉引导全身控制与真实部署，包含深度感知、历史本体感知和策略蒸馏，和legged whole-body control高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.09286v1) | 📥 [PDF](https://arxiv.org/pdf/2606.09286v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes** (Score: 51) [Link](https://arxiv.org/abs/2606.08744v1)
- **HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning** (Score: 50) [Link](https://arxiv.org/abs/2606.08610v1)
- **Efficient Minimal Solvers for Relative Pose Estimation in Autonomous Driving Applications** (Score: 49) [Link](https://arxiv.org/abs/2606.09569v1)
- **Efficient Minimal Solvers for Visual-Inertial Relative Pose Estimation in Multi-Camera Systems** (Score: 49) [Link](https://arxiv.org/abs/2606.09477v1)
- **MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry** (Score: 49) [Link](https://arxiv.org/abs/2606.09355v1)
- **IR-SIM: A Lightweight Skill-Native Simulator for Navigation, Learning, and Benchmarking** (Score: 46) [Link](https://arxiv.org/abs/2606.08729v1)
- **OASIS: From Simulation Data Collection to Real-World Humanoid Loco-Manipulation** (Score: 46) [Link](https://arxiv.org/abs/2606.08548v1)
- **Geometry-Aware Fisheye-LiDAR Fusion for Robust 3D Object Detection in Low-Overlap Setups** (Score: 45) [RA-L] [Link](https://arxiv.org/abs/2606.08844v1)
- **Language as a Sensor: Calibrated Spatial Belief Estimation in 3D Scenes from Natural Language** (Score: 45) [Link](https://arxiv.org/abs/2606.08666v1)
- **Towards End to End Motion Planning and Execution for Autonomous Underwater Vehicles Using Reinforcement Learning** (Score: 45) [Link](https://arxiv.org/abs/2606.08513v1)
- **Autonomous Obstacle Removal for Excavators through Policy Learning with Particle Simulation** (Score: 43) [Link](https://arxiv.org/abs/2606.09183v1)
- **SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning** (Score: 43) [Link](https://arxiv.org/abs/2606.08992v1)
- **Autonomous Aerial Manipulation via Contextual Contrastive Meta Reinforcement Learning** (Score: 38) [Link](https://arxiv.org/abs/2606.08533v1)
- **Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video** (Score: 38) [Link](https://arxiv.org/abs/2606.08828v1)
- **Trajectory Optimization in Single and Dual-UAV Bearing-Only Target Localization** (Score: 35) [Link](https://arxiv.org/abs/2606.09188v1)

## 📊 今日统计
- 总抓取: 561 篇 | 通过初筛: 84 篇 | 精选: 5 篇 (含 LLM 精筛)
