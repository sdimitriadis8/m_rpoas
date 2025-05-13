from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    urdf_path = os.path.join(
        os.path.dirname(__file__), '..', 'urdf', 'patrol_bot.urdf'
    )
    urdf_path = os.path.abspath(urdf_path)

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', '-v4', 'empty.sdf'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'ros_gz_sim', 'create',
                '-name', 'patrol_bot',
                '-file', urdf_path
            ],
            output='screen'
        )
    ])
