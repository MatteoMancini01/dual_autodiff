# dual_autodiff
`dual_autodiff`is a Python package for automatic differentiation. It provides both pure Python and Cythonized implementations for efficient differentiation. Detailed information and examples can be found in the documentation. Follow the steps below to get started:


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

  Deactivate your environment with:
   ```bash
    deactivate


3. Install the package

   You can install the `dual_autodiff` in two ways (ensure your virtual environment activated):

   - `pip install .` (or `pip install -e .` where `-e` flag allows you to install the package in editable mode) by executing this comand you will install both the pure python and the cythonised packages.

   - Alternatively you can use wheels `pip install wheelhouse/dual_autodiff_x-0.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl` (or navigate to the wheelhose directory `cd wheelhouse` and then execute the command `pip install dual_autodiff_x-0.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`)

#### Using dual_autodiff

There are two packages containing two libraries each, `dual_autodiff` (pure python containing libraries `Dual` and `NumDiff`) and `dual_autodiff_x` (cythonised package with libraries `DualX` and `NumDiffX`).

1. Pure python
   You can import the package as follows:
   - ```python
      import dual_autodiff 
   - ```python
      from dual_autodiff import Dual
      from dual_autodiff import NumDiff
2. Cythonised 
    ```python
    from src/dual_autodiff_x import DualX
    from src/dual_autodiff_x import NumDiffx

For more instructions on how to use the two packages please use the notebook provided i.e. dual_autodiff.ipynb, furthermore you can access the documentation, where the Jupyter Notebook and detailed explenation with exaples are provided.

#### Access Documentation
To view the detailed documentation:

1. Navigate to the `docs` directory:
   ```bash
   cd docs

2. Install the required dependencies (e.g. `sphinx`) to generate the documentation, make sure yoru virtual environment is activated:
   ```python
   pip install -r requirements.txt

3. Building documentation.

   To build documentation run the following commands:
   ```python
   make clean
   make html

4. Access documentation.

   To access documentation you can either run
   - ```python
      open _build/html/index.html

   - Navigate on your file explorer to index.html and click on it (documentation should open on your default browser)

I would recomend to follow the second option.

#### Additional Notes

- For users: Ensure that your Python version matches the package requirements. The package is tested with Python 3.12x.
- For contributions: Editable installation (`pip install -e .`) is recomended for development purposes.

If you encounter issues or have feedback, feel free to contribute or raise issues in the repository.