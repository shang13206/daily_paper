# 🤖 具身智能/机器人学术日报 (2026-07-09)

## 🏆 精选论文 (Top 5)

### 1. RadLoc: Radar-based 3-DoF Global Localization via Fast, Robust, and Lightweight Spatial Descriptor Across Diverse Environmental Scenarios
- **Score:** 63
- **Categories:** cs.RO
- **Abstract:** While global localization using spinning radar has gained attention for its robustness to adverse weather and challenging environments, many studies have focused on individual components such as place recognition or pose estimation. In this paper, we take a holistic view of radar sensor-based global localization and present RadLoc, a fast, robust, and lightweight end-to-end pipeline from place recognition to 3-DoF pose estimation.
- **AI 点评:** 雷达全局定位可直接用于 SLAM 和多会话定位，和机器人导航、状态估计高度相关。
- 📄 [arXiv](https://arxiv.org/abs/2607.08115v1) | 📥 [PDF](https://arxiv.org/pdf/2607.08115v1)

---

### 2. D-CLIPSE: Distributed Consensus-based Localization with Passive Listening on Shared State Exchange
- **Score:** 58
- **Categories:** cs.RO
- **Venue:** Robotics and Automation Letters
- **Abstract:** Multi-robot localization that is accurate and consistent is imperative for downstream tasks such as planning and control. Centralized filtering approaches optimally fuse all available sensor measurements of the team. However, a centralized solution is rarely implementable due to hardware, communication, and computational constraints. Distributed approaches deploy a filter on each robot to estimate their own state and neighbours' states using inter-robot communication.
- **AI 点评:** 多机器人分布式定位与一致性状态估计对导航和控制有直接支撑，但未涉及轮足/四足运动控制、地形适应或实机locomotion部署。
- 📄 [arXiv](https://arxiv.org/abs/2607.07995v1) | 📥 [PDF](https://arxiv.org/pdf/2607.07995v1)

---

### 3. EVIS: A Physics-Grounded Event Camera Plugin for NVIDIA Isaac Sim
- **Score:** 48
- **Categories:** cs.CV, cs.RO
- **Abstract:** Event cameras offer microsecond temporal resolution, low latency, and high dynamic range, making them attractive for robotics. However, labeled event-camera data for a specific robot and scene is scarce and expensive to collect, which slows the development of event-based perception and control. We present EVIS: a physics-grounded event camera plugin for NVIDIA Isaac Sim that generates high-rate, fully labeled event streams directly inside a physics simulator.
- **AI 点评:** Isaac Sim/Isaac Lab 事件相机插件有助于机器人感知仿真和数据生成，但未直接落到 locomotion 或导航策略。
- 📄 [arXiv](https://arxiv.org/abs/2607.08098v1) | 📥 [PDF](https://arxiv.org/pdf/2607.08098v1)

---

### 4. On Exploring Input Resolution Scaling For Anytime LiDAR Object Detection
- **Score:** 43
- **Categories:** cs.LG, cs.RO
- **Abstract:** Making tradeoffs between execution latency and result utility (i.e., anytime computing) for adapting to dynamic operational requirements has been shown to enhance the performance of cyber-physical systems. In this work, we focus on enabling anytime computing for deep neural networks (DNNs) that process LiDAR point clouds for 3D object detection.
- **AI 点评:** LiDAR 感知服务自动驾驶避障导航，和机器人感知-导航闭环相关，但不涉及足式/轮足运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2607.08391v1) | 📥 [PDF](https://arxiv.org/pdf/2607.08391v1)

---

### 5. FSD-VLN: Fast-Slow Dual-System Modeling for Aerial Long-Horizon Vision-Language Navigation
- **Score:** 37
- **Categories:** cs.AI, cs.RO
- **Abstract:** Vision-Language Navigation (VLN) enables UAV autonomous navigation in unknown environments by mapping language instructions to real-time visual inputs. Compared with GPS-dependent or pre-programmed navigation, VLN supports intuitive human-machine interaction and stronger environmental adaptability, requiring tight integration of high-level semantic reasoning and low-latency flight control.
- **AI 点评:** 面向 UAV 长航程视觉语言导航并包含低延迟飞控输出，导航相关但偏 VLN/语义决策而非机器人运动控制。
- 📄 [arXiv](https://arxiv.org/abs/2607.08359v1) | 📥 [PDF](https://arxiv.org/pdf/2607.08359v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

_今日无其他值得关注论文_

## 📊 今日统计
- 总抓取: 250 篇 | 通过初筛: 32 篇 | 精选: 5 篇 (含 LLM 精筛)
