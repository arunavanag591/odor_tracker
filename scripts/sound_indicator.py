#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String
from std_msgs.msg import Float64

from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

soundhandle = SoundClient()

def sound_play(msg):
    # soundhandle.play(1,1)    
    # rospy.loginfo("%f" %msg.data)
    # rospy.sleep(1)
    if(msg.data >=0 and msg.data <= 2):
        soundhandle.play(1, 0.2)
        rospy.sleep(0.1)
    elif(msg.data > 2 and msg.data <= 4):
        soundhandle.play(1, 0.4)
        rospy.sleep(0.1)
    elif(msg.data > 4 and msg.data <= 6):
        print("Voltage is between 4-6")
        soundhandle.play(1, 0.6)
        rospy.sleep(0.1)
    elif(msg.data > 6.0 and msg.data <= 8.0):
        print("Voltage is between 6-8")
        soundhandle.play(1, 0.1)
        rospy.sleep(0.5)
    elif(msg.data > 8 and msg.data <= 10.0):
        soundhandle.play(1, 1.0)
        rospy.sleep(0.1)
        

def initialize():
    rospy.init_node('mynode', anonymous=True)   
    rospy.Subscriber("analog_output", Float64, sound_play)  
    rospy.spin()
    
    
if __name__ == '__main__':
    try:
        initialize()
    except rospy.ROSInterruptException: pass
    
   