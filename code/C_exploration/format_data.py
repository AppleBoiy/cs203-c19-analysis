import pandas as pd


def format_type(df, pre=False):
    # Date is not a string, it's a date
    df["date"] = pd.to_datetime(df["date"])

    if pre:
        df["FIPS"] = df["FIPS"].astype(str).str.replace(".0", "")
        # Lat and Lon are not string, they are floated
        df["lat"] = df["lat"].astype(float)
        df["lon"] = df["lon"].astype(float)
    else:
        df["cases"] = df["cases"].astype(int)
        df["deaths"] = df["death"].astype(int)
        df.drop(columns=["death"], inplace=True)

    if "id" in df.columns:
        df.set_index("id", inplace=True)
    else:
        # use first column as index
        df.set_index("FIPS", inplace=True)
