#include "ros/ros.h"
#include "ros_basics_tutorials/DivideTwoInts.h"

bool divide(ros_basics_tutorials::DivideTwoInts::Request &req, ros_basics_tutorials::DivideTwoInts::Response &res)
{
    res.result = (double)req.a / req.b;
    ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
    ROS_INFO("sending response: [%lf]", (double)res.result);
    return true;
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "divide_two_ints_server");
    ros::NodeHandle n;

    ros::ServiceServer service = n.advertiseService("divide_two_ints", divide);
    ROS_INFO("Ready to divide");
    ros::spin();

    return 0;
}