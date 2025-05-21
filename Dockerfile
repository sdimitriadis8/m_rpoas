# Base ROS 2 Humble image
FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive

# Install required tools
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-pip \
    ros-humble-rviz2 \
    ros-humble-joint-state-publisher \
    ros-humble-robot-state-publisher \
    ros-humble-xacro \
    && rm -rf /var/lib/apt/lists/*

# Create workspace
WORKDIR /ros2_ws
COPY . ./src

# Build workspace
RUN . /opt/ros/humble/setup.sh && \
    colcon build --symlink-install

SHELL ["/bin/bash", "-c"]

# Source setup + interactive shell
ENTRYPOINT ["bash", "-c", "source /ros2_ws/install/setup.bash && exec bash"]