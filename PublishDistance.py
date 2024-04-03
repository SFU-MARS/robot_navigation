#!/usr/bin/env python3

import rospy
from zed_interfaces.msg import ObjectsStamped

def object_callback(msg):
    # Print the received objects data
    rospy.loginfo("Received objects data: %s", msg.objects)

def object_listener():
    rospy.init_node('object_listener', anonymous=True)

    # Subscribe to the object detection topic
    rospy.Subscriber("/zed2/zed_node/obj_det/objects", ObjectsStamped, object_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        object_listener()
    except rospy.ROSInterruptException:
        pass
