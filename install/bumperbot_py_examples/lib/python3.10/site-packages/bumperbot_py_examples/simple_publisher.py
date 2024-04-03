import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
    
        self.pub_ = self.create_publisher(String,"chatter",10)

        self.counter_ = 0 # initialise counter function that count n. of messages that we are publishing within the chatter topic
        self.frequency_ = 1.0 # initialise frequency function at which messages are published within the chatter topic

        self.get_logger().info("Publishing at %d Hz" % self.frequency_)

        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter_

        self.pub_.publish(msg)
        self.counter_ += 1

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher) # keep the node (timer and publisher) active 
    simple_publisher.destroy_node() # destroy the node when ctrl+c is pressed
    rclpy.shutdown() # shuhtdown ros interface


if __name__ == '__main__':
   main() 
