# Azure Kinect debugger

Simple ROS 2 node to check the publishing frequency of Azure Kinect, since 'ros2 topic hz' is broken for large messages.

Subscribes to:
- `/depth/image_raw`
- `/rgb/image_raw`
- `/points2`

and publishes the total count of the received messages for each topic on:
- `/ak_debug/depth_image_raw_received`
- `/ak_debug/rgb_image_raw_received`
-  `/ak_debug/points2_received`

To run it: `ros2 run azure_kinect_debugger kinect_subscriber`
