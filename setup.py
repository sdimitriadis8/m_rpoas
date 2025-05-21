from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mrpoas_core'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/mrpoas_core']),
    ('share/mrpoas_core', ['package.xml']),
    ('share/mrpoas_core/launch', ['launch/spawn_bot.launch.py']),
    ('share/mrpoas_core/urdf', ['urdf/2wd_patrol_bot.urdf','urdf/4wd_patrol_bot.urdf']),
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
