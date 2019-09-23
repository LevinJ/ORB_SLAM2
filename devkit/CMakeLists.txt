cmake_minimum_required (VERSION 3.10)
project (evaluate_odometry)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}  -Wall  -O0 -march=native ")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall   -O0 -march=native")

# add the executable
add_executable (evaluate_odometry cpp/evaluate_odometry.cpp cpp/matrix.cpp)



