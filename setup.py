import os
import platform
import numpy as np

from setuptools import find_packages
from skbuild import setup

numpy_include_dir = np.get_include()

package = "pupil_detectors"
package_dir = "src"

cmake_args = [

    # Hardcode the NumPy variables to bypass legacy scikit-build's execution check
        f"-DNumPy_INCLUDE_DIR={numpy_include_dir}",
        f"-DNUMPY_INCLUDE_DIR={numpy_include_dir}",
        f"-DPython3_NumPy_INCLUDE_DIRS={numpy_include_dir}",
        
    # 1. Provide a dummy path for the executable so it skips searching on the host filesystem
        "-DCYTHON_EXECUTABLE=cython",
        
        # 2. Hardcode the version variables to prevent it from executing the "--version" command
        "-DCYTHON_VERSION=3.0.11",
        "-DCHOSEN_CYTHON_VERSION=3.0.11", 
        
        "-DOpenCV_DIR=/Users/ajc212/Desktop/Tmp/OpenCV-android-sdk/sdk/native/jni",
        "-DANDROID_NDK_ABI_NAME=arm64-v8a",
        "-DANDROID_ABI=arm64-v8a",
]

if platform.system() == "Windows":
    # The Ninja cmake generator will use mingw (gcc) on windows travis instances, but we
    # need to use msvc for compatibility.
    cmake_args.append("-GVisual Studio 17 2022")


if __name__ == "__main__":
    setup(
        cmake_args=cmake_args,
        cmake_install_dir="src/pupil_detectors",
        cmake_source_dir="src/pupil_detectors",
        packages=find_packages(package_dir),
        package_dir={"": package_dir},
        include_package_data=False,
    )
