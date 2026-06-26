# 🤖 具身智能/机器人学术日报 (2026-06-25)

## 🏆 精选论文 (Top 5)

### 1. Ordinal Neural Collapse as a Representation Prior for Visual Navigation
- **Score:** 76
- **Categories:** cs.CV, cs.RO
- **Abstract:** Learning robust navigation policies directly from visual observations remains a fundamental challenge in vision-based robotic navigation. In end-to-end imitation learning approaches, the visual encoder and action decoder are jointly optimized using a single action loss, which provides only an indirect supervisory signal to the encoder. This indirect supervision frequently results in the encoder learning ambiguous, action-agnostic representations.
- **AI 点评:** 直接面向视觉机器人导航策略学习，并在仿真和真实场景验证，感知与控制耦合明确。
- 📄 [arXiv](https://arxiv.org/abs/2606.26839v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26839v1)

---

### 2. A Closed-Form 4-DoF Inter-Robot Pose Estimator using Bearing-only Measurements
- **Score:** 65
- **Categories:** cs.RO
- **Abstract:** Bearing-odometry-based cooperative localization has attracted increasing research interest due to its minimal infrastructure requirements, low communication bandwidth and broad applicability in complex environments. However, existing 6-DoF approaches still face challenges in rapidly obtaining accurate and reliable inter-robot pose estimation, as the system is prone to observability degeneracy under specific motion patterns.
- **AI 点评:** 轴承量测下的协同定位和机器人相对位姿估计直接服务多机器人导航与状态估计，相关性很高。
- 📄 [arXiv](https://arxiv.org/abs/2606.26616v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26616v1)

---

### 3. UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping
- **Score:** 65
- **Categories:** cs.RO, cs.SI
- **Venue:** RA-L
- **Abstract:** Large-scale point cloud maps are essential for robotics and spatial intelligence tasks. UAVs provide an efficient means for large-scale map acquisition; however, due to limited flight endurance and onboard storage, mapping a large-scale scene within a single flight remains difficult. Existing multi-session map merging methods can extend the mapping range, yet in UAV scenarios they still struggle to simultaneously suppress long-range drift and preserve local geometric accuracy.
- **AI 点评:** UAV多会话点云建图、RTK约束和因子图优化与机器人SLAM/地图构建高度相关，但不涉及足式运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2606.26928v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26928v1)

---

### 4. BOWConnect: Parallel Bayesian Optimization over Windows with Learned Local Cost Maps for Sample-Efficient Kinodynamic Motion Planning
- **Score:** 58
- **Categories:** cs.RO
- **Venue:** IROS
- **Abstract:** This paper presents BOWConnect, a bidirectional parallel kinodynamic motion planner that addresses three fundamental limitations of existing sampling-based methods: sample inefficiency in high-dimensional state spaces, unreliable cost heuristics under dynamic constraints, and poor performance in narrow passage environments.
- **AI 点评:** 面向地面车和四旋翼的实时 kinodynamic motion planning 与碰撞规避，和机器人导航规划高度相关但非腿式运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2606.27292v1) | 📥 [PDF](https://arxiv.org/pdf/2606.27292v1)

---

### 5. OctoSense: Self-Supervised Learning for Multimodal Robot Perception
- **Score:** 58
- **Categories:** cs.CV, cs.RO
- **Abstract:** We present OctoSense, an open-source sensor platform with stereo RGB and event cameras, LiDAR, a thermal camera, an inertial measurement unit, RTK-corrected global positioning system, and proprioception (CAN bus data from a car, and joint angles for a quadruped robot). The eponymous OctoSense dataset contains 59 hours of time-synchronized driving data across different types of environments at different times of the day, including situations with highly degraded sensors.
- **AI 点评:** 多模态机器人感知数据与自监督表示直接服务深度、语义、里程计等移动机器人状态估计与导航任务，且含四足传感数据。
- 📄 [arXiv](https://arxiv.org/abs/2606.27317v1) | 📥 [PDF](https://arxiv.org/pdf/2606.27317v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views** (Score: 48) [IROS] [Link](https://arxiv.org/abs/2606.27071v1)
- **IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control** (Score: 46) [Link](https://arxiv.org/abs/2606.26575v1)
- **Bridging Performance and Generalization in Reinforcement Learning for Agile Flight** (Score: 45) [Link](https://arxiv.org/abs/2606.27348v1)

## 📊 今日统计
- 总抓取: 296 篇 | 通过初筛: 51 篇 | 精选: 5 篇 (含 LLM 精筛)
