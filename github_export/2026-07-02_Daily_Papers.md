# 🤖 具身智能/机器人学术日报 (2026-07-02)

## 🏆 精选论文 (Top 5)

### 1. Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots
- **Score:** 96
- **Categories:** cs.RO, math.OC
- **Venue:** IROS
- **Abstract:** This paper presents a novel layered planning and control framework based on multi-rate nonlinear model predictive control (MR-NMPC) that enables quadrupedal robots to perform hybrid bipedal locomotion with wall-assisted support in constrained environments. Real-time trajectory optimization for this locomotion presents significant challenges, as the controller must simultaneously plan for both the contact points and the continuous trajectories of the robot's center of mass (CoM) and orientation w...
- **AI 点评:** 直接面向四足机器人复杂接触运动、NMPC、WBC和粗糙地形，通过Unitree A1仿真验证，高度契合核心方向。
- 📄 [arXiv](https://arxiv.org/abs/2607.01574v1) | 📥 [PDF](https://arxiv.org/pdf/2607.01574v1)

---

### 2. Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning
- **Score:** 90
- **Categories:** cs.RO
- **Abstract:** Sim-to-real transfer in robot learning is often limited by discrepancies between the ideal actuator dynamics assumed during policy training and the nonlinear, hardware-dependent behavior of physical motors. While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learned actuator models, we introduce an alternative paradigm: actuator reality shaping.
- **AI 点评:** 直接面向机器人学习的零样本sim-to-real执行器接口，并覆盖轮足机器人和人形行走，非常契合核心方向。
- 📄 [arXiv](https://arxiv.org/abs/2607.02205v1) | 📥 [PDF](https://arxiv.org/pdf/2607.02205v1)

---

### 3. A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity
- **Score:** 71
- **Categories:** cs.CV, cs.RO
- **Abstract:** This paper presents OCD SLAM, a dynamic stereo visual SLAM framework that extends ORB-SLAM2 by jointly addressing dynamic objects and dynamic features in the scene. Usual visual SLAM systems operating in dynamic environments often fail in the presence of moving objects, due to the static-world assumption used in pose estimation and mapping.
- **AI 点评:** 动态环境下的立体视觉SLAM直接关联机器人导航、定位与建图，是高相关感知方向。
- 📄 [arXiv](https://arxiv.org/abs/2607.02005v1) | 📥 [PDF](https://arxiv.org/pdf/2607.02005v1)

---

### 4. DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability
- **Score:** 70
- **Categories:** cs.CV, cs.RO
- **Abstract:** Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in dense dynamic Simultaneous Localization And Mapping (SLAM). Prevailing methods typically discard predefined dynamic objects, ignoring that transiently static objects offer valuable geometric constraints for pose estimation. A recent work attempts to leverage this potential by employing per-pixel uncertainty maps to quantify the magnitude of motion.
- **AI 点评:** 动态环境中的高保真Gaussian Splatting SLAM直接服务定位与建图，和机器人导航感知高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2607.01860v1) | 📥 [PDF](https://arxiv.org/pdf/2607.01860v1)

---

### 5. DL-VINS-Factory: A Modular Framework for Learned Visual Front-Ends in Visual-Inertial SLAM
- **Score:** 68
- **Categories:** cs.CV, cs.RO
- **Abstract:** Deep-learning features excel in visual matching, yet their practical value in tightly coupled visual-inertial SLAM (VI-SLAM) remains insufficiently characterized. We present DL-VINS-Factory, a unified framework that integrates learned feature extractors (ALIKED, RaCo, SuperPoint, XFeat) with either Lucas--Kanade (LK) optical-flow tracking or LightGlue (LG) descriptor matching.
- **AI 点评:** 学习型视觉前端VI-SLAM、实时嵌入式部署和ROS2实现高度契合状态估计与机器人导航需求。
- 📄 [arXiv](https://arxiv.org/abs/2607.01757v1) | 📥 [PDF](https://arxiv.org/pdf/2607.01757v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **SPLC: Social Preference Learning for Crowd Robot Navigation** (Score: 60) [Link](https://arxiv.org/abs/2607.01925v1)
- **Path planning for unmanned naval surface vehicles** (Score: 41) [Link](https://arxiv.org/abs/2607.01631v1)
- **Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation** (Score: 37) [Link](https://arxiv.org/abs/2607.02298v1)

## 📊 今日统计
- 总抓取: 289 篇 | 通过初筛: 39 篇 | 精选: 5 篇 (含 LLM 精筛)
