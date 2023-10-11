# Prerequisites

Before you can effectively utilize this project, it's essential to ensure that you have the necessary prerequisites and
dataset prepared. Follow the steps outlined below to set up your environment and data.

## Optional: Dataset Download

For comprehensive information about the dataset, consider downloading it directly using the provided `download.sh`
script. Open your terminal and execute the following command:

```bash
bash src/download.sh
```

This script will facilitate the dataset download, making it readily available for your project.

## Environment Setup

In order to establish the required environment for this project, you'll need to install all the necessary packages.
First, let's determine which version of Python is available:

```bash
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
    PIP_CMD="python3 -m pip"
else
    PYTHON_CMD="python"
    PIP_CMD="python -m pip"
fi

# Use $PYTHON_CMD and $PIP_CMD for commands based on available Python version.
echo "Using $PYTHON_CMD for Python and $PIP_CMD for pip."
```

Now, you can use the $PYTHON_CMD and $PIP_CMD variables to run commands based on the available Python version. For
example, to install packages:

```bash
$PIP_CMD install -r dev-requirements.txt
````

## Dataset Verification and Download

Before utilizing the dataset, it's crucial to verify its integrity and ensure it's been correctly downloaded and
prepared for use. Execute the following command in your terminal:

```bash
$PYTHON_CMD prerequisites.py
```

This script will conduct the necessary verification steps and ensure the dataset is correctly configured for your
project.

## Additional Setup (Troubleshooting)

If you encounter any errors during the setup process, follow these additional steps for troubleshooting:

1. Directly download the Kaggle dataset from the Kaggle website.
2. Place the downloaded dataset within the `data/` folder located at the root of your project.
3. Re-run the `prerequistes.py` file.

This will assist in successfully setting up the dataset.

## Optional: FIPS Dataset Integration

If you wish to incorporate the FIPS dataset into your analysis, it is necessary to execute the `api/setup.py` script in
order to download and prepare the dataset. To initiate this process, please utilize the following command:

```bash
$PYTHON_CMD src/api/setup.py
```

By running this command, you will ensure that the FIPS dataset is properly acquired and configured, enhancing the
comprehensiveness of your analysis.

## Optional: Create Python Environment

If you need to set up a Python environment for this project,
we have provided detailed instructions in a separate document.
Please refer to the [`pythonenv.md`](pythonenv.md) file for step-by-step instructions
on creating a Python environment with the necessary dependencies.

Creating a dedicated Python environment is highly recommended to ensure a consistent and isolated development
environment for your project. This helps in managing project-specific dependencies and avoiding conflicts with other
Python projects.

To get started, simply follow the instructions in the [pythonenv.md](pythonenv.md) document, and you'll be up and
running in no time.

## Unset Environment Variables

Once you've completed the setup and verification process, you can unset the environment variables to keep your
environment clean:

```bash
unset PYTHON_CMD
unset PIP_CMD
```

Once you've completed these prerequisites, along with any necessary troubleshooting, you'll be well-prepared to engage
with the Coronavirus Covid-19 US Counties Dataset and embark on your project.
