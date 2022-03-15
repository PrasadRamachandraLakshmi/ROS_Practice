#!/usr/bin/env python
from dis import dis
import rospy
import time
import math
import sys

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def poseCallback(msg):
    global x
    global y, yaw

    x = msg.x
    y = msg.y
    yaw = msg.theta


def move(velocity_publisher, speed, distance, is_forward):
    velocity_message = Twist()
    global x, y
    x0 = x
    y0 = y

    if(is_forward):
        velocity_message.linear.x = abs(speed)
    else:
        velocity_message.linear.x = -abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(10)

    while(True):
        rospy.loginfo("Turtlesim moves forward:")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        distance_moved = abs(math.sqrt((x-x0)**2)+((y-y0)**2))
        print("Distance moved:%.2f" % distance_moved)
        if(distance_moved >= distance):
            rospy.loginfo("Reached")
            break

    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)


def rotate(velocity_publisher, angular_speed_degree, relative_angle_degree, clockwise):
    velocity_message = Twist()

    angular_speed_degree = math.radians(abs(angular_speed_degree))
    #relative_angle_degree = math.radians(abs(relative_angle_degree))

    if(clockwise):
        velocity_message.angular.z = -abs(angular_speed_degree)
    else:
        velocity_message.angular.z = abs(angular_speed_degree)

    loop_rate = rospy.Rate(100)
    t0 = rospy.Time.now().to_sec()

    while True:
        rospy.loginfo("Turtle Rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()
        print(math.degrees(current_angle_degree), " ", relative_angle_degree)

        if(math.degrees(current_angle_degree) > relative_angle_degree):
            rospy.loginfo("reached")
            break
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


def setDesiredOrientation(velocity_publisher, desiredOrientation):
    desiredOrientation = math.radians(desiredOrientation)
    relative_angle = desiredOrientation - yaw
    print(relative_angle)
    if(relative_angle > 0):
        clockwise = False
    else:
        clockwise = True
    relative_angle = math.degrees(abs(relative_angle))
    rotate(velocity_publisher, rotation_speed, rotation_angle, clockwise)


def go_to_goal(velocity_publisher, x_goal, y_goal):
    global x
    global y, yaw

    velocity_message = Twist()

    while(True):
        K_linear = 3.0  # Proportional gain
        distance = abs(math.sqrt(((x_goal-x)**2) + ((y_goal-y)**2)))

        linear_speed = distance*K_linear

        K_angular = 4.0

        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal-yaw)*K_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)

        print('x=', x, ', y=', y, ', distance to goal = ', distance)

        if(distance < 0.01):
            break


def spiral(velocity_publisher, wk, rk):
    velocity_message = Twist()
    loop_rate = rospy.Rate(1)

    while((x < 10.5) and (y < 10.5)):
        rk += 0.5
        velocity_message.linear.x = rk
        velocity_message.angular.z = wk
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

    velocity_message.linear.x = 0
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)


if __name__ == '__main__':
    try:
        # if(len(sys.argv) > 1):
        #     speed = float(sys.argv[1])
        #     distance = float(sys.argv[2])
        #     rotation_speed = float(sys.argv[4])
        #     rotation_angle = float(sys.argv[5])
        #     if sys.argv[3] == "True":
        #         is_forward = True
        #     else:
        #         is_forward = False

        # else:
        speed = rospy.get_param("speed")
        distance = rospy.get_param("distance")
        rotation_speed = rospy.get_param("rotation_speed")
        rotation_angle = rospy.get_param("rotation_angle")
        is_forward = rospy.get_param("is_forward")

        rospy.init_node('turtle_pose_motion', anonymous=True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(
            cmd_vel_topic, Twist, queue_size=10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)

        #move(velocity_publisher, speed, distance, is_forward)
        #setDesiredOrientation(velocity_publisher, rotation_angle)
        #go_to_goal(velocity_publisher=velocity_publisher,x_goal=3.0, y_goal=3.0)
        spiral(velocity_publisher=velocity_publisher, rk=0, wk=2)
    except rospy.ROSInterruptException:
        pass
