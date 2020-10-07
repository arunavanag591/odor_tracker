#!/bin/bash
# Author: Arunava Nag 

echo "Will start Recording"

  rosbag record --split --duration=5m -O ~/dataOctober/October.bag \
  /tf /tf_static \
  /ublox_gps/fix \
  /ublox_gps/fix_velocity \
  /trisonica /analog_output \
  /imu/data /imu/mag \
  /camera/accel/sample /camera/gyro/sample /camera/odom/sample

echo "Done Recording"
