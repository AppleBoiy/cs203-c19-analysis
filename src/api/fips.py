import json

import pandas as pd
from urllib import request

root = '../../data/'


def create_fips_csv():
    url = "https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*"
    response = request.urlopen(url)
    data = json.loads(response.read())

    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_csv(root + 'country_fips.csv', index=False)

    print(df.head())


def get_fips(name):
    df = pd.read_csv(root + 'country_fips.csv')
    try:
        fips = df[df['NAME'] == name]
        return fips
    except IndexError:
        print(f'Error: {name} not found')
        return None


def get_data(file=None) -> pd.DataFrame:
    if file is None:
        file = root + 'country_fips.csv'
    df = pd.read_csv(file)
    return df


def sample():
    df = pd.read_csv(root + 'country_fips.csv')
    print(df.head())