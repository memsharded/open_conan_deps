import shutil
import os

os.chdir("say")
os.system("conan export memsharded/testing")
os.chdir("..")

try:
  shutil.rmtree("build")
except:
  print "BUILD folder not existing, or impossible to remove, please check"
os.makedirs("build")
os.chdir("build")

os.makedirs("say")
os.makedirs("hello")

os.chdir("say")
os.system("conan install ../../say")
os.system("cmake ../../say")
os.system("cmake --build . --config Release")
os.chdir("..")


os.chdir("hello")
os.system("conan install ../../hello --scope say:open=True")
os.system("cmake ../../hello")
os.system("cmake --build . --config Release")
os.system("bin\main.exe")


new_content = """#include "say.h"
#include <iostream>

void say(std::string msg){
  std::cout<<"I have modified it!!!"<<std::endl;
  std::cout<<msg<<std::endl;
}
"""
with open("../../say/say.cpp", "r") as f:
  old_content = f.read()

with open("../../say/say.cpp", "w") as f:
  f.write(new_content)

os.chdir("../say")
os.system("cmake --build . --config Release")

os.chdir("../hello")
os.system("cmake --build . --config Release")
os.system("bin\main.exe")

with open("../../say/say.cpp", "w") as f:
  f.write(old_content)





