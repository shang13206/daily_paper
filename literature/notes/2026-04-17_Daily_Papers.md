# 🤖 具身智能/机器人学术日报 (2026-04-17)

## 🏆 精选论文 (Top 5)

### 1. BIEVR-LIO: Robust LiDAR-Inertial Odometry through Bump-Image-Enhanced Voxel Maps
- **Score:** 75
- **Categories:** cs.RO
- **Abstract:** Reliable odometry is essential for mobile robots as they increasingly enter more challenging environments, which often contain little information to constrain point cloud registration, resulting in degraded LiDAR-Inertial Odometry (LIO) accuracy or even divergence. To address this, we present BIEVR-LIO, a novel approach designed specifically to exploit subtle variations in the available geometry for improved robustness.
- **AI 点评:** 提出用于移动机器人的鲁棒LiDAR-惯性里程计方法，并明确展示了对机器人locomotion高程建图的下游应用，与导航感知方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.14421) | 📥 [PDF](https://arxiv.org/pdf/2604.14421.pdf)

---

### 2. RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM
- **Score:** 72
- **Categories:** cs.RO
- **Abstract:** Real-time 3D Gaussian splatting (3DGS)-based Simultaneous Localization and Mapping (SLAM) in large-scale real-world environments remains challenging, as existing methods often struggle to jointly achieve low-latency pose estimation, 3D Gaussian reconstruction in step with incoming sensor streams, and long-term global consistency.
- **AI 点评:** 实时LiDAR-惯性-视觉紧耦合3DGS SLAM系统，支持大规模户外场景的位姿估计与建图，直接服务于移动机器人导航与状态估计。
- 📄 [arXiv](https://arxiv.org/abs/2604.12942) | 📥 [PDF](https://arxiv.org/pdf/2604.12942.pdf)

---

### 3. RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment
- **Score:** 70
- **Categories:** cs.RO, cs.CV
- **Abstract:** Radar is more resilient to adverse weather and lighting conditions than visual and Lidar simultaneous localization and mapping (SLAM). However, most radar SLAM pipelines still rely heavily on frame-to-frame odometry, which leads to substantial drift. While loop closure can correct long-term errors, it requires revisiting places and relies on robust place recognition.
- **AI 点评:** 雷达-惯性里程计结合高斯泼溅做束调整，显著降低位姿漂移，直接服务于移动机器人SLAM与状态估计需求。
- 📄 [arXiv](https://arxiv.org/abs/2604.13492v1) | 📥 [PDF](https://arxiv.org/pdf/2604.13492v1)

---

### 4. Abstract Sim2Real through Approximate Information States
- **Score:** 69
- **Categories:** cs.RO
- **Abstract:** In recent years, reinforcement learning (RL) has shown remarkable success in robotics when a fast and accurate simulator is available for a given task. When using RL and simulation, more simulator realism is generally beneficial but becomes harder to obtain as robots are deployed in increasingly complex and widescale domains.
- **AI 点评:** 直接针对sim2real迁移的形式化方法，提出用真实数据修正抽象仿真器动力学，与Isaac Lab训练→实机部署路线高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.15289) | 📥 [PDF](https://arxiv.org/pdf/2604.15289.pdf)

---

### 5. CART: Context-Aware Terrain Adaptation using Temporal Sequence Selection for Legged Robots
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Animals in nature combine multiple modalities, such as sight and feel, to perceive terrain and develop an understanding of how to walk on uneven terrain in a stable manner. Similarly, legged robots need to develop their ability to stably walk on complex terrains by developing an understanding of the relationship between vision and proprioception.
- **AI 点评:** 在IsaacSim和真实ANYmal/SPOT机器人上验证的地形自适应高层控制器，融合本体感知与外感知实现复杂地形locomotion，与核心研究方向高度契合。
- 📄 [arXiv](https://arxiv.org/abs/2604.14344) | 📥 [PDF](https://arxiv.org/pdf/2604.14344.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **A Foot Resistive Force Model for Legged Locomotion on Muddy Terrains** (Score: 66) [Link](https://arxiv.org/abs/2604.12006)
- **Bipedal-Walking-Dynamics Model on Granular Terrains** (Score: 66) [ICRA] [Link](https://arxiv.org/abs/2604.11981)
- **RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment** (Score: 66) [Link](https://arxiv.org/abs/2604.13492)
- **E2E-Fly: An Integrated Training-to-Deployment System for End-to-End Quadrotor Autonomy** (Score: 63) [Link](https://arxiv.org/abs/2604.12916)
- **GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments** (Score: 63) [ICRA] [Link](https://arxiv.org/abs/2604.12837)
- **Switch: Learning Agile Skills Switching for Humanoid Robots** (Score: 59) [Link](https://arxiv.org/abs/2604.14834)
- **CT-VIR: Continuous-Time Visual-Inertial-Ranging Fusion for Indoor Localization with Sparse Anchors** (Score: 55) [Link](https://arxiv.org/abs/2604.14545)
- **Asymptotically Stable Gait Generation and Instantaneous Walkability Determination for Planar Almost Linear Biped with Knees** (Score: 54) [ICRA] [Link](https://arxiv.org/abs/2604.12274)
- **Reliability-Guided Depth Fusion for Glare-Resilient Navigation Costmaps** (Score: 54) [Link](https://arxiv.org/abs/2604.12753)
- **3DRO: Lidar-level SE(3) Direct Radar Odometry Using a 2D Imaging Radar and a Gyroscope** (Score: 53) [Link](https://arxiv.org/abs/2604.12027)
- **Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control** (Score: 53) [Link](https://arxiv.org/abs/2604.13323)
- **Keep It CALM: Toward Calibration-Free Kilometer-Level SLAM with Visual Geometry Foundation Models via an Assistant Eye** (Score: 47) [Link](https://arxiv.org/abs/2604.14795)
- **Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning** (Score: 47) [Link](https://arxiv.org/abs/2604.13192)
- **Uncertainty Guided Exploratory Trajectory Optimization for Sampling-Based Model Predictive Control** (Score: 47) [ICRA] [Link](https://arxiv.org/abs/2604.12149)
- **Geometric Context Transformer for Streaming 3D Reconstruction** (Score: 46) [Link](https://arxiv.org/abs/2604.14141v2)
- **CAVERS: Multimodal SLAM Data from a Natural Karstic Cave with Ground Truth Motion Capture** (Score: 45) [Link](https://arxiv.org/abs/2604.15052)
- **D-BDM: A Direct and Efficient Boundary-Based Occupancy Grid Mapping Framework for LiDARs** (Score: 45) [Link](https://arxiv.org/abs/2604.12436)
- **Dual Pose-Graph Semantic Localization for Vision-Based Autonomous Drone Racing** (Score: 45) [Link](https://arxiv.org/abs/2604.15168)
- **4D Radar Gaussian Modeling and Scan Matching with RCS** (Score: 44) [ICRA] [Link](https://arxiv.org/abs/2604.14868)
- **PAINT: Partner-Agnostic Intent-Aware Cooperative Transport with Legged Robots** (Score: 44) [Link](https://arxiv.org/abs/2604.12852)
- **UNRIO: Uncertainty-Aware Velocity Learning for Radar-Inertial Odometry** (Score: 44) [Link](https://arxiv.org/abs/2604.13584)
- **Graph Theoretical Outlier Rejection for 4D Radar Registration in Feature-Poor Environments** (Score: 41) [Link](https://arxiv.org/abs/2604.14857)
- **ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting** (Score: 38) [Link](https://arxiv.org/abs/2604.11992)
- **Capability-Aware Heterogeneous Control Barrier Functions for Decentralized Multi-Robot Safe Navigation** (Score: 37) [Link](https://arxiv.org/abs/2604.13245)
- **Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots** (Score: 37) [Link](https://arxiv.org/abs/2604.12909)

## 📊 今日统计
- 总抓取: 717 篇 | 通过初筛: 162 篇 | 精选: 5 篇 (含 LLM 精筛)
