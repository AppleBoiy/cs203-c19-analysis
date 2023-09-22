import logging

import pandas as pd


def validator(file='../data/validated.csv'):

    # log debug if progress is started
    logging.debug('Data is validating...')

    df = pd.read_csv(file)

    df.dropna(inplace=True)

    # drop location column because it is not needed for the model
    df.drop(['location'], axis=1, inplace=True)

    # change header name
    df.rename(
        columns={
            'Admin 2 Level (City/County/Borough/Region)': 'City/County/Borough/Region'
        },
        inplace=True
    )

    # convert datatype
    df['Date'] = pd.to_datetime(df['Date'])

    df.sort_values(
        by=[
            'Province/State',
            'City/County/Borough/Region',
            'Total Death', 'Total Confirmed'
        ],
        inplace=True
    )

    df.drop_duplicates(
        subset=[
            'Province/State',
            'City/County/Borough/Region'
        ],
        keep='last',
        inplace=True
    )

    # Drop the data that City/County/Borough/Region startswith 'out of' case-insensitive
    df = df[~df['City/County/Borough/Region'].str.contains('out of', case=False)]

    # log debug if progress is run successfully
    logging.debug('Data is validated successfully')

    return df


def clean_data(df):

    # log debug if progress is started
    logging.debug( 'Data is cleaning...')

    # Sort the data by total death and total confirmed
    df.sort_values(
        by=[
            'Province/State',
            'Total Death',
            'Total Confirmed'
        ],
        inplace=True
    )

    df['Death Rate'] = df['Total Death'] / df['Total Confirmed']

    # Total Death is zero, and Total Confirmed is zero then death rate is 0
    df.loc[df['Death Rate'].isnull(), 'Death Rate'] = 0

    # log debug if progress is run successfully
    logging.debug('Data is cleaned successfully')


if __name__ == '__main__':
    data = validator()
    clean_data(data)
    data.to_csv('../data/data.csv', index=False)
