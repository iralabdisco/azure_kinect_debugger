from setuptools import setup

package_name = 'azure_kinect_debugger'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Federica Di Lauro',
    maintainer_email='federicadilauro1998@gmail.com',
    description='ROS 2 hz tool sucks.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kinect_subscriber = azure_kinect_debugger.kinect_subscriber:main',
        ],
    },
)
