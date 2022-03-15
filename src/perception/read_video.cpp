#include <iostream>

#include "opencv4/opencv2/opencv.hpp"

using namespace cv;

int read_video()
{
    VideoCapture video_capture(0);

    if (!video_capture.isOpened())
    {
        return -1;
    }

    Mat gray_image;
    namedWindow("Gray_Image", 1);

    while (true)
    {
        Mat frame;
        video_capture >> frame;
        cvtColor(frame, gray_image, COLOR_BGR2GRAY);
        imshow("Gray_Image", gray_image);
        if (waitKey(30) >= 0)
            break;
    }

    return 0;
}

int image_read(cv::String image_name)
{
    std::cout << "Reading Image" << image_name << std::endl;
    Mat image;
    image = imread(image_name, IMREAD_COLOR);

    if (!image.data)
    {
        std::cout << "Can't Open the Image" << std::endl;
        return -1;
    }
    namedWindow("Copy", WINDOW_AUTOSIZE);
    if (!imwrite("/home/prasad/ROS_Tutorials/catkin_ws/src/ros_basics_tutorials/src/perception/images/copy/color.jpg", image))
    {
        std::cout << "Could not write to path" << std::endl;
        return -1;
    }
    imshow("Copy", image);

    waitKey(0);
    return 0;
}
int main(int argc, char **argv)
{
    int return_code{};

    // return_code = read_video();
    return_code = image_read("/home/prasad/ROS_Tutorials/catkin_ws/src/ros_basics_tutorials/src/perception/images/colour.jpg");
    return return_code;
}