#include <iostream>
#include <vector>
#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"
#include "laserscan/LaserScanner.h"

float degree2radian(float degree)
{
    return (degree * (PI / 180));
}

class tb3_move
{
private:
    ros::NodeHandle nh;
    ros::Publisher tb3_pub;
    ros::Subscriber tb3_sub;

public:
    void process_scan_data(sensor_msgs::LaserScan scan_data);
    tb3_move(int argc, char **argv);
    void move();
    void rotate(std::string direction);
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "tb3_move");
    tb3_move turtle = tb3_move(argc, argv);
    ros::spin();
    return 0;
}
tb3_move::tb3_move(int argc, char **argv)
{
    tb3_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
    tb3_sub = nh.subscribe("/scan", 1000, &tb3_move::process_scan_data, this);
    std::cout << "Publish:" << std::endl;
    move();
}

void tb3_move::process_scan_data(sensor_msgs::LaserScan scan_data)
{
    std::vector<float> left, right;
    for (int i = 0; i < 5; i++)
    {
        // std::cout << "Left Range: " << scan_data.ranges.at(i) << " at " << i << std::endl;
        left.push_back(scan_data.ranges.at(i));
    }
    for (int i = 360 - 6; i < 360; i++)
    {
        // std::cout << "Right Range: " << scan_data.ranges.at(i) << " at " << i << std::endl;
        right.push_back(scan_data.ranges.at(i));
    }
    left.insert(std::end(left), std::begin(right), std::end(right));
    bool rot = false, mv = true;
    for (auto range : left)
    {
        if (range < 0.6)
            rot = true;
        if (range < 3)
            mv = false;
    }
    if (rot)
        rotate("left");
    if (mv)
        move();
}

void tb3_move::rotate(std::string direction)
{
    geometry_msgs::Twist twist = geometry_msgs::Twist();
    ros::Rate loop_rate(10);
    if (direction == "left")
    {
        twist.angular.z = degree2radian(10.0);
    }
    else
    {
        twist.angular.z = degree2radian(-10.0);
    }
    std::cout << "Rotating: " << twist.angular.z << std::endl;
    tb3_pub.publish(twist);
    loop_rate.sleep();
}

void tb3_move::move()
{
    geometry_msgs::Twist twist = geometry_msgs::Twist();
    ros::Rate loop_rate(10);
    twist.linear.x = 0.2;
    twist.angular.z = 0.0;
    std::cout << "Moving Forward" << std::endl;
    tb3_pub.publish(twist);
    loop_rate.sleep();
}
