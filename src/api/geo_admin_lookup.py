import os

import pandas as pd
import json
import sys
from urllib import request


def google_key():
    sys.path.append('/')
    home = os.path.expanduser("~")
    key_path = os.path.join(home, '.keys', 'google_map_api.key')
    with open(key_path, 'r') as f:
        key = f.read()
    return key


def generate_fips_code(state_code, county_code):
    # Ensure the state code and county code are valid and in the correct format.
    if len(state_code) != 2 or not state_code.isdigit() or \
            len(county_code) != 3 or not county_code.isdigit():
        raise ValueError("Invalid state or county code format")

    # Concatenate the state code and county code to create the FIPS code.
    fips_code = state_code + county_code

    return fips_code


def get_response(lat, lon):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={google_key()}"
    response = request.urlopen(url)
    data = json.loads(response.read())

    print(data)

    if data['status'] == 'OK':
        return data['results']

    raise PermissionError(f'{data["status"]}: {data["error_message"]}')


def get_admin2_info():
    df = pd.read_csv('../../data/coronavirus-covid-19-pandemic-usa-counties.csv', sep=';')
    lost_admin2 = df[df['Admin 2 FIPS Code'].isnull()]

    print(f'Number of rows with missing Admin 2 FIPS Code: {len(lost_admin2)}')
