#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped, Point, PointStamped, Pose, Quaternion
import sys
import math

import rospkg


import moveit_commander

def shutdown():
    """When node is shut down, remove the previous added objects from the planning scene."""
    scene.remove_world_object()
    #scene.remove_attached_object("tool0", "welding_gun")
    scene.remove_attached_object("tool0", "nozzle")# not sure


def initialize_planning_obstacles():
    """Fill this method for adding obstacles"""

    # Configure pose of obstacle
    plane_pose = PoseStamped()
    plane_pose.header.frame_id = "map"
    plane_pose.pose.position.x = 0.0
    plane_pose.pose.position.y = 0.0
    plane_pose.pose.position.z = -0.04  # Set Z to -0.04 meters
    plane_pose.pose.orientation.w = 1.0
    plane_size = (2.0, 2.0, 0.001)  # Very thin box to represent a plane (length, width, height)
    scene.add_box("plane", plane_pose, plane_size)
    
    rospack = rospkg.RosPack()
    package_path = rospack.get_path("robot_environment")
    stl_path = package_path + "/meshes/ros_obstacle.stl"
    
    # Define pose of the obstacle relative to world frame
    obstacle_pose = PoseStamped()
    obstacle_pose.header.frame_id = "map"
    obstacle_pose.pose.position.x = 0.0
    obstacle_pose.pose.position.y = -0.20
    obstacle_pose.pose.position.z = 0.79  # Adjust if needed
    obstacle_pose.pose.orientation.x = -math.sqrt(2)/2
    obstacle_pose.pose.orientation.y = -math.sqrt(2)/2
    obstacle_pose.pose.orientation.z = 0.0
    obstacle_pose.pose.orientation.w = 0.0

    # Add the obstacle to the planning scene
    scene.add_mesh("obstacle", obstacle_pose, stl_path, size=(0.001, 0.001, 0.001))
    # add it to the planning scene
    #scene.add_XYZ()



def initialize_nozzle():
    """Fill this method for adding the nozzle to the planning scene.
    It's important, otherwise the nozzle can collide with the robot/ the environment."""

    # path to nozzle
    rospack = rospkg.RosPack()
    nozzle_path = rospack.get_path("robot_environment") + "/meshes/" + "welding_nozzle.stl"

    # pose of nozzle relative to frame tool0
    nozzle_pose = PoseStamped()
    nozzle_pose.header.frame_id = "tool0"
    nozzle_pose.pose.orientation.x = math.sqrt(2)/2
    nozzle_pose.pose.orientation.y = 0.0
    nozzle_pose.pose.orientation.z = 0.0
    nozzle_pose.pose.orientation.w = math.sqrt(2)/2
    nozzle_pose.pose.position.x = 0.0
    nozzle_pose.pose.position.y = 0.0
    nozzle_pose.pose.position.z = 0.001

    #scene.attach_XYZ()
    scene.attach_mesh("tool0", "nozzle", nozzle_pose, nozzle_path,size=(0.01, 0.01, 0.01))


if __name__ == "__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    scene = moveit_commander.PlanningSceneInterface()

    rospy.init_node("configure_robot_env")
    
    initialize_planning_obstacles()
    initialize_nozzle()

    rospy.on_shutdown(shutdown)
    
    while not rospy.is_shutdown():
        rospy.rostime.wallsleep(0.5)

