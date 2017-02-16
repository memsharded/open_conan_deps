PROJECT(Say CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_LIBRARY(say STATIC say.cpp)

install(TARGETS say
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(FILES FindSay.cmake
        DESTINATION /)

install(FILES say.h
        DESTINATION include)
