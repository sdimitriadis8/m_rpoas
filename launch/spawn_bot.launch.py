"""
Launch file to start robot_state_publisher, joint_state_publisher, and RViz2
using the robot's URDF description file.

This file is part of the Multi-Robot Patrol & Obstacle Avoidance System (M-RPOAS).
"""

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import os


def generate_launch_description():
    
    # Get the absolute path to the robot URDF file
    urdf_file = os.path.join(
        get_package_share_directory("mrpoas_core"), "urdf", "4wd_patrol_bot.urdf"
    )

    return LaunchDescription(
        [
            # Publish joint transforms using the URDF model
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                parameters=[{"robot_description": open(urdf_file).read()}],
            ),
            # Provide joint values for RViz visualization
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
            ),
            # Launch RViz2 for visualizing the robot model
            Node(package="rviz2", executable="rviz2", name="rviz2", output="screen"),
        ]
    )