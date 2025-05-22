from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import os


def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory("mrpoas_core"), "urdf", "4wd_patrol_bot.urdf"
    )

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                parameters=[{"robot_description": open(urdf_file).read()}],
            ),
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
            ),
            Node(package="rviz2", executable="rviz2", name="rviz2", output="screen"),
        ]
    )
