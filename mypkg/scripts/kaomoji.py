#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
n = 0

def cb(message):
    global n
    if(message.data % 10 == 0):
        n = "(^ v ^)b"
    else:
        n =  str(message.data)

if __name__ == '__main__': 
    rospy.init_node('kaomoji')
    sub = rospy.Subscriber('count_up', Float64, cb) 
    pub = rospy.Publisher('kaomoji', String, queue_size=1) 
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
