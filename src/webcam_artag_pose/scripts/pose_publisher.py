#! /usr/bin/env python3

import rospy
import tf2_ros
import time

from geometry_msgs.msg import TransformStamped


def print_transform(target, source) -> TransformStamped:
    if not tf_buffer.can_transform(target, source, rospy.Time.now(), timeout=rospy.Duration(1)):
        print("Error")
        return
    print(f"=== transformation: {target} - {source}")
    transform = tf_buffer.lookup_transform(target, source, rospy.Time.now(), timeout=rospy.Duration(1))
    print(transform)
    print("---"*4)
    return transform


if __name__ == "__main__":

    rospy.init_node("transform_01_node")
    tf_buffer = tf2_ros.Buffer(rospy.Duration(5.0))
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    # need to wait a bit, so that buffer has actually some done transformations to look up.
    # remember the publishing frequency of the static transform publisher?
    time.sleep(0.5)
    
    # t1 = print_transform("map", "camera_frame")

    # t2 = print_transform("camera_frame", "ar_marker_2")

    t3 = print_transform("map", "ar_marker_2")
    