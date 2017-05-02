import os

import conans


class PackageInfoBugTest(conans.ConanFile):
    """
    This tests the PackageInfoBug package by building an application that uses it.
    This uses Conan's CMake integration to build.
    """
    author = 'Kent Rosenkoetter <kent.rosenkoetter@multiscalehn.com>'
    exports_sources = 'CMakeLists.txt', 'main.cpp'
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'PackageInfoBug/1.0.0@kent_at_multiscale/stable'
    generators = 'cmake', 'env', 'txt'
    
    def system_requirements(self):
        installer = conans.tools.SystemPackageTool()
        installer.install('cmake')
    
    def build(self):
        # .conanfile_directory
        cmake = conans.CMake(self)
        
        args = []
        defs = {}
        if self.scope.verbose:
            defs['CMAKE_VERBOSE_MAKEFILE'] = 'ON'
        else:
            defs['CMAKE_VERBOSE_MAKEFILE'] = 'OFF'
        
        self.output.info('Creating build scripts')
        cmake.configure(args, defs)
        
        self.output.info('Compiling')
        cmake.build()
        
        self.output.info('Running tests')
        cmake.build(target='test')
    
    def test(self):
        cpu_count = conans.tools.cpu_count()
        self.output.info('Detected %s CPUs' % cpu_count)
        
        self.output.info('Running tests')
        self.run('ctest --parallel %s' % (cpu_count))
