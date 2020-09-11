#!/usr/bin/env python
#import roslib; roslib.load_manifest('sound_play')
#import rospy
from playsound import playsound
import alsaaudio

sound = ('~/tracking_ws/src/tracking_master/config/sound/sound.wav')
playsound(sound)
