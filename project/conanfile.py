from conans import ConanFile, CMake, tools
from conans.util.files import mkdir
import os


class ProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    packages = ["app", "hello"]

    def build(self):
        self.get_projects()
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line, ))
        self.run("cmake --build . %s" % cmake.build_config)

    def get_projects(self):
        for r in self.packages:
            mkdir(r)
            cd = os.getcwd()
            os.chdir(r)
            self.run("conan install ../../%s --build=missing" % r)