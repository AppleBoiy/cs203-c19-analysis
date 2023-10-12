import pandas as pd


def get_data():
    files = [
        "spring1.csv",
        "summer1.csv",
        "fall1.csv",
        "winter1.csv",
        "spring2.csv",
        "summer2.csv",
        "fall2.csv",
        "winter2.csv",
    ]
    data_dir = "../C_exploration/data"
    data = pd.concat(
        [pd.read_csv(f"{data_dir}/{file}") for file in files], ignore_index=True
    )
    data["date"] = pd.to_datetime(data["date"])
    data["cases"] = data["cases"].astype("int")
    data["death"] = data["death"].astype("int")
    return data


def create_ready_to_use_data():
    data = get_data()
    data.drop(columns=["state"], inplace=True)
    data.to_csv("data.csv", index=False)


if __name__ == "__main__":
    create_ready_to_use_data()
