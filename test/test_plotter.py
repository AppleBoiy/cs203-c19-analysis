import folium
import numpy as np
import pandas as pd
import pytest
from matplotlib import pyplot as plt

from src.plotter import display_heatmap, histogram_plot, box_plot, density_plot


@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'State': ['California', 'Texas', 'New York'],
        'Total Death': [1000, 2000, 3000],
        'lat': [37.7749, 29.7604, 40.7128],
        'lon': [-122.4194, -95.3698, -74.0060]
    })


def test_display_heatmap(sample_data):
    result = display_heatmap(sample_data, 'California')
    assert isinstance(result, folium.Map)
    assert result.location == [37.7749, -122.4194]


def test_display_heatmap_no_data(sample_data):
    assert display_heatmap(sample_data, 'Florida') is None


def test_histogram_plot():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    column_name = 'TestData'
    bins = 5
    path = 'test/histogram.png'

    histogram_plot(data, column_name, bins, path)

    assert np.all(plt.gcf().get_size_inches() == (8, 6))
    assert plt.gca().get_xlabel() == column_name
    assert plt.gca().get_ylabel() == 'Frequency'
    assert plt.gca().get_title() == f'Distribution of {column_name}'
    assert plt.gca().get_legend() is None
    assert plt.gca().get_xlim() == (0.55, 10.45)
    assert plt.gca().get_ylim() == (0.0, 2.1)
    assert plt.gca().get_xticks().tolist() == [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
    assert plt.gcf().get_facecolor() == (1.0, 1.0, 1.0, 1.0)


def test_box_plot():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    column_name = 'TestData'
    path = 'test/boxplot.png'

    box_plot(data, column_name, path)

    assert np.all(plt.gcf().get_size_inches() == (8, 6))
    assert plt.gca().get_xlabel() == column_name
    assert plt.gca().get_ylabel() == ''
    assert plt.gca().get_title() == f'Box Plot of {column_name}'
    assert plt.gca().get_legend() is None
    assert plt.gca().get_xlim() == (0.55, 10.45)
    assert plt.gca().get_ylim() == (0.5, 1.5)
    assert plt.gcf().get_facecolor() == (1.0, 1.0, 1.0, 1.0)
    assert sum(len(line.get_xdata()) for line in plt.gca().get_lines()) == 10


def test_density_plot():
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    column_name = 'TestData'
    path = 'test/densityplot.png'

    density_plot(data, column_name, path)

    assert np.all(plt.gcf().get_size_inches() == (8, 6))
    assert plt.gca().get_xlabel() == column_name
    assert plt.gca().get_ylabel() == 'Density'
    assert plt.gca().get_title() == f'Density Plot of {column_name}'
    assert plt.gca().get_legend() is None
    assert len(plt.gca().get_lines()) == 1
    assert plt.gcf().get_facecolor() == (1.0, 1.0, 1.0, 1.0)
