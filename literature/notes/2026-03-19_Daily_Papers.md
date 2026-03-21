# 🤖 具身智能/机器人学术日报 (2026-03-19)

## 🏆 精选论文 (Top 5)

### 1. PRIOR: Perceptive Learning for Humanoid Locomotion with Reference Gait Priors
- **Score:** 67
- **Categories:** cs.AI, cs.RO
- **Venue:** IROS
- **Abstract:** Training perceptive humanoid locomotion policies that traverse complex terrains with natural gaits remains an open challenge, typically demanding multi-stage training pipelines, adversarial objectives, or extensive real-world calibration. We present PRIOR, an efficient and reproducible framework built on Isaac Lab that achieves robust terrain traversal with human-like gaits through a simple yet effective design: (i) a parametric gait generator that supplies stable reference trajectories derived...
- **AI 点评:** 基于Isaac Lab的人形机器人感知运动控制框架，涵盖地形适应、参考步态先验和深度图像感知，与研究者的Isaac Lab训练和地形适应方向高度相关，但针对人形而非轮足机器人。
- 📄 [arXiv](https://arxiv.org/abs/2603.18979v1) | 📥 [PDF](https://arxiv.org/pdf/2603.18979v1)

---

### 2. Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning
- **Score:** 62
- **Categories:** cs.RO
- **Abstract:** Recent work in reinforcement learning has shown that incorporating structural priors for articulated robots, such as link connectivity, into policy networks improves learning efficiency. However, dynamics properties, despite their fundamental role in determining how forces and motion propagate through the body, remain largely underexplored as an inductive bias for policy learning.
- **AI 点评:** 提出基于关节体动力学的图神经网络策略架构，在四足机器人（Unitree Go2）上实现sim-to-real迁移，与四轮足机器人RL运动控制研究高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2603.19078v1) | 📥 [PDF](https://arxiv.org/pdf/2603.19078v1)

---

### 3. Efficient and Versatile Quadrupedal Skating: Optimal Co-design via Reinforcement Learning and Bayesian Optimization
- **Score:** 50
- **Categories:** cs.RO
- **Abstract:** In this paper, we present a hardware-control co-design approach that enables efficient and versatile roller skating on quadrupedal robots equipped with passive wheels. Passive-wheel skating reduces leg inertia and improves energy efficiency, particularly at high speeds. However, the absence of direct wheel actuation tightly couples mechanical design and control.
- **AI 点评:** 四足机器人被动轮滑行的强化学习控制与硬件协同设计，与轮足机器人RL运动控制高度相关，但侧重于被动轮而非主动轮足混合系统。
- 📄 [arXiv](https://arxiv.org/abs/2603.18408v1) | 📥 [PDF](https://arxiv.org/pdf/2603.18408v1)

---

### 4. ADMM-Based Distributed MPC with Control Barrier Functions for Safe Multi-Robot Quadrupedal Locomotion
- **Score:** 47
- **Categories:** cs.RO, math.OC
- **Abstract:** This paper proposes a fully decentralized model predictive control (MPC) framework with control barrier function (CBF) constraints for safety-critical trajectory planning in multi-robot legged systems. The incorporation of CBF constraints introduces explicit inter-agent coupling, which prevents direct decomposition of the resulting optimal control problems.
- **AI 点评:** 多足机器人分布式MPC安全控制框架，涉及四足机器人硬件实验，但使用MPC而非强化学习，且不涉及轮足机器人或sim-to-real。
- 📄 [arXiv](https://arxiv.org/abs/2603.19170v1) | 📥 [PDF](https://arxiv.org/pdf/2603.19170v1)

---

### 5. Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds
- **Score:** 38
- **Categories:** cs.AI, cs.LG, cs.RO
- **Abstract:** The strong performance of large vision-language models (VLMs) trained with reinforcement learning (RL) has motivated similar approaches for fine-tuning vision-language-action (VLA) models in robotics. Many recent works fine-tune VLAs directly in the real world to avoid addressing the sim-to-real gap. While real-world RL circumvents sim-to-real issues, it inherently limits the generality of the resulting VLA, as scaling scene and object diversity in the physical world is prohibitively difficult.
- **AI 点评:** VLA模型的sim-to-real强化学习微调方法，涉及仿真到真实迁移的核心技术，但聚焦操作任务而非轮足机器人运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2603.18532v1) | 📥 [PDF](https://arxiv.org/pdf/2603.18532v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 342 篇 | 通过初筛: 257 篇 | 精选: 5 篇 (含 LLM 精筛)
