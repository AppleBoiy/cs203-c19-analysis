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


def test_plotter():
    result = display_heatmap(sample_data, 'Alabama')
    assert result is not None

    header = 'Total Death'
    total_death = sample_data[header]

    path = 'test/histogram_plot.png'
    histogram_plot(total_death, header, bins=5, path=path)
    assert os.path.exists(path)

    path = 'test/box_plot.png'
    box_plot(total_death, header, path=path)
    assert os.path.exists(path)

    path = 'test/density_plot.png'
    density_plot(total_death, header, path=path)

    assert os.path.exists(path)
