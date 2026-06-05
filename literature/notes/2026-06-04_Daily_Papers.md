# 🤖 具身智能/机器人学术日报 (2026-06-04)

## 🏆 精选论文 (Top 5)

### 1. DRL-Based Pose Control for Double-Ackermann Robots Under Actuation Uncertainties
- **Score:** 96
- **Categories:** cs.AI, cs.RO
- **Venue:** ICRA
- **Abstract:** Robust deployment of deep reinforcement learning (DRL) policies on real robots remains challenging due to discrepancies between simulation and real-world dynamics. We address this issue in the context of maneuvering with double-Ackermann-steering mobile robots, which introduce additional constraints due to their non-holonomic nature. Building upon the DRL framework ManeuverNet, we extend its objective from position control to full pose control, resulting in a more challenging task.
- **AI 点评:** relevant to sim-to-real transfer pipeline
- 📄 [arXiv](https://arxiv.org/abs/2606.00313) | 📥 [PDF](https://arxiv.org/pdf/2606.00313.pdf)

---

### 2. CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation
- **Score:** 94
- **Categories:** cs.AI, cs.RO
- **Abstract:** Humans primarily rely on walking and running to traverse complex terrains, without resorting to unnecessarily complex motion patterns. Similarly, humanoid robots should achieve smooth transitions between walking and running while maintaining natural and stable locomotion. However, unifying gait transition and multi-terrain adaptation within a single policy remains challenging due to gradient interference and the distribution shift induced by terrain-dependent visual and dynamic variations.
- **AI 点评:** relevant to locomotion control
- 📄 [arXiv](https://arxiv.org/abs/2606.04718) | 📥 [PDF](https://arxiv.org/pdf/2606.04718.pdf)

---

### 3. Autonomous Navigation System for Library Service Robot Based on Unitree Go2 Edu
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Libraries require autonomous robots to move quietly through narrow aisles while remaining safe around readers, chairs, bags, and carts. This paper presents a ROS 2 navigation system for a Unitree Go2 Edu quadruped equipped with a 4D LiDAR, a front depth camera, and an IMU. Rather than assuming the library is rough terrain, we target the practical mobility discontinuities of real deployments, including floor transitions, temporary clutter, and partially blocked passages where low-clearance wheele...
- **AI 点评:** relevant to terrain adaptation and traversal
- 📄 [arXiv](https://arxiv.org/abs/2606.03340) | 📥 [PDF](https://arxiv.org/pdf/2606.03340.pdf)

---

### 4. Global-Local Attention Decomposition for Terrain Encoding in Humanoid Perceptive Locomotion
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Although reinforcement learning has significantly advanced humanoid locomotion, perceptive policies still struggle on sparse-foothold terrain and constrained environments. Success in these scenarios requires both broad terrain awareness and precise foothold selection, two perceptual roles that conventional encoders often entangle. To address this challenge, we propose Global-Local Attention Decomposition (GLAD) for terrain encoding in humanoid locomotion.
- **AI 点评:** relevant to locomotion control
- 📄 [arXiv](https://arxiv.org/abs/2606.00637) | 📥 [PDF](https://arxiv.org/pdf/2606.00637.pdf)

---

### 5. Too Much of a Good Thing: When sim2real Efforts Impede Policy Learning (And What to Do About It)
- **Score:** 66
- **Categories:** cs.AI, cs.RO
- **Abstract:** While sim2real efforts are necessary for effective policy transfer to hardware, there is such a thing as too much of a good thing. We argue that sim2real efforts have led to misaligned incentives with policy learning, resulting in simulator lock in and poor policy exploration due to the unreasonable constraints imposed by the real world.
- **AI 点评:** relevant to sim-to-real transfer pipeline
- 📄 [arXiv](https://arxiv.org/abs/2606.02636) | 📥 [PDF](https://arxiv.org/pdf/2606.02636.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **FW-NKF: Frequency-Weighted Neural Kalman Filters** (Score: 65) [ICRA] [Link](https://arxiv.org/abs/2606.02251)
- **SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation** (Score: 63) [Link](https://arxiv.org/abs/2606.03297)
- **MAD: Mapping-Aware World Models for Agile Quadrotor Flight** (Score: 60) [Link](https://arxiv.org/abs/2606.04534)
- **MineXplore: An Open-Source Reinforcement Learning Exploration Benchmark for GNSS-Denied Underground Environment** (Score: 60) [ICRA] [Link](https://arxiv.org/abs/2606.04569)
- **Teaching Robots to Say 'I Don't Know' : SENTINEL for Uncertainty-Aware SLAM** (Score: 60) [ICRA] [Link](https://arxiv.org/abs/2606.04853)
- **WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation** (Score: 58) [Link](https://arxiv.org/abs/2606.04907)
- **Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling** (Score: 57) [International Journal of Robotics Research] [Link](https://arxiv.org/abs/2606.04355)
- **M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking** (Score: 55) [Link](https://arxiv.org/abs/2606.04829)
- **ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM** (Score: 55) [Link](https://arxiv.org/abs/2606.00307)
- **Multi-Agent Next-Best-View Optimization for Risk-Averse Planning** (Score: 52) [IROS] [Link](https://arxiv.org/abs/2606.04158)
- **Behavior Cloning of MPC for 3-DOF Robotic Manipulators** (Score: 50) [ICRA] [Link](https://arxiv.org/abs/2606.00383)
- **Distribution-Free Risk-Aware Planning and Control Under Uncertainty Using Conformal Spectral Risk Control** (Score: 50) [Robotics and Automation Letters] [Link](https://arxiv.org/abs/2606.04185)
- **Embedding Semantic Risk into Distance Fields and CBFs for Online Monocular Safe Control** (Score: 50) [Link](https://arxiv.org/abs/2606.01605)
- **SAVMap: Structure-Aided Visual Mapping of Large-Scale 2.5D Manhattan Wireframes from Panoramic Video** (Score: 50) [ICRA] [Link](https://arxiv.org/abs/2606.01939)
- **Geodesic Flow Matching for Denoising High-Dimensional Structured Representations** (Score: 48) [ICML] [Link](https://arxiv.org/abs/2606.00248)
- **Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control** (Score: 48) [Link](https://arxiv.org/abs/2606.00297)
- **Robust Integrated Planning and Control for Quadrotors in Dynamic Environments via NMPC with CBF Penalties** (Score: 48) [Link](https://arxiv.org/abs/2606.01038)
- **S2M-Trek: From Single to Multi-Sphere Transport via Per-Frame Deep Sets on a Wheel-Legged Robot** (Score: 47) [Link](https://arxiv.org/abs/2606.01332)
- **ActMVS: Active Scene Reconstruction with Monocular Multi-View Stereo** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2606.01367)
- **Hierarchical Object Representation for Spatial Robot Perception: Points, Meshes, and Superquadrics** (Score: 42) [Link](https://arxiv.org/abs/2606.01545)
- **MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry** (Score: 42) [CVPR] [Link](https://arxiv.org/abs/2606.02996)
- **PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2606.00104)
- **TransTac: Visuo-Tactile Modality Transition via Ultraviolet-Encoded Transparent Elastomers** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2606.04477)
- **BPDA-GMM: Bayesian Probabilistic Data Association via Gaussian Mixture Models for Semantic SLAM** (Score: 40) [Link](https://arxiv.org/abs/2606.04618)
- **Bionic Human-Motion Style Transfer for Physically Executable Whole-Body Control of Humanoid Robots** (Score: 40) [Link](https://arxiv.org/abs/2606.03536)
- **HORIZON: Recoverability-Governed Curriculum for Physical-Domain Scaling** (Score: 40) [Link](https://arxiv.org/abs/2606.05143)
- **Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking** (Score: 40) [CVPR] [Link](https://arxiv.org/abs/2606.03985)
- **Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking** (Score: 40) [CVPR] [Link](https://arxiv.org/abs/2606.03985v1)
- **Motion Planning in Dynamic Environments: A Survey from Classical to Modern Methods** (Score: 40) [Link](https://arxiv.org/abs/2606.02677)
- **PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation** (Score: 38) [Link](https://arxiv.org/abs/2606.03989)
- **PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation** (Score: 38) [Link](https://arxiv.org/abs/2606.03989v1)
- **Dynamic Resilient Spatio-Semantic Memory with Hybrid Localization for Mobile Manipulation** (Score: 37) [Link](https://arxiv.org/abs/2606.00576)
- **Hierarchical Semantic-Augmented Navigation: Optimal Transport and Graph-Driven Reasoning for Vision-Language Navigation** (Score: 37) [NeurIPS] [Link](https://arxiv.org/abs/2606.01565)
- **Position: Good Embodied Reward Models Need Bad Behavior Data** (Score: 37) [ICML] [Link](https://arxiv.org/abs/2606.01036)
- **Semantic-weighted ICP for LiDAR Odometry: Class-Aware Residual Reweighting for Robust Scan Registration** (Score: 37) [Link](https://arxiv.org/abs/2606.03905)
- **The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset** (Score: 37) [Link](https://arxiv.org/abs/2606.02956)
- **EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations** (Score: 35) [CoRL] [Link](https://arxiv.org/abs/2606.03268)

## 📊 今日统计
- 总抓取: 2408 篇 | 通过初筛: 329 篇 | 精选: 5 篇 (含 LLM 精筛)
