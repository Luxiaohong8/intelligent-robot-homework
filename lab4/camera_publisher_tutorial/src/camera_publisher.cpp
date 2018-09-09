
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>
int main(int argc, char** argv)
{
  ros::init(argc, argv, "simple_image_publisher");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("static_image", 1);

  cv::Mat image = cv::imread(argv[1], CV_LOAD_IMAGE_COLOR);

  sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();
  msg->header.frame_id = "head_camera";
  msg->width=3;
  msg->height=11;
  msg->is_bigendian = false;
  msg->header.stamp= ros::Time::now();
  msg->step=4;

  ros::Rate loop_rate(5);
  while (nh.ok()) {
    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
}
