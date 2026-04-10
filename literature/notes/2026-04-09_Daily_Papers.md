# 🤖 具身智能/机器人学术日报 (2026-04-09)

## 🏆 精选论文 (Top 5)

### 1. Robust Quadruped Locomotion via Evolutionary Reinforcement Learning
- **Score:** 70
- **Categories:** cs.RO
- **Venue:** TRO
- **Abstract:** Deep reinforcement learning has recently achieved strong results in quadrupedal locomotion, yet policies trained in simulation often fail to transfer when the environment changes. Evolutionary reinforcement learning aims to address this limitation by combining gradient-based policy optimisation with population-driven exploration. This work evaluates four methods on a simulated walking task: DDPG, TD3, and two Cross-Entropy-based variants CEM-DDPG and CEM-TD3.
- **AI 点评:** 四足运动控制+RL与进化算法结合，研究sim-to-real鲁棒性和terrain transfer，与核心方向高度相关，但缺乏实机验证且发表venue不明。
- 📄 [arXiv](https://arxiv.org/abs/2604.07224v1) | 📥 [PDF](https://arxiv.org/pdf/2604.07224v1)

---

### 2. Precise Aggressive Aerial Maneuvers with Sensorimotor Policies
- **Score:** 53
- **Categories:** cs.RO
- **Abstract:** Precise aggressive maneuvers with lightweight onboard sensors remains a key bottleneck in fully exploiting the maneuverability of drones. Such maneuvers are critical for expanding the systems' accessible area by navigating through narrow openings in the environment. Among the most relevant problems, a representative one is aggressive traversal through narrow gaps with quadrotors under SE(3) constraints, which require the quadrotors to leverage a momentary tilted attitude and the asymmetry of the...
- **AI 点评:** 无人机通过窄缝的感知运动策略，使用RL+sim-to-real，与研究者的核心方法高度一致，虽平台为无人机但技术路线直接可借鉴。
- 📄 [arXiv](https://arxiv.org/abs/2604.05828v2) | 📥 [PDF](https://arxiv.org/pdf/2604.05828v2)

---

### 3. Instantaneous Planning, Control and Safety for Navigation in Unknown Underwater Spaces
- **Score:** 43
- **Categories:** cs.RO
- **Venue:** TRO
- **Abstract:** Navigating autonomous underwater vehicles (AUVs) in unknown environments is significantly challenging due to poor visibility, weak signal transmission, and dynamic water currents. These factors pose challenges in accurate global localization, reliable communication, and obstacle avoidance. Local sensing provides critical real time environmental data to enable online decision making.
- **AI 点评:** 水下无人机的规划与控制框架，涉及障碍回避和导航，与研究方向有一定关联但平台和场景差异较大。
- 📄 [arXiv](https://arxiv.org/abs/2604.05310v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05310v1)

---

### 4. MARS-Dragonfly: Agile and Robust Flight Control of Modular Aerial Robot Systems
- **Score:** 35
- **Categories:** cs.RO, eess.SY
- **Abstract:** Modular Aerial Robot Systems (MARS) comprise multiple drone units with reconfigurable connected formations, providing high adaptability to diverse mission scenarios, fault conditions, and payload capacities. However, existing control algorithms for MARS rely on simplified quasi-static models and rule-based allocation, which generate discontinuous and unbounded motor commands.
- **AI 点评:** 模块化无人机系统的飞行控制，涉及预测控制与动态分配，有一定方法借鉴价值，但与腿足/轮足运动控制方向相关性有限。
- 📄 [arXiv](https://arxiv.org/abs/2604.05499v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05499v1)

---

### 5. LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios
- **Score:** 33
- **Categories:** cs.CV, cs.RO
- **Venue:** RA-L
- **Abstract:** Visual localization in large-scale UAV scenarios is a critical capability for autonomous systems, yet it remains challenging due to geometric complexity and environmental variations. While 3D Gaussian Splatting (3DGS) has emerged as a promising scene representation, existing 3DGS-based visual localization methods struggle with robust pose initialization and sensitivity to rendering artifacts in large-scale settings.
- **AI 点评:** 面向大规模UAV场景的视觉定位方法，涉及无人机导航相关的位姿估计，与导航方向有一定关联但缺乏运动控制深度。
- 📄 [arXiv](https://arxiv.org/abs/2604.05402v1) | 📥 [PDF](https://arxiv.org/pdf/2604.05402v1)

---

## 👀 值得关注 (Score >= 30 的其余论文)

- **A Co-Design Framework for High-Performance Jumping of a Five-Bar Monoped with Actuator Optimization** (Score: 32) [Link](https://arxiv.org/abs/2604.06025v1)
- **Differentiable Environment-Trajectory Co-Optimization for Safe Multi-Agent Navigation** (Score: 31) [Link](https://arxiv.org/abs/2604.06972v1)
- **Robots that learn to evaluate models of collective behavior** (Score: 31) [Link](https://arxiv.org/abs/2604.07303v1)

## 📊 今日统计
- 总抓取: 66 篇 | 通过初筛: 64 篇 | 精选: 5 篇 (含 LLM 精筛)
