PROJECT(MyChat CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(mychat main.cpp)
target_link_libraries(mychat ${CONAN_LIBS})