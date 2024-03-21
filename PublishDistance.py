#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from zed_interfaces.msg import ObjectsStamped

def zed_callback(data):
def zed_distance_publisher():
    rospy.init_node('zed_distance_publisher', anonymous=True)
    distance_pub = rospy.Publisher('zed_object_distance', Float64, queue_size=10)
    rospy.Subscriber('zed/objects', ObjectsStamped, zed_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        zed_distance_publisher()
    except rospy.ROSInterruptException:
        pass
