# 🤖 具身智能/机器人学术日报 (2026-06-25)

## 🏆 精选论文 (Top 5)

### 1. Ordinal Neural Collapse as a Representation Prior for Visual Navigation
- **Score:** 70
- **Categories:** cs.CV, cs.RO
- **Abstract:** Learning robust navigation policies directly from visual observations remains a fundamental challenge in vision-based robotic navigation. In end-to-end imitation learning approaches, the visual encoder and action decoder are jointly optimized using a single action loss, which provides only an indirect supervisory signal to the encoder. This indirect supervision frequently results in the encoder learning ambiguous, action-agnostic representations.
- **AI 点评:** 视觉导航策略、真实场景验证和感知表征服务控制决策，与移动机器人导航方向紧密相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.26839v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26839v1)

---

### 2. A Closed-Form 4-DoF Inter-Robot Pose Estimator using Bearing-only Measurements
- **Score:** 64
- **Categories:** cs.RO
- **Abstract:** Bearing-odometry-based cooperative localization has attracted increasing research interest due to its minimal infrastructure requirements, low communication bandwidth and broad applicability in complex environments. However, existing 6-DoF approaches still face challenges in rapidly obtaining accurate and reliable inter-robot pose estimation, as the system is prone to observability degeneracy under specific motion patterns.
- **AI 点评:** 面向多机器人协同定位的 bearing-only 位姿估计，直接关联机器人导航、状态估计和实机实验。
- 📄 [arXiv](https://arxiv.org/abs/2606.26616v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26616v1)

---

### 3. UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping
- **Score:** 62
- **Categories:** cs.RO, cs.SI
- **Venue:** RA-L
- **Abstract:** Large-scale point cloud maps are essential for robotics and spatial intelligence tasks. UAVs provide an efficient means for large-scale map acquisition; however, due to limited flight endurance and onboard storage, mapping a large-scale scene within a single flight remains difficult. Existing multi-session map merging methods can extend the mapping range, yet in UAV scenarios they still struggle to simultaneously suppress long-range drift and preserve local geometric accuracy.
- **AI 点评:** UAV多会话点云建图、RTK对齐和因子图优化与机器人SLAM和导航地图构建高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.26928v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26928v1)

---

### 4. IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control
- **Score:** 55
- **Categories:** cs.AI, cs.RO
- **Abstract:** Complex multi-agent control tasks remain challenging for traditional rule-based and model-based approaches, motivating the adoption of learning-based methods. However, learning-based methods often struggle with sim-to-real transfer because they rely on accurate dynamics modeling or system identification and learn policies in low-level control spaces that are highly sensitive to dynamics mismatch, making them costly and fragile in complex environments.
- **AI 点评:** 聚焦多智能体导航任务中的 sim-to-real 与动力学失配鲁棒性，和部署型机器人学习较相关但不特指轮足/四足。
- 📄 [arXiv](https://arxiv.org/abs/2606.26575v1) | 📥 [PDF](https://arxiv.org/pdf/2606.26575v1)

---

### 5. PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views
- **Score:** 50
- **Categories:** cs.CV
- **Venue:** IROS
- **Abstract:** Panoramic sensing offers wide field-of-view coverage, yet 3D reconstruction from sparse panoramas remains challenging under rotation-dominant, weak-parallax motion. In such regimes, SfM/SLAM initialization is often ill-conditioned and unreliable. We present PanoImager, an SfM-free framework that combines feed-forward pose/depth priors, geometry-conditioned diffusion view completion, and depth-guided 3DGS optimization.
- **AI 点评:** 稀疏全景重建和SLAM失败时地图细化与机器人建图导航相关，但偏离运动控制和实机策略学习。
- 📄 [arXiv](https://arxiv.org/abs/2606.27071v1) | 📥 [PDF](https://arxiv.org/pdf/2606.27071v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 240 篇 | 通过初筛: 39 篇 | 精选: 5 篇 (含 LLM 精筛)
