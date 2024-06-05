import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import String

class KinectSubscriber(Node):
    def __init__(self):
        super().__init__('kinect_subscriber')
        self.subscription_depth_image_raw = self.create_subscription(
            Image,
            '/depth/image_raw',
            self.listener_dir_callback,
            10)
        self.publisher_depth_image_raw = self.create_publisher(String, '/ak_debug/depth_image_raw_received', 10)
        self.depth_raw_count = 0

        self.subscription_depth_image_raw = self.create_subscription(
            Image,
            '/rgb/image_raw',
            self.listener_rgb_callback,
            10)
        self.publisher_rgb_image_raw = self.create_publisher(String, '/ak_debug/rgb_image_raw_received', 10)
        self.rgb_raw_count = 0

        self.subscription_points2 = self.create_subscription(
            PointCloud2,
            '/points2',
            self.listener_points2_callback,
            10)
        self.publisher_points2 = self.create_publisher(String, '/ak_debug/points2_received', 10)
        self.points2_count = 0


    def listener_dir_callback(self, msg):
        self.depth_raw_count += 1
        count_msg = String()
        count_msg.data = f'Received {self.depth_raw_count} depth images'
        self.publisher_depth_image_raw.publish(count_msg)
        self.get_logger().debug(count_msg.data)

    def listener_rgb_callback(self, msg):
        self.rgb_raw_count += 1
        count_msg = String()
        count_msg.data = f'Received {self.rgb_raw_count} rgb images'
        self.publisher_rgb_image_raw.publish(count_msg)
        self.get_logger().debug(count_msg.data)
    
    def listener_points2_callback(self, msg):
        self.points2_count += 1
        count_msg = String()
        count_msg.data = f'Received {self.points2_count} pcd'
        self.publisher_points2.publish(count_msg)
        self.get_logger().debug(count_msg.data)


def main(args=None):
    rclpy.init(args=args)
    kinect_subscriber = KinectSubscriber()
    rclpy.spin(kinect_subscriber)
    kinect_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
