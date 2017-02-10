from conans import ConanFile, CMake, tools
import os


class SayConan(ConanFile):
    name = "say"
    version = "0.1"
    license = "MIT"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line, ))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.scope.open:
            self.cpp_info.rootpath = "../say"
            self.cpp_info.includedirs = [""]
            self.cpp_info.libdirs = ["../build/say/lib"]
        self.cpp_info.libs = ["say"]
