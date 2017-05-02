cmake_minimum_required(VERSION 2.8)

project(PackageInfoBugTest C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
if(CMAKE_VERSION VERSION_LESS 3.1.2)
conan_basic_setup()
else()
conan_basic_setup(TARGETS)
endif()

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_executable(main main.c)

if(CMAKE_VERSION VERSION_LESS 3.1.2)
target_link_libraries(main ${CONAN_LIBS})
else()
target_link_libraries(main CONAN_PKG::PackageInfoBug)
endif()

enable_testing()

add_test(NAME verify_executable COMMAND main)
set_tests_properties(verify_executable PROPERTIES
    PASS_REGULAR_EXPRESSION "client version: 2.1.3\nserver version: 5.4.16\n"
)
