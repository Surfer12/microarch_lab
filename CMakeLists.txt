cmake_minimum_required(VERSION 3.10)
project(microarch_lab C)

set(CMAKE_C_STANDARD 99)

# Include custom linting targets from twxs.cmake if available
if(EXISTS "${CMAKE_SOURCE_DIR}/twxs.cmake")
    include(${CMAKE_SOURCE_DIR}/twxs.cmake)
else()
    message(STATUS "twxs.cmake not found; skipping lint module")
endif()

# Add executables for the C source files
add_executable(memory_operations memory_operations.c)
add_executable(cache_visualizer cache_visualizer.c)