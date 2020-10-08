#!/usr/bin/env python
from __future__ import print_function
import rospy
import sys
from std_msgs.msg import String
from std_msgs.msg import Float64

import numpy as np
import sounddevice as sd
from math import pi

def sound_play(msg):
    if(msg.data >=0.0 and msg.data <= 2.0):
        pass
    elif(msg.data > 2.0 and msg.data <= 4.0):
        #rospy.loginfo("level 1")
        sine_wave_generator(5000)
        
    elif(msg.data > 4.0 and msg.data <= 6.0):
        #rospy.loginfo("level 2")
        sine_wave_generator(10000)
        
    elif(msg.data > 6.0 and msg.data <= 8.0):
        #rospy.loginfo("level 3")
        sine_wave_generator(15000)
        
    elif(msg.data > 8.0 and msg.data <= 10.0):
        #rospy.loginfo("level 4")
        sine_wave_generator(20000)

def sine_wave_generator(amplitude):
    frequency = 500 #makes it shrill
    #amplitude = msg.data*1000    
    samples = np.arange(44100 * 0.3) / 44100.0 #sample generation
    wave = amplitude * np.sin(2 * np.pi * frequency * samples) #w(t) = A*sin(2*pi*f*t)
    wav_wave = np.array(wave, dtype=np.int16) #wav conversion
    sd.play(wav_wave, blocking=True)


def initialize():
    rospy.init_node('odor_concentration_indicator', anonymous=True)   
    rospy.Subscriber("analog_output_throttle", Float64, sound_play)  
    rospy.spin()
        
if __name__ == '__main__':
    try:
        initialize()
    except rospy.ROSInterruptException: pass
    
   
