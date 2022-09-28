cmake_minimum_required(VERSION 3.9.2)
project(png_to_tensor)

add_executable(png_to_tensor png_to_tensor.cpp)

find_package(PNG REQUIRED)
target_link_libraries(png_to_tensor PUBLIC png)

find_package(EDDL REQUIRED)
target_link_libraries(png_to_tensor PUBLIC EDDL::eddl)
