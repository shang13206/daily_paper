# 🤖 具身智能/机器人学术日报 (2026-06-05)

## 🏆 精选论文 (Top 5)

### 1. CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation
- **Score:** 90
- **Categories:** cs.AI, cs.RO
- **Abstract:** Humans primarily rely on walking and running to traverse complex terrains, without resorting to unnecessarily complex motion patterns. Similarly, humanoid robots should achieve smooth transitions between walking and running while maintaining natural and stable locomotion. However, unifying gait transition and multi-terrain adaptation within a single policy remains challenging due to gradient interference and the distribution shift induced by terrain-dependent visual and dynamic variations.
- **AI 点评:** 多地形人形locomotion、RL gait adaptation、MoE策略和Unitree G1零样本实机部署高度契合地形适应与可部署机器人学习。
- 📄 [arXiv](https://arxiv.org/abs/2606.04718v1) | 📥 [PDF](https://arxiv.org/pdf/2606.04718v1)

---

### 2. HORIZON: Recoverability-Governed Curriculum for Physical-Domain Scaling
- **Score:** 73
- **Categories:** cs.RO
- **Abstract:** Scaling robust robot policies requires more than broader randomization, because physical-domain experience must remain organized and learnable throughout training. We study when a policy can benefit from harder physics and identify recoverability as a central constraint in on-policy physical-domain scaling.
- **AI 点评:** 直接研究四足 locomotion 策略在物理域随机化中的可恢复课程学习，与鲁棒运动控制和 sim-to-real 高度契合。
- 📄 [arXiv](https://arxiv.org/abs/2606.05143v1) | 📥 [PDF](https://arxiv.org/pdf/2606.05143v1)

---

### 3. M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking
- **Score:** 72
- **Categories:** cs.RO
- **Abstract:** Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on distinct motion reference modalities: locomotion primarily depends on coordinated robot joint trajectories, whereas manipulation requires precise end-effector trajectory tracking.
- **AI 点评:** 人形机器人多模态 whole-body controller 与 sim-to-real 强相关，虽非四足/轮足但契合全身控制和 locomotion 学习。
- 📄 [arXiv](https://arxiv.org/abs/2606.04829v1) | 📥 [PDF](https://arxiv.org/pdf/2606.04829v1)

---

### 4. Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation
- **Score:** 70
- **Categories:** cs.RO, eess.SY
- **Abstract:** In humanoid motion control, model predictive control (MPC) offers physically grounded prediction and constraint handling, while reinforcement learning (RL) enables robust whole-body skills through large-scale simulation. However, using MPC inside RL often requires time-consuming problem construction or excessive training overhead, making such frameworks difficult to justify in practice.
- **AI 点评:** MPC 指导 RL 的人形 locomotion 与硬件验证直接相关，对 whole-body control、训练加速和部署有较高价值。
- 📄 [arXiv](https://arxiv.org/abs/2606.05687v1) | 📥 [PDF](https://arxiv.org/pdf/2606.05687v1)

---

### 5. TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion
- **Score:** 69
- **Categories:** cs.RO
- **Abstract:** Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local geometry understanding. Motivated by the way humans selectively look at relevant terrain during locomotion, we introduce TAGA, a Terrain-aware Active Gaze learning framework for Attention-based humanoid control.
- **AI 点评:** 高度契合感知驱动的类人敏捷 locomotion、地形适应、RL 训练与实机部署，对 OmniBot 的感知-控制耦合很有参考价值。
- 📄 [arXiv](https://arxiv.org/abs/2606.05880v1) | 📥 [PDF](https://arxiv.org/pdf/2606.05880v1)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **MAD: Mapping-Aware World Models for Agile Quadrotor Flight** (Score: 68) [Link](https://arxiv.org/abs/2606.04534v1)
- **Learning Contact Representation for Leg Odometry** (Score: 66) [Link](https://arxiv.org/abs/2606.05501v1)
- **MineXplore: An Open-Source Reinforcement Learning Exploration Benchmark for GNSS-Denied Underground Environment** (Score: 66) [ICRA] [Link](https://arxiv.org/abs/2606.04569v1)
- **Teaching Robots to Say 'I Don't Know' : SENTINEL for Uncertainty-Aware SLAM** (Score: 66) [ICRA] [Link](https://arxiv.org/abs/2606.04853v1)
- **WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation** (Score: 66) [Link](https://arxiv.org/abs/2606.04907v1)
- **Breaking Time: A Fully Gaussian Framework for Distributed and Continuous-Time SLAM** (Score: 63) [RA-L] [Link](https://arxiv.org/abs/2606.06250v1)
- **LadderMan: Learning Humanoid Perceptive Ladder Climbing** (Score: 63) [Link](https://arxiv.org/abs/2606.05873v1)
- **HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers** (Score: 61) [Link](https://arxiv.org/abs/2606.06493v1)
- **GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors** (Score: 60) [Link](https://arxiv.org/abs/2606.05160v1)
- **Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation** (Score: 58) [Link](https://arxiv.org/abs/2606.05015v1)
- **Meridian: Metric-Semantic Primitive Matching for Cross-View Geo-Localization Beyond Urban Environments** (Score: 58) [Link](https://arxiv.org/abs/2606.06312v1)
- **RadiusFPS: Efficient Farthest Point Sampling on CPUs and GPUs via Spherical Voxel Pruning** (Score: 58) [Link](https://arxiv.org/abs/2606.06255v1)
- **BPDA-GMM: Bayesian Probabilistic Data Association via Gaussian Mixture Models for Semantic SLAM** (Score: 56) [Link](https://arxiv.org/abs/2606.04618v1)
- **Towards Realistic 3D Sonar Simulation** (Score: 55) [Link](https://arxiv.org/abs/2606.06130v1)
- **Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling** (Score: 54) [International Journal of Robotics Research] [Link](https://arxiv.org/abs/2606.04355v1)
- **Uncertainty-Aware Adaptive Sensor Fusion for Autonomous Navigation** (Score: 51) [Link](https://arxiv.org/abs/2606.05437v1)
- **CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation** (Score: 45) [Link](https://arxiv.org/abs/2606.05011v1)
- **Merging model-based control with multi-agent reinforcement learning for multi-agent cooperative teaming strategies** (Score: 45) [Link](https://arxiv.org/abs/2606.06011v1)
- **MoDex: A Diffusion Policy for Sequential Multi-Object Dexterous Grasping** (Score: 44) [CoRL] [Link](https://arxiv.org/abs/2606.05407v1)
- **Real-World Deployment of a 5G-Connected Edge-Controlled Aerial Robot in Industrial Subterranean Mines** (Score: 43) [Link](https://arxiv.org/abs/2606.04818v1)
- **Amortized Nonlinear Model Predictive Control** (Score: 39) [Link](https://arxiv.org/abs/2606.05840v1)
- **Z-FLoc: Zero-Shot Floorplan Localization via Geometric Primitives** (Score: 39) [Link](https://arxiv.org/abs/2606.04788v1)
- **CADENCE: Predicting Realized MAPF Execution Time Beyond Sum of Costs** (Score: 38) [ICRA] [Link](https://arxiv.org/abs/2606.04746v1)
- **TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation** (Score: 38) [Link](https://arxiv.org/abs/2606.06218v1)

## 📊 今日统计
- 总抓取: 822 篇 | 通过初筛: 103 篇 | 精选: 5 篇 (含 LLM 精筛)
