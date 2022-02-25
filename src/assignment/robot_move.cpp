#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"

void getPose(turtlesim::Pose pose)
{
    std::cout << pose;
}

void moveup(geometry_msgs::Twist &msg)
{
    std::cout << "Up" << std::endl;
    msg.linear.x = 1;
    // msg.linear.y = msg.linear.z = 0;
    // msg.angular.x = msg.angular.y = msg.angular.z = 0;
    return;
}
void movedown(geometry_msgs::Twist &msg)
{
    msg.linear.x = -1;
    // msg.linear.y = msg.linear.z = 0;
    // msg.angular.x = msg.angular.y = msg.angular.z = 0;
    return;
}
void moveleft(geometry_msgs::Twist &msg)
{
    // msg.linear.x = msg.linear.y = msg.linear.z = 0;
    // msg.angular.x = msg.angular.y = 0;
    msg.angular.z = 2 * 3.14 / 3;
    return;
}
void moveright(geometry_msgs::Twist &msg)
{
    // msg.linear.x = msg.linear.y = msg.linear.z = 0;
    // msg.angular.x = msg.angular.y = 0;
    msg.angular.z = -2 * 3.14 / 3;
    return;
}

geometry_msgs::Twist move(const char key)
{
    geometry_msgs::Twist msg;
    switch (key)
    {
    case 'W':
    case 'w':
        moveup(msg);
        break;
    case 'S':
    case 's':
        movedown(msg);
        break;

    case 'A':
    case 'a':
        moveleft(msg);
        break;

    case 'D':
    case 'd':
        moveright(msg);
        break;

    default:
        break;
    }
    std::cout << "Details:" << std::endl;
    std::cout << msg.linear.x << std::endl;
    std::cout << msg.angular.z << std::endl;
    return msg;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_move");
    ros::NodeHandle node_handle;
    ros::Publisher pub = node_handle.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
    ros::Subscriber sub = node_handle.subscribe("/turtle1/pose", 1, getPose);

    char key = '\0';
    while (key != 'q' && ros::ok())
    {
        key = std::getchar();
        std::cout << key << std::endl;
        if (toascii(key) == 10)
            continue;
        if (key != 'q')
        {
            pub.publish(move(key));
            ros::spinOnce();
        }
        else
            break;
    }
}