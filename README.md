# dual_autodiff
`dual_autodiff`is a Python package for automatic differentiation. It provides both pure Python and Cythonized implementations for efficient differentiation. Detailed information and examples can be found in the documentation. Follow the steps below to get started:

#### Pre-requisites
Make sure you have C compliers installed (in particular `gcc`), if this is not installed, then the Cythonised package will not compile.
How to ensure `gcc` is installed!

On Debian/Ubuntu and related distributions:
```bash
sudo apt-get install build-essential
```
This command will install `gcc`, `g++`, `make` and other utilities needed to compile C/C++ extensions in Python packages.

If you are on other operating system, you need the platform-appropriate development tools:

- macOS: Install Xcode Command Line Tools:
```bash
xcode-select --install
```

- Windows: Install Microsoft Build Tools (or have Visual Studio with appropriate C++ build tools). You can install `mingw-w64` and make sure it is on your PATH.

Python Development Headers:
```bash
sudo apt-get install python3-dev

```
For Python 3.12:
```bash
sudo apt-get install python3.12-dev

```
<b>Pandoc</b>: Pandoc is a universal documentation converter that `nbsphinx` uses to convert Jupyter notebook (`.ipynb` files) into reStructuredText or 
HTML for inclusion in Sphinx-generated documentation

This is required for the automatic documentation! This is included when running the command `pip install .[docs]`, only perform the following steps
in case you encounter the following error:
```bash
Notebook error:
PandocMissing in Solutions.ipynb:
Pandoc wasn't found.
Please check that pandoc is installed:
https://pandoc.org/installing.html
make: *** [Makefile:19: html] Error 2
```
while making documentation.

On Debian/Ubuntu-based systems:
```bash
sudo apt-get install pandoc
```
On macOS:
```bash
brew install pandoc
```
On Windows:
You can download the installer from the [official Pandoc website](https://pandoc.org/installing.html), and follow the steps provided.


#### Installing Package dual_autodiff

1. Create a Virtual Environment

   Run the following command to create your virtual environment

   ``` bash
    python -m venv <your_env>

- If the above command fails, please try:
   ```bash
   python3 -m venv <your_env>

Replace `<your_env>` with your preferred environment name, e.g. `dual_venv`.

2. Activate your virtual environment

  Activate your virtual environment with:
   ```bash
    source <your_env>/bin/activate
   ```
  Deactivate your environment with:
   ```bash
    deactivate
   ```

3. Install the package

   You can install the `dual_autodiff` in two ways (ensure your virtual environment activated):

   - `pip install .` (or `pip install -e .` where `-e` flag allows you to install the package in editable mode) by executing this comand you will install both the pure python and the cythonised packages.

   - Alternatively you can use wheels `pip install wheelhouse/dual_autodiff_x-0.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl` (or navigate to the wheelhose directory `cd wheelhouse` and then execute the command `pip install dual_autodiff_x-0.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`)

#### Using dual_autodiff

There are two packages containing two libraries each, `dual_autodiff` (pure python containing libraries `Dual` and `NumDiff`) and `dual_autodiff_x` (cythonised package with libraries `DualX` and `NumDiffX`).

1. Pure python
   You can import the package as follows:
-   ```python
      import dual_autodiff 
     ```
-   ```python
      from dual_autodiff import Dual
      from dual_autodiff import NumDiff
     ```
2. Cythonised 
    ```python
    from dual_autodiff_x import DualX
    from dual_autodiff_x import NumDiffx
    ```

For more instructions on how to use the two packages please use the notebook provided i.e. dual_autodiff.ipynb, furthermore you can access the documentation, where the Jupyter Notebook and detailed explenation with exaples are provided.

#### Access Documentation
Building documentation; to build the documentation install the required dependencies:
```bash
pip install -e .[docs]
```

Then follow these steps:

1. Navigate to the `docs` directory:
   ```bash
   cd docs
   ```

2. Building documentation.

   To build documentation run the following commands:
   ```python
   make clean
   make html
   ```
3. Access documentation.

   To access documentation you can either run
-    ```python
      open _build/html/index.html
     ```
- Navigate on your file explorer to index.html and click on it (documentation should open on your default browser)

I would recomend to follow the second option.

#### Additional Notes

- For users: Ensure that your Python version matches the package requirements. The package is tested with Python 3.12x.
- For contributions: Editable installation (`pip install -e .`) is recomended for development purposes.

If you encounter issues or have feedback, feel free to contribute or raise issues in the repository.