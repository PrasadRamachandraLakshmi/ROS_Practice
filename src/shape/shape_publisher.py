#!/usr/bin/env python3
from random import random
import rospy
from std_msgs.msg import String
from ros_basics_tutorials.msg import Shape


def publish():

    # String is not python String but ros msg String
    # queue_size buffer to wait until subscriber process the msgs, if size is more
    # then it needs more memory and delay in processing, if it is very small loss of msgs

    pub = rospy.Publisher('chatter', Shape, queue_size=10)

    # anonymous = True flag means that rospy will choose a unique name for the node name
    # If two nodes with thw same name are launched, the previous one is kicked off.
    rospy.init_node('shape_publisher_py', anonymous=True)

    # Rate of Publication, 1hz = 1 message/sec
    rate = rospy.Rate(1)

    i = 0
    while not rospy.is_shutdown():
        Shape = Shape()
        Shape.id = 1
        Shape.name = "Seonsor_1"
        Shape.height = 32.5 + random()*5
        Shape.width = 33.41 + random()*5
        rospy.loginfo(Shape)
        pub.publish(Shape)
        rate.sleep()  # if rate = rospy.Rate(10) then, sleep for 0.1 second or 10 messages/sec
        i += 1


if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
