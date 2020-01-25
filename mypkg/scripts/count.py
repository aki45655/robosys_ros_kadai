#!/usr/bin/python2 
import rospy
from std_msgs.msg import Float64

if __name__ == '__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Float64, queue_size=1)
    rate = rospy.Rate(1)
    n = 0
    while not rospy.is_shutdown():
        n += 1
        pub.publish(n)
        rate.sleep() 
