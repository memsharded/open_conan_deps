PROJECT(Say CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()

set(LIB_NAME say)

ADD_LIBRARY(${LIB_NAME} STATIC ${LIB_NAME}.cpp)

if(CONAN_EXPORTED)
        install(TARGETS ${LIB_NAME}
                LIBRARY DESTINATION lib
                ARCHIVE DESTINATION lib)

        install(FILES Find${LIB_NAME}.cmake
                DESTINATION /)

        install(FILES ${LIB_NAME}.h
                DESTINATION include)  
else()
        set(INSTALL_DIR ${CMAKE_BINARY_DIR}/output/${LIB_NAME})
        install(TARGETS ${LIB_NAME}
                LIBRARY DESTINATION ${INSTALL_DIR}/lib
                ARCHIVE DESTINATION ${INSTALL_DIR}/lib)

        install(FILES Find${LIB_NAME}.cmake
                DESTINATION ${INSTALL_DIR}/)

        install(FILES ${LIB_NAME}.h
                DESTINATION ${INSTALL_DIR}/include)
endif()


add_custom_command(TARGET ${LIB_NAME}
                   POST_BUILD
                   COMMAND cmake
                   ARGS -P cmake_install.cmake )