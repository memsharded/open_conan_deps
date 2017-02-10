PROJECT(Hello CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_LIBRARY(hello STATIC hello.cpp)
ADD_EXECUTABLE(main main.cpp)
target_link_libraries(main hello ${CONAN_LIBS})