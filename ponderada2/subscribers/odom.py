from .base import Subscriber
from nav_msgs.msg import Odometry
from rclpy.node import Node
from tf_transformations import euler_from_quaternion


class Position(Subscriber):
    def __init__(self, node: Node, callback):
        super().__init__("pose", node, "/odom", Odometry)
        super().connect(lambda msg: callback(self.convert_data(msg)))
        
        
    def convert_data(self, msg: Odometry):
        orientation = msg.pose.pose.orientation
        _, _, orientation = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])

        return {
                "x": round(msg.pose.pose.position.x, 3),
                "y": round(msg.pose.pose.position.y, 3),
                "z": round(msg.pose.pose.position.z, 3),
                "theta": round(orientation, 3)
                
            }
        
    def teste(self):
        dadoatual = self.convert_data()
        print(dadoatual)
        
    
