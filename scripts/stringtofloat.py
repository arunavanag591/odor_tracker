#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float64

rospy.init_node("spam")
p = rospy.Publisher("/analog_float", Float64, queue_size=20)

def callback(msg):
    p.publish(float(msg.data))        

rospy.Subscriber("/analog_output", String, callback)
rospy.spin()