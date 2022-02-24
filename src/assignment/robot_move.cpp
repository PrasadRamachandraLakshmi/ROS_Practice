#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include "geometry_msgs/Vector3.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_move");
    ros::NodeHandle node_handle;

    ros::Publisher pub = node_handle.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);

    ros::Rate loop_rate(1);
    for (int i{0}; i < 100 && ros::ok(); i++)
    {
        geometry_msgs::Twist msg;
        msg.linear.x = 0.8;
        msg.angular.z = 0.5;
        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}