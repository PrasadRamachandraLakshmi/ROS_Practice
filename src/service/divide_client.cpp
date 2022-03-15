#include "ros/ros.h"
#include "ros_basics_tutorials/DivideTwoInts.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "divide_two_ints_client");
    if (argc != 3)
    {
        ROS_INFO("usage: divide_two_ints_client x y");
        return 1;
    }

    ros::NodeHandle n;
    ros::ServiceClient client = n.serviceClient<ros_basics_tutorials::DivideTwoInts>("divide_two_ints");
    ros_basics_tutorials::DivideTwoInts srv;

    srv.request.a = atoll(argv[1]);
    srv.request.b = atoll(argv[2]);

    if (client.call(srv))
    {
        ROS_INFO("Result: %lf", (double)srv.response.result);
    }
    else
    {
        ROS_ERROR("Failed to call service divide_two_ints");
        return 1;
    }

    return 0;
}