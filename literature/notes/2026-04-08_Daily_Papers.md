# 🤖 具身智能/机器人学术日报 (2026-04-08)

## 🏆 精选论文 (Top 5)

### 1. FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control
- **Score:** 65
- **Categories:** cs.LG, cs.RO
- **Abstract:** Reinforcement learning (RL) is a core approach for robot control when expert demonstrations are unavailable. On-policy methods such as Proximal Policy Optimization (PPO) are widely used for their stability, but their reliance on narrowly distributed on-policy data limits accurate policy evaluation in high-dimensional state and action spaces.
- **AI 点评:** 提出FlashSAC这一快速稳定的off-policy RL算法，在人形机器人sim-to-real运动控制上大幅缩短训练时间，与研究者核心方向高度契合。
- 📄 [arXiv](https://arxiv.org/abs/2604.04539v1) | 📥 [PDF](https://arxiv.org/pdf/2604.04539v1)

---

### 2. GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields
- **Score:** 56
- **Categories:** cs.RO
- **Abstract:** Learning visuomotor policies for Autonomous Aerial Vehicles (AAVs) relying solely on monocular vision is an attractive yet highly challenging paradigm. Existing end-to-end learning approaches directly map high-dimensional RGB observations to action commands, which frequently suffer from low sample efficiency and severe sim-to-real gaps due to the visual discrepancy between simulation and physical domains.
- **AI 点评:** 面向无人机的视觉运动策略学习框架，结合对比表示学习与RL实现sim-to-real零样本迁移，与研究者关注的sim-to-real和导航方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.05062v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05062v1)

---

### 3. Precise Aggressive Aerial Maneuvers with Sensorimotor Policies
- **Score:** 53
- **Categories:** cs.RO
- **Abstract:** Precise aggressive maneuvers with lightweight onboard sensors remains a key bottleneck in fully exploiting the maneuverability of drones. Such maneuvers are critical for expanding the systems' accessible area by navigating through narrow openings in the environment. Among the most relevant problems, a representative one is aggressive traversal through narrow gaps with quadrotors under SE(3) constraints, which require the quadrotors to leverage a momentary tilted attitude and the asymmetry of the...
- **AI 点评:** 无人机RL策略学习+端到端sim-to-real，研究窄缝穿越等高难度机动，方法论与locomotion policy learning高度相似，有实机验证。
- 📄 [arXiv](https://arxiv.org/abs/2604.05828v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05828v1)

---

### 4. Instantaneous Planning, Control and Safety for Navigation in Unknown Underwater Spaces
- **Score:** 49
- **Categories:** cs.RO
- **Venue:** TRO
- **Abstract:** Navigating autonomous underwater vehicles (AUVs) in unknown environments is significantly challenging due to poor visibility, weak signal transmission, and dynamic water currents. These factors pose challenges in accurate global localization, reliable communication, and obstacle avoidance. Local sensing provides critical real time environmental data to enable online decision making.
- **AI 点评:** 针对未知水下环境的AUV规划与控制框架，涉及障碍回避和轨迹控制，属于导航与运动控制范畴，但平台为水下无人机且无RL方法，与核心研究方向有一定距离。
- 📄 [arXiv](https://arxiv.org/abs/2604.05310v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05310v1)

---

### 5. Differentiable Invariant Sets for Hybrid Limit Cycles with Application to Legged Robots
- **Score:** 44
- **Categories:** eess.SY, cs.RO
- **Abstract:** For hybrid systems exhibiting periodic behavior, analyzing the invariant set containing the limit cycle is a natural way to study the robustness of the closed-loop system. However, computing these sets can be computationally expensive, especially when applied to contact-rich cyber-physical systems such as legged robots.
- **AI 点评:** 针对双足机器人混合周期轨道的前向不变集计算方法，涉及步态鲁棒性分析，与腿足运动控制相关但偏理论验证，无RL或实机实验。
- 📄 [arXiv](https://arxiv.org/abs/2604.05108v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05108v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **A Co-Design Framework for High-Performance Jumping of a Five-Bar Monoped with Actuator Optimization** (Score: 36) [Link](https://arxiv.org/abs/2604.06025v1)
- **MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot Systems** (Score: 35) [Link](https://arxiv.org/abs/2604.05499v1)
- **Visual Prompt Based Reasoning for Offroad Mapping using Multimodal LLMs** (Score: 35) [Link](https://arxiv.org/abs/2604.04564v1)
- **Finite-Step Invariant Sets for Hybrid Systems with Probabilistic Guarantees** (Score: 34) [Link](https://arxiv.org/abs/2604.05102v1)
- **AnyImageNav: Any-View Geometry for Precise Last-Meter Image-Goal Navigation** (Score: 31) [Link](https://arxiv.org/abs/2604.05351v1)
- **LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios** (Score: 31) [RA-L] [Link](https://arxiv.org/abs/2604.05402v1)

## 📊 今日统计
- 总抓取: 507 篇 | 通过初筛: 359 篇 | 精选: 5 篇 (含 LLM 精筛)
