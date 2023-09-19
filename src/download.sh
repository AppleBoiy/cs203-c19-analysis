#!/usr/bin/env bash
# this script downloads the data from kaggle

mkdir -p "data" && data_dir="data"

zip_file="corona-virus-covid19-us-counties.zip"
csv_file="coronavirus-covid-19-pandemic-usa-counties.csv"



# Check if the CSV file already exists in the data directory
if [ ! -f "$zip_file" ] && [ ! -f "$csv_file " ] ; then
    # If it doesn't exist, download and unzip the data
    kaggle datasets download -d yasirabdaali/corona-virus-covid19-us-counties
fi

if [ -f "$zip_file" ] && [ ! -f "$csv_file" ]; then
    unzip "$zip_file"
fi

if [ -f "$csv_file" ]; then
    # If it doesn't exist, unzip the data
    mv "$csv_file" "$data_dir/" &&
    rm "$zip_file"
fi
