#Esse codico é a base para criar um subscriber

from rclpy.node import Node

class Subscriber:
    def __init__(self, name, node: Node, topic_name, topic_type):
    #O init é o construtor da minha classe e está instanciando as variaveis para criar um publisher
        self.name = name    
        self.node = node
        self.topic_name = topic_name
        self.topic_type = topic_type
        
        self.node.get_logger().info(f"Subscriber {self.name} criado.")
        
    def connect(self, subscription_callback):
        self.publisher = self.node.create_subscription(
            msg_type = self.topic_type,
            topic = self.topic_name,
            callback=subscription_callback,
            qos_profile = 10)
        
        
        self.node.get_logger().info(f"Subscription {self.name} connected.")
    
