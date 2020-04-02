#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('vel_publisher', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    move = Twist()
    while not rospy.is_shutdown():
        move.linear.x = 1
        move.angular.z = 1
        pub.publish(move)
        rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
