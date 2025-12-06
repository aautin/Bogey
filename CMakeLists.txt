cmake_minimum_required(VERSION 3.10)

project(Bogey)
add_executable(${PROJECT_NAME})

include(${CMAKE_CURRENT_SOURCE_DIR}/code/CMakeLists.txt)

target_include_directories(${PROJECT_NAME} PRIVATE ${HDRS})
target_sources(${PROJECT_NAME} PRIVATE ${SRCS})