#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def detect_key_pressed(data):
    if data.linear.x == 2.0:
        return "UP"
    elif data.linear.x == -2.0:
        return "DOWN"
    elif data.angular.z == 2.0:
        return "LEFT"
    elif data.angular.z == -2.0:
        return "RIGHT"
    else:
        return "NOT A KEY PRESS!"

def callback(data):
    rospy.loginfo("Key Pressed: " + detect_key_pressed(data))

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('turtle1/cmd_vel', Twist, callback) 

    rospy.spin()

if __name__ == '__main__':
    listener()
