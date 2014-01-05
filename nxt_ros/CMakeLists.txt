# Catkin User Guide: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/user_guide.html
# Catkin CMake Standard: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/standards.html
cmake_minimum_required(VERSION 2.8.3)
project(nxt_ros)
find_package(catkin REQUIRED COMPONENTS rospy nxt_python sensor_msgs nxt_msgs)

# catkin_package parameters: http://ros.org/doc/groovy/api/catkin/html/dev_guide/generated_cmake_api.html#catkin-package
# TODO: fill in what other packages will need to use this package
catkin_package(
    DEPENDS rospy nxt_python sensor_msgs nxt_msgs
)

install(PROGRAMS scripts/nxt_ros.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
  
install(PROGRAMS scripts/joint_states_aggregator.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

