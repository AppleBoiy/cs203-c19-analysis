import subprocess


def run_flake8():
    try:
        result = subprocess.run(['flake8', '.'], capture_output=True, text=True, check=False)
        print(result.stdout)
        if result.returncode == 0:
            print("No linting issues found.")
        else:
            print("Linting issues found. Please review the output above.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_flake8()
