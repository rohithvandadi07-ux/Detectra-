import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# 👇 import Detectra logger
from detectra.core.logger import alert


class Attacker(Node):
    def __init__(self):
        super().__init__('attacker_node')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.attack)

        alert("⚠️ Attacker node initialized (unauthorized)")

    def attack(self):
        msg = String()
        msg.data = "🚨 HACKED MESSAGE"

        self.publisher_.publish(msg)

        # 🚨 log instead of print
        alert("🚨 Attacker attempting message injection on topic: chatter")


def main():
    rclpy.init()

    try:
        node = Attacker()
        rclpy.spin(node)

    except Exception as e:
        # 🔥 this is important — logs failure when blocked
        alert(f"🚫 Attacker blocked or failed: {e}")

    finally:
        try:
            node.destroy_node()
        except:
            pass
        rclpy.shutdown()


if __name__ == '__main__':
    main()