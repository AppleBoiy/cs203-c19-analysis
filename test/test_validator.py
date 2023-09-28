import logging

import pandas as pd
import pytest

from src.validator import validator, clean_data


@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
        'Admin 2 Level (City/County/Borough/Region)': ['City1', 'City2', 'City3'],
        'Province/State': ['State1', 'State2', 'State3'],
        'Total Death': [10, 5, 8],
        'Total Confirmed': [100, 50, 80],
        'location': ['(37.7749, -122.4194)', '(29.7604, -95.3698)', '(40.7128, -74.0060)'],
        'Death Rate': [0.1, 0.1, 0.1],
    })
    return data


def test_validator(sample_data, caplog):
    caplog.set_level(logging.DEBUG)  # Capture debug logs

    data = validator(sample_data)

    # Assert debug logs
    assert 'Data is validating...' in caplog.text
    assert 'Data is validated successfully' in caplog.text

    # Assert data correctness and changes
    assert isinstance(data, pd.DataFrame)
    assert data.columns.tolist() == [
        'Date', 'City/County/Borough/Region', 'State',
        'Total Death', 'Total Confirmed', 'Death Rate'
    ]
    assert (data['City/County/Borough/Region'] == ['City1', 'City2', 'City3']).all()
    assert data['State'].tolist() == ['State1', 'State2', 'State3']
    assert data['Total Death'].tolist() == [10, 5, 8]
    assert data['Total Confirmed'].tolist() == [100, 50, 80]


def test_clean_data(sample_data, caplog):
    caplog.set_level(logging.DEBUG)  # Capture debug logs

    data = validator(sample_data.copy())
    clean_data(data)

    # Assert debug logs
    assert 'Data is cleaning...' in caplog.text
    assert 'Data is cleaned successfully' in caplog.text

    # Assert data correctness and changes
    assert isinstance(data, pd.DataFrame)
    assert data.columns.tolist() == [
        'Date', 'City/County/Borough/Region', 'State',
        'Total Death', 'Total Confirmed', 'Death Rate'
    ]
    assert data['Death Rate'].tolist() == [0.1, 0.1, 0.1]
    assert not data.loc[data['Death Rate'].isnull(), 'Death Rate'].tolist()
