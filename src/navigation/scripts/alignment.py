#!/usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg

from nav_msgs.msg import Odometry

def callback(msg):

    initialpose.header.frame_id = "map"
    initialpose.pose.pose.position.x = msg.pose.pose.position.x
    initialpose.pose.pose.position.y = msg.pose.pose.position.y
    initialpose.pose.pose.position.z = 0
    initialpose.pose.covariance=[0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
    initialpose.pose.pose.orientation.z = msg.pose.pose.orientation.z
    initialpose.pose.pose.orientation.w = msg.pose.pose.orientation.w

    pub.publish(initialpose)


initialpose = geometry_msgs.msg.PoseWithCovarianceStamped()
rospy.init_node('alignment', anonymous=True) #make node
rospy.Subscriber('odom',Odometry, callback)
pub = rospy.Publisher('/initialpose', geometry_msgs.msg.PoseWithCovarianceStamped, queue_size=10)


rospy.spin()
