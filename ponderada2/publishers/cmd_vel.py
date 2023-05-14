from .base import Publisher
from rclpy.node import Node
from geometry_msgs.msg import Twist #tipo de dado  enviado

class Movement(Publisher):
    def __init__(self, node: Node):
        super().__init__(
            name = "movement",
            node = node, 
            topic_name = "/cmd_vel",
            topic_type = Twist)
        
    def apply(self, linear, angular):
        self.publish(Twist(linear=linear, angular=angular))