# 🤖 具身智能/机器人学术日报 (2026-06-10)

## 🏆 精选论文 (Top 5)

### 1. GUIDE: Goal-Initialized Directional Understanding for End-to-End Visual Navigation
- **Score:** 86
- **Categories:** cs.RO
- **Abstract:** Learning-based visual navigation for legged robots typically relies on continuous goal updates from hierarchical state estimation to provide a persistent directional reference. This reliance incurs additional sensory and computational overhead and deviates from fully end-to-end mobile autonomy. Furthermore, under partial observability, policies are prone to learn myopic behaviors, easily becoming trapped in dead ends and complex structural layouts.
- **AI 点评:** 四足机器人端到端视觉导航、深度感知、强化学习、长时空间记忆和仿真到实机部署直接命中legged navigation与policy learning核心方向。
- 📄 [arXiv](https://arxiv.org/abs/2606.10832v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10832v1)

---

### 2. Safe Polytope-in-Polytope Motion Planning and Control with Control Barrier Functions
- **Score:** 75
- **Categories:** cs.RO
- **Abstract:** Autonomous mobile robots operating in tight environments require motion planning frameworks that account for the physical footprint of the robot. Simplifying the geometry to a point or a circle is conservative and discards information needed to successfully and safely traverse narrow passages. This work proposes a safe local motion planning and control method that guarantees that a polytopic robot footprint stays inside a continuously updated convex free-space region.
- **AI 点评:** 针对移动机器人的实时局部规划与CBF/MPC安全控制，含LiDAR和实机验证，虽非腿式但与导航避障部署高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.09719v1) | 📥 [PDF](https://arxiv.org/pdf/2606.09719v1)

---

### 3. MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds
- **Score:** 69
- **Categories:** cs.RO
- **Abstract:** Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions required for safety-critical locomotion where small errors can cause catastrophic failures.
- **AI 点评:** 直接研究视觉感知驱动的人形稀疏落脚点 locomotion，并含模型辅助RL、教师学生蒸馏和 Unitree G1 实机部署，非常契合。
- 📄 [arXiv](https://arxiv.org/abs/2606.10288v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10288v1)

---

### 4. GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Humanoid robots have achieved strong locomotion capabilities, but reliable navigation on versatile terrains remains challenging because obstacle avoidance must be coordinated with dynamically feasible motion. In this work, we present GuideWalk, a unified end-to-end framework that integrates traversability-aware navigation guidance with terrain-adaptive locomotion teacher for humanoid navigation.
- **AI 点评:** 直接研究人形机器人在复杂地形上的导航与地形自适应运动统一学习，高度契合locomotion、terrain adaptation和导航控制一体化方向。
- 📄 [arXiv](https://arxiv.org/abs/2606.10449v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10449v1)

---

### 5. Locomotion analysis of a quadruped interacting with the lunar granular surface
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Deploying legged robots in extra-terrestrial environments includes many challenges due to complex terrain interactions, energy, and thermal constraints. For effective mechanical design of a lunar exploration quadrupedal robot, careful consideration of motor torques, energy expenditure, and cost of transport is required. The lunar surface is composed of granular regolith, which impacts the locomotion of legged robots and their performance.
- **AI 点评:** 四足机器人在月壤颗粒软接触地形上的RL locomotion与刚/软接触仿真对比，强相关于地形适应和sim-to-real接触建模。
- 📄 [arXiv](https://arxiv.org/abs/2606.10273v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10273v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **AgniNav: Configuration-Driven Cross-Embodiment Local Planning for Robot Navigation** (Score: 65) [Link](https://arxiv.org/abs/2606.10903v1)
- **Information-Preserving Continuous Occupancy Mapping with Variance-Weighted Submap Joining** (Score: 65) [Link](https://arxiv.org/abs/2606.10442v1)
- **OMG: Omni-Modal Motion Generation for Generalist Humanoid Control** (Score: 65) [Link](https://arxiv.org/abs/2606.10340v1)
- **VGP-Nav: Metric-Aware Visual Geometric Perception for Robot Navigation** (Score: 63) [Link](https://arxiv.org/abs/2606.09268v1)
- **A Distributed Multi-UGV Exploration Framework With Loop-Aware Planning and Descriptor-Aided Localization in Resource-Limited Environments** (Score: 60) [Link](https://arxiv.org/abs/2606.11088v1)
- **PTDL:Multi-Terrain Fall Recovery via Phase-Terrain Decoupled Learning** (Score: 60) [Link](https://arxiv.org/abs/2606.08922v1)
- **Resilient Navigation for Autonomous Farm Robots by Leveraging Jerk-Augmented Models with IMU-Only Disturbance Rejection** (Score: 55) [Link](https://arxiv.org/abs/2606.10971v1)
- **Globally Localizing Lunar Rover in Pixels via Graph Alignment** (Score: 50) [Link](https://arxiv.org/abs/2606.10602v1)
- **MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry** (Score: 50) [Link](https://arxiv.org/abs/2606.09355v1)
- **Planar-Sector LOS Guidance for Interception of Agile Targets with Lifting-Wing Quadcopters** (Score: 50) [ICRA] [Link](https://arxiv.org/abs/2606.10639v1)
- **Autonomous Obstacle Removal for Excavators through Policy Learning with Particle Simulation** (Score: 49) [Link](https://arxiv.org/abs/2606.09183v1)
- **Efficient Minimal Solvers for Relative Pose Estimation in Autonomous Driving Applications** (Score: 49) [Link](https://arxiv.org/abs/2606.09569v1)
- **A Spiking Neural Architecture for Coordinating Arm and Locomotor Control** (Score: 47) [Link](https://arxiv.org/abs/2606.11034v1)
- **Dual Quaternion-Based Unscented Kalman Filter with Visual Inertial Odometry for Navigation in GPS-Denied Environments** (Score: 47) [Link](https://arxiv.org/abs/2606.09292v1)
- **VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands** (Score: 47) [Link](https://arxiv.org/abs/2606.09286v1)
- **Efficient Minimal Solvers for Visual-Inertial Relative Pose Estimation in Multi-Camera Systems** (Score: 46) [Link](https://arxiv.org/abs/2606.09477v1)
- **Vehicle Prediction Model for Enhanced MPC Path Tracking in Formula Student Driverless** (Score: 45) [Link](https://arxiv.org/abs/2606.10732v1)
- **SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning** (Score: 43) [Link](https://arxiv.org/abs/2606.08992v1)
- **Multi-UAV Active Sensing with Information Gain-based Planning and Belief Fusion** (Score: 41) [Link](https://arxiv.org/abs/2606.10986v1)
- **Bridged SBI: Correcting Biased Low-Fidelity Posteriors for Cost-Efficient High-Fidelity Inference** (Score: 39) [Link](https://arxiv.org/abs/2606.09155v1)
- **Rethinking Embodied Navigation via Relational Inductive Bias** (Score: 38) [Link](https://arxiv.org/abs/2606.10348v1)
- **LieIPM: Lie Group Interior Point Method for Direct Trajectory Optimization of Rigid Bodies** (Score: 37) [Link](https://arxiv.org/abs/2606.10579v1)
- **ATN3D: Density-Aware LiDAR-Radar Early 3D Object Detection Under Extreme Sparsity** (Score: 35) [Link](https://arxiv.org/abs/2606.09634v1)
- **AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning** (Score: 35) [Link](https://arxiv.org/abs/2606.10927v1)
- **Counterfactual Transport Flows for Offline Conservative Trajectory Refinement** (Score: 35) [ICML] [Link](https://arxiv.org/abs/2606.09115v1)

## 📊 今日统计
- 总抓取: 827 篇 | 通过初筛: 135 篇 | 精选: 5 篇 (含 LLM 精筛)
