import folium


def display_heatmap(df, state_name) -> folium.Map | None:
    total_deaths_sum = df['Total Death'].sum()
    total_confirmed_sum = df['Total Confirmed'].sum()

    # Filter the dataset based on the input state or province name
    state_df = df[df['Province/State'] == state_name]

    if state_df.empty:
        print(f"No data found for {state_name}.")
        return None

    # Calculate the Death Ratio and Confirmed Ratio for the selected state
    death_ratio = state_df.iloc[0]['Total Death'] / total_deaths_sum
    confirmed_ratio = state_df.iloc[0]['Total Confirmed'] / total_confirmed_sum

    # Create a base map centered at the selected state's location
    m = folium.Map(location=[state_df.iloc[0]['lat'], state_df.iloc[0]['lon']], zoom_start=6)

    # Create and add the Death Ratio Heatmap
    folium.CircleMarker(
        location=(state_df.iloc[0]['lat'], state_df.iloc[0]['lon']),
        radius=10 * death_ratio,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        popup=f"State: {state_name}<br>Death Ratio: {death_ratio:.2f}",
    ).add_to(m)

    # Create and add the Confirmed Ratio Heatmap
    folium.CircleMarker(
        location=(state_df.iloc[0]['lat'], state_df.iloc[0]['lon']),
        radius=10 * confirmed_ratio,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=f"State: {state_name}<br>Confirmed Ratio: {confirmed_ratio:.2f}",
    ).add_to(m)

    # Display the map in the Jupyter Notebook
    return m
