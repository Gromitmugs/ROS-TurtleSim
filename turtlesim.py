#!/usr/bin/env python

# Assignment 1.1a and 1.1b
# Sattra Piyapunsutti 62382039211

import rospy
from geometry_msgs.msg import Twist
 
def get_path(path_type):
    paths = []
    cmd = Twist()
    walktime = []

    if path_type.lower() == 'circle':
        cmd.linear.x = 1; cmd.angular.z = 1
        paths.append(cmd)
        walktime.append(0)

    elif path_type.lower() == 'triangle':
        for i in range(3):
            cmd = Twist()
            if i == 0:
                cmd.linear.y = 1
                walktime.append(3)
            elif i == 1:
                cmd.linear.y = -1; cmd.linear.x = 1
                walktime.append(1.5)
            else:
                cmd.linear.y = -1; cmd.linear.x = -1
                walktime.append(1.5)
            paths.append(cmd)
    else:
        raise ValueError("Wrong Path Type")
    
    return paths, walktime

def talker(path_type): # node name
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    payload, walktimes = get_path(path_type)
    while not rospy.is_shutdown():
        for path, walktime in zip(payload, walktimes):
            time_start = rospy.get_time()
            while True:
                pub.publish(path)
                rate.sleep()
                if rospy.get_time() - time_start > walktime:
                    break

if __name__ == '__main__':
    try:
        talker('circle') # Select Path Type here (Circle / Triange)
    except rospy.ROSInterruptException:
        pass

