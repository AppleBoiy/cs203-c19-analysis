import os
import pandas as pd
from src.plotter import display_heatmap, histogram_plot, box_plot, density_plot


sample_data = pd.DataFrame({
    'State': ['Alabama', 'Alabama', 'Alabama'],
    'City/County/Borough/Region': ['City1', 'City2', 'City3'],
    'Total Death': [10, 20, 30],
    'Total Confirmed': [100, 200, 300],
    'Death Rate': [0.1, 0.2, 0.3],
    'lat': [34.7, 33.8, 35.0],
    'lon': [-86.6, -87.2, -86.7],
})


def test_display_heatmap():
    result = display_heatmap(sample_data, 'Alabama')
    assert result is not None


def test_histogram_plot():
    path = 'test/histogram_plot.png'
    histogram_plot(sample_data['Total Death'], 'Total Death', bins=5, path=path)
    assert os.path.exists(path)


def test_box_plot():
    path = 'test/box_plot.png'
    box_plot(sample_data['Total Death'], 'Total Death', path=path)
    assert os.path.exists(path)


def test_density_plot():
    path = 'test/density_plot.png'
    density_plot(sample_data['Total Death'], 'Total Death', path=path)
    assert os.path.exists(path)
