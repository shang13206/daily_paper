# 🤖 具身智能/机器人学术日报 (2026-03-25)

## 🏆 精选论文 (Top 5)

### 1. Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
- **Score:** 66
- **Categories:** cs.AI, cs.RO
- **Abstract:** This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Unlike prior methods that typically rely on domain randomization over a fixed finite set of parameters, the proposed approach injects state-dependent perturbations into the input joint torque during forward simulation.
- **AI 点评:** 直接针对人形机器人sim-to-real问题，提出关节力矩扰动注入方法替代域随机化，有实机验证，与核心研究方向高度契合。
- 📚 **已在 Zotero 库中** (Collections: Humanoid)
- 📄 [arXiv](https://arxiv.org/abs/2603.21853v2) | 📥 [PDF](https://arxiv.org/pdf/2603.21853v2)

---

### 2. Learning Multi-Agent Local Collision-Avoidance for Collaborative Carrying tasks with Coupled Quadrupedal Robots
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Robotic collaborative carrying could greatly benefit human activities like warehouse and construction site management. However, coordinating the simultaneous motion of multiple robots represents a significant challenge. Existing works primarily focus on obstacle-free environments, making them unsuitable for most real-world applications.
- **AI 点评:** 基于RL的多四足机器人协同搬运与障碍回避，采用分层策略结合预训练运动策略，有实机验证，与四足运动控制研究高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.23278v1) | 📥 [PDF](https://arxiv.org/pdf/2603.23278v1)

---

### 3. Learning Safe-Stoppability Monitors for Humanoid Robots
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Emergency stop (E-stop) mechanisms are the de facto standard for robot safety. However, for humanoid robots, abruptly cutting power can itself cause catastrophic failures; instead, an emergency stop must execute a predefined fallback controller that preserves balance and drives the robot toward a minimum-risk condition.
- **AI 点评:** 研究人形机器人紧急停止的安全性问题，涉及sim-to-real迁移和平衡控制，与人形机器人运动控制研究有一定相关性。
- 📄 [arXiv](https://arxiv.org/abs/2603.22703v1) | 📥 [PDF](https://arxiv.org/pdf/2603.22703v1)

---

### 4. MEVIUS2: Practical Open-Source Quadruped Robot with Sheet Metal Welding and Multimodal Perception
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Various quadruped robots have been developed to date, and thanks to reinforcement learning, they are now capable of traversing diverse types of rough terrain. In parallel, there is a growing trend of releasing these robot designs as open-source, enabling researchers to freely build and modify robots themselves.
- **AI 点评:** 开源四足机器人MEVIUS2，具备多模态感知并验证了复杂地形穿越能力，与四足运动控制和地形适应研究直接相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.22031v1) | 📥 [PDF](https://arxiv.org/pdf/2603.22031v1)

---

### 5. PCHC: Enabling Preference Conditioned Humanoid Control via Multi-Objective Reinforcement Learning
- **Score:** 54
- **Categories:** cs.RO
- **Abstract:** Humanoid robots often need to balance competing objectives, such as maximizing speed while minimizing energy consumption. While current reinforcement learning (RL) methods can master complex skills like fall recovery and perceptive locomotion, they are constrained by fixed weighting strategies that produce a single suboptimal policy, rather than providing a diverse set of solutions for sophisticated multi-objective control.
- **AI 点评:** 基于MORL的偏好条件化人形机器人控制框架，实现单一策略覆盖多目标行为空间，有实机验证，与人形运动控制研究高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.24047v1) | 📥 [PDF](https://arxiv.org/pdf/2603.24047v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **CATNAV: Cached Vision-Language Traversability for Efficient Zero-Shot Robot Navigation** (Score: 52) [Link](https://arxiv.org/abs/2603.22800v1)
- **Cross-Modal Reinforcement Learning for Navigation with Degraded Depth Measurements** (Score: 49) [TRO] [Link](https://arxiv.org/abs/2603.22182v1)
- **QuadFM: Foundational Text-Driven Quadruped Motion Dataset for Generation and Control** (Score: 47) [Link](https://arxiv.org/abs/2603.24021v1)
- **SafeFlow: Real-Time Text-Driven Humanoid Whole-Body Control via Physics-Guided Rectified Flow and Selective Safety Gating** (Score: 44) [Link](https://arxiv.org/abs/2603.23983v1)
- **Can a Robot Walk the Robotic Dog: Triple-Zero Collaborative Navigation for Heterogeneous Multi-Agent Systems** (Score: 43) [Link](https://arxiv.org/abs/2603.21723v1)
- **Accelerated Spline-Based Time-Optimal Motion Planning with Continuous Safety Guarantees for Non-Differentially Flat Systems** (Score: 40) [TRO] [Link](https://arxiv.org/abs/2603.24133v1)
- **MIRROR: Visual Motion Imitation via Real-time Retargeting and Teleoperation with Parallel Differential Inverse Kinematics** (Score: 40) [Link](https://arxiv.org/abs/2603.23995v1)
- **Path Planning and Reinforcement Learning-Driven Control of On-Orbit Free-Flying Multi-Arm Robots** (Score: 40) [International Journal of Robotics Research] [Link](https://arxiv.org/abs/2603.23182v1)
- **Tightly-Coupled Radar-Visual-Inertial Odometry** (Score: 39) [TRO] [Link](https://arxiv.org/abs/2603.23052v1)
- **Allometric Scaling Laws for Bipedal Robots** (Score: 37) [Link](https://arxiv.org/abs/2603.22560v1)
- **Conformal Koopman for Embedded Nonlinear Control with Statistical Robustness: Theory and Real-World Validation** (Score: 37) [ICRA] [Link](https://arxiv.org/abs/2603.21580v1)
- **Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning** (Score: 37) [Link](https://arxiv.org/abs/2603.22430v1)
- **Decentralized End-to-End Multi-AAV Pursuit Using Predictive Spatio-Temporal Observation via Deep Reinforcement Learning** (Score: 35) [Link](https://arxiv.org/abs/2603.24238v1)
- **Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models** (Score: 35) [Link](https://arxiv.org/abs/2603.22876v1)
- **Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control** (Score: 35) [Link](https://arxiv.org/abs/2603.22201v1)
- **RAFL: Generalizable Sim-to-Real of Soft Robots with Residual Acceleration Field Learning** (Score: 35) [Link](https://arxiv.org/abs/2603.22039v1)
- **DexDrummer: In-Hand, Contact-Rich, and Long-Horizon Dexterous Robot Drumming** (Score: 34) [Link](https://arxiv.org/abs/2603.22263v1)
- **Wake Up to the Past: Using Memory to Model Fluid Wake Effects on Robots** (Score: 33) [IROS] [Link](https://arxiv.org/abs/2603.22472v1)
- **Energy-Aware Collaborative Exploration for a UAV-UGV Team** (Score: 32) [Link](https://arxiv.org/abs/2603.22507v1)
- **Task-Aware Positioning for Improvisational Tasks in Mobile Construction Robots via an AI Agent with Multi-LMM Modules** (Score: 32) [Link](https://arxiv.org/abs/2603.22903v1)
- **Partial Attention in Deep Reinforcement Learning for Safe Multi-Agent Control** (Score: 30) [TRO] [Link](https://arxiv.org/abs/2603.21810v1)

## 📊 今日统计
- 总抓取: 1029 篇 | 通过初筛: 751 篇 | 精选: 5 篇 (含 LLM 精筛) | 已在 Zotero: 1 篇
