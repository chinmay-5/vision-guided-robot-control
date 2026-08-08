#! /usr/bin/env python3
    #!/usr/bin/env python3
import actionlib
import sys
import rospy
import tf2_ros
import time

from geometry_msgs.msg import TransformStamped
from welding_robot_msgs.msg import WeldingPathAction 
from welding_robot_msgs.msg import WeldingPathFeedback
from welding_robot_msgs.msg import WeldingPathGoal
from welding_robot_msgs.msg import WeldingPathResult

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

    rospy.init_node("mover_client_node")
    tf_buffer = tf2_ros.Buffer(rospy.Duration(5.0))
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    # need to wait a bit, so that buffer has actually some done transformations to look up.
    # remember the publishing frequency of the static transform publisher?
    time.sleep(0.5)
    
    # t1 = print_transform("map", "camera_frame")

    # t2 = print_transform("camera_frame", "ar_marker_2")

    # t3 = print_transform("map", "ar_marker_2")

    waypoints = []
    for x in range(2):
        if input() == '':
            waypoints.append(print_transform("base_link", "ar_marker_2"))
    

from my_actionlib.msg import MultiplyTwoIntsAction,
MultiplyTwoIntsResult, MultiplyTwoIntsFeedback, MultiplyTwoIntsGoal
def multiply_two_ints_client(a,b):
    # Creates the SimpleActionClient, passing the type of the action
    to the constructor.

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    # Creates a goal to send to the action server.
    goal = MultiplyTwoIntsGoal(A=a,B=b)
    # Sends the goal to the action server.
    client.send_goal(goal)
    # Waits for the server to finish performing the action.
    client.wait_for_result()
    # Prints out the result of executing the action
    return client.get_result()
    if __name__ == '__main__':
        try:
        rospy.init_node('multiply_two_ints_client')
        a, b = 1, 2
        if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        else:
        print("Using default argument: (1,2)")
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        result = multiply_two_ints_client(a,b)
        print("Result:", result)
        except rospy.ROSInterruptException:
        print("program interrupted before completion",
        file=sys.stderr)
    