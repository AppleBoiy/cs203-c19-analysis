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
$PIP_CMD install -r requirements.txt
````

## Dataset Verification and Download

Before utilizing the dataset, it's crucial to verify its integrity and ensure it's been correctly downloaded and
prepared for use. Execute the following command in your terminal:

```bash
$PYTHON_CMD processor.py
```

This script will conduct the necessary verification steps and ensure the dataset is correctly configured for your
project.

## Additional Setup (Troubleshooting)

If you encounter any errors during the setup process, follow these additional steps for troubleshooting:

1. Directly download the Kaggle dataset from the Kaggle website.
2. Place the downloaded dataset within the `data/` folder located at the root of your project.
3. Re-run the `processor.py` file.

After completing these additional steps, navigate to the `src/` folder and execute the following command:

```bash
cd src

$PYTHON_CMD validator.py
```

This will assist in successfully setting up the dataset.

## Unset Environment Variables

Once you've completed the setup and verification process, you can unset the environment variables to keep your
environment clean:

```bash
unset PYTHON_CMD
unset PIP_CMD
```

Once you've completed these prerequisites, along with any necessary troubleshooting, you'll be well-prepared to engage
with the Coronavirus Covid-19 US Counties Dataset and embark on your project.
