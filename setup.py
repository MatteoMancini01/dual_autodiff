from setuptools import setup, Extension
from Cython.Build import cythonize
import sysconfig

# Get the include directory for Python
python_include_dir = sysconfig.get_paths()["include"]

extensions = [
    Extension(
        "dual_autodiff_x.dual", 
        ["src/dual_autodiff_x/dual.pyx"],
        include_dirs=[python_include_dir],  # Add the include path
    ),
    Extension(
        "dual_autodiff_x.n_diff", 
        ["src/dual_autodiff_x/n_diff.pyx"],
        include_dirs=[python_include_dir],  # Add the include path
    ),
]

setup(
    name="dual_autodiff_x",
    version="0.1.0",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    package_dir={"": "src"},
    packages=["dual_autodiff_x"],
    package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},
    exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},
    zip_safe=False,
)

