from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'm_r_poas_core'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/m_r_poas_core']),
    ('share/m_r_poas_core', ['package.xml']),
    ('share/m_r_poas_core/launch', ['launch/spawn_bot.launch.py']),
    ('share/m_r_poas_core/urdf', ['urdf/robot.urdf.xacro']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sokratis',
    maintainer_email='info@28x.gr',
    description='Core system of the m-rpoas patrol robot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)