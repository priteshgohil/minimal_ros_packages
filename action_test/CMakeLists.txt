cmake_minimum_required(VERSION 2.8.3)
project(action_test)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  actionlib_tutorials
)

catkin_package()

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
  install(PROGRAMS
   scripts/action_test_client
   scripts/action_test_server
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )

## Mark cpp header files for installation
  install(DIRECTORY launch/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/ros/launch
  )
