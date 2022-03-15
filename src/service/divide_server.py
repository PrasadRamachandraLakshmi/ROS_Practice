#!/usr/bin/env python

from ros_basics_tutorials.srv import DivideTwoInts
from ros_basics_tutorials.srv import DivideTwoIntsRequest
from ros_basics_tutorials.srv import DivideTwoIntsResponse
import rospy

import time


def handle_divide_two_inits(req):
    print("Returning [%s / %s = %s]" % (req.a, req.b, (req.a/req.b)))
    time.sleep(5)
    response = DivideTwoIntsResponse(req.a/req.b)
    return response


def divide_two_ints_server():
    rospy.init_node('divide_two_ints_server')
    s = rospy.Service('divide_two_ints', DivideTwoInts,
                      handle_divide_two_inits)
    print("Ready to divide tow ints.")
    rospy.spin()


if __name__ == "__main__":
    divide_two_ints_server()
