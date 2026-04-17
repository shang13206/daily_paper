# 🤖 具身智能/机器人学术日报 (2026-04-16)

## 🏆 精选论文 (Top 5)

### 1. RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM
- **Score:** 72
- **Categories:** cs.RO
- **Abstract:** Real-time 3D Gaussian splatting (3DGS)-based Simultaneous Localization and Mapping (SLAM) in large-scale real-world environments remains challenging, as existing methods often struggle to jointly achieve low-latency pose estimation, 3D Gaussian reconstruction in step with incoming sensor streams, and long-term global consistency.
- **AI 点评:** 紧耦合LiDAR-Inertial-Visual 3DGS SLAM系统，实时位姿估计与大场景建图，直接支持移动机器人状态估计与导航需求。
- 📄 [arXiv](https://arxiv.org/abs/2604.12942v1) | 📥 [PDF](https://arxiv.org/pdf/2604.12942v1)

---

### 2. RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment
- **Score:** 66
- **Categories:** cs.CV, cs.RO
- **Abstract:** Radar is more resilient to adverse weather and lighting conditions than visual and Lidar simultaneous localization and mapping (SLAM). However, most radar SLAM pipelines still rely heavily on frame-to-frame odometry, which leads to substantial drift. While loop closure can correct long-term errors, it requires revisiting places and relies on robust place recognition.
- **AI 点评:** 雷达-惯性里程计结合高斯泼溅的BA框架，显著减少位姿漂移，与移动机器人SLAM/状态估计方向中度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.13492v1) | 📥 [PDF](https://arxiv.org/pdf/2604.13492v1)

---

### 3. E2E-Fly: An Integrated Training-to-Deployment System for End-to-End Quadrotor Autonomy
- **Score:** 63
- **Categories:** cs.RO
- **Abstract:** Training and transferring learning-based policies for quadrotors from simulation to reality remains challenging due to inefficient visual rendering, physical modeling inaccuracies, unmodeled sensor discrepancies, and the absence of a unified platform integrating differentiable physics learning into end-to-end training.
- **AI 点评:** 四旋翼端到端自主控制系统，涵盖sim-to-real、domain randomization、系统辨识等与研究高度相关的方法论，但平台为四旋翼而非轮足/四足。
- 📄 [arXiv](https://arxiv.org/abs/2604.12916v1) | 📥 [PDF](https://arxiv.org/pdf/2604.12916v1)

---

### 4. GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments
- **Score:** 57
- **Categories:** cs.RO
- **Venue:** ICRA
- **Abstract:** Visual SLAM algorithms achieve significant improvements through the exploration of 3D Gaussian Splatting (3DGS) representations, particularly in generating high-fidelity dense maps. However, they depend on a static environment assumption and experience significant performance degradation in dynamic environments.
- **AI 点评:** 动态环境下的单目3DGS SLAM，面向移动机器人定位与建图，但未明确针对足式/轮足机器人，与导航感知方向中等相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.12837v1) | 📥 [PDF](https://arxiv.org/pdf/2604.12837v1)

---

### 5. UNRIO: Uncertainty-Aware Velocity Learning for Radar-Inertial Odometry
- **Score:** 50
- **Categories:** cs.RO
- **Abstract:** We present UNRIO, an uncertainty-aware radar-inertial odometry system that estimates ego-velocity directly from raw mmWave radar IQ signals rather than processed point clouds. Existing radar-inertial odometry methods rely on handcrafted signal processing pipelines that discard latent information in the raw spectrum and require careful parameter tuning.
- **AI 点评:** 毫米波雷达惯性里程计系统，直接服务于移动机器人状态估计与导航，与SLAM/视觉里程计方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.13584v1) | 📥 [PDF](https://arxiv.org/pdf/2604.13584v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning** (Score: 47) [Link](https://arxiv.org/abs/2604.13192v1)
- **Geometric Context Transformer for Streaming 3D Reconstruction** (Score: 44) [Link](https://arxiv.org/abs/2604.14141v1)
- **PAINT: Partner-Agnostic Intent-Aware Cooperative Transport with Legged Robots** (Score: 44) [Link](https://arxiv.org/abs/2604.12852v1)
- **Reliability-Guided Depth Fusion for Glare-Resilient Navigation Costmaps** (Score: 44) [Link](https://arxiv.org/abs/2604.12753v1)
- **Asymptotically Stable Gait Generation and Instantaneous Walkability Determination for Planar Almost Linear Biped with Knees** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2604.12274v1)
- **Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots** (Score: 41) [Link](https://arxiv.org/abs/2604.12909v1)
- **Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control** (Score: 41) [Link](https://arxiv.org/abs/2604.13323v1)
- **D-BDM: A Direct and Efficient Boundary-Based Occupancy Grid Mapping Framework for LiDARs** (Score: 39) [Link](https://arxiv.org/abs/2604.12436v1)
- **Neuromorphic Spiking Ring Attractor for Proprioceptive Joint-State Estimation** (Score: 37) [Link](https://arxiv.org/abs/2604.14021v1)

## 📊 今日统计
- 总抓取: 1354 篇 | 通过初筛: 159 篇 | 精选: 5 篇 (含 LLM 精筛)
