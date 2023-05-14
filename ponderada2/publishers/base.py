#Esse codico é a base para criar um subscriber

from rclpy.node import Node

class Publisher:
    def __init__(self, name, node: Node, topic_name, topic_type):
    #O init é o construtor da minha classe e está instanciando as variaveis para criar um publisher
        self.name = name    
        self.node = node
        self.topic_name = topic_name
        self.topic_type = topic_type
        
        self.connect()
        
        self.node.get_logger().info(f"Publisher {self.name} criado.")
        
    def connect(self):
        self.publisher = self.node.create_publisher(
            msg_type = self.topic_type,
            topic = self.topic_name,
            qos_profile = 10)
    
    def publish(self, msg):
        self.publisher.publish(msg)