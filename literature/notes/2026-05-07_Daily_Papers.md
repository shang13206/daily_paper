# 🤖 具身智能/机器人学术日报 (2026-05-07)

## 🏆 精选论文 (Top 5)

### 1. Dynamics Aware Quadrupedal Locomotion via Intrinsic Dynamics Head
- **Score:** 76
- **Categories:** cs.RO
- **Abstract:** Quadrupedal locomotion plays a critical role in enabling agile, versatile movement across complex terrains. Understanding and estimating the underlying physical dynamics are essential for achieving efficient and stable quadrupedal locomotion. We propose a novel training framework for quadrupedal locomotion that enables the Control Policy to understand and reason about physical dynamics.
- **AI 点评:** 直接针对四足机器人运动控制，提出内在动力学头辅助训练框架并验证了sim-to-real迁移，与核心研究方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2605.01227) | 📥 [PDF](https://arxiv.org/pdf/2605.01227.pdf)

---

### 2. Dr-PoGO: Direct Radar Pose-Graph Optimization
- **Score:** 75
- **Categories:** cs.RO
- **Venue:** ICRA
- **Abstract:** This paper introduces Dr-PoGO, a method for Simultaneous Localization And Mapping (SLAM) using a 2D spinning radar. Unlike cameras or lidars that require line-of-sight, millimetre-wave radars can `see' through dust, falling snow, rain, etc. Accordingly, it is a great modality for robust perception regardless of the weather conditions.
- **AI 点评:** 基于2D旋转雷达的SLAM方法，在恶劣天气下具有鲁棒感知能力，与移动机器人导航和状态估计方向相关。
- 📄 [arXiv](https://arxiv.org/abs/2605.04806) | 📥 [PDF](https://arxiv.org/pdf/2605.04806.pdf)

---

### 3. Natural Gradient Bayesian Filtering: Geometry-Aware Filter for Dynamical Systems
- **Score:** 75
- **Categories:** cs.RO, eess.SY
- **Abstract:** Bayesian filtering is a cornerstone of state estimation in complex systems such as aerospace systems, yet exact solutions are available only for linear Gaussian models. In practice,nonlinear systems are handled through tractable approximations,with Gaussian filters such as the extended and unscented Kalman filters being among the most widely used methods.
- **AI 点评:** 提出几何感知的自然梯度贝叶斯滤波器，案例涵盖SLAM和四足/人形机器人状态估计，与研究者的状态估计方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2605.02306) | 📥 [PDF](https://arxiv.org/pdf/2605.02306.pdf)

---

### 4. Right Model, Right Time: Real-Time Cascaded-Fidelity MPC for Bipedal Walking
- **Score:** 74
- **Categories:** cs.RO
- **Venue:** ICRA
- **Abstract:** This paper presents a multi-phase whole-body model predictive control approach for bipedal walking, combining a detailed whole-body model in the near horizon with a simplified single-rigid-body model in the later prediction steps. This reduces computational complexity while retaining prediction capabilities. The resulting nonlinear optimal control problem is solved using sequential quadratic programming (SQP) in acados.
- **AI 点评:** 针对双足机器人的多阶段全身MPC方法，结合MuJoCo仿真验证，与轮足/人形运动控制和MPC方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2605.04607) | 📥 [PDF](https://arxiv.org/pdf/2605.04607.pdf)

---

### 5. LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
- **Score:** 70
- **Categories:** cs.RO
- **Venue:** Transactions on Robotics
- **Abstract:** Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes.
- **AI 点评:** LiDAR-Radar跨模态导航系统，在多机器人平台上进行40+km长期部署验证，对移动机器人的环境鲁棒定位与导航具有较强参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2605.02809) | 📥 [PDF](https://arxiv.org/pdf/2605.02809.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Constraint-Enhanced Reinforcement Learning Based on Dynamic Decoupled Spherical Radial Squashing** (Score: 61) [Link](https://arxiv.org/abs/2605.04185v1)
- **Change-Robust Online Spatial-Semantic Topological Mapping** (Score: 59) [Link](https://arxiv.org/abs/2605.02227)
- **DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation** (Score: 57) [Link](https://arxiv.org/abs/2605.02759)
- **Constraint-Enhanced Reinforcement Learning Based on Dynamic Decoupled Spherical Radial Squashing** (Score: 56) [Link](https://arxiv.org/abs/2605.04185)
- **Robust Visual SLAM for UAV Navigation in GPS-Denied and Degraded Environments: A Multi-Paradigm Evaluation and Deployment Study** (Score: 55) [Link](https://arxiv.org/abs/2605.03678)
- **SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision** (Score: 55) [Link](https://arxiv.org/abs/2605.03846)
- **A Closed-Form Dual-Barrier CBF Safety Filter for Holonomic Robots on Incrementally Built Occupancy Grid Maps** (Score: 54) [Link](https://arxiv.org/abs/2605.05182)
- **Feedback Motion Planning for Stochastic Nonlinear Systems with Signal Temporal Logic Specifications** (Score: 54) [Link](https://arxiv.org/abs/2605.02361)
- **Height Control and Optimal Torque Planning for Jumping With Wheeled-Bipedal Robots** (Score: 52) [Link](https://arxiv.org/abs/2605.03302)
- **Sim-to-Real Transfer and Robustness Evaluation of Reinforcement Learning Control with Integrated Perception on an ASV for Floating Waste Capture** (Score: 50) [Link](https://arxiv.org/abs/2605.02529)
- **Beyond Specialization: Robust Reinforcement Learning Navigation via Procedural Map Generators** (Score: 49) [Link](https://arxiv.org/abs/2605.02528)
- **Stability of Control Lyapunov Function Guided Reinforcement Learning** (Score: 49) [Link](https://arxiv.org/abs/2605.01978)
- **Learning to Race in Minutes: Infoprop Dyna on the Mini Wheelbot** (Score: 48) [Link](https://arxiv.org/abs/2605.01096)
- **Do We Really Need Immediate Resets? Rethinking Collision Handling for Efficient Robot Navigation** (Score: 46) [Link](https://arxiv.org/abs/2605.02192)
- **Sampling-Based Control via Entropy-Regularized Optimal Transport** (Score: 45) [Link](https://arxiv.org/abs/2605.02147)
- **From Language to Logic: A Theoretical Architecture for VLM-Grounded Safe Navigation** (Score: 44) [Link](https://arxiv.org/abs/2605.04327)
- **Observability Conditions and Filter Design for Visual Pose Estimation via Dual Quaternions** (Score: 43) [Link](https://arxiv.org/abs/2605.02054)
- **VOFA: Visual Object Goal Pushing with Force-Adaptive Control for Humanoids** (Score: 40) [Link](https://arxiv.org/abs/2605.01518)
- **Action Agent: Agentic Video Generation Meets Flow-Constrained Diffusion** (Score: 38) [Link](https://arxiv.org/abs/2605.01477)
- **Parking Assistance for Trailer-Truck Transport Vehicles Using Sensor Fusion and Motion Planning** (Score: 38) [Link](https://arxiv.org/abs/2605.02716)
- **Zero-Shot, Safe and Time-Efficient UAV Navigation via Potential-Based Reward Shaping, Control Lyapunov and Barrier Functions** (Score: 37) [Link](https://arxiv.org/abs/2605.01787)
- **EdgeLPR: On the Deep Neural Network trade-off between Precision and Performance in LiDAR Place Recognition** (Score: 36) [Link](https://arxiv.org/abs/2605.02275)
- **Robust Adaptive Predictive Control for Hook-Based Aerial Transportation Between Moving Platforms** (Score: 36) [Link](https://arxiv.org/abs/2605.02370)

## 📊 今日统计
- 总抓取: 1358 篇 | 通过初筛: 207 篇 | 精选: 5 篇 (含 LLM 精筛)
