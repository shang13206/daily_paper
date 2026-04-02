# 🤖 具身智能/机器人学术日报 (2026-04-01)

## 🏆 精选论文 (Top 5)

### 1. Model Predictive Path Integral PID Control for Learning-Based Path Following
- **Score:** 43
- **Categories:** eess.SY, cs.LG, cs.RO, math.OC
- **Venue:** TRO
- **Abstract:** Classical proportional--integral--derivative (PID) control is widely employed in industrial applications; however, achieving higher performance often motivates the adoption of model predictive control (MPC). Although gradient-based methods are the standard for real-time optimization, sampling-based approaches have recently gained attention.
- **AI 点评:** MPPI-PID结合用于路径跟踪控制，采样效率和平滑输入值得借鉴，但应用场景为叉车而非典型机器人运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2603.29499v1) | 📥 [PDF](https://arxiv.org/pdf/2603.29499v1)

---

### 2. Dynamic Lookahead Distance via Reinforcement Learning-Based Pure Pursuit for Autonomous Racing
- **Score:** 41
- **Categories:** cs.RO, cs.AI, eess.SY
- **Abstract:** Pure Pursuit (PP) is a widely used path-tracking algorithm in autonomous vehicles due to its simplicity and real-time performance. However, its effectiveness is sensitive to the choice of lookahead distance: shorter values improve cornering but can cause instability on straights, while longer values improve smoothness but reduce accuracy in curves.
- **AI 点评:** PPO结合经典Pure Pursuit控制器实现自适应前视距离，有sim-to-real验证，方法思路（RL增强经典控制器）对运动控制有一定参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2603.28625v1) | 📥 [PDF](https://arxiv.org/pdf/2603.28625v1)

---

### 3. Hybrid Framework for Robotic Manipulation: Integrating Reinforcement Learning and Large Language Models
- **Score:** 28
- **Categories:** cs.RO, cs.AI
- **Abstract:** This paper introduces a new hybrid framework that combines Reinforcement Learning (RL) and Large Language Models (LLMs) to improve robotic manipulation tasks. By utilizing RL for accurate low-level control and LLMs for high level task planning and understanding of natural language, the proposed framework effectively connects low-level execution with high-level reasoning in robotic systems.
- **AI 点评:** 涉及机械臂操作任务（非运动控制），仿真环境为PyBullet，与locomotion/导航研究方向相关性低。
- 📄 [arXiv](https://arxiv.org/abs/2603.30022v1) | 📥 [PDF](https://arxiv.org/pdf/2603.30022v1)

---

### 4. HyperKKL: Learning KKL Observers for Non-Autonomous Nonlinear Systems via Hypernetwork-Based Input Conditioning
- **Score:** 27
- **Categories:** eess.SY, cs.LG
- **Venue:** TRO
- **Abstract:** Kazantzis-Kravaris/Luenberger (KKL) observers are a class of state observers for nonlinear systems that rely on an injective map to transform the nonlinear dynamics into a stable quasi-linear latent space, from where the state estimate is obtained in the original coordinates via a left inverse of the transformation map. Current learning-based methods for these maps are designed exclusively for autonomous systems and do not generalize well to controlled or non-autonomous systems.
- **AI 点评:** 针对非自治非线性系统的KKL观测器学习方法，在状态估计上有一定通用性，但未涉及机器人运动控制场景。
- 📄 [arXiv](https://arxiv.org/abs/2603.29744v1) | 📥 [PDF](https://arxiv.org/pdf/2603.29744v1)

---

### 5. Learning Surrogate LPV State-Space Models with Uncertainty Quantification
- **Score:** 27
- **Categories:** eess.SY, cs.LG
- **Venue:** TRO
- **Abstract:** The Linear Parameter-Varying (LPV) framework enables the construction of surrogate models of complex nonlinear and high-dimensional systems, facilitating efficient stability and performance analysis together with controller design. Despite significant advances in data-driven LPV modelling, existing approaches do not quantify the uncertainty of the obtained LPV models.
- **AI 点评:** LPV框架用于非线性系统建模与控制器设计，与机器人控制有边缘相关性，但无实际机器人应用。
- 📄 [arXiv](https://arxiv.org/abs/2603.29532v1) | 📥 [PDF](https://arxiv.org/pdf/2603.29532v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 344 篇 | 通过初筛: 249 篇 | 精选: 5 篇 (含 LLM 精筛)
