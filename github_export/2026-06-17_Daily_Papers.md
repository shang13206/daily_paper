# 🤖 具身智能/机器人学术日报 (2026-06-17)

## 🏆 精选论文 (Top 5)

### 1. Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots
- **Score:** 90
- **Categories:** cs.RO, cs.CV
- **Abstract:** Autonomous navigation of quadrupedal robots in diverse environments fundamentally relies on resilient Simultaneous Localization and Mapping (SLAM). While visual-inertial SLAM has matured across wheeled, handheld, and aerial platforms, a critical evaluation gap remains regarding how hardware-level sensor configurations affect performance under the aggressive dynamics of legged locomotion.
- **AI 点评:** 系统评估四足机器人在剧烈运动下的多模态 SLAM 与传感器配置，对实机感知部署和导航设计高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.19067v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19067v1)

---

### 2. SRL: Combining SLIP Model and Reinforcement Learning for Agile Robotic Jumping
- **Score:** 84
- **Categories:** cs.RO
- **Abstract:** Robotic jumping is pivotal in applications such as search and rescue and logistics, where crossing obstacles and enhancing mobility efficiency are critical. The Spring-Loaded Inverted Pendulum (SLIP) model leverages simplified spring-mass dynamics that naturally encode biologically plausible hopping motions, yet its performance degrades on irregular terrain due to idealized assumptions regarding contact and joint dynamics.
- **AI 点评:** 结合 SLIP 与强化学习实现双足/四足跳跃，并包含 stair jumping、sim-to-sim 和 sim-to-real，和 OmniBot 运动控制选题非常贴近。
- 📄 [arXiv](https://arxiv.org/abs/2606.18625v1) | 📥 [PDF](https://arxiv.org/pdf/2606.18625v1)

---

### 3. FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry
- **Score:** 79
- **Categories:** cs.RO
- **Venue:** IROS
- **Abstract:** Robust state estimation and mapping in long-term, large-scale, and highly dynamic environments remains a key challenge in robotics. Existing LiDAR-Inertial-Visual Odometry (LIVO) systems achieve strong local accuracy but suffer from accumulated drift over long distances and may fail in geometrically degraded or textureless scenes.
- **AI 点评:** 多传感器LiDAR-惯性-视觉-GNSS融合里程计面向鲁棒状态估计和建图，对机器人导航与部署强相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.19190v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19190v1)

---

### 4. C-ARC: Continuous-Adaptive Range Clustering for Non-Repetitive LiDAR Sensors
- **Score:** 75
- **Categories:** cs.RO
- **Venue:** Robotics and Automation Letters
- **Abstract:** Real-time LiDAR clustering identifies structures in point clouds, which is an essential prerequisite for many mobile robotics algorithms. Current methods are mostly developed for repetitive mechanical LiDAR sensors. Recently, the use of non-repetitive LiDAR sensors is strongly increasing due to their small cost and form factor. Such non-repetitive Risley prism-based sensors violate two key assumptions of repetitive mechanical sensors: structured scan lines and well-defined frame boundaries.
- **AI 点评:** 针对非重复 LiDAR 的实时聚类可作为 SLAM、跟踪和移动机器人感知前端，对导航感知系统较相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.18948v1) | 📥 [PDF](https://arxiv.org/pdf/2606.18948v1)

---

### 5. ZiMPedance: Impedance-Aware ZMP Modeling and Control for Payload Carrying with Quadruped Robots
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Load transportation with quadruped robots is strongly affected by the dynamics of the physical interface between the robot and the load. Passive spring-based arms reduce weight and complexity compared to active manipulators, but their spring-damper dynamics can introduce oscillatory forces that degrade locomotion stability.
- **AI 点评:** 直接研究四足机器人负载搬运中的 ZMP/阻抗建模与 MPC 控制，强相关于 locomotion 稳定性和实机控制。
- 📄 [arXiv](https://arxiv.org/abs/2606.18883v1) | 📥 [PDF](https://arxiv.org/pdf/2606.18883v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Mobile Pedipulation for Object Sliding via Hierarchical Control on a Wheeled Bipedal Robot** (Score: 66) [Link](https://arxiv.org/abs/2606.19233v1)
- **Viking Hill Dataset: A Lidar-Radar-Camera Dataset for Detection and Segmentation in Forest Scenes** (Score: 63) [Link](https://arxiv.org/abs/2606.19154v1)
- **Monocular 3D Occupancy Perception for Robots on Sidewalks via Hybrid 2D-3D Learning** (Score: 56) [Link](https://arxiv.org/abs/2606.19122v1)
- **DNN Koopman-Based Deviation Compensation for UGV Path Tracking Control on Coupled Slope and Potholed Road** (Score: 55) [Link](https://arxiv.org/abs/2606.18630v1)
- **VISTA: Scale-Aware Visual Navigation via Action History Conditioning** (Score: 55) [Link](https://arxiv.org/abs/2606.17294)
- **Observability and Consistency Analysis for Visual-Inertial Navigation with Anchored Feature Parameterizations** (Score: 53) [IROS] [Link](https://arxiv.org/abs/2606.19307v1)
- **A Mixed-Reality Testbed for Autonomous Vehicles** (Score: 50) [Link](https://arxiv.org/abs/2606.19267v1)
- **TactSpace: Learning a Physics-enriched Shared Latent Space for Tactile Sim-to-Real Transfer** (Score: 47) [IROS] [Link](https://arxiv.org/abs/2606.18959v1)
- **Congestion-Aware Robot Tour Planning in Crowded Environments** (Score: 46) [IROS] [Link](https://arxiv.org/abs/2606.19031v1)
- **Leveraging Energy Features for Surface Classification with Deep Learning: A Comparative Analysis Across Three Independent Datasets** (Score: 46) [Link](https://arxiv.org/abs/2606.18698v1)
- **Constant Time-Delay Leader Following with Neural Networks and Invariant Extended Kalman Filters for Arbitrary Trajectories** (Score: 43) [Link](https://arxiv.org/abs/2606.19227v1)
- **Technical Report for ICRA 2026 GOOSE 2D Fine-Grained Semantic Segmentation Challenge: Leveraging DINOv3 for Robust Outdoor Scene Understanding in Field Robotics** (Score: 43) [Link](https://arxiv.org/abs/2606.18582v1)
- **A High-accuracy Event-based Underwater SLAM System** (Score: 40) [Link](https://arxiv.org/abs/2606.18951v1)

## 📊 今日统计
- 总抓取: 430 篇 | 通过初筛: 62 篇 | 精选: 5 篇 (含 LLM 精筛)
