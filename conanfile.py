import glob
import os
import shutil
import tempfile

import conans


class PackageInfoBugConan(conans.ConanFile):
    """
    A Conan recipe for building PackageInfoBug.
    """
    name = 'PackageInfoBug'
    version = '1.0.0'
    description = 'A demonstration of a bug in Conan where consuming packages are not getting the correct package_info.'
    url = 'git@github.com:kent-at-multiscale/conan-package-info-bug.git'
    license = 'GNU GPLv3'
    author = 'Kent Rosenkoetter <kent.rosenkoetter@multiscalehn.com>'
    exports_sources = os.path.join('src', 'client', 'client_version.h'), os.path.join('src', 'server', 'server_version.h')
    settings = None
    generators = 'env', 'txt'
    
    def build(self):
        pass
    
    def package(self):
        self.copy(pattern='*', dst=os.path.join('client', 'include'), src=os.path.join('src', 'client'))
        self.copy(pattern='*', dst=os.path.join('server', 'include'), src=os.path.join('src', 'server'))
    
    def package_info(self):
        self.cpp_info.includedirs = [os.path.join('client', 'include'), os.path.join('server', 'include')]  # Ordered list of include paths
        self.cpp_info.libs = []  # The libs to link against
        self.cpp_info.libdirs = []  # Directories where libraries can be found
        self.cpp_info.resdirs = []  # Directories where resources, data, etc can be found
        self.cpp_info.bindirs = []  # Directories where executables and shared libs can be found
        self.cpp_info.defines = []  # preprocessor definitions
        self.cpp_info.cflags = []  # pure C flags
        self.cpp_info.cppflags = []  # C++ compilation flags
        self.cpp_info.sharedlinkflags = []  # linker flags
        self.cpp_info.exelinkflags = []  # linker flags
