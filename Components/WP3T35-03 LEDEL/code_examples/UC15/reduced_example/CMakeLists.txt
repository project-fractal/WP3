cmake_minimum_required(VERSION 3.9.2)
project(uc15_eddl_train)

add_executable(uc15_eddl_train main.cpp)

find_package(EDDL REQUIRED)
target_link_libraries(uc15_eddl_train PUBLIC EDDL::eddl)
