macro(conan_set_find_paths)
    set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/output/say
                          ${CMAKE_BINARY_DIR}/output/hello
                          ${CMAKE_BINARY_DIR}/output/chat
                          ${CMAKE_MODULE_PATH})
    set(CMAKE_PREFIX_PATH ${CMAKE_MODULE_PATH} ${CMAKE_PREFIX_PATH})
endmacro()

macro(conan_output_dirs_setup)
endmacro()