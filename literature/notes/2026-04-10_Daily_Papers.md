# 🤖 具身智能/机器人学术日报 (2026-04-10)

## 🏆 精选论文 (Top 5)

### 1. Robust Quadruped Locomotion via Evolutionary Reinforcement Learning
- **Score:** 70
- **Categories:** cs.RO
- **Venue:** TRO
- **Abstract:** Deep reinforcement learning has recently achieved strong results in quadrupedal locomotion, yet policies trained in simulation often fail to transfer when the environment changes. Evolutionary reinforcement learning aims to address this limitation by combining gradient-based policy optimisation with population-driven exploration. This work evaluates four methods on a simulated walking task: DDPG, TD3, and two Cross-Entropy-based variants CEM-DDPG and CEM-TD3.
- **AI 点评:** 直接研究四足机器人运动控制，对比进化强化学习与标准RL（DDPG/TD3）在平坦和崎岖地形的迁移性能，与研究方向高度相关，但缺乏实机验证和顶级期刊背书。
- 📄 [arXiv](https://arxiv.org/abs/2604.07224v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07224v1)

---

### 2. Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation
- **Score:** 64
- **Categories:** cs.RO
- **Abstract:** This paper presents a sim-to-real approach that enables legged robots to dynamically manipulate large and heavy objects with whole-body dexterity. Our key insight is that by performing test-time steering of a pre-trained whole-body control policy with a sample-based planner, we can enable these robots to solve a variety of dynamic loco-manipulation tasks.
- **AI 点评:** Spot四足机器人全身运动操作的sim-to-real方法，结合预训练策略与采样规划实现动态loco-manipulation，与运动控制和sim-to-real高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.08508v1) | 📥 [PDF](https://arxiv.org/pdf/2604.08508v1)

---

### 3. PriPG-RL: Privileged Planner-Guided Reinforcement Learning for Partially Observable Systems with Anytime-Feasible MPC
- **Score:** 62
- **Categories:** cs.LG, cs.RO
- **Abstract:** This paper addresses the problem of training a reinforcement learning (RL) policy under partial observability by exploiting a privileged, anytime-feasible planner agent available exclusively during training. We formalize this as a Partially Observable Markov Decision Process (POMDP) in which a planner agent with access to an approximate dynamical model and privileged state information guides a learning agent that observes only a lossy projection of the true state.
- **AI 点评:** 直接相关：提出结合特权MPC规划器与RL策略的POMDP框架，在Isaac Lab中训练并部署到Unitree Go2四足机器人，完成复杂障碍环境导航，与研究者核心方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2604.08036v1) | 📥 [PDF](https://arxiv.org/pdf/2604.08036v1)

---

### 4. Reset-Free Reinforcement Learning for Real-World Agile Driving: An Empirical Study
- **Score:** 53
- **Categories:** cs.RO
- **Abstract:** This paper presents an empirical study of reset-free reinforcement learning (RL) for real-world agile driving, in which a physical 1/10-scale vehicle learns continuously on a slippery indoor track without manual resets. High-speed driving near the limits of tire friction is particularly challenging for learning-based methods because complex vehicle dynamics, actuation delays, and other unmodeled effects hinder both accurate simulation and direct sim-to-real transfer of learned policies.
- **AI 点评:** 真实物理平台上的免重置RL敏捷驾驶研究，涉及sim-to-real gap、残差学习与MPPI基线对比，方法论对运动策略学习有参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2604.07672v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07672v1)

---

### 5. Safe Large-Scale Robust Nonlinear MPC in Milliseconds via Reachability-Constrained System Level Synthesis on the GPU
- **Score:** 47
- **Categories:** cs.AI, cs.RO, eess.SY, math.OC
- **Abstract:** We present GPU-SLS, a GPU-parallelized framework for safe, robust nonlinear model predictive control (MPC) that scales to high-dimensional uncertain robotic systems and long planning horizons. Our method jointly optimizes an inequality-constrained, dynamically-feasible nominal trajectory, a tracking controller, and a closed-loop reachable set under disturbance, all in real-time.
- **AI 点评:** GPU并行化鲁棒非线性MPC框架，在四足（61D）和人形（75D）全身控制上验证，实时性强，对机器人运动控制有较高参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2604.07644v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07644v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **CMP: Robust Whole-Body Tracking for Loco-Manipulation via Competence Manifold Projection** (Score: 46) [Link](https://arxiv.org/abs/2604.07457v1)
- **Incremental Residual Reinforcement Learning Toward Real-World Learning for Social Navigation** (Score: 36) [Link](https://arxiv.org/abs/2604.07945v1)
- **Differentiable Environment-Trajectory Co-Optimization for Safe Multi-Agent Navigation** (Score: 31) [Link](https://arxiv.org/abs/2604.06972v1)
- **SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments** (Score: 31) [Link](https://arxiv.org/abs/2604.07599v1)

## 📊 今日统计
- 总抓取: 732 篇 | 通过初筛: 510 篇 | 精选: 5 篇 (含 LLM 精筛)
