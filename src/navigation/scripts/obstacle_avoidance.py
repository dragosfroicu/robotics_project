#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    print('===========================================================')
    print('s1 [0]')
    print msg.ranges[0]   #print the distance to an obstacle in front of the robot

    print('s2 [90]')
    print msg.ranges[90]

    print('s3 [270]')
    print msg.ranges[270]

    if msg.ranges[0] < 0.7:
        move.linear.x = 0.0
        move.angular.z = -0.3
    elif msg.ranges[90] < 0.5:
        move.linear.x = 0.0
        move.angular.z = -0.3
    elif msg.ranges[270] < 0.5:
        move.linear.x = 0.0
        move.angular.z = 0.3
    else:
        move.linear.x = 0.3
        move.angular.z = 0.0


    pub.publish(move)


move = Twist()
pub = rospy.Publisher('cmd_vel', Twist)
sub = rospy.Subscriber ('scan', LaserScan, callback)
rospy.init_node('obstacle_avoidance', anonymous=True)


rospy.spin()
