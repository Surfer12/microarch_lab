/*
 * File: test_framework.h
 * Purpose: Provides macros and functions for running test suites with clear and descriptive assertion messages.
 * Enhanced Assert Macro Example:
 *   #define ASSERT(expr, msg) \
 *       do { \
 *           if (!(expr)) { \
 *               fprintf(stderr, "Assertion failed: %s\nMessage: %s\nFile: %s, Line: %d\n", #expr, msg, __FILE__, __LINE__); \
 *               exit(EXIT_FAILURE); \
 *           } \
 *       } while (0)
 *
 * Please ensure that all tests provide useful messages to help diagnose failures.
 */

// ... existing code ...