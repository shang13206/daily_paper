# 🤖 具身智能/机器人学术日报 (2026-06-03)

## 🏆 精选论文 (Top 5)

### 1. DRL-Based Pose Control for Double-Ackermann Robots Under Actuation Uncertainties
- **Score:** 96
- **Categories:** cs.AI, cs.RO
- **Venue:** ICRA
- **Abstract:** Robust deployment of deep reinforcement learning (DRL) policies on real robots remains challenging due to discrepancies between simulation and real-world dynamics. We address this issue in the context of maneuvering with double-Ackermann-steering mobile robots, which introduce additional constraints due to their non-holonomic nature. Building upon the DRL framework ManeuverNet, we extend its objective from position control to full pose control, resulting in a more challenging task.
- **AI 点评:** relevant to sim-to-real transfer pipeline
- 📄 [arXiv](https://arxiv.org/abs/2606.00313) | 📥 [PDF](https://arxiv.org/pdf/2606.00313.pdf)

---

### 2. Autonomous Navigation System for Library Service Robot Based on Unitree Go2 Edu
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Libraries require autonomous robots to move quietly through narrow aisles while remaining safe around readers, chairs, bags, and carts. This paper presents a ROS 2 navigation system for a Unitree Go2 Edu quadruped equipped with a 4D LiDAR, a front depth camera, and an IMU. Rather than assuming the library is rough terrain, we target the practical mobility discontinuities of real deployments, including floor transitions, temporary clutter, and partially blocked passages where low-clearance wheele...
- **AI 点评:** relevant to terrain adaptation and traversal
- 📄 [arXiv](https://arxiv.org/abs/2606.03340) | 📥 [PDF](https://arxiv.org/pdf/2606.03340.pdf)

---

### 3. Global-Local Attention Decomposition for Terrain Encoding in Humanoid Perceptive Locomotion
- **Score:** 68
- **Categories:** cs.RO
- **Abstract:** Although reinforcement learning has significantly advanced humanoid locomotion, perceptive policies still struggle on sparse-foothold terrain and constrained environments. Success in these scenarios requires both broad terrain awareness and precise foothold selection, two perceptual roles that conventional encoders often entangle. To address this challenge, we propose Global-Local Attention Decomposition (GLAD) for terrain encoding in humanoid locomotion.
- **AI 点评:** relevant to locomotion control
- 📄 [arXiv](https://arxiv.org/abs/2606.00637) | 📥 [PDF](https://arxiv.org/pdf/2606.00637.pdf)

---

### 4. Too Much of a Good Thing: When sim2real Efforts Impede Policy Learning (And What to Do About It)
- **Score:** 66
- **Categories:** cs.AI, cs.RO
- **Abstract:** While sim2real efforts are necessary for effective policy transfer to hardware, there is such a thing as too much of a good thing. We argue that sim2real efforts have led to misaligned incentives with policy learning, resulting in simulator lock in and poor policy exploration due to the unreasonable constraints imposed by the real world.
- **AI 点评:** relevant to sim-to-real transfer pipeline
- 📄 [arXiv](https://arxiv.org/abs/2606.02636) | 📥 [PDF](https://arxiv.org/pdf/2606.02636.pdf)

---

### 5. FW-NKF: Frequency-Weighted Neural Kalman Filters
- **Score:** 65
- **Categories:** cs.AI, cs.RO, eess.SP
- **Venue:** ICRA
- **Abstract:** Robust state estimation is central to robotic autonomy, yet classical Kalman filters struggle with frequency-dependent disturbances and model mismatch such as sensor vibrations, electromagnetic interference, and periodic noise. Although Deep Kalman Filter (DKF) variants extend the Extended Kalman Filtering (EKF) framework by learning latent transitions, they lack explicit mechanisms to suppress band-limited noise components that typically corrupt sensor measurements in real-world scenarios.
- **AI 点评:** Matches keywords: state estimation, localization, pose estimation
- 📄 [arXiv](https://arxiv.org/abs/2606.02251) | 📥 [PDF](https://arxiv.org/pdf/2606.02251.pdf)

---

## 👀 值得关注 (Score >= 35 的其余论文)

- **SplitAdapter: Load-Aware Humanoid Loco-Manipulation via Factorized Adaptation** (Score: 63) [Link](https://arxiv.org/abs/2606.03297)
- **Geometry-Aware Control Barrier Functions for Collision Avoidance via Bernstein Polynomial Approximations** (Score: 60) [ICRA] [Link](https://arxiv.org/abs/2605.30696)
- **Exploiting Chordal Sparsity for Globally Optimal Estimation with Factor Graphs** (Score: 58) [Link](https://arxiv.org/abs/2605.30617)
- **ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM** (Score: 55) [Link](https://arxiv.org/abs/2606.00307)
- **Behavior Cloning of MPC for 3-DOF Robotic Manipulators** (Score: 50) [ICRA] [Link](https://arxiv.org/abs/2606.00383)
- **Embedding Semantic Risk into Distance Fields and CBFs for Online Monocular Safe Control** (Score: 50) [Link](https://arxiv.org/abs/2606.01605)
- **SAVMap: Structure-Aided Visual Mapping of Large-Scale 2.5D Manhattan Wireframes from Panoramic Video** (Score: 50) [ICRA] [Link](https://arxiv.org/abs/2606.01939v1)
- **Geodesic Flow Matching for Denoising High-Dimensional Structured Representations** (Score: 48) [ICML] [Link](https://arxiv.org/abs/2606.00248)
- **Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control** (Score: 48) [Link](https://arxiv.org/abs/2606.00297)
- **Robust Integrated Planning and Control for Quadrotors in Dynamic Environments via NMPC with CBF Penalties** (Score: 48) [Link](https://arxiv.org/abs/2606.01038)
- **S2M-Trek: From Single to Multi-Sphere Transport via Per-Frame Deep Sets on a Wheel-Legged Robot** (Score: 47) [Link](https://arxiv.org/abs/2606.01332)
- **CoMo3R-SLAM: Collaborative Monocular Dense SLAM with Learned 3D Reconstruction Priors for Outdoor Multi-Agent Systems** (Score: 45) [Link](https://arxiv.org/abs/2605.30488)
- **ActMVS: Active Scene Reconstruction with Monocular Multi-View Stereo** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2606.01367)
- **Hierarchical Object Representation for Spatial Robot Perception: Points, Meshes, and Superquadrics** (Score: 42) [Link](https://arxiv.org/abs/2606.01545)
- **MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry** (Score: 42) [CVPR] [Link](https://arxiv.org/abs/2606.02996)
- **MARIO: Motion-Augmented Real-Time Multi-Sensor Inertial Odometry** (Score: 42) [CVPR] [Link](https://arxiv.org/abs/2606.02996v1)
- **PEACE: A Planner-Executor Agent with Constraint Enforcement for UAVs** (Score: 42) [ICRA] [Link](https://arxiv.org/abs/2606.00104)
- **VLM-GLoc: Vision-Language Model Enhanced Monte Carlo Localization for Robust Semantic Global Localization in Cluttered Quasi-Static Environments** (Score: 42) [Link](https://arxiv.org/abs/2605.30506)
- **Batched Differentiable Rigid Body Dynamics in PyTorch for GPU-Accelerated Robot Learning** (Score: 40) [Link](https://arxiv.org/abs/2605.31481)
- **Bionic Human-Motion Style Transfer for Physically Executable Whole-Body Control of Humanoid Robots** (Score: 40) [Link](https://arxiv.org/abs/2606.03536)
- **Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking** (Score: 40) [CVPR] [Link](https://arxiv.org/abs/2606.03985)
- **Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking** (Score: 40) [CVPR] [Link](https://arxiv.org/abs/2606.03985v1)
- **Motion Planning in Dynamic Environments: A Survey from Classical to Modern Methods** (Score: 40) [Link](https://arxiv.org/abs/2606.02677)
- **RDGen: Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning** (Score: 40) [Link](https://arxiv.org/abs/2605.30957)
- **Triangle Splatting SLAM** (Score: 40) [Link](https://arxiv.org/abs/2605.31419)
- **PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation** (Score: 38) [Link](https://arxiv.org/abs/2606.03989v1)
- **Dynamic Resilient Spatio-Semantic Memory with Hybrid Localization for Mobile Manipulation** (Score: 37) [Link](https://arxiv.org/abs/2606.00576)
- **Hierarchical Semantic-Augmented Navigation: Optimal Transport and Graph-Driven Reasoning for Vision-Language Navigation** (Score: 37) [NeurIPS] [Link](https://arxiv.org/abs/2606.01565)
- **Hierarchical Semantic-Augmented Navigation: Optimal Transport and Graph-Driven Reasoning for Vision-Language Navigation** (Score: 37) [NeurIPS] [Link](https://arxiv.org/abs/2606.01565v1)
- **Position: Good Embodied Reward Models Need Bad Behavior Data** (Score: 37) [ICML] [Link](https://arxiv.org/abs/2606.01036)
- **Semantic-weighted ICP for LiDAR Odometry: Class-Aware Residual Reweighting for Robust Scan Registration** (Score: 37) [Link](https://arxiv.org/abs/2606.03905)
- **TARIC: Memory-Augmented Traversability-Aware Outdoor VLN under Interrupted Semantic Cues** (Score: 37) [Link](https://arxiv.org/abs/2605.31121)
- **The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset** (Score: 37) [Link](https://arxiv.org/abs/2606.02956)
- **The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset** (Score: 37) [Link](https://arxiv.org/abs/2606.02956v1)
- **EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations** (Score: 35) [CoRL] [Link](https://arxiv.org/abs/2606.03268)
- **Prior Availability in Industrial Visual Sim-to-Real: A Review of CAD-Guided and CAD-Unavailable Regimes** (Score: 35) [Link](https://arxiv.org/abs/2605.30581)

## 📊 今日统计
- 总抓取: 2059 篇 | 通过初筛: 329 篇 | 精选: 5 篇 (含 LLM 精筛)
