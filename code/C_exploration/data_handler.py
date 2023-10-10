import pandas as pd


def format_type(df):
    df["FIPS"] = df["FIPS"].astype(str).str.replace(".0", "")

    # Date is not a string, it's a date
    df["Date"] = pd.to_datetime(df["Date"])

    # Lat and Lon are not string, they are floated
    df["lat"] = df["lat"].astype(float)
    df["lon"] = df["lon"].astype(float)

    df.set_index("id", inplace=True)
