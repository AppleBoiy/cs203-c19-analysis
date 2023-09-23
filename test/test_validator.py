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


def test_clean_data(sample_data):
    clean_data(sample_data)
    assert isinstance(sample_data, pd.DataFrame)
    assert not sample_data.empty

    assert 'Death Rate' in sample_data.columns
    assert 'Date' in sample_data.columns
    assert 'City/County/Borough/Region' in sample_data.columns

    assert sample_data['Death Rate'][0] == 1  # 10 / 10 = 1
    assert sample_data['Death Rate'][1] == 0.1  # 20 / 200 = 0.1
    assert sample_data['Death Rate'][2] == 0  # 0 / 30 = 0
    assert sample_data['Death Rate'][3] == 0  # 0 / 0 = 0

    assert not sample_data.isnull().any().any()
