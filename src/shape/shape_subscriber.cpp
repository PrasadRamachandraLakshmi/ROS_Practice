#include "ros/ros.h"
#include "std_msgs/String.h"
#include "ros_basics_tutorials/Shape.h"

void chatterCallback(const ros_basics_tutorials::Shape::ConstPtr &msg)
{
    ROS_INFO("[Listener] I heard sensor %s with id %d, temp=%f, hum=%f\n", msg->name.c_str(), msg->id, msg->height, msg->width);
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "shape_subscriber");
    ros::NodeHandle nh;
    ros::Subscriber chatter_subscriber = nh.subscribe("shape_info", 1000, chatterCallback);
    ros::spin();

    return 0;
}