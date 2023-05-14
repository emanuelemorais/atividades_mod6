import rclpy
from rclpy.node import Node
from publishers.cmd_vel import Movement
from geometry_msgs.msg import Vector3
from subscribers.odom import Position
import math

class Controller(Node):

    def __init__(self):
        super().__init__("turtlebot")
        self.euler = {"x": 0.0, "y": 0.0, "theta": 0.0}
        self.position_goal = {"x": 3.0, "y": 9.0, "theta": 0.0}
        self.movement = Movement(self) 
        self.position = Position(self, self.callback)
       
        self.create_timer(
            timer_period_sec = 1,
            callback=self.publish_movement)
        
    def publish_movement(self):
        self.movement.apply(
            linear=Vector3(x=self.movement_x(self.euler, self.position_goal), y=0.0, z=0.0),
            angular=Vector3(x=0.0, y=0.0, z=self.movement_z(self.euler, self.position_goal)))
        
        
    def callback(self, euler_data):
        self.euler = euler_data
        self.get_logger().info(str(euler_data))
                  
        
    def movement_z(self, data, position):
        delta_x = data["x"] - position["x"]
        delta_y = data["y"] - position["y"]
        tan = delta_x / delta_y
        atan_result = math.atan(tan)
        angulo = data["theta"] - atan_result
        return 0.5 if angulo < 0.1 else 0.0
    
    def movement_x(self, data, position):
        return 0.5 if data["x"] - position["x"] < 0.1 else 0.0
        
    
    
        
if __name__ == "__main__":
    rclpy.init()
    controller = Controller()
    rclpy.spin(controller)
    rclpy.shutdown()      