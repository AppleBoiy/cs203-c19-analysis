import os

from urllib.error import URLError
import requests
import pandas as pd

from code.Z_playground.directories import Path
from code.Z_playground.src.api.gdrive import get_url


def fips_csv():
    file = "country_fips.csv"
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
        fips = df[df["NAME"] == name]
        return fips
    except IndexError:
        print(f"Error: {name} not found")
        return None


def get_data(path=None) -> pd.DataFrame:
    try:
        if path is None:
            path = fips_csv()

        # Check if the 'file' is a URL or a local file path
        if path.startswith("http") or path.startswith("https"):
            response = requests.get(path, timeout=10)
            response.raise_for_status()
            df = pd.read_csv(response.text)
        else:
            df = pd.read_csv(path)

        return df
    except URLError:
        url = get_url(path)
        return get_data(url)

    except FileNotFoundError as e:
        print(f"File Not Found Error: {e}")
        raise e


if __name__ == "__main__":
    create_fips_csv()
