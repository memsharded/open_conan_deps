from conans import ConanFile, CMake, tools
import os


class ChatConan(ConanFile):
    name = "chat"
    version = "0.1"
    license = "MIT"
    requires = "hello/0.1@memsharded/testing"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s' % (cmake.command_line, ))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["chat"]
