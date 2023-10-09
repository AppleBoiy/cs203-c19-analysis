import pandas as pd

from src.api import fips_csv, get_fips, get_data


def test_get_fips_existing(capsys, mocker):
    name = "County1"

    mocker.patch("pandas.read_csv")
    df_mock = mocker.MagicMock()
    df_mock.__getitem__.return_value = df_mock
    df_mock.__eq__.return_value = df_mock
    df_mock.sel.return_value = df_mock
    df_mock.to_csv.return_value = df_mock
    df_mock.head.return_value = df_mock

    pd.read_csv.return_value = df_mock

    result = get_fips(name)

    assert result == df_mock
    out, _ = capsys.readouterr()
    assert out == ""


def test_get_data_with_file(capsys, mocker):
    file = "data.csv"

    mocker.patch("pandas.read_csv")
    df_mock = mocker.MagicMock()
    df_mock.to_csv.return_value = df_mock
    df_mock.head.return_value = df_mock

    pd.read_csv.return_value = df_mock

    result = get_data(file)

    assert result == df_mock

    pd.read_csv.assert_called_once_with(file)
    df_mock.to_csv.assert_not_called()
    df_mock.head.assert_not_called()

    out, _ = capsys.readouterr()
    assert out == ""


def test_get_data_no_file(capsys, mocker):
    mocker.patch("pandas.read_csv")
    df_mock = mocker.MagicMock()
    df_mock.to_csv.return_value = df_mock
    df_mock.head.return_value = df_mock

    pd.read_csv.return_value = df_mock

    result = get_data()

    assert result == df_mock

    pd.read_csv.assert_called_once_with(fips_csv())
    df_mock.to_csv.assert_not_called()
    df_mock.head.assert_not_called()

    out, _ = capsys.readouterr()
    assert out == ""
