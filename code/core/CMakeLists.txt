project(${PROJECT_NAME}Core)

add_library(${PROJECT_NAME})

set(SRCS utils.cpp)
set(HDRS ${CMAKE_CURRENT_LIST_DIR})

target_include_directories(${PROJECT_NAME} PUBLIC ${HDRS})
target_sources(${PROJECT_NAME} PRIVATE ${SRCS})