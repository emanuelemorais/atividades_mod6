import rclpy
from .controller_1 import Queue, Turtle_Controller

def main(args=None):
    rclpy.init(args=args)
    queue = Queue()
    subscriebr_node = Turtle_Controller(queue)
    rclpy.spin(subscriebr_node)
    subscriebr_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()