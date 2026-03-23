# 🤖 具身智能/机器人学术日报 (2026-03-18)

## 🏆 精选论文 (Top 5)

### 1. REAL: Robust Extreme Agility via Spatio-Temporal Policy Learning and Physics-Guided Filtering
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Extreme legged parkour demands rapid terrain assessment and precise foot placement under highly dynamic conditions. While recent learning-based systems achieve impressive agility, they remain fundamentally fragile to perceptual degradation, where even brief visual noise or latency can cause catastrophic failure. To overcome this, we propose Robust Extreme Agility Learning (REAL), an end-to-end framework for reliable parkour under sensory corruption.
- **AI 点评:** 四足机器人极限跑酷的鲁棒运动学习，结合视觉-本体感知融合与Mamba骨干网络，有实机验证，高度符合研究方向。
- 📄 [arXiv](https://arxiv.org/abs/2603.17653v1) | 📥 [PDF](https://arxiv.org/pdf/2603.17653v1)

---

### 2. Proprioceptive-only State Estimation for Legged Robots with Set-Coverage Measurements of Learned Dynamics
- **Score:** 53
- **Categories:** cs.RO
- **Abstract:** Proprioceptive-only state estimation is attractive for legged robots since it is computationally cheaper and is unaffected by perceptually degraded conditions. The history of joint-level measurements contains rich information that can be used to infer the dynamics of the system and subsequently produce navigational measurements. Recent approaches produce these estimates with learned measurement models and fuse with IMU data, under a Gaussian noise assumption.
- **AI 点评:** 针对腿式机器人的纯本体感知状态估计，使用集合覆盖测量替代高斯噪声假设，在真实四足机器人数据集上验证，与导航和运动控制密切相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.18308v1) | 📥 [PDF](https://arxiv.org/pdf/2603.18308v1)

---

### 3. Real-Time Online Learning for Model Predictive Control using a Spatio-Temporal Gaussian Process Approximation
- **Score:** 45
- **Categories:** eess.SY, cs.RO, math.OC
- **Venue:** ICRA
- **Abstract:** Learning-based model predictive control (MPC) can enhance control performance by correcting for model inaccuracies, enabling more precise state trajectory predictions than traditional MPC. A common approach is to model unknown residual dynamics as a Gaussian process (GP), which leverages data and also provides an estimate of the associated uncertainty. However, the high computational cost of online learning poses a major challenge for real-time GP-MPC applications.
- **AI 点评:** 基于高斯过程的在线学习MPC方法，用于自主赛车控制，方法可借鉴但平台和场景与主要研究方向有一定距离。
- 📄 [arXiv](https://arxiv.org/abs/2603.17632v1) | 📥 [PDF](https://arxiv.org/pdf/2603.17632v1)

---

### 4. Uncovering Latent Phase Structures and Branching Logic in Locomotion Policies: A Case Study on HalfCheetah
- **Score:** 41
- **Categories:** cs.AI, cs.RO
- **Abstract:** In locomotion control tasks, Deep Reinforcement Learning (DRL) has demonstrated high performance; however, the decision-making process of the learned policy remains a black box, making it difficult for humans to understand. On the other hand, in periodic motions such as walking, it is well known that implicit motion phases exist, such as the stance phase and the swing phase.
- **AI 点评:** 分析DRL运动控制策略的内部相位结构，基于MuJoCo HalfCheetah，有一定参考价值但偏可解释性研究而非运动控制方法创新。
- 📄 [arXiv](https://arxiv.org/abs/2603.18084v1) | 📥 [PDF](https://arxiv.org/pdf/2603.18084v1)

---

### 5. Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation
- **Score:** 36
- **Categories:** cs.RO
- **Abstract:** Robots operating in human-shared environments must not only achieve task-level navigation objectives such as safety and efficiency, but also adapt their behavior to human preferences. However, as human preferences are typically expressed in natural language and depend on environmental context, it is difficult to directly integrate them into low-level robot control policies.
- **AI 点评:** 基于MORL的机器人导航策略结合VLM理解用户偏好，有实机验证，与导航方向相关但平台为轮式机器人且重点在人机交互而非运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2603.17510v1) | 📥 [PDF](https://arxiv.org/pdf/2603.17510v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **Rapid Adaptation of Particle Dynamics for Generalized Deformable Object Mobile Manipulation** (Score: 33) [ICRA] [Link](https://arxiv.org/abs/2603.18246v1)

## 📊 今日统计
- 总抓取: 369 篇 | 通过初筛: 286 篇 | 精选: 5 篇 (含 LLM 精筛)
