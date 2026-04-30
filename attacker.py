import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Attacker(Node):
    def __init__(self):
        super().__init__('attacker_node')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.attack)

    def attack(self):
        msg = String()
        msg.data = "🚨 HACKED MESSAGE"
        self.publisher_.publish(msg)
        print("🚨 Attacker sent fake message")


def main():
    rclpy.init()
    node = Attacker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
