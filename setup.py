from setuptools import setup,find_packages, Extension
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
    name="dual_autodiff",
    version="0.1.0",
    description="This is a Python package designed to implement automatic differentiation using dual numbers.",
    author="Matteo Mancini",
    author_email="mem97@cam.ac.uk",
    license="Unilicense",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    install_requires=[
        "numpy>=1.26.4,<2.0.0",
        "pandas>=2.0.0,<3.0.0",
        "matplotlib>=3.9.0,<4.0.0",
        "pytest >=6.2, < 9.0.0",
        "ipytest >= 0.14.2, <1.0.0",
    ],
    extras_require={
        "notebooks": ["jupyter", "matplotlib", "pandas", "ipywidgets"],
        "docs": ["sphinx", "myst-parser", "sphinx-rtd-theme", "sphinx-gallery", "nbsphinx", "pylatex"],
    },
    package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},
    exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},
    zip_safe=False,
)

