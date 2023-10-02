import os
import requests
import pandas as pd

from directories import Path


def fips_csv():
    file = 'country_fips.csv'
    return os.path.join(Path.DATA.value, file)


def create_fips_csv(return_df=False):
    url = "https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*"
    with requests.get(url, timeout=10) as response:
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data[1:], columns=data[0])
            if return_df:
                return df
            df.to_csv(fips_csv(), index=False)
            print(df.head())
        else:
            print(f"Error: {response.status_code}")

    return None


def get_fips(name):
    try:
        df = pd.read_csv(fips_csv())
        fips = df[df['NAME'] == name]
        return fips
    except IndexError:
        print(f'Error: {name} not found')
        return None


def get_data(file=None) -> pd.DataFrame:
    if file is None:
        file: str = fips_csv()
    df = pd.read_csv(file)
    return df


if __name__ == '__main__':
    create_fips_csv()
