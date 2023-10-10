import pandas as pd


def format_type(df):
    if "FIPS" in df.columns:
        df["FIPS"] = df["FIPS"].astype(str).str.replace(".0", "")

    # Date is not a string, it's a date
    df["date"] = pd.to_datetime(df["date"])

    # Lat and Lon are not string, they are floated
    df["lat"] = df["lat"].astype(float)
    df["lon"] = df["lon"].astype(float)

    if "id" in df.columns:
        df.set_index("id", inplace=True)
    else:
        # use first column as index
        df.set_index("FIPS", inplace=True)
