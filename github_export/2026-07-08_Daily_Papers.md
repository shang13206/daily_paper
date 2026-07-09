# 🤖 具身智能/机器人学术日报 (2026-07-08)

## 🏆 精选论文 (Top 5)

### 1. GemNav: Discrete-Token Visual Robot Navigation using a Multimodal Large Language Model
- **Score:** 82
- **Categories:** cs.AI, cs.RO
- **Abstract:** Visual navigation policies built on large pretrained models have so far followed a common recipe: a dedicated visual encoder, a bespoke action head, and training on thousands of hours of cross-embodiment datasets. We ask whether this recipe is necessary. In this paper, we introduce GemNav, a visual robot navigation policy that adapts a frozen Multimodal Large Language Model (MLLM) for short-to-medium horizon waypoint navigation using Low-Rank Adaptation (LoRA) on the language tower alone, with n...
- **AI 点评:** 面向真实机器人视觉导航的可部署策略，与导航和感知-决策耦合高度相关，但偏MLLM导航而非轮足/四足locomotion核心。
- 📄 [arXiv](https://arxiv.org/abs/2607.06882v1) | 📥 [PDF](https://arxiv.org/pdf/2607.06882v1)

---

### 2. Dynamic Object Detection and Tracking in Construction: A Fisheye Camera and LiDAR Sensor Fusion Model
- **Score:** 81
- **Categories:** cs.RO, cs.CV
- **Venue:** ICRA
- **Abstract:** Robust dynamic object detection and tracking are essential for enabling robots to operate safely and effectively alongside humans in complex environments such as construction sites. While LiDAR-based SLAM and occupancy grid methods offer viable solutions for detecting and tracking motion, many state-of-the-art 3D vision approaches rely heavily on pre-trained neural networks and require additional post-processing to identify moving objects.
- **AI 点评:** 四足机器人上的LiDAR-鱼眼相机融合动态目标检测与跟踪，直接服务真实场景导航/安全感知部署，但不涉及运动控制或策略学习。
- 📄 [arXiv](https://arxiv.org/abs/2607.06896v1) | 📥 [PDF](https://arxiv.org/pdf/2607.06896v1)

---

### 3. PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments
- **Score:** 77
- **Categories:** cs.RO
- **Venue:** IROS
- **Abstract:** Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliability of features.
- **AI 点评:** 事件相机VIO/SLAM面向动态环境下鲁棒状态估计，直接契合导航、感知和状态估计方向。
- 📄 [arXiv](https://arxiv.org/abs/2607.07374v1) | 📥 [PDF](https://arxiv.org/pdf/2607.07374v1)

---

### 4. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM
- **Score:** 64
- **Categories:** cs.RO
- **Abstract:** Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering.
- **AI 点评:** 密集单目SLAM与几何建图直接服务导航和避障，和机器人感知-导航链路强相关，但不涉及运动控制或部署。
- 📄 [arXiv](https://arxiv.org/abs/2607.07452v1) | 📥 [PDF](https://arxiv.org/pdf/2607.07452v1)

---

### 5. HumAIN: Human-Aware Implicit Social Robot Navigation
- **Score:** 62
- **Categories:** cs.AI, cs.RO
- **Venue:** IROS
- **Abstract:** Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation.
- **AI 点评:** 面向社交机器人导航，将人体姿态线索融入规划闭环，与移动机器人导航和部署效率较相关。
- 📄 [arXiv](https://arxiv.org/abs/2607.07357v1) | 📥 [PDF](https://arxiv.org/pdf/2607.07357v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Disturbance-aware Motion Planning for Over-actuated Underwater Vehicles Exploiting Actuation Redundancy for High-fidelity 3D Reconstruction** (Score: 45) [Link](https://arxiv.org/abs/2607.07139v1)
- **Residual-Conservative Model Predictive Path Integral Control** (Score: 40) [Link](https://arxiv.org/abs/2607.06950v1)
- **Safe Reinforcement Learning using Ideas from Model Predictive Control** (Score: 37) [Link](https://arxiv.org/abs/2607.07252v1)

## 📊 今日统计
- 总抓取: 191 篇 | 通过初筛: 32 篇 | 精选: 5 篇 (含 LLM 精筛)
