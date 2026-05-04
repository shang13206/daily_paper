# 🤖 具身智能/机器人学术日报 (2026-05-01)

## 🏆 精选论文 (Top 5)

### 1. HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments
- **Score:** 80
- **Categories:** cs.RO
- **Venue:** RA-L
- **Abstract:** Navigating quadruped robots in unstructured 3D environments poses significant challenges, requiring goal-directed motion, effective exploration to escape from local minima, and posture adaptation to traverse narrow, height-constrained spaces. Conventional approaches employ a sequential mapping-planning pipeline but suffer from accumulated perception errors and high computational overhead, restricting their applicability on resource-constrained platforms.
- **AI 点评:** 直接针对四足机器人在非结构3D环境中的层次化姿态自适应导航，结合高层导航策略与底层运动控制器，高度契合locomotion policy learning与导航一体化研究。
- 📄 [arXiv](https://arxiv.org/abs/2604.26504) | 📥 [PDF](https://arxiv.org/pdf/2604.26504.pdf)

---

### 2. asRoBallet: Closing the Sim2Real Gap via Friction-Aware Reinforcement Learning for Underactuated Spherical Dynamics
- **Score:** 66
- **Categories:** cs.AI, cs.RO
- **Abstract:** We introduce asRoBallet, to the best of our knowledge, the first successful deployment of reinforcement learning (RL) on a humanoid ballbot hardware. Historically, ballbots have served as a canonical benchmark for underactuated and nonholonomic control, which are characterized by a reality gap in complex friction models for wheel-sphere-ground interactions.
- **AI 点评:** ballbot人形机器人的RL sim-to-real部署，使用MuJoCo建模摩擦与接触，与sim2real、欠驱动运动控制方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.24916) | 📥 [PDF](https://arxiv.org/pdf/2604.24916.pdf)

---

### 3. GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning
- **Score:** 59
- **Categories:** cs.RO
- **Venue:** Robotics: Science and Systems
- **Abstract:** Embodied AI research is undergoing a shift toward vision-centric perceptual paradigms. While massively parallel simulators have catalyzed breakthroughs in proprioception-based locomotion, their potential remains largely untapped for vision-informed tasks due to the prohibitive computational overhead of large-scale photorealistic rendering.
- **AI 点评:** 基于3DGS的高吞吐量视觉仿真框架，支持locomotion/navigation/manipulation任务，sim-to-real和视觉感知相关度较高，但缺乏对四足/轮足的针对性。
- 📄 [arXiv](https://arxiv.org/abs/2604.25459) | 📥 [PDF](https://arxiv.org/pdf/2604.25459.pdf)

---

### 4. FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction
- **Score:** 51
- **Categories:** cs.RO, cs.CV
- **Venue:** RSS
- **Abstract:** Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments. We present FreeOcc, a training-free framework for open-vocabulary occupancy prediction from monocular or RGB-D sequences. Unlike prior approaches that require voxel-level supervision and ground-truth camera poses, FreeOcc operates without 3D annotations, pose ground truth, or any learning stage.
- **AI 点评:** 训练无关的开放词汇占用预测框架，结合SLAM构建语义地图，对移动机器人导航有一定参考价值，但主要面向室内具身智能场景而非legged robot部署。
- 📄 [arXiv](https://arxiv.org/abs/2604.28115) | 📥 [PDF](https://arxiv.org/pdf/2604.28115.pdf)

---

### 5. Bi-Level Optimization for Contact and Motion Planning in Rope-Assisted Legged Robots
- **Score:** 50
- **Categories:** cs.RO
- **Abstract:** This paper presents a planning pipeline framework for locomotion in rope-assisted robots climbing vertical surfaces. The proposed framework is formulated as a bi-level optimization scheme that addresses a mixed-integer problem: selecting feasible terrain regions for landing while simultaneously optimizing the control inputs, namely rope tensions and leg forces, and landing location.
- **AI 点评:** 针对绳辅助腿式机器人攀爬垂直表面的双层运动规划，涉及足式机器人运动控制与非结构地形，但场景较特殊（攀爬）且偏传统优化方法。
- 📄 [arXiv](https://arxiv.org/abs/2604.26910) | 📥 [PDF](https://arxiv.org/pdf/2604.26910.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction** (Score: 49) [RSS] [Link](https://arxiv.org/abs/2604.28115v1)
- **Learning-Based Hierarchical Scene Graph Matching for Robot Localization Leveraging Prior Maps** (Score: 47) [Link](https://arxiv.org/abs/2604.27821)
- **RAY-TOLD: Ray-Based Latent Dynamics for Dense Dynamic Obstacle Avoidance with TDMPC** (Score: 46) [Link](https://arxiv.org/abs/2604.27450)
- **VISION-SLS: Safe Perception-Based Control from Learned Visual Representations via System Level Synthesis** (Score: 45) [RSS] [Link](https://arxiv.org/abs/2604.24894)
- **Robust Graph Matching through Semantic Relationship Generation for SLAM** (Score: 41) [Link](https://arxiv.org/abs/2604.25404)
- **Learning Tactile-Aware Quadrupedal Loco-Manipulation Policies** (Score: 40) [Link](https://arxiv.org/abs/2604.27224)
- **Optimal UGV-UAV Cooperative Partitioning and Inspection of Shortest Paths** (Score: 39) [Robotics: Science and Systems] [Link](https://arxiv.org/abs/2604.25284)
- **3D Generation for Embodied AI and Robotic Simulation: A Survey** (Score: 38) [Link](https://arxiv.org/abs/2604.26509v1)
- **Egocentric Tactile and Proximity Sensors as Observation Priors for Humanoid Collision Avoidance** (Score: 37) [ICRA] [Link](https://arxiv.org/abs/2604.25554)
- **Bridging the Indoor-Outdoor Gap: Cross-Technology Ranging for Seamless Robot Navigation** (Score: 35) [Link](https://arxiv.org/abs/2604.25541)

## 📊 今日统计
- 总抓取: 994 篇 | 通过初筛: 159 篇 | 精选: 5 篇 (含 LLM 精筛)
