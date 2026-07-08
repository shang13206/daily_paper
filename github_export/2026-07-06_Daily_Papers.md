# 🤖 具身智能/机器人学术日报 (2026-07-06)

## 🏆 精选论文 (Top 5)

### 1. DIVO: Continuous-time DVL-Inertial-Visual Odometry for Unmanned Underwater Vehicles
- **Score:** 76
- **Categories:** cs.RO
- **Abstract:** This paper presents a novel acoustic-visual-inertial odometry solution leveraging a continuous-time trajectory estimation framework for unmanned underwater vehicles. Underwater environments present unique challenges for visual localization and mapping, such as light attenuation, illumination variance, and the presence of particulate matter. This motivates the use of additional sensing modalities and a visual tracking pipeline that is robust to diverse subsea conditions.
- **AI 点评:** 面向水下移动机器人的多传感器视觉惯性里程计，直接关联导航、SLAM和状态估计，相关性较高。
- 📄 [arXiv](https://arxiv.org/abs/2607.04615v1) | 📥 [PDF](https://arxiv.org/pdf/2607.04615v1)

---

### 2. WinTA-GIL: Windowed Trajectory Alignment for GNSS-IMU-LiDAR Heading Refinement in Intermittent Signal Environments
- **Score:** 68
- **Categories:** cs.RO
- **Venue:** IROS
- **Abstract:** Although multi-source fusion positioning systems have achieved significant progress, accurate and reliable heading estimation remains a critical challenge due to the lack of gravitational constraints and the inherent weak observability of heading in complex environments. Most existing methodologies are specifically tailored for the startup phase, relying on a singular initial alignment to establish the heading reference.
- **AI 点评:** GNSS-IMU-LiDAR航向 refinement 直接面向导航状态估计与鲁棒定位，和研究方向高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2607.04879v1) | 📥 [PDF](https://arxiv.org/pdf/2607.04879v1)

---

### 3. Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control
- **Score:** 66
- **Categories:** cs.RO
- **Abstract:** Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions.
- **AI 点评:** 直接研究人形机器人whole-body control、策略专家、可部署观测和RL微调，强相关于locomotion控制。
- 📄 [arXiv](https://arxiv.org/abs/2607.04837v1) | 📥 [PDF](https://arxiv.org/pdf/2607.04837v1)

---

### 4. Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies
- **Score:** 62
- **Categories:** cs.CV, cs.RO
- **Venue:** RSS
- **Abstract:** Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer.
- **AI 点评:** 面向VLA导航策略的可通行区域视觉 grounding，和机器人导航感知耦合相关但偏VLA评测。
- 📄 [arXiv](https://arxiv.org/abs/2607.05122v1) | 📥 [PDF](https://arxiv.org/pdf/2607.05122v1)

---

### 5. ECO: Incremental Ego-Centric Octree Update for Point Streams
- **Score:** 53
- **Categories:** cs.RO, cs.GR
- **Abstract:** Constructing octrees for mobile robots that process continuous point streams in real time poses significant computational and memory challenges. Standard global structures often suffer from high latency and unbalanced tree growth. We introduce the Ego-Centric Octree (ECO), a spatial data structure that acts as a 3D sliding window, dynamically bounding the mapping space to the robot's immediate surroundings.
- **AI 点评:** 面向移动机器人点云流的实时局部三维地图结构，直接服务空间感知和导航建图。
- 📄 [arXiv](https://arxiv.org/abs/2607.05092v1) | 📥 [PDF](https://arxiv.org/pdf/2607.05092v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **SLAM: Structured and Localized Analytic Manifold Adaptation for Lifelong VPR** (Score: 49) [Link](https://arxiv.org/abs/2607.04764v1)
- **Multi-Robot Open Adaptive Teaming Across Unseen Environments, Partners, and Scales** (Score: 46) [Link](https://arxiv.org/abs/2607.04972v1)
- **VLM-CASE: Vision-Language Model Enabled Context-Adaptive Safety Envelopes for Anticipatory Safe Autonomous Driving** (Score: 45) [Link](https://arxiv.org/abs/2607.05180v1)
- **Geometry-Aware Visual Odometry for Bronchoscopic Navigation via High-Gain Observer Fusion** (Score: 36) [Link](https://arxiv.org/abs/2607.05162v1)

## 📊 今日统计
- 总抓取: 297 篇 | 通过初筛: 46 篇 | 精选: 5 篇 (含 LLM 精筛)
