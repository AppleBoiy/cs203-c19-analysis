import subprocess

required_libraries = [
    'requests',
    'pandas',
    'numpy',
    'matplotlib',
    'kaggle'
]


def is_library_installed(library_name):
    try:
        __import__(library_name)
        return True
    except ImportError:
        return False


def install_libraries():
    for library in required_libraries:
        try:
            if not is_library_installed(library):
                subprocess.check_call(["python", '-m', 'pip', 'install', library])
        except subprocess.CalledProcessError as e:
            print(f'Error while installing {library}: {e}')


if __name__ == "__main__":
    install_libraries()
