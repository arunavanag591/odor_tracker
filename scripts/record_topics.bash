#!/bin/bash
# Author: Arunava Nag 

echo "Will start Recording"

  rosbag record --split --duration=5m -O ~/dataOctoberDesert/CarDesert1020.bag \
  /ublox_gps/fix \
  /ublox_gps/fix_velocity \
  /trisonica \
  /imu/data /imu/mag \
#  /camera/accel/sample /camera/gyro/sample /camera/odom/sample

echo "Done Recording"
