# 🤖 具身智能/机器人学术日报 (2026-06-11)

## 🏆 精选论文 (Top 5)

### 1. GUIDE: Goal-Initialized Directional Understanding for End-to-End Visual Navigation
- **Score:** 87
- **Categories:** cs.RO
- **Abstract:** Learning-based visual navigation for legged robots typically relies on continuous goal updates from hierarchical state estimation to provide a persistent directional reference. This reliance incurs additional sensory and computational overhead and deviates from fully end-to-end mobile autonomy. Furthermore, under partial observability, policies are prone to learn myopic behaviors, easily becoming trapped in dead ends and complex structural layouts.
- **AI 点评:** 四足机器人端到端视觉导航、深度感知、强化学习、实机部署和长时空间记忆均高度契合OmniBot导航-运动一体化方向。
- 📄 [arXiv](https://arxiv.org/abs/2606.10832v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10832v1)

---

### 2. Mind Your Steps: A General Learning Framework for Accurate Humanoid Foothold Tracking
- **Score:** 87
- **Categories:** cs.RO, cs.LG
- **Venue:** RSS
- **Abstract:** Enabling humanoid robots to operate in complex, dynamic environments remains a critical challenge, fundamentally limited by the ability to navigate robustly, safely, and accurately. While reinforcement learning with velocity-commanded policies has achieved remarkable robustness in humanoid locomotion, this approach lacks explicit control of the foothold placement, leading to unsafe behavior, such as stepping onto human feet, or imprecise navigation, hindering the following manipulation task.
- **AI 点评:** 直接面向人形机器人 foothold tracking、真实部署、状态估计噪声鲁棒和高低层规划接口，对腿足 locomotion 与导航控制高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.08253) | 📥 [PDF](https://arxiv.org/pdf/2606.08253.pdf)

---

### 3. GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains
- **Score:** 71
- **Categories:** cs.RO
- **Abstract:** Humanoid robots have achieved strong locomotion capabilities, but reliable navigation on versatile terrains remains challenging because obstacle avoidance must be coordinated with dynamically feasible motion. In this work, we present GuideWalk, a unified end-to-end framework that integrates traversability-aware navigation guidance with terrain-adaptive locomotion teacher for humanoid navigation.
- **AI 点评:** 统一导航与地形自适应 locomotion 的 humanoid 框架高度契合感知-导航-控制一体化研究。
- 📄 [arXiv](https://arxiv.org/abs/2606.10449v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10449v1)

---

### 4. Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation
- **Score:** 69
- **Categories:** cs.RO, cs.LG
- **Venue:** ICRA
- **Abstract:** Multi-objective reinforcement learning for humanoid robots must coordinate locomotion and manipulation within a single policy. A natural design choice is whether to use a single (unified) critic that estimates the combined value of all objectives, or separate (dual) critics with disjoint reward signals.
- **AI 点评:** 在人形机器人Isaac Lab中研究locomotion-manipulation多目标RL critic结构，虽非轮足但与全身控制、RL训练和策略设计高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.11891) | 📥 [PDF](https://arxiv.org/pdf/2606.11891.pdf)

---

### 5. Locomotion analysis of a quadruped interacting with the lunar granular surface
- **Score:** 69
- **Categories:** cs.RO
- **Abstract:** Deploying legged robots in extra-terrestrial environments includes many challenges due to complex terrain interactions, energy, and thermal constraints. For effective mechanical design of a lunar exploration quadrupedal robot, careful consideration of motor torques, energy expenditure, and cost of transport is required. The lunar surface is composed of granular regolith, which impacts the locomotion of legged robots and their performance.
- **AI 点评:** 四足机器人在月壤软接触地形上的 RL locomotion 与 terrain adaptation/sim2sim 分析高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.10273v1) | 📥 [PDF](https://arxiv.org/pdf/2606.10273v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds** (Score: 69) [Link](https://arxiv.org/abs/2606.10288v1)
- **AgniNav: Configuration-Driven Cross-Embodiment Local Planning for Robot Navigation** (Score: 66) [Link](https://arxiv.org/abs/2606.10903v1)
- **Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation** (Score: 66) [ICRA] [Link](https://arxiv.org/abs/2606.11891v1)
- **KinematicRL: A Sim-to-Real Reinforcement Learning Framework For Social Navigation With Kinodynamic Feasibility** (Score: 64) [Link](https://arxiv.org/abs/2606.12042v1)
- **Information-Preserving Continuous Occupancy Mapping with Variance-Weighted Submap Joining** (Score: 62) [Link](https://arxiv.org/abs/2606.10442v1)
- **Explore From Sketch: Accelerating UAV Exploration in Large-scale Environments with Prior Maps** (Score: 58) [Link](https://arxiv.org/abs/2606.11708v1)
- **A Distributed Multi-UGV Exploration Framework With Loop-Aware Planning and Descriptor-Aided Localization in Resource-Limited Environments** (Score: 57) [Link](https://arxiv.org/abs/2606.11088v1)
- **Cross-Modal Benchmarking for Robotic Perception in Natural Environments** (Score: 56) [ICRA] [Link](https://arxiv.org/abs/2606.11563v1)
- **OMG: Omni-Modal Motion Generation for Generalist Humanoid Control** (Score: 55) [Link](https://arxiv.org/abs/2606.10340v1)
- **SAFER-Nav: Enhancing Safety for Visual Robot Navigation via Segmentation-Aware Fine-Tuning** (Score: 55) [Link](https://arxiv.org/abs/2606.11636v1)
- **Globally Localizing Lunar Rover in Pixels via Graph Alignment** (Score: 51) [Link](https://arxiv.org/abs/2606.10602v1)
- **IR-SIM: A Lightweight Skill-Native Simulator for Navigation, Learning, and Benchmarking** (Score: 49) [Link](https://arxiv.org/abs/2606.08729)
- **Resilient Navigation for Autonomous Farm Robots by Leveraging Jerk-Augmented Models with IMU-Only Disturbance Rejection** (Score: 49) [Link](https://arxiv.org/abs/2606.10971v1)
- **A Spiking Neural Architecture for Coordinating Arm and Locomotor Control** (Score: 47) [Link](https://arxiv.org/abs/2606.11034v1)
- **Towards End to End Motion Planning and Execution for Autonomous Underwater Vehicles Using Reinforcement Learning** (Score: 47) [Link](https://arxiv.org/abs/2606.08513)
- **Bridging the sim2real gap in the table tennis robot with a transformer-based ball states predictor** (Score: 46) [Link](https://arxiv.org/abs/2606.11464v1)
- **Steering Multirobot Behavior via Closed-Loop Affine Activation Editing** (Score: 46) [Link](https://arxiv.org/abs/2606.11489v1)
- **Autonomous Aerial Manipulation via Contextual Contrastive Meta Reinforcement Learning** (Score: 43) [Link](https://arxiv.org/abs/2606.08533)
- **LieIPM: Lie Group Interior Point Method for Direct Trajectory Optimization of Rigid Bodies** (Score: 43) [Link](https://arxiv.org/abs/2606.10579v1)
- **UGV-Conditioned Multi-UAV Informative Planning on a Shared Exposure Belief** (Score: 43) [Link](https://arxiv.org/abs/2606.12306v1)
- **Vehicle Prediction Model for Enhanced MPC Path Tracking in Formula Student Driverless** (Score: 43) [Link](https://arxiv.org/abs/2606.10732v1)
- **Planar-Sector LOS Guidance for Interception of Agile Targets with Lifting-Wing Quadcopters** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2606.10639v2)
- **Learning Unions of Convex Sets via Invertible Latent Decomposition for Path Planning** (Score: 41) [Link](https://arxiv.org/abs/2606.12027v1)
- **Rethinking Embodied Navigation via Relational Inductive Bias** (Score: 41) [Link](https://arxiv.org/abs/2606.10348v1)
- **SG2Loc: Sequential Visual Localization on 3D Scene Graphs** (Score: 41) [Link](https://arxiv.org/abs/2606.11880v1)
- **Fibration Trees: A Unified Approach to Multi-Robot Motion Planning** (Score: 40) [Link](https://arxiv.org/abs/2606.12070v1)
- **Implicit Neural Representations of Individual Behavior** (Score: 40) [ICML] [Link](https://arxiv.org/abs/2606.12200)
- **Implicit Neural Representations of Individual Behavior** (Score: 40) [ICML] [Link](https://arxiv.org/abs/2606.12200v1)
- **A Modular Dual-Camera Pipeline for Micro-Inspection Using Aerial Robots** (Score: 38) [Link](https://arxiv.org/abs/2606.11419v1)
- **Difference-Aware Retrieval Policies for Imitation Learning** (Score: 38) [ICLR] [Link](https://arxiv.org/abs/2606.09758)
- **Multi-UAV Active Sensing with Information Gain-based Planning and Belief Fusion** (Score: 38) [Link](https://arxiv.org/abs/2606.10986v1)
- **Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics** (Score: 37) [Link](https://arxiv.org/abs/2606.12365v1)
- **MPPI-based Informative Trajectory Planning for Search and Capture of Drifting Targets with ASVs** (Score: 37) [Link](https://arxiv.org/abs/2606.12019v1)
- **MODIP: Efficient Model-Based Optimization for Diffusion Policies** (Score: 36) [Link](https://arxiv.org/abs/2606.10825)
- **PAWS: Preference Learning with Advantage-Weighted Segments** (Score: 36) [ICML] [Link](https://arxiv.org/abs/2606.11982)

## 📊 今日统计
- 总抓取: 1485 篇 | 通过初筛: 197 篇 | 精选: 5 篇 (含 LLM 精筛)
