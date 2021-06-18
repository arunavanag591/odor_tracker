## Odor_Tracker

This package contains the ROS Setup for the odor tracker experiment, that launches several sensor and collects data. It also has some functionality node that indicates the amplitude of certain sensor like the odor.

## Table of Contents

1. [Dependency Installation](#dependency-installation)
2. [Package Overview](#package-overview)
    
    2a. [Directory Structure](#directory-structure)
3. [Usage](#usage)
    
    2a. [Running the Master Data Collector](#running-the-master-data-collector)

## Dependency Installation
The setup depends on several packages as it launches several sensors from the stack. The master launch is called [tracking_master](launch/tracking_master.launch). The following needs to be installed in order to launch all the sensors:

### Librealsense and Realsense ROS:

To run the T265 tracker camera the following must be installed:
* <a href="https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md">Librealsense</a>
* <a href="https://github.com/IntelRealSense/realsense-ros"> Realsense ROS</a>. Having it in source in the workspace is necessary to be able to change the launch file parameters.

### Ublox:
The GPS needs to be installed from <a href="https://github.com/KumarRobotics/ublox">ublox</a> repository.

### Phidgets Imu:
The imu and its udev could be installed from <a href="https://github.com/ros-drivers/phidgets_drivers">here</a>. Needs to be added to dialout to give permission to particular port.

### Trisonica Wind Sensor
Details on <a href ="https://github.com/florisvb/trisonica_ros">Trisonica</a> Installation and <a href = "https://github.com/florisvb/gps_wind_stationData"> logging</a> could found as on clicking. Needs to be added to dialout to give permission to particular port.

### Odor sensor
Odor sensor is handled by the [read_daq](scripts/read_daq.py) script.

The config files contains all the udev and meshes required for launching the physical model of the sensor stack in rviz.


## Directory Structure:
Below is the directory structure of the package, including the general function of certain scripts.

    |--odor_tracker
        |-- launch
            |--tracking_master.launch           # launches the sensor stack
        |-- scripts
            |-- bag_to_csv.py                   # converts ros bag to csv file
            |-- bag2hdf5.py                     # converts ros bag to hdf5 file for pandas dataframework
            |-- read_daq.py                     # read odor sensor voltage from the daq
            |-- sound_indicator.py              # generates sine wave indicator for incoming reading on a topic - odor for now
        |-- CMakeLists.txt
        |-- package.xml
        |-- README.md


## Usage
```
roslaunch odor_tracker tracking_master.launch
```
To get sound indication; throttle the message into 5KHz - 20KHz range as 
```
rosrun topic_tools throttle messages analog_output 5
```
and then run the sound indicator node as
```
rosrun odor_tracker sound_indicator.py
```

## GPS BASE STATION SETUP
Follow this [GPS Station Setup Guide](Base_Station_Setup.md)
