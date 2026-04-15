# 🤖 具身智能/机器人学术日报 (2026-04-14)

## 🏆 精选论文 (Top 5)

### 1. Simulator Adaptation for Sim-to-Real Learning of Legged Locomotion via Proprioceptive Distribution Matching
- **Score:** 85
- **Categories:** cs.RO
- **Abstract:** Simulation trained legged locomotion policies often exhibit performance loss on hardware due to dynamics discrepancies between the simulator and the real world, highlighting the need for approaches that adapt the simulator itself to better match hardware behavior. Prior work typically quantify these discrepancies through precise, time-aligned matching of joint and base trajectories. This process requires motion capture, privileged sensing, and carefully controlled initial conditions.
- **AI 点评:** 直接针对四足机器人(Go2)的sim-to-real迁移，提出基于本体感知分布匹配的仿真器适应方法，高度契合sim-to-real、系统辨识和legged locomotion核心研究方向。
- 📄 [arXiv](https://arxiv.org/abs/2604.11090v1) | 📥 [PDF](https://arxiv.org/pdf/2604.11090v1)

---

### 2. AWARE: Adaptive Whole-body Active Rotating Control for Enhanced LiDAR-Inertial Odometry under Human-in-the-Loop Interaction
- **Score:** 67
- **Categories:** cs.RO
- **Abstract:** Human-in-the-loop (HITL) UAV operation is essential in complex and safety-critical aerial surveying environments, where human operators provide navigation intent while onboard autonomy must maintain accurate and robust state estimation. A key challenge in this setting is that resource-constrained UAV platforms are often limited to narrow-field-of-view LiDAR sensors.
- **AI 点评:** 针对UAV提出全身主动偏航控制以增强LiDAR惯性里程计在几何退化场景的鲁棒性，结合MPC+RL框架，与状态估计、LIO鲁棒性及RL控制研究方向中度相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.10598v1) | 📥 [PDF](https://arxiv.org/pdf/2604.10598v1)

---

### 3. MR.ScaleMaster: Scale-Consistent Collaborative Mapping from Crowd-Sourced Monocular Videos
- **Score:** 59
- **Categories:** cs.RO
- **Venue:** IROS
- **Abstract:** Crowd-sourced cooperative mapping from monocular cameras promises scalable 3D reconstruction without specialized sensors, yet remains hindered by two scale-specific failure modes: abrupt scale collapse from false-positive loop closures in repetitive environments, and gradual scale drift over long trajectories and per-robot scale ambiguity that prevent direct multi-session fusion. We present MR.
- **AI 点评:** 多机器人单目相机协同建图与尺度估计，涉及SLAM和多session融合，对移动机器人导航有参考价值，但未直接涉及legged robot或运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2604.11372v1) | 📥 [PDF](https://arxiv.org/pdf/2604.11372v1)

---

### 4. LEADER: Learning Reliable Local-to-Global Correspondences for LiDAR Relocalization
- **Score:** 47
- **Categories:** cs.CV
- **Venue:** CVPR
- **Abstract:** LiDAR relocalization has attracted increasing attention as it can deliver accurate 6-DoF pose estimation in complex 3D environments. Recent learning-based regression methods offer efficient solutions by directly predicting global poses without the need for explicit map storage. However, these methods often struggle in challenging scenes due to their equal treatment of all predicted points, which is vulnerable to noise and outliers.
- **AI 点评:** LiDAR重定位与6-DoF位姿估计，直接服务于移动机器人导航与状态估计，方法和数据集（Oxford RobotCar）与轮足机器人部署场景相关。
- 📄 [arXiv](https://arxiv.org/abs/2604.11355v1) | 📥 [PDF](https://arxiv.org/pdf/2604.11355v1)

---

### 5. CLAW: Composable Language-Annotated Whole-body Motion Generation
- **Score:** 44
- **Categories:** cs.RO
- **Abstract:** Training language-conditioned whole-body controllers for humanoid robots requires large-scale datasets pairing motion trajectories with natural-language descriptions.Existing approaches based on motion capture are costly and limited in diversity, while text-to-motion generative models produce purely kinematic outputs that are not guaranteed to be physically feasible.
- **AI 点评:** 人形机器人全身控制与MuJoCo仿真相关，但核心是语言标注数据生成pipeline，与locomotion policy learning和sim-to-real部署关联较弱。
- 📄 [arXiv](https://arxiv.org/abs/2604.11251v1) | 📥 [PDF](https://arxiv.org/pdf/2604.11251v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **MonoEM-GS: Monocular Expectation-Maximization Gaussian Splatting SLAM** (Score: 43) [Link](https://arxiv.org/abs/2604.10593v1)
- **Modeling, Analysis and Activation of Planar Viscoelastically-combined Rimless Wheels** (Score: 42) [IROS] [Link](https://arxiv.org/abs/2604.11295v1)
- **Robust Adversarial Policy Optimization Under Dynamics Uncertainty** (Score: 37) [Link](https://arxiv.org/abs/2604.10974v1)
- **Safe Human-to-Humanoid Motion Imitation Using Control Barrier Functions** (Score: 37) [Link](https://arxiv.org/abs/2604.11447v1)
- **GeomPrompt: Geometric Prompt Learning for RGB-D Semantic Segmentation Under Missing and Degraded Depth** (Score: 36) [CVPR] [Link](https://arxiv.org/abs/2604.11585v1)

## 📊 今日统计
- 总抓取: 570 篇 | 通过初筛: 73 篇 | 精选: 5 篇 (含 LLM 精筛)
