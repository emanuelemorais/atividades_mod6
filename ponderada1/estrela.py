#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 1)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.timer = 0
        
          
    def movimento1(self):
        self.twist_msg_.linear.y = 4.0
        self.twist_msg_.linear.x = 2.0
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        
        
    def movimento2(self):
        self.twist_msg_.linear.y = -4.5
        self.twist_msg_.linear.x = 1.0
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        
    def movimento3(self):
        self.twist_msg_.linear.y = 3.0
        self.twist_msg_.linear.x = -3.5
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        
    def movimento4(self):
        self.twist_msg_.linear.y = 0.0
        self.twist_msg_.linear.x = 4.5
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1

    def movimento5(self):
        self.twist_msg_.linear.y = -1.4
        self.twist_msg_.linear.x = -2.0
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        


    def move_turtle(self):
        if (self.timer < 10):
            self.movimento1()
            print(self.timer)
            
        if (self.timer >= 10 and self.timer < 20):
            self.movimento2()
            
        if (self.timer >= 20 and self.timer < 30):
            self.movimento3()
        
        if (self.timer >= 30 and self.timer < 40):
            self.movimento4()
            
        if (self.timer >= 40 and self.timer < 50):
            self.movimento5()

def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
