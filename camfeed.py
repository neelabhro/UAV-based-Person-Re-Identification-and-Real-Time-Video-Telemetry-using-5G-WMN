#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

bridge = CvBridge()

def callback(data):
	cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	#cv2.imshow("Image window", cv_image)
	#cv2.waitKey(3)




def camFeed():
	rospy.init_node('camfeed', anonymous=True)

	rospy.Subscriber("/webcam/image_raw", Image, callback)

	rospy.spin()

if __name__ == '__main__':
	camFeed()

