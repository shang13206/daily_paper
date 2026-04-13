# 🤖 具身智能/机器人学术日报 (2026-04-10)

## 🏆 精选论文 (Top 5)

### 1. SafeMind: A Risk-Aware Differentiable Control Framework for Adaptive and Safe Quadruped Locomotion
- **Score:** 53
- **Categories:** cs.AI, cs.RO
- **Abstract:** Learning-based quadruped controllers achieve impressive agility but typically lack formal safety guarantees under model uncertainty, perception noise, and unstructured contact conditions. We introduce SafeMind, a differentiable stochastic safety-control framework that unifies probabilistic Control Barrier Functions with semantic context understanding and meta-adaptive risk calibration.
- **AI 点评:** 将概率控制障碍函数与元自适应风险校准结合，部署于Unitree A1和ANYmal C实机，在12种地形验证安全四足运动控制，与研究方向高度契合。
- 📄 [arXiv](https://arxiv.org/abs/2604.09474v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09474v1)

---

### 2. Sim-to-Real Transfer for Muscle-Actuated Robots via Generalized Actuator Networks
- **Score:** 47
- **Categories:** cs.LG, cs.RO
- **Abstract:** Tendon drives paired with soft muscle actuation enable faster and safer robots while potentially accelerating skill acquisition. Still, these systems are rarely used in practice due to inherent nonlinearities, friction, and hysteresis, which complicate modeling and control. So far, these challenges have hindered policy transfer from simulation to real systems.
- **AI 点评:** 针对肌肉驱动机器人臂的sim-to-real迁移方法，提出广义执行器网络解决非线性建模难题，实机验证充分，sim-to-real方法论有参考价值，但平台为操作臂而非运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2604.09487v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09487v1)

---

### 3. Simulation of Adaptive Running with Flexible Sports Prosthesis using Reinforcement Learning of Hybrid-link System
- **Score:** 41
- **Categories:** cs.RO
- **Abstract:** This study proposes a reinforcement learning-based adaptive running motion simulation for a unilateral transtibial amputee with the flexibility of a leaf-spring-type sports prosthesis using hybrid-link system. The design and selection of sports prostheses often rely on trial and error. A comprehensive whole-body dynamics analysis that considers the interaction between human motion and prosthetic deformation could provide valuable insights for user-specific design and selection.
- **AI 点评:** 基于RL的截肢者跑步假肢运动仿真，结合模仿学习与全身动力学分析，方法与locomotion policy learning有一定交叉，但应用场景为假肢设计而非机器人平台。
- 📄 [arXiv](https://arxiv.org/abs/2604.08882v1) | 📥 [PDF](https://arxiv.org/pdf/2604.08882v1)

---

### 4. Musculoskeletal Motion Imitation for Learning Personalized Exoskeleton Control Policy in Impaired Gait
- **Score:** 31
- **Categories:** cs.RO
- **Abstract:** Designing generalizable control policies for lower-limb exoskeletons remains fundamentally constrained by exhaustive data collection or iterative optimization procedures, which limit accessibility to clinical populations. To address this challenge, we introduce a device-agnostic framework that combines physiologically plausible musculoskeletal simulation with reinforcement learning to enable scalable personalized exoskeleton assistance for both able-bodied and clinical populations.
- **AI 点评:** 利用肌肉骨骼仿真与RL学习个性化外骨骼控制策略，涉及步态与RL方法，但聚焦于辅助医疗而非机器人运动平台。
- 📄 [arXiv](https://arxiv.org/abs/2604.09431v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09431v1)

---

### 5. Physics-Informed Reinforcement Learning of Spatial Density Velocity Potentials for Map-Free Racing
- **Score:** 31
- **Categories:** cs.RO
- **Abstract:** Autonomous racing without prebuilt maps is a grand challenge for embedded robotics that requires kinodynamic planning from instantaneous sensor data at the acceleration and tire friction limits. Out-Of-Distribution (OOD) generalization to various racetrack configurations utilizes Machine Learning (ML) to encode the mathematical relation between sensor data and vehicle actuation for end-to-end control, with implicit localization.
- **AI 点评:** 基于DRL的无地图自主赛车控制，涉及sim-to-real迁移和物理驱动奖励设计，方法有一定借鉴价值，但平台为轮式车辆赛车而非locomotion研究。
- 📄 [arXiv](https://arxiv.org/abs/2604.09499v1) | 📥 [PDF](https://arxiv.org/pdf/2604.09499v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 271 篇 | 通过初筛: 201 篇 | 精选: 5 篇 (含 LLM 精筛)
