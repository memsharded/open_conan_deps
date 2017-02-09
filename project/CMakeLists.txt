PROJECT(PROJECT CXX)
cmake_minimum_required(VERSION 2.8.12)

#add_subdirectory(../hello ${CMAKE_BINARY_DIR}/hello)
#add_subdirectory(../app  ${CMAKE_BINARY_DIR}/app)

INCLUDE_EXTERNAL_MSPROJECT(hello hello/Hello.vcxproj)
INCLUDE_EXTERNAL_MSPROJECT(app app/MyChat.vcxproj)