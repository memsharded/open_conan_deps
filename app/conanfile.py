from conans import ConanFile, CMake, tools
import os


class ChatConan(ConanFile):
    requires = "chat/0.1@memsharded/testing"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line, ))
        self.run("cmake --build . %s" % cmake.build_config)

