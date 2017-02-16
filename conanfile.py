from conans import ConanFile, CMake
import os


class HelloTestConan(ConanFile):
  requires = "say/0.1@memsharded/testing", "hello/0.1@memsharded/testing", \
             "chat/0.1@memsharded/testing"

  def imports(self):
    self.copy("*", dst="output/say", root_package="say")
    self.copy("*", dst="output/hello", root_package="hello")
    self.copy("*", dst="output/chat", root_package="chat")
