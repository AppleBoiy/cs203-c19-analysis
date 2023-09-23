import os
import json
import sys

from urllib import request
import pandas as pd


def google_key():
    sys.path.append('/')
    home = os.path.expanduser("~")
    key_path = os.path.join(home, '.keys', 'google_map_api.key')
    with open(key_path, 'r', encoding='utf-8') as f:
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


def get_response(lat, lon, google_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={google_key}"

    try:
        with request.urlopen(url, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data
            print(f"HTTP Error {response.status}: {response.reason}")
    except request.URLError as e:
        print(f"URLError: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")

    return None  # Return None in case of errors


def get_admin2_info():
    df = pd.read_csv('../../data/coronavirus-covid-19-pandemic-usa-counties.csv', sep=';')
    lost_admin2 = df[df['Admin 2 FIPS Code'].isnull()]

    print(f'Number of rows with missing Admin 2 FIPS Code: {len(lost_admin2)}')
