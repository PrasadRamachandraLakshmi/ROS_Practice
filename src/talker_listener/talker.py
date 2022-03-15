#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def talker():

    # String is not python String but ros msg String
    # queue_size buffer to wait until subscriber process the msgs, if size is more
    # then it needs more memory and delay in processing, if it is very small loss of msgs

    pub = rospy.Publisher('chatter', String, queue_size=10)

    # anonymous = True flag means that rospy will choose a unique name for the node name
    # If two nodes with thw same name are launched, the previous one is kicked off.
    rospy.init_node('talker', anonymous=True)

    # Rate of Publication, 1hz = 1 message/sec
    rate = rospy.Rate(1)

    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()  # if rate = rospy.Rate(10) then, sleep for 0.1 second or 10 messages/sec
        i += 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
