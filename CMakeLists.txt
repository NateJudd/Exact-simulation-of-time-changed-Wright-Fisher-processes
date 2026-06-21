cmake_minimum_required(VERSION 3.18)
project(EWF LANGUAGES CXX VERSION 2.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

option(BUILD_SHARED_LIBS "Enable compilation of shared libraries" OFF)
option(PYTHON_BINDINGS "Whether to build python bindings" ON)

if (PYTHON_BINDINGS)
    include(FetchContent)
    FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG        v2.12.1
    )
    FetchContent_GetProperties(pybind11)
    if (NOT pybind11_POPULATED)
        FetchContent_MakeAvailable(pybind11)
    endif()
endif()

add_subdirectory(src)
