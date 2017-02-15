import shutil
import os
import sys

os.chdir("say")
os.system("conan test_package")
os.chdir("..")

print os.getcwd()
if os.path.exists("build"):
  print "REMOVING BUILD FOLDER"
  shutil.rmtree("build")


os.makedirs("build")
os.chdir("build")

os.makedirs("say")
os.makedirs("hello")

os.chdir("say")
os.system("conan install ../../say")
os.system("cmake ../../say")
# os.system("cmake --build . --config Release")
os.makedirs("lib")

os.system("cmake --build . --config Release")
os.chdir("..")
sys.exit(0)

os.chdir("hello")
os.system("conan install ../../hello --scope say:open=True")
os.system('cmake ../../hello -G "Visual Studio 14 Win64"')
os.system("cmake --build . --config Release")
os.system("bin\main.exe")

sys.exit(0)

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





