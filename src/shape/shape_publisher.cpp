#include "ros/ros.h"
#include "std_msgs/String.h"
#include "ros_basics_tutorials/Shape.h"

#include <sstream>

int main(int argc, char **argv)
{
    // initialise a node
    ros::init(argc, argv, "shaper_publisher");
    /*The ros::NodeHandle class serves two purposes.
    First, it provides RAII-style startup and shutdown of the internal node inside a roscpp program.
    Second, it provides an extra layer of namespace resolution that can make writing subcomponents easier.*/
    ros::NodeHandle nh;
    ros::Publisher chatter_publisher = nh.advertise<ros_basics_tutorials::Shape>("shape_info", 1000);
    ros::Rate loop_rate(0.5);

    int cnt{0};
    while (ros::ok())
    {
        ros_basics_tutorials::Shape msg;
        msg.id = 1;
        msg.name = "Sensor_1";
        msg.width = 0.852;
        msg.height = 35;
        ROS_INFO("[Talker] I Published sensor %s with id %d, temp=%f, hum=%f\n", msg.name.c_str(), msg.id, msg.height, msg.width);
        chatter_publisher.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        cnt++;
    }
    return 0;
}
