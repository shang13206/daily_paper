# 🤖 具身智能/机器人学术日报 (2026-05-06)

## 🏆 精选论文 (Top 5)

### 1. LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
- **Score:** 70
- **Categories:** cs.RO
- **Venue:** Transactions on Robotics
- **Abstract:** Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes.
- **AI 点评:** LiDAR-Radar跨模态Teach-and-Repeat导航系统，在多平台长期大规模部署中验证，直接关联移动机器人导航、定位与鲁棒感知。
- 📄 [arXiv](https://arxiv.org/abs/2605.02809v1) | 📥 [PDF](https://arxiv.org/pdf/2605.02809v1)

---

### 2. Natural Gradient Bayesian Filtering: Geometry-Aware Filter for Dynamical Systems
- **Score:** 69
- **Categories:** cs.RO, eess.SY
- **Abstract:** Bayesian filtering is a cornerstone of state estimation in complex systems such as aerospace systems, yet exact solutions are available only for linear Gaussian models. In practice,nonlinear systems are handled through tractable approximations,with Gaussian filters such as the extended and unscented Kalman filters being among the most widely used methods.
- **AI 点评:** 从信息几何视角重新审视高斯滤波，并在四足/人形机器人状态估计及SLAM上做了案例验证，与状态估计和导航方向直接相关。
- 📄 [arXiv](https://arxiv.org/abs/2605.02306v1) | 📥 [PDF](https://arxiv.org/pdf/2605.02306v1)

---

### 3. SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
- **Score:** 54
- **Categories:** cs.RO
- **Abstract:** Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation.
- **AI 点评:** 四足机器人loco-manipulation系统，涉及本体视觉状态估计和sim-to-real，但核心聚焦manipulation而非locomotion/导航。
- 📄 [arXiv](https://arxiv.org/abs/2605.03846v1) | 📥 [PDF](https://arxiv.org/pdf/2605.03846v1)

---

### 4. Change-Robust Online Spatial-Semantic Topological Mapping
- **Score:** 53
- **Categories:** cs.RO
- **Abstract:** Autonomous robots require change-robust spatial-semantic reasoning: using spatial and semantic knowledge to decide where to go, how to get there, and where the robot is despite environmental change. Existing approaches typically attach semantics to SLAM-built metric maps, but these pipelines are brittle under appearance shifts and scene dynamics, where data association and relocalization degrade.
- **AI 点评:** 提出基于拓扑图的鲁棒空间语义建图方案，在真实机器人目标导航任务中验证，与移动机器人导航和场景变化鲁棒性相关。
- 📄 [arXiv](https://arxiv.org/abs/2605.02227v1) | 📥 [PDF](https://arxiv.org/pdf/2605.02227v1)

---

### 5. Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study
- **Score:** 53
- **Categories:** cs.RO
- **Abstract:** Reliable localization in GPS-denied, visually degraded environments is critical for autonomous UAV opera- tions. This paper presents a systematic comparative evaluation of five V-SLAM systems ORB-SLAM3, DPVO, DROID-SLAM, DUSt3R, and MASt3R spanning classical, deep learning, recurrent, and Vision Transformer (ViT) paradigms.
- **AI 点评:** 针对GPS拒止环境的UAV视觉SLAM系统评测与部署，与机器人导航感知直接相关，评估了多种SLAM范式在降级条件下的鲁棒性。
- 📄 [arXiv](https://arxiv.org/abs/2605.03678v1) | 📥 [PDF](https://arxiv.org/pdf/2605.03678v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Beyond Specialization: Robust Reinforcement Learning Navigation via Procedural Map Generators** (Score: 52) [Link](https://arxiv.org/abs/2605.02528v1)
- **DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation** (Score: 52) [Link](https://arxiv.org/abs/2605.02759v1)
- **Sim-to-Real Transfer and Robustness Evaluation of Reinforcement Learning Control with Integrated Perception on an ASV for Floating Waste Capture** (Score: 50) [Link](https://arxiv.org/abs/2605.02529v1)
- **Feedback Motion Planning for Stochastic Nonlinear Systems with Signal Temporal Logic Specifications** (Score: 49) [Link](https://arxiv.org/abs/2605.02361v1)
- **Height Control and Optimal Torque Planning for Jumping With Wheeled-Bipedal Robots** (Score: 49) [Link](https://arxiv.org/abs/2605.03302v1)
- **Do We Really Need Immediate Resets? Rethinking Collision Handling for Efficient Robot Navigation** (Score: 46) [Link](https://arxiv.org/abs/2605.02192v1)
- **Parking Assistance for Trailer-Truck Transport Vehicles Using Sensor Fusion and Motion Planning** (Score: 41) [Link](https://arxiv.org/abs/2605.02716v1)
- **Sampling-Based Control via Entropy-Regularized Optimal Transport** (Score: 39) [Link](https://arxiv.org/abs/2605.02147v1)
- **On Surprising Effects of Risk-Aware Domain Randomization for Contact-Rich Sampling-based Predictive Control** (Score: 37) [Link](https://arxiv.org/abs/2605.03290v1)
- **EdgeLPR: On the Deep Neural Network trade-off between Precision and Performance in LiDAR Place Recognition** (Score: 36) [Link](https://arxiv.org/abs/2605.02275v1)
- **CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation** (Score: 35) [Robotics: Science and Systems] [Link](https://arxiv.org/abs/2605.02600v1)

## 📊 今日统计
- 总抓取: 619 篇 | 通过初筛: 88 篇 | 精选: 5 篇 (含 LLM 精筛)
