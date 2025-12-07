#include <gtest/gtest.h>
#include <utils.h>

TEST(MyTestSuite, TestCase1) {
    EXPECT_EQ(test(), "Hello World");
}