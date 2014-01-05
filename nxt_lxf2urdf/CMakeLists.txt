# Catkin User Guide: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/user_guide.html
# Catkin CMake Standard: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/standards.html
cmake_minimum_required(VERSION 2.8.3)
project(nxt_lxf2urdf)
find_package(catkin REQUIRED )

# catkin_package parameters: http://ros.org/doc/groovy/api/catkin/html/dev_guide/generated_cmake_api.html#catkin-package
catkin_package(
)

install(PROGRAMS scripts/nxt_test
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
