#!/usr/bin/env python3
from src.api import create_fips_csv

log = \
    """
What's the purpose of this file?:

    This file is used to create a csv file that contains all the fips code for each state in the US
(Get API from Google Maps) and then use the fips code to get the latitude and longitude of each state

Note:
    this file is not used in the project just for checking the fips code and latitude and longitude of each state
that is collected from the API and from the csv file is matching or not.

Do you want to continue? (y/n):
"""


def main():
    create_fips_csv()


if __name__ == "__main__":
    res = input(log)
    if res.lower() == 'y':
        main()
