#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from ros_basics_tutorials.msg import Shape


def chatter_callback(message):
    rospy.loginfo("I heard: (%d, %s, %.2f, %.2f)", message.id,
                  message.name, message.height, message.width)


def listener():
    rospy.init_node('shape_subscriber_py', anonymous=True)

    rospy.Subscriber('shape_info', Shape, chatter_callback)

    # To start listen, it will keep listening
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
