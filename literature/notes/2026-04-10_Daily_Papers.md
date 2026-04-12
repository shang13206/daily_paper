# 🤖 具身智能/机器人学术日报 (2026-04-10)

## 🏆 精选论文 (Top 5)

### 1. Robust Quadruped Locomotion via Evolutionary Reinforcement Learning
- **Score:** 70
- **Categories:** cs.RO
- **Venue:** TRO
- **Abstract:** Deep reinforcement learning has recently achieved strong results in quadrupedal locomotion, yet policies trained in simulation often fail to transfer when the environment changes. Evolutionary reinforcement learning aims to address this limitation by combining gradient-based policy optimisation with population-driven exploration. This work evaluates four methods on a simulated walking task: DDPG, TD3, and two Cross-Entropy-based variants CEM-DDPG and CEM-TD3.
- **AI 点评:** 进化强化学习用于四足机器人步态控制，研究Sim-to-Real迁移鲁棒性和地形适应，与研究方向高度相关，但缺乏实机验证且发表平台不明。
- 📄 [arXiv](https://arxiv.org/abs/2604.07224v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07224v1)

---

### 2. PriPG-RL: Privileged Planner-Guided Reinforcement Learning for Partially Observable Systems with Anytime-Feasible MPC
- **Score:** 65
- **Categories:** cs.LG, cs.RO
- **Abstract:** This paper addresses the problem of training a reinforcement learning (RL) policy under partial observability by exploiting a privileged, anytime-feasible planner agent available exclusively during training. We formalize this as a Partially Observable Markov Decision Process (POMDP) in which a planner agent with access to an approximate dynamical model and privileged state information guides a learning agent that observes only a lossy projection of the true state.
- **AI 点评:** 直接相关：将MPC作为特权规划器指导RL策略训练，解决部分可观测问题，在Isaac Lab中训练并在Unitree Go2四足机器人上完成实机验证，与研究方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2604.08036v1) | 📥 [PDF](https://arxiv.org/pdf/2604.08036v1)

---

### 3. Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation
- **Score:** 64
- **Categories:** cs.RO
- **Abstract:** This paper presents a sim-to-real approach that enables legged robots to dynamically manipulate large and heavy objects with whole-body dexterity. Our key insight is that by performing test-time steering of a pre-trained whole-body control policy with a sample-based planner, we can enable these robots to solve a variety of dynamic loco-manipulation tasks.
- **AI 点评:** 四足机器人全身运动操控（loco-manipulation），采用sim-to-real方法结合预训练策略与采样规划器，在真实Spot机器人上验证，与全身控制和移动操作高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.08508v1) | 📥 [PDF](https://arxiv.org/pdf/2604.08508v1)

---

### 4. Reset-Free Reinforcement Learning for Real-World Agile Driving: An Empirical Study
- **Score:** 59
- **Categories:** cs.RO
- **Abstract:** This paper presents an empirical study of reset-free reinforcement learning (RL) for real-world agile driving, in which a physical 1/10-scale vehicle learns continuously on a slippery indoor track without manual resets. High-speed driving near the limits of tire friction is particularly challenging for learning-based methods because complex vehicle dynamics, actuation delays, and other unmodeled effects hinder both accurate simulation and direct sim-to-real transfer of learned policies.
- **AI 点评:** 研究真实平台上的无重置RL敏捷驾驶，涉及sim-to-real迁移、残差学习与MPC结合，方法论与研究方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.07672v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07672v1)

---

### 5. CMP: Robust Whole-Body Tracking for Loco-Manipulation via Competence Manifold Projection
- **Score:** 52
- **Categories:** cs.AI, cs.LG, cs.RO
- **Abstract:** While decoupled control schemes for legged mobile manipulators have shown robustness, learning holistic whole-body control policies for tracking global end-effector poses remains fragile against Out-of-Distribution (OOD) inputs induced by sensor noise or infeasible user commands. To improve robustness against these perturbations without sacrificing task performance and continuity, we propose Competence Manifold Projection (CMP).
- **AI 点评:** 足式移动操作机器人的全身控制策略，涉及legged robot的loco-manipulation全身追踪，与研究方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.07457v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07457v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **Safe Large-Scale Robust Nonlinear MPC in Milliseconds via Reachability-Constrained System Level Synthesis on the GPU** (Score: 49) [Link](https://arxiv.org/abs/2604.07644v1)
- **Incremental Residual Reinforcement Learning Toward Real-World Learning for Social Navigation** (Score: 36) [Link](https://arxiv.org/abs/2604.07945v1)
- **SANDO: Safe Autonomous Trajectory Planning for Dynamic Unknown Environments** (Score: 35) [Link](https://arxiv.org/abs/2604.07599v1)
- **HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation** (Score: 30) [Link](https://arxiv.org/abs/2604.07993v1)

## 📊 今日统计
- 总抓取: 732 篇 | 通过初筛: 510 篇 | 精选: 5 篇 (含 LLM 精筛)
