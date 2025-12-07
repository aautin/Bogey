from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake

class BogeyConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    
    def requirements(self):
        self.requires("gtest/1.17.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        cmake = CMake(self)
        cmake.configure()