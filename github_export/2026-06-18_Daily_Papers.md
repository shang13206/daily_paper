# 🤖 具身智能/机器人学术日报 (2026-06-18)

## 🏆 精选论文 (Top 5)

### 1. SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour
- **Score:** 72
- **Categories:** cs.RO
- **Abstract:** While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model.
- **AI 点评:** 直接面向四足机器人敏捷parkour、世界模型、对称先验、真实部署和地形泛化，和OmniBot locomotion学习高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.19928v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19928v1)

---

### 2. MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM
- **Score:** 71
- **Categories:** cs.CV, cs.RO
- **Venue:** ICRA
- **Abstract:** 3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to inconsistent maps.
- **AI 点评:** 视觉SLAM、结构化建图和位姿优化与移动机器人导航/建图强相关，但未直接耦合腿式控制或部署。
- 📄 [arXiv](https://arxiv.org/abs/2606.19874v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19874v1)

---

### 3. ForEnt: A Multi-Modal Dataset for Characterizing Quadruped Robot Entrapments in Forest Environments
- **Score:** 67
- **Categories:** cs.RO
- **Abstract:** Legged robots are increasingly deployed in forests for ecological surveying and monitoring, yet their autonomy is often interrupted consequent to the challenges posed in traversing forest environments. Forest entrapments, for example, when a robot's legs are ensnared in vines or other vegetation, result in loss of stability and toppling. Such events not only disrupt the mission and require manual intervention, but also risk damage to the robot hardware.
- **AI 点评:** Unitree Go2四足机器人森林困陷多模态数据集，直接服务粗糙自然环境下的感知、地形适应与鲁棒部署。
- 📄 [arXiv](https://arxiv.org/abs/2606.19675v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19675v1)

---

### 4. TIDY: Thermal Infrared Image Denoising via Wavelet Domain Entropy and Directional Stripe Index
- **Score:** 62
- **Categories:** cs.RO
- **Abstract:** Thermal infrared (TIR) imaging has been a popular choice for field robotics due to its robust perception capability under low light visual degradation, but it suffers from severe stochastic and fixed-pattern noise that breaks downstream estimation. This noise is intensified indoors due to low thermal contrast and uniform temperature distributions, contributing to the relative lack of indoor TIR deployments.
- **AI 点评:** 面向field robotics的热红外去噪，并验证对热惯性里程计和深度估计的下游增益，和鲁棒感知导航较相关。
- 📄 [arXiv](https://arxiv.org/abs/2606.19813v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19813v1)

---

### 5. Route-Constrained Robust Fusion Estimation for MEMS/GNSS Integrated Navigation of Unmanned Ground Vehicles in GNSS Degraded Environments
- **Score:** 61
- **Categories:** cs.RO
- **Venue:** ICRA
- **Abstract:** To address cumulative localization drift of unmanned ground vehicles in structured road environments under severe Global Navigation Satellite System signal occlusion, this paper proposes a robust route-constrained state estimation method. During periods without satellite signals, the proposed method establishes the correspondence between the historical dead reckoning trajectory and local segments of the mission route extracted from a high-definition map, and estimates a route-referenced position...
- **AI 点评:** 面向UGV在GNSS退化环境下的融合定位与路线约束状态估计，和导航/部署相关，但不涉及足式运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2606.19687v1) | 📥 [PDF](https://arxiv.org/pdf/2606.19687v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **Comparative Study on Agility, Efficiency, and Impact Absorption of Bipedal Robots with Active Toes** (Score: 55) [Link](https://arxiv.org/abs/2606.19699v1)
- **An Infrastructure-less, Control-Independent Solution to Relative Localisation of a Team of Mobile Robots using Ranging Measurements** (Score: 53) [Link](https://arxiv.org/abs/2606.20365v1)
- **Towards 3D karst underwater scene reconstruction from rotating sonar data** (Score: 51) [Link](https://arxiv.org/abs/2606.20322v1)
- **Motor Angular Speed Preintegration for Multirotor UAV State Estimation** (Score: 50) [Link](https://arxiv.org/abs/2606.19929v1)
- **Safe Local Navigation for Ackermann-Steered Robots in Unmapped Environments** (Score: 43) [Link](https://arxiv.org/abs/2606.19672v1)
- **Stable Transformer-Actor-Critic Model Predictive Control: A Contraction Analysis Approach** (Score: 40) [Link](https://arxiv.org/abs/2606.20197v1)
- **HilDA: Hierarchical Distillation with Diffusion for Advancing Self-Supervised LiDAR Pre-trainin** (Score: 39) [ECCV] [Link](https://arxiv.org/abs/2606.20189v1)
- **Deep-Unfolded Coordination** (Score: 37) [Link](https://arxiv.org/abs/2606.19920v1)

## 📊 今日统计
- 总抓取: 268 篇 | 通过初筛: 48 篇 | 精选: 5 篇 (含 LLM 精筛)
