PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()
conan_set_find_paths()
conan_output_dirs_setup()

find_package(Hello REQUIRED)

ADD_EXECUTABLE(example example.cpp)
TARGET_INCLUDE_DIRECTORIES(example PUBLIC ${LIBHELLO_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES(example ${LIBHELLO_LIBRARIES})
