import folium

from matplotlib import pyplot as plt


def display_heatmap(df, state_name):
    total_deaths_sum = df["Total Death"].sum()

    # Filter the dataset based on the input state or province name
    state_df = df[df["State"] == state_name]

    if state_df.empty:
        print(f"No data found for {state_name}.")
        return None

    # Calculate the Death Ratio and Confirmed Ratio for the selected state
    death_ratio = state_df.iloc[0]["Total Death"] / total_deaths_sum

    # Create a base map centered at the selected state's location
    m = folium.Map(
        location=[state_df.iloc[0]["lat"], state_df.iloc[0]["lon"]], zoom_start=6
    )

    # Create and add the Death Ratio Heatmap
    folium.CircleMarker(
        location=(state_df.iloc[0]["lat"], state_df.iloc[0]["lon"]),
        radius=10 * death_ratio,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        popup=f"State: {state_name}<br>Death Ratio: {death_ratio:.2f}",
    ).add_to(m)

    # Display the map in the Jupyter Notebook
    return m


def histogram_plot(data, column_name, bins=20, path=None):
    _, ax = plt.subplots(figsize=(8, 6))

    ax.hist(data, bins=bins, color="skyblue", edgecolor="black")
    ax.set_xlabel(column_name)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of {column_name}")
    ax.grid(True, linestyle="--", alpha=0.6)

    if path is not None:
        plt.savefig(path)


def box_plot(data, column_name, path=None):
    _, ax = plt.subplots(figsize=(8, 6))

    ax.boxplot(
        data,
        vert=False,
        widths=0.7,
        patch_artist=True,
        boxprops={"facecolor": "skyblue"},
    )
    ax.set_xlabel(column_name)
    ax.set_title(f"Box Plot of {column_name}")
    ax.grid(True, linestyle="--", alpha=0.6)

    if path is not None:
        plt.savefig(path)


def density_plot(data, column_name, path=None):
    _, ax = plt.subplots(figsize=(8, 6))

    data.plot(kind="density", color="skyblue", ax=ax)
    ax.set_xlabel(column_name)
    ax.set_ylabel("Density")
    ax.set_title(f"Density Plot of {column_name}")
    ax.grid(True, linestyle="--", alpha=0.6)

    if path is not None:
        plt.savefig(path)
