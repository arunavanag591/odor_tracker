cmake_minimum_required(VERSION 3.0.2)
project(odor_tracker)

find_package(catkin REQUIRED roslaunch
 rospy
 sensor_msgs
 std_msgs)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs sensor_msgs
)

###########
## Build ##
###########

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)


install(
  DIRECTORY launch meshes urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
