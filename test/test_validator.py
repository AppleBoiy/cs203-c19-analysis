import pandas as pd
import pytest
from src.validator import clean_data


@pytest.fixture
def sample_data():
    data = {
        'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
        'State': ['State A', 'State B', 'State A', 'State B'],
        'City/County/Borough/Region': ['City X', 'City Y', 'City Z', 'City W'],
        'Total Death': [10, 20, 0, 0],
        'Total Confirmed': [10, 200, 30, 0],
        'location': ['1.1,2.2', '5.5,6.6', '7.7,8.8', '0, 0']
    }
    return pd.DataFrame(data)


# Define a test for the clean_data function
def test_clean_data(sample_data):
    # Call the clean_data function on the sample data
    clean_data(sample_data)

    # Check if the result is a DataFrame and not empty
    assert isinstance(sample_data, pd.DataFrame)
    assert not sample_data.empty

    # Check the presence of specific columns
    assert 'Death Rate' in sample_data.columns
    assert 'Date' in sample_data.columns
    assert 'City/County/Borough/Region' in sample_data.columns

    # Check the values in the 'Death Rate' column
    death_rate = sample_data['Death Rate']
    assert death_rate[0] == 1
    assert death_rate[1] == 0.1
    assert death_rate[2] == 0
    assert death_rate[3] == 0

    # Check that there are no missing values in the DataFrame
    assert not sample_data.isnull().any().any()
