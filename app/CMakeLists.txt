PROJECT(MyChat CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()
conan_set_find_paths()
conan_output_dirs_setup()

find_package(Chat REQUIRED)

set(LIB_NAME main)

# All this common code
ADD_EXECUTABLE(${LIB_NAME} ${LIB_NAME}.cpp)


TARGET_INCLUDE_DIRECTORIES(main PUBLIC ${LIBCHAT_INCLUDE_DIRS})
TARGET_LINK_LIBRARIES(main ${LIBCHAT_LIBRARIES})