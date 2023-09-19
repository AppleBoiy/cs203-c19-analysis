import pandas as pd


def validate(file='coronavirus-covid-19-pandemic-usa-counties.csv'):
    df = pd.read_csv(file, sep=';')

    # drop FIPS code column (not needed)
    df.drop('Admin 2 FIPS Code', axis=1, inplace=True)

    return df


def create_validated_csv():
    df = validate()
    df.to_csv('validated.csv', index=False)

    print(df.head())


if __name__ == "__main__":
    create_validated_csv()
