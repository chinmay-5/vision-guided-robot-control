#!/usr/bin/env python

import rospy
import actionlib
from moveit_commander import MoveGroupCommander
from welding_robot_msgs.msg import RobotMoverAction, RobotMoverResult

class RobotMoverServer:
    def __init__(self):
        # Initialize the action server
        self.server = actionlib.SimpleActionServer('robot_mover', RobotMoverAction, execute_cb=self.execute_callback, auto_start=False)
        self.server.start()

        # Initialize MoveGroupCommander
        self.move_group = MoveGroupCommander()

    def execute_callback(self, goal):
        # Perform motion planning and execution here
        # You can use self.move_group to plan and execute robot motions
        # Update the result based on the success of the motion execution
        result = RobotMoverResult()
        result.success = True  # Set the appropriate success value
        result.message = "Motion executed successfully"  # Set the appropriate message

        # Publish the result
        self.server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('robot_mover_server')
    server = RobotMoverServer()
    rospy.spin()
