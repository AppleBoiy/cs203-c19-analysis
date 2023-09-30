#!/usr/bin/env python3
import logging

import pandas as pd

from directories import Path

LOG = \
    """
This action is used to validate and clean the data by remove the missing value and duplicate value.
Keeps the last duplicate value and remove all the missing value.
(Not recommended if you want to analyze data by date and location)

Removed:
- Remove the missing value
- Remove the duplicate value (Total Death, Total Confirmed)
- Remove the data that City/County/Borough/Region startswith 'out of' case-insensitive

Change:
- Change the header name (Admin 2 Level (City/County/Borough/Region) -> City/County/Borough/Region)
- Change the header name (Province/State -> State)
- Sort the data by State, Total Death, Total Confirmed

Added:
- Add Death Rate column
"""

admin2 = 'City/County/Borough/Region'
header = ['State', 'Total Death', 'Total Confirmed', 'Death Rate']


def validator(data=None):
    # log debug if progress is started
    logging.debug('Data is validating...')

    if isinstance(data, str):
        df = pd.read_csv(data)
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise TypeError('file must be a string or a pandas DataFrame')

    df.dropna(inplace=True)

    # drop location column because it is not needed for the model
    df.drop(['location'], axis=1, inplace=True)

    # change header name
    df.rename(
        columns={
            'Admin 2 Level (City/County/Borough/Region)': admin2
        },
        inplace=True
    )

    df.rename(columns={'Province/State': 'State'}, inplace=True)

    # convert datatype
    df['Date'] = pd.to_datetime(df['Date'])

    df.sort_values(by=header, inplace=True)

    df.drop_duplicates(
        subset=['State', admin2],
        keep='last',
        inplace=True
    )

    # Drop the data that City/County/Borough/Region startswith 'out of' case-insensitive
    df = df[~df[admin2].str.contains('out of', case=False)]

    # log debug if progress is run successfully
    logging.debug('Data is validated successfully')

    return df


def clean_data(df):
    # log debug if progress is started
    logging.debug('Data is cleaning...')

    # Sort the data by total death and total confirmed
    df.sort_values(
        by=header[:3],
        inplace=True
    )

    df['Death Rate'] = df['Total Death'] / df['Total Confirmed']

    # Total Death is zero, and Total Confirmed is zero then death rate is 0
    df.loc[df['Death Rate'].isnull(), 'Death Rate'] = 0

    # log debug if progress is run successfully
    logging.debug('Data is cleaned successfully')


if __name__ == '__main__':
    print(LOG)
    data = validator()
    clean_data(data)
    data.to_csv(f'{Path.DATA.value}/data.csv', index=False)
