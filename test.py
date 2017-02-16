import shutil
import os
import sys

# Bootstrap the packages in the conan local cache, as coming from CI
def bootstrap():
  for pkg in ["say", "hello", "chat"]:
    os.chdir(pkg)
    os.system("conan test_package")
    os.chdir("..")

if "noboost" not in sys.argv:
  bootstrap()

# Create and move to a clean build folder
if os.path.exists("build"):
  shutil.rmtree("build")
os.makedirs("build")
os.chdir("build")


os.system("conan install ..")
shutil.copy("../conanbuildinfo.cmake", ".")
os.system('cmake .. -G "Visual Studio 14 Win64"')
