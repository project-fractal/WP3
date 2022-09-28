cmake_minimum_required(VERSION 3.9.2)
project(mnist_eddl_inference)

add_executable(mnist_eddl_inference main.cpp)
 
find_package(EDDL REQUIRED)
target_link_libraries(mnist_eddl_inference PUBLIC EDDL::eddl)
