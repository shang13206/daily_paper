# 🤖 具身智能/机器人学术日报 (2026-06-11)

## 🏆 精选论文 (Top 5)

### 1. Redesigning Regularization for Effective Policy Smoothing
- **Score:** 75
- **Categories:** cs.RO
- **Venue:** RA-L
- **Abstract:** This paper proposes a novel regularization design to effectively smooth policy functions in reinforcement learning. While regularization that enhances ``global'' Lipschitz continuity was initially considered, it has been limited to ``local'' Lipschitz continuity due to a tradeoff between smoothness and expressiveness. However, it has become apparent that the original implementation is cumbersome and does not provide sufficient smoothing, leading to a preference for simpler implementations.
- **AI 点评:** 直接研究 RL policy smoothing 并应用于四足机器人 sim-to-real，提高运动平滑性和速度突变鲁棒性，契合 locomotion policy learning。
- 📄 [arXiv](https://arxiv.org/abs/2606.13169v1) | 📥 [PDF](https://arxiv.org/pdf/2606.13169v1)

---

### 2. NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation
- **Score:** 72
- **Categories:** cs.RO, cs.CV
- **Abstract:** Goal-conditioned visual navigation requires a robot to act under partial observability by anticipating how its motion will change the future egocentric view and whether that change brings it closer to the goal. Navigation world models provide such visual foresight, but they remain prediction modules that require an external planner to convert predicted futures into closed-loop control.
- **AI 点评:** 视觉导航世界模型直接转化为闭环机器人控制，并含仿真预训练与实机适配，和导航-感知-控制一体化高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.13494v1) | 📥 [PDF](https://arxiv.org/pdf/2606.13494v1)

---

### 3. Proprioceptive-visual correspondence enables self-other distinction in humanoid robots
- **Score:** 45
- **Categories:** cs.AI, cs.RO
- **Abstract:** Distinguishing self from others is a prerequisite for social intelligence, yet humanoid robots that increasingly share workspaces with humans still lack this ability. Here we show that a humanoid robot can learn self-other distinction from proprioceptive-visual correspondence, without any identity labels or kinematic models.
- **AI 点评:**  humanoid 自我建模可支持碰撞感知规划和运动规划，但重点偏自他区分与人形社交场景，非核心 locomotion/导航。
- 📄 [arXiv](https://arxiv.org/abs/2606.13222v1) | 📥 [PDF](https://arxiv.org/pdf/2606.13222v1)

---

### 4. Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants
- **Score:** 41
- **Categories:** cs.RO
- **Abstract:** Quadruped robots are capable of traversing a wide range of complex terrains with high flexibility. As highly mobile ground-based intelligent platforms, they can be equipped with modules for navigation control, environmental perception, and intelligent interaction, thereby serving as real-world mobile deployment platforms for various algorithms. In this paper, we introduce Y-BotFrame, an extensible embodied platform that turns a robot into an intelligent ground assistant.
- **AI 点评:** 基于四足机器人的具身助手框架包含导航、感知和实机部署，但核心偏 LLM 任务规划与交互，不是 locomotion policy 学习。
- 📄 [arXiv](https://arxiv.org/abs/2606.13049v1) | 📥 [PDF](https://arxiv.org/pdf/2606.13049v1)

---

### 5. Embedding ISO 10218 Safety Compliance in Robots via Control Barrier Functions for Human-Robot Collaboration
- **Score:** 33
- **Categories:** cs.RO
- **Abstract:** Human-Robot Collaboration (HRC) requires strict adherence to safety standards, such as ISO 10218, to prevent harmful interactions. Standard Speed and Separation Monitoring (SSM) filters calculate safe robotic speeds based on conservative assumptions, such as constant human velocity, which prevents accurate predictions of minimum separation distances and causes unnecessary operational halts.
- **AI 点评:** CBF 安全控制与真实机器人实验相关，但对象是协作机械臂安全合规，和轮足/四足运动控制关系较弱。
- 📄 [arXiv](https://arxiv.org/abs/2606.13203v1) | 📥 [PDF](https://arxiv.org/pdf/2606.13203v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 220 篇 | 通过初筛: 33 篇 | 精选: 5 篇 (含 LLM 精筛)
