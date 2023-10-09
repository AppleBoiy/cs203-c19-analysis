import pandas as pd


def func_name(df):
    df["FIPS"] = df["FIPS"].astype(str).str.replace(".0", "")

    # Date is not a string, it's a date
    df["Date"] = pd.to_datetime(df["Date"])

    # Lat and Lon are not string, they are floated
    df["lat"] = df["lat"].astype(float)
    df["lon"] = df["lon"].astype(float)

    length = df.shape[0]
    length = len(str(length))

    df["id"] = df["Abbr"] + df.index.astype(str).str.zfill(length)

    df = df.set_index("id", inplace=True)

    new_cols = [
        "FIPS",
        "lat",
        "lon",
        "State",
        "Abbr",
        "City/County/Borough/Region",
        "infected total",
        "death total",
    ]
    df = df.reindex(columns=new_cols)

    return df
