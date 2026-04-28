# 🤖 具身智能/机器人学术日报 (2026-04-27)

## 🏆 精选论文 (Top 5)

### 1. False Feasibility in Variable Impedance MPC for Legged Locomotion
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Variable impedance model predictive control (MPC) formulations that treat joint stiffness as an instantaneous decision variable operate on a feasible set strictly larger than the physically realizable set under first-order actuator dynamics. We identify this as a formulation error rather than a modeling approximation, formalize the distinction between the parameter-based feasible set Fparam and the realizable set Freal, and characterize the regime of mismatch via the dimensionless parameter alph...
- **AI 点评:** 分析了变阻抗MPC在腿足运动控制中的可行性问题，直接针对腿足机器人的MPC控制器设计缺陷，与locomotion policy和执行器动力学建模相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.22251) | 📥 [PDF](https://arxiv.org/pdf/2604.22251.pdf)

---

### 2. ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
- **Score:** 49
- **Categories:** cs.RO
- **Venue:** Robotics and Automation Letters
- **Abstract:** Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence.
- **AI 点评:** 基于ADMM的并行轨迹优化框架结合深度强化学习，有实时重规划能力和sim-to-real无退化特性，对机器人运动规划有一定参考价值，但不直接针对腿足运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2604.22715) | 📥 [PDF](https://arxiv.org/pdf/2604.22715.pdf)

---

### 3. Robust Localization for Autonomous Vehicles in Highway Scenes
- **Score:** 38
- **Categories:** cs.RO
- **Venue:** ICRA
- **Abstract:** Localization for autonomous vehicles on highways remains under-explored compared to urban roads, and state-of-the-art methods for urban scenes degrade when directly applied to highways. We identify key challenges including environment changes under information homogeneity, heavy occlusion, degraded GNSS signals, and stringent downstream requirements on accuracy and latency.
- **AI 点评:** 面向自动驾驶的高速公路激光雷达定位，与轮足机器人导航方法有部分方法论交集，但场景差异较大。
- 📄 [arXiv](https://arxiv.org/abs/2604.22040) | 📥 [PDF](https://arxiv.org/pdf/2604.22040.pdf)

---

### 4. SNGR: Selective Non-Gaussian Refinement for Ambiguous SLAM Factor Graphs
- **Score:** 37
- **Categories:** cs.RO, math.NA
- **Abstract:** We present Selective Non-Gaussian Refinement (SNGR), a SLAM framework that augments iSAM2 with targeted nested sampling on windows where Gaussian approximations are likely to fail. We detect such regions using the condition number of joint marginal covariances and selectively refine them using the full nonlinear factor graph likelihood, with a gating mechanism to avoid degradation in multimodal cases.
- **AI 点评:** SLAM因子图中的非高斯优化方法，对机器人状态估计有一定参考价值，但未针对足式或移动机器人场景。
- 📄 [arXiv](https://arxiv.org/abs/2604.22065) | 📥 [PDF](https://arxiv.org/pdf/2604.22065.pdf)

---

### 5. Learning Control Policies to Provably Satisfy Hard Affine Constraints for Black-Box Hybrid Dynamical Systems
- **Score:** 33
- **Categories:** cs.RO
- **Abstract:** Ensuring safety for black-box hybrid dynamical systems presents significant challenges due to their instantaneous state jumps and unknown explicit nonlinear dynamics. Existing solutions for strict safety constraint satisfaction, like control barrier functions (CBFs) and reachability analysis, rely on direct knowledge of the dynamics. Similarly, safe reinforcement learning (RL) approaches often rely on known system dynamics or merely discourage safety violations through reward shaping.
- **AI 点评:** 针对黑盒混合动力系统的安全RL策略学习，方法具有通用性但主要验证于简单摆和乒乓球拍环境，与腿足机器人控制相关性较弱。
- 📄 [arXiv](https://arxiv.org/abs/2604.22244) | 📥 [PDF](https://arxiv.org/pdf/2604.22244.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 30 篇 | 通过初筛: 23 篇 | 精选: 5 篇 (含 LLM 精筛)
