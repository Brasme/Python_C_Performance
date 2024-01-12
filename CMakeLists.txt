cmake_minimum_required(VERSION 3.9)

set(CMAKE_BUILD_TYPE Release)

project(c_math VERSION "1.0.0" LANGUAGES C CXX)

add_library(${PROJECT_NAME} SHARED fisqrt.c fsqr.c)
