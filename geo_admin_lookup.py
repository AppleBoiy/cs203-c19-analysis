import pandas as pd
import json
from urllib import request


def api_request():
    url = "https://geo.fcc.gov/api/census/#!/area/get_area"
    headers = {"accept": "application/json"}
    response = request.urlopen(url)
    print(response.text)

def get_admin2_info():
    df = pd.read_csv('coronavirus-covid-19-pandemic-usa-counties.csv', sep=';')
    lost_admin2 = df[df['Admin 2 FIPS Code'].isnull()]

    print(f'Number of rows with missing Admin 2 FIPS Code: {len(lost_admin2)}')
    print(lost_admin2.head())


if __name__ == "__main__":
    api_request()
