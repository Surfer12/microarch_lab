#ifndef TEST_FRAMEWORK_H
#define TEST_FRAMEWORK_H

#include <stdio.h>
#include <stdlib.h>

#define TEST(description) \
    printf("Running test: %s\n", description); \
    do { \

#define END_TEST \
        printf("Test passed!\n\n"); \
    } while (0); \

#define ASSERT(condition) \
    if (!(condition)) { \
        printf("Assertion failed at %s:%d\n", __FILE__, __LINE__); \
        exit(1); \
    }

#define ASSERT_EQUAL(expected, actual) \
    if ((expected) != (actual)) { \
        printf("Assertion failed at %s:%d\n", __FILE__, __LINE__); \
        printf("Expected: %d, Got: %d\n", (expected), (actual)); \
        exit(1); \
    }

#endif // TEST_FRAMEWORK_H