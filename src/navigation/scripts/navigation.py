#!/usr/bin/env python

import rospy
import actionlib
import numpy as np

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
	
waypoints=[]

with open('goals.txt', 'r') as filehandle:
    for line in filehandle.readlines():
        	f_list = [float(i) for i in line.split(",")]
		waypoints.append(f_list)
print waypoints[0]
print waypoints[1]
print waypoints[2]


def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0]
    goal_pose.target_pose.pose.position.y = pose[1]
    goal_pose.target_pose.pose.position.z = pose[2]
    goal_pose.target_pose.pose.orientation.x = pose[3]
    goal_pose.target_pose.pose.orientation.y = pose[4]
    goal_pose.target_pose.pose.orientation.z = pose[5]
    goal_pose.target_pose.pose.orientation.w = pose[6]

    return goal_pose

if __name__ == '__main__':
    rospy.init_node('navigation_node')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    for pose in waypoints:
        goal = goal_pose(pose)
        client.send_goal(goal)
        client.wait_for_result()

rospy.spin()

