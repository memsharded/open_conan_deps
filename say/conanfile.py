from conans import ConanFile, CMake, tools
import os


class SayConan(ConanFile):
    name = "say"
    version = "0.1"
    license = "MIT"
    url = ""
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self.settings)
        install = '-DCMAKE_INSTALL_PREFIX="%s"' % self.package_folder
        self.run('cmake %s %s %s' % (self.conanfile_directory, cmake.command_line, install))
        self.run("cmake --build . --target install %s" % cmake.build_config)

