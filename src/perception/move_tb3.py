#!/usr/bin/env python

import rospy
import numpy as np

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class MoveStopRotateNode:

    def __init__(self):
        rospy.init_node('move_stop_rotate_node')

        self.sub_laserscan = rospy.Subscriber(
            '/scan', LaserScan, callback=self.on_laserscan)
        self.teleop_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.move()

    def on_laserscan(self, laserscan_msg: LaserScan):
        ranges_front_roi = np.array(
            laserscan_msg.ranges[0:6] + laserscan_msg.ranges[-5:])
        if np.any(ranges_front_roi < 0.6):
            self.rotate('left')
        elif np.all(ranges_front_roi > 3):
            self.move()

    def rotate(self, direction):
        twist_msg = Twist()
        twist_msg.linear.x = 0
        if direction == 'left':
            rospy.loginfo("turn left")
            twist_msg.angular.z = np.deg2rad(10)
        elif direction == 'right':
            rospy.loginfo("turn right")
            twist_msg.angular.z = np.deg2rad(-10)
        self.teleop_pub.publish(twist_msg)

    def move(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.2
        twist_msg.angular.z = 0
        rospy.loginfo("move forward")
        self.teleop_pub.publish(twist_msg)


def main(args=None):
    node = MoveStopRotateNode()
    rospy.spin()


if __name__ == '__main__':
    main()
