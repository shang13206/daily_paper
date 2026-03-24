# 🤖 具身智能/机器人学术日报 (2026-03-23)

## 🏆 精选论文 (Top 5)

### 1. Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
- **Score:** 66
- **Categories:** cs.AI, cs.RO
- **Abstract:** This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Unlike prior methods that typically rely on domain randomization over a fixed finite set of parameters, the proposed approach injects state-dependent perturbations into the input joint torque during forward simulation.
- **AI 点评:** 直接针对人形机器人sim-to-real迁移，提出基于关节力矩扰动注入的新方法替代域随机化，与研究核心方向高度吻合。
- 📄 [arXiv](https://arxiv.org/abs/2603.21853v1) | 📥 [PDF](https://arxiv.org/pdf/2603.21853v1)

---

### 2. Can a Robot Walk the Robotic Dog: Triple-Zero Collaborative Navigation for Heterogeneous Multi-Agent Systems
- **Score:** 45
- **Categories:** cs.RO, cs.MA
- **Abstract:** We present Triple Zero Path Planning (TZPP), a collaborative framework for heterogeneous multi-robot systems that requires zero training, zero prior knowledge, and zero simulation. TZPP employs a coordinator--explorer architecture: a humanoid robot handles task coordination, while a quadruped robot explores and identifies feasible paths using guidance from a multimodal large language model.
- **AI 点评:** 异构多机器人（人形+四足）协作导航的零训练路径规划框架，涉及真实Unitree机器人部署，与导航研究方向相关但缺乏RL/运动控制深度。
- 📄 [arXiv](https://arxiv.org/abs/2603.21723v1) | 📥 [PDF](https://arxiv.org/pdf/2603.21723v1)

---

### 3. Conformal Koopman for Embedded Nonlinear Control with Statistical Robustness: Theory and Real-World Validation
- **Score:** 34
- **Categories:** cs.RO, eess.SY
- **Venue:** ICRA
- **Abstract:** We propose a fully data-driven, Koopman-based framework for statistically robust control of discrete-time nonlinear systems with linear embeddings. Establishing a connection between the Koopman operator and contraction theory, it offers distribution-free probabilistic bounds on the state tracking error under Koopman modeling uncertainty.
- **AI 点评:** 基于Koopman算子的非线性控制框架，在扑翼无人机上有实机验证，方法论（数据驱动控制+形式安全保证）对运动控制有一定参考价值，但与核心研究方向关联较弱。
- 📄 [arXiv](https://arxiv.org/abs/2603.21580v1) | 📥 [PDF](https://arxiv.org/pdf/2603.21580v1)

---

### 4. RTD-RAX: Fast, Safe Trajectory Planning for Systems under Unknown Disturbances
- **Score:** 29
- **Categories:** cs.RO, eess.SY
- **Abstract:** Reachability-based Trajectory Design (RTD) is a provably safe, real-time trajectory planning framework that combines offline reachable-set computation with online trajectory optimization. However, standard RTD implementations suffer from two key limitations: conservatism induced by worst-case reachable-set overapproximations, and an inability to account for real-time disturbances during execution.
- **AI 点评:** 基于可达性的安全轨迹规划框架，处理未知扰动下的实时安全认证，对导航和运动规划有一定参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2603.21635v1) | 📥 [PDF](https://arxiv.org/pdf/2603.21635v1)

---

### 5. Partial Attention in Deep Reinforcement Learning for Safe Multi-Agent Control
- **Score:** 28
- **Categories:** eess.SY, cs.MA, cs.RO
- **Venue:** TRO
- **Abstract:** Attention mechanisms excel at learning sequential patterns by discriminating data based on relevance and importance. This provides state-of-the-art performance in advanced generative artificial intelligence models. This paper applies this concept of an attention mechanism for multi-agent safe control. We specifically consider the design of a neural network to control autonomous vehicles in a highway merging scenario.
- **AI 点评:** 多智能体自动驾驶控制，与机器人运动/导航无关，RL方法也仅用于车辆场景。
- 📄 [arXiv](https://arxiv.org/abs/2603.21810v1) | 📥 [PDF](https://arxiv.org/pdf/2603.21810v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 201 篇 | 通过初筛: 146 篇 | 精选: 5 篇 (含 LLM 精筛)
