# 🤖 具身智能/机器人学术日报 (2026-06-24)

## 🏆 精选论文 (Top 5)

### 1. WaveForward: An Omnidirectional Passive Wheeled Quadruped Robot with Casters
- **Score:** 85
- **Categories:** cs.RO
- **Abstract:** Wheeled-legged robots possess both agile mobility for traversing complex terrains and high efficiency, making them suitable for long-distance transportation applications. Conventional actuated wheeled robots require specialized hardware and electrical design due to the incorporation of wheel components. We propose a novel and low-cost passive wheeled legged robot equipped with standard casters on each leg to obtain omnidirectional mobility.
- **AI 点评:** 被动轮足四足机器人、强化学习控制和全向运动能力，几乎完全贴合OmniBot轮足locomotion方向。
- 📄 [arXiv](https://arxiv.org/abs/2606.25299v1) | 📥 [PDF](https://arxiv.org/pdf/2606.25299v1)

---

### 2. StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots
- **Score:** 78
- **Categories:** cs.RO
- **Abstract:** Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains.
- **AI 点评:** 四足机器人感知耦合强化学习、极端地形适应、深度仿真建模和Go2实机零样本部署高度契合。
- 📄 [arXiv](https://arxiv.org/abs/2606.25765v1) | 📥 [PDF](https://arxiv.org/pdf/2606.25765v1)

---

### 3. OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos
- **Score:** 72
- **Categories:** cs.CV
- **Venue:** ECCV
- **Abstract:** Continuous 6-DoF pose estimation is essential for autonomous UAV operations. Yet, existing visual odometry and SLAM methods accumulate drift and yield only relative, up-to-scale trajectories. Single-frame geo-localization, in turn, discards temporal continuity and remains too slow for real-time use. We present OrthoTrack, a training-free system that estimates continuous 6-DoF UAV trajectories using only publicly available orthophotos and surface models as a map prior.
- **AI 点评:** 面向UAV的实时6DoF轨迹估计和地图锚定视觉里程计，和机器人导航/状态估计方向较相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.25245v1) | 📥 [PDF](https://arxiv.org/pdf/2606.25245v1)

---

### 4. Event-Adaptive Motion Planning with Distilled Vision-Language Model in Safety-Critical Situations
- **Score:** 71
- **Categories:** cs.RO
- **Venue:** IROS
- **Abstract:** Robot navigation in safety-critical scenarios faces significant challenges from unforeseen semantic events, where collisions arise primarily from the unpredictable behaviors of dynamic agents rather than unseen objects. While large vision-language models (VLMs) offer remarkable capabilities in commonsense reasoning, frequently invoking them within the continuous control loop introduces severe computational latency, fundamentally destabilizing physical execution.
- **AI 点评:** 将VLM语义事件检测与MPC运动规划结合，面向安全关键机器人导航，相关性较高但偏语义规划。
- 📄 [arXiv](https://arxiv.org/abs/2606.25629v1) | 📥 [PDF](https://arxiv.org/pdf/2606.25629v1)

---

### 5. MAPL: Multi-Objective Preference Learning for Robot Locomotion
- **Score:** 71
- **Categories:** cs.RO
- **Abstract:** Reward design remains a major bottleneck in reinforcement learning for robot locomotion, where successful policies often depend on carefully tuned, task-specific reward functions. Preference-based reinforcement learning offers an alternative, but existing LLM-based methods typically ask for a single overall judgment between behaviors, making it difficult to capture the multiple competing objectives that underlie high-quality locomotion.
- **AI 点评:** 直接针对四足机器人RL locomotion的奖励学习，和locomotion policy learning高度匹配。
- 📄 [arXiv](https://arxiv.org/abs/2606.25398v1) | 📥 [PDF](https://arxiv.org/pdf/2606.25398v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **SA-LIVO: Efficient LiDAR-Inertial-Visual Odometry with Subspace-Aware Degeneracy Handling** (Score: 68) [Link](https://arxiv.org/abs/2606.25699v1)
- **GROVE: Grounded Pedestrian Simulation via Natural Language for Interactive Social Robot Navigation** (Score: 64) [IROS] [Link](https://arxiv.org/abs/2606.25504v1)
- **MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework** (Score: 59) [Link](https://arxiv.org/abs/2606.25796v1)
- **Large-Scale Tunnel Air--Ground Collaboration With FLISP: Fast LiDAR-IMU Synchronized Path Planne** (Score: 58) [Link](https://arxiv.org/abs/2606.25393v1)
- **Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots** (Score: 56) [Link](https://arxiv.org/abs/2606.25706v1)
- **WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning** (Score: 53) [Link](https://arxiv.org/abs/2606.25591v1)
- **Delta-Position Estimation-Based IMU Odometry: A Comparison of MLP and Kolmogorov-Arnold Networks** (Score: 43) [Link](https://arxiv.org/abs/2606.25454v1)
- **1000 Rallies: An Event-Camera Dataset and Real-Time Learned Ball-State Estimation for Robotic Table Tennis** (Score: 38) [Link](https://arxiv.org/abs/2606.25620v1)
- **Beyond a Shadow of a Doubt: Close Proximity Geometry Reconstruction Using FMCW Radar Shadow Effects** (Score: 35) [Link](https://arxiv.org/abs/2606.25829v1)

## 📊 今日统计
- 总抓取: 199 篇 | 通过初筛: 38 篇 | 精选: 5 篇 (含 LLM 精筛)
