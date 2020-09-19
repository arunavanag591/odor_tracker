#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String
from std_msgs.msg import Float64

from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

soundhandle = SoundClient()

def sound_play(msg):
    
    if(msg.data >=0 or msg.data <= 2):
        return soundhandle.playWave("~/Downloads/test.wav", 0.2)
    elif(msg.data > 2 or msg.data <= 4):
        return soundhandle.playWave("/home/ecc/Downloads/test.wav", 0.4)
    elif(data > 4 or data <= 6):
        print("Voltage is between 4-6")
        return soundhandle.playWave("/home/ecc/Downloads/test.wav", 0.6)
    elif(data > 6.0 or data <= 8.0):
        print("Voltage is between 6-8")
        return soundhandle.playWave("/home/ecc/Downloads/test.wav", 0.8)
    elif(data > 8 or data <= 10.0):
        return soundhandle.playWave("/home/ecc/Downloads/test.wav", 1.0)

def initialize():
    rospy.init_node('mynode', anonymous=True)
    
    rospy.Subscriber("analog_output", Float64, sound_play)
    rospy.spin()
    
    
if __name__ == '__main__':
    try:
        initialize()
    except rospy.ROSInterruptException: pass
    
   