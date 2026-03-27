# 🤖 具身智能/机器人学术日报 (2026-03-26)

## 🏆 精选论文 (Top 5)

### 1. Learning Multi-Agent Local Collision-Avoidance for Collaborative Carrying tasks with Coupled Quadrupedal Robots
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Robotic collaborative carrying could greatly benefit human activities like warehouse and construction site management. However, coordinating the simultaneous motion of multiple robots represents a significant challenge. Existing works primarily focus on obstacle-free environments, making them unsuitable for most real-world applications.
- **AI 点评:** 基于RL的多四足机器人协同搬运避障策略，采用分层架构结合预训练运动策略，有实机验证，与四足运动控制研究高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.23278v1) | 📥 [PDF](https://arxiv.org/pdf/2603.23278v1)

---

### 2. Learning Safe-Stoppability Monitors for Humanoid Robots
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Emergency stop (E-stop) mechanisms are the de facto standard for robot safety. However, for humanoid robots, abruptly cutting power can itself cause catastrophic failures; instead, an emergency stop must execute a predefined fallback controller that preserves balance and drives the robot toward a minimum-risk condition.
- **AI 点评:** 人形机器人安全停止策略的sim-to-real研究，涉及人形机器人平衡控制与安全认证，与人形机器人运动控制方向中等相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.22703v1) | 📥 [PDF](https://arxiv.org/pdf/2603.22703v1)

---

### 3. PCHC: Enabling Preference Conditioned Humanoid Control via Multi-Objective Reinforcement Learning
- **Score:** 50
- **Categories:** cs.RO
- **Abstract:** Humanoid robots often need to balance competing objectives, such as maximizing speed while minimizing energy consumption. While current reinforcement learning (RL) methods can master complex skills like fall recovery and perceptive locomotion, they are constrained by fixed weighting strategies that produce a single suboptimal policy, rather than providing a diverse set of solutions for sophisticated multi-objective control.
- **AI 点评:** 人形机器人多目标RL locomotion控制，提出偏好条件化策略和MoE机制，有实机验证，与人形运动控制方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.24047v1) | 📥 [PDF](https://arxiv.org/pdf/2603.24047v1)

---

### 4. Path Planning and Reinforcement Learning-Driven Control of On-Orbit Free-Flying Multi-Arm Robots
- **Score:** 50
- **Categories:** cs.RO, eess.SY
- **Venue:** International Journal of Robotics Research
- **Abstract:** This paper presents a hybrid approach that integrates trajectory optimization (TO) and reinforcement learning (RL) for motion planning and control of free-flying multi-arm robots in on-orbit servicing scenarios. The proposed system integrates TO for generating feasible, efficient paths while accounting for dynamic and kinematic constraints, and RL for adaptive trajectory tracking under uncertainties.
- **AI 点评:** 轨迹优化与RL结合的空间自由飞行多臂机器人控制，混合TO+RL方法论有借鉴价值，但平台为空间机器人且无实机验证。
- 📄 [arXiv](https://arxiv.org/abs/2603.23182v1) | 📥 [PDF](https://arxiv.org/pdf/2603.23182v1)

---

### 5. CATNAV: Cached Vision-Language Traversability for Efficient Zero-Shot Robot Navigation
- **Score:** 46
- **Categories:** cs.RO
- **Abstract:** Navigating unstructured environments requires assessing traversal risk relative to a robot's physical capabilities, a challenge that varies across embodiments. We present CATNAV, a cost-aware traversability navigation framework that leverages multimodal LLMs for zero-shot, embodiment-aware costmap generation without task-specific training.
- **AI 点评:** 基于VLM的四足机器人零样本导航框架，在非结构化室内外环境中进行traversability评估，与导航研究方向较为契合。
- 📄 [arXiv](https://arxiv.org/abs/2603.22800v1) | 📥 [PDF](https://arxiv.org/pdf/2603.22800v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **Accelerated Spline-Based Time-Optimal Motion Planning with Continuous Safety Guarantees for Non-Differentially Flat Systems** (Score: 44) [TRO] [Link](https://arxiv.org/abs/2603.24133v1)
- **QuadFM: Foundational Text-Driven Quadruped Motion Dataset for Generation and Control** (Score: 43) [Link](https://arxiv.org/abs/2603.24021v1)
- **SafeFlow: Real-Time Text-Driven Humanoid Whole-Body Control via Physics-Guided Rectified Flow and Selective Safety Gating** (Score: 42) [Link](https://arxiv.org/abs/2603.23983v1)
- **Tightly-Coupled Radar-Visual-Inertial Odometry** (Score: 39) [TRO] [Link](https://arxiv.org/abs/2603.23052v1)
- **Decentralized End-to-End Multi-AAV Pursuit Using Predictive Spatio-Temporal Observation via Deep Reinforcement Learning** (Score: 35) [Link](https://arxiv.org/abs/2603.24238v1)
- **Towards Safe Learning-Based Non-Linear Model Predictive Control through Recurrent Neural Network Modeling** (Score: 35) [Link](https://arxiv.org/abs/2603.24503v1)
- **MIRROR: Visual Motion Imitation via Real-time Retargeting and Teleoperation with Parallel Differential Inverse Kinematics** (Score: 34) [Link](https://arxiv.org/abs/2603.23995v1)
- **Off-Policy Safe Reinforcement Learning with Constrained Optimistic Exploration** (Score: 34) [ICLR] [Link](https://arxiv.org/abs/2603.23889v1)
- **Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models** (Score: 31) [Link](https://arxiv.org/abs/2603.22876v1)
- **Quadrature Oscillation System for Coordinated Motion in Crawling Origami Robot** (Score: 30) [ICRA] [Link](https://arxiv.org/abs/2603.23666v1)

## 📊 今日统计
- 总抓取: 270 篇 | 通过初筛: 216 篇 | 精选: 5 篇 (含 LLM 精筛)
