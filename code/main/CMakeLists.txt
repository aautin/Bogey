project(${PROJECT_NAME}Main)

add_executable(${PROJECT_NAME})

set(SRCS main.cpp)
set(HDRS)

target_link_libraries(${PROJECT_NAME} PRIVATE BogeyCore)
target_include_directories(${PROJECT_NAME} PRIVATE ${HDRS})
target_sources(${PROJECT_NAME} PRIVATE ${SRCS})