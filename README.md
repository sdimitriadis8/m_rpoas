# 🤖 Multi-Robot Patrol & Obstacle Avoidance System (M-RPOS)

A modular ROS2-based simulation system for coordinating multiple robot agents to patrol an area and avoid obstacles. Supports Gazebo (gz sim) and keyboard control input.

## 🔧 Features

- Differential drive robots with obstacle sensors
- Multi-robot coordination with patrol zones
- Gazebo simulation + ROS2 nodes
- Keyboard teleoperation and velocity command bridges
- Docker support for reproducible environments

## 🧰 Tech Stack

- ROS2 (Humble or Jazzy)
- Gazebo Sim (Ignition/GZ)
- Python (for control nodes)
- URDF/Xacro for robot models
- Docker (optional)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/M-RPOS.git
cd M-RPOS

# Build workspace
colcon build --symlink-install

# Source environment
source install/setup.bash

# Launch simulation
ros2 launch launch/m_rpos.launch.py
