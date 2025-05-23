# 🛰️ M-RPOAS: Multi-Robot Patrol & Obstacle Avoidance System

A ROS 2-based simulation project that models differential-drive robot patrols with basic obstacle avoidance. Built using **ROS 2 Humble**, **Gazebo**, **URDF**, and **Docker** for reproducibility.

> 🔧 Currently supports:  
> - 2WD and 4WD patrol robot models  
> - RViz + robot_state_publisher launch  
> - ROS 2 + Gazebo integration in progress

---

## 🚀 Quick Start (ROS 2)

### 🔧 Requirements

- Ubuntu 22.04
- [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html)
- `colcon`, `rosdep`, `gazebo`, and `rviz2`

### 📦 Build the workspace

```bash
# Clone the repository
git clone https://github.com/sdimitriadis8/mrpoas.git

# Build workspace
cd ~/ros2_ws
colcon build --symlink-install

# Source environment
source install/setup.bash

# Launch simulation
ros2 launch mrpoas spawn_bot.launch.py
