#!/usr/bin/env python

from ros_basics_tutorials.srv import DivideTwoInts
from ros_basics_tutorials.srv import DivideTwoIntsRequest
from ros_basics_tutorials.srv import DivideTwoIntsResponse

import rospy
import time
import sys


def divide_two_ints_client(x, y):
    rospy.wait_for_service('divide_two_ints')
    try:
        divide_two_ints = rospy.ServiceProxy('divide_two_ints', DivideTwoInts)
        resp1 = divide_two_ints(x, y)
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [x y]" % sys.argv[0])
        sys.exit(1)
    print("Requesting %s+%s" % (x, y))
    s = divide_two_ints_client(x, y)
    print("%s / %s = %s" % (x, y, s))
