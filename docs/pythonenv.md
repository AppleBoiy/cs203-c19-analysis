# Python Environment Setup

This document outlines the steps to create a Python environment from an existing configuration file (`environment.yml`
or `requirements.txt`). These steps will help you set up the necessary dependencies for your Python project.

# Table of Contents

- [Python Virtual Environment Setup with conda env](#python-virtual-environment-setup-with-conda-env)
    - [Create a New Virtual Environment from environment.yml](#create-a-new-virtual-environment-from-environmentyml)
    - [Create a New Virtual Environment from requirements.txt](#create-a-new-virtual-environment-from-requirementstxt)
- [Python Virtual Environment Setup with pyenv](#python-virtual-environment-setup-with-pyenv)
    - [Install pyenv](#install-pyenv)
    - [Create a Virtual Environment](#create-a-virtual-environment)

## Python Virtual Environment Setup with `conda env`

### Create a New Virtual Environment from environment.yml

1. **Activate Conda (if not already activated):**
   If you haven't activated Conda, open a terminal or command prompt and activate it by running:

   ```bash
   conda activate
   ```

2. **Create a New Conda Environment:**
   To create a new Conda environment from an existing `environment.yml` file, navigate to the directory containing
   the `environment.yml` file and run:

   ```bash
   conda env create -f environment.yml
   ```

   Replace `environment.yml` with the actual filename if it differs.

3. **Activate the New Environment:**
   Activate the newly created environment with the following command:

   ```bash
   conda activate <environment_name>
   ```

   Replace `<environment_name>` with the name of the environment specified in the `environment.yml` file.

### Create a New Virtual Environment from `requirements.txt`

1. **Activate Conda (if not already activated):**
   If you haven't activated Conda, open a terminal or command prompt and activate it by running:

   ```bash
   conda activate
   ```

2. **Create a New Conda Environment (Optional):**
   If you prefer using Conda to create a virtual environment, you can do so by running:

   ```bash
   conda create --name myenv python=3.8
   ```

   Replace `myenv` with the desired environment name and adjust the Python version if needed.

3. **Activate the Conda Environment:**
   Activate the Conda environment you just created or an existing one with the following command:

   ```bash
   conda activate <environment_name>
   ```

   Replace `<environment_name>` with the name of the environment you created or intend to use.

4. **Install Dependencies from `requirements.txt`:**
   Navigate to the directory containing the `requirements.txt` file and run:

   ```bash
   pip install -r dev-requirements.txt
   ```

   This will install the Python packages listed in the `requirements.txt` file.

## Python Virtual Environment Setup with `pyenv`

### Install `pyenv`

1. **Install `pyenv` (if not already installed):**

   If you haven't installed `pyenv` on your system, you can follow the official installation instructions for your
   operating system: [pyenv Installation](https://github.com/pyenv/pyenv#installation).

## Create a Virtual Environment

2. **Install the Desired Python Version:**

   Use `pyenv` to install the Python version you want to use for your virtual environment. Replace `<python_version>`
   with the Python version you prefer:

   ```bash
   pyenv install <python_version>
   ```

3. **Create a Python Virtual Environment:**

   Create a new Python virtual environment using `pyenv`. You can name your environment as desired,
   replacing `<env_name>` with a suitable name:

   ```bash
   pyenv virtualenv <python_version> <env_name>
   ```

This command creates a virtual environment named `myenv` using the specified Python version.

4. **Activate the Virtual Environment:**

   Activate your newly created virtual environment with the following command:

   ```bash
   pyenv activate <env_name>
   ```

   Replace `<env_name>` with the name you chose for your virtual environment (e.g., `myenv`).

5. **Navigate to Your Project Directory:**

   Use the `cd` command to navigate to the directory where your Python project and the `requirements.txt` file are
   located:

   ```bash
   cd /path/to/your/project
   ```

6. **Install Packages from `requirements.txt`:**

   While your virtual environment is activated, use `pip` to install the packages listed in the `requirements.txt` file:

   ```bash
   pip install -r dev-requirements.txt
   ```

This will install the required Python packages into your virtual environment.

7. **Verify the Installation:**

   You can verify that the packages have been successfully installed in your virtual environment by running:

   ```bash
   pip list
   ```

   This will display a list of installed packages in your virtual environment.