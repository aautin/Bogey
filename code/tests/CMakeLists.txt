project(${PROJECT_NAME}Tests)

add_executable(${PROJECT_NAME})

set(SRCS main.cpp utilsTests.cpp)
set(HDRS)

enable_testing()
add_test(
	NAME ${PROJECT_NAME}
	COMMAND $<TARGET_FILE:${PROJECT_NAME}>
)

target_link_libraries(${PROJECT_NAME} PRIVATE BogeyCore gtest::gtest)
target_include_directories(${PROJECT_NAME} PRIVATE ${HDRS})
target_sources(${PROJECT_NAME} PRIVATE ${SRCS})

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME})