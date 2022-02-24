#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def chatter_callback(message):
    print("I heard %s" % message.data)


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, chatter_callback)

    # To start listen, it will keep listening
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
