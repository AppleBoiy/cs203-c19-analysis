import os
import subprocess
import pandas as pd


def is_library_installed(library_name):
    try:
        __import__(library_name)
        return True
    except ImportError:
        return False


def install_libraries():
    required_libraries = [
        'requests',
        'pandas',
        'numpy',
        'matplotlib',
        'kaggle'
    ]
    for library in required_libraries:
        try:
            if not is_library_installed(library):
                subprocess.check_call(["python", '-m', 'pip', 'install', library])
        except subprocess.CalledProcessError as e:
            print(f'Error while installing {library}: {e}')


def validate(file, debug=False):
    df = pd.read_csv(file, sep=';')
    if debug:
        debug_prompt = f"""
        data was read successfully from {file}
        
        Dataframe shape: {df.shape}
        Dataframe columns: {df.columns}
        Dataframe head: {df.head()}
        """

    # drop FIPS code column (not needed)
    df.drop('Admin 2 FIPS Code', axis=1, inplace=True)

    return df


def create_validated_csv(file, debug=False) -> os.EX_OK:
    try:
        df = validate(file, debug)
        df.to_csv('data/validated.csv', index=False)

        print('Validated CSV created successfully.')
        return os.EX_OK, pd.read_csv('data/validated.csv')
    except FileNotFoundError as e:
        print(f'Error while creating validated CSV: {e}')
        return os.EX_SOFTWARE, None
