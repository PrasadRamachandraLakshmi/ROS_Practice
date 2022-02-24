#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

int main(int argc, char **argv)
{
    // initialise a node
    ros::init(argc, argv, "talker_node");
    /*The ros::NodeHandle class serves two purposes.
    First, it provides RAII-style startup and shutdown of the internal node inside a roscpp program.
    Second, it provides an extra layer of namespace resolution that can make writing subcomponents easier.*/
    ros::NodeHandle nh;
    ros::Publisher chatter_publisher = nh.advertise<std_msgs::String>("chatter", 1000);
    ros::Rate loop_rate(0.5);

    int cnt{0};
    while (ros::ok())
    {
        std_msgs::String msg;
        std::stringstream ss;
        ss << "Hello World" << cnt;
        msg.data = ss.str();
        ROS_INFO("[Talker] I Published %s\n", msg.data.c_str());
        chatter_publisher.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        cnt++;
    }
    return 0;
}
