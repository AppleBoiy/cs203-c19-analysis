import os
import glob
import subprocess

import prerequisites


def get_data():
    """
    Get a list of CSV files in the 'data' directory.

    Returns:
        List[str]: List of CSV file paths.
    """
    directory_path = "data"
    csv_files = glob.glob(os.path.join(directory_path, "*.csv"))
    return csv_files


class DataDownloader:

    def __init__(self, debug=False):
        self.debug = debug

    def download_data(self, data=None):
        """
        Download data using a shell script.

        Raises:
            subprocess.CalledProcessError: If the shell script fails.
        """
        script_path = "src/download.sh"

        try:
            output = subprocess.check_output(
                ['bash', script_path],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            if self.debug:
                print("Downloaded data successfully.")
                print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error running the shell script: {e}")

    def start(self):
        """
        Start the data download and validation process.
        """
        prerequisites.install_libraries()
        data = get_data()

        if not data:
            if self.debug:
                print("Data not found. Downloading data...")
            self.download_data()
            data = get_data()

        excluded_files = ["data/validated.csv", "data/country_flips.csv"]
        raw_data = [file for file in data if file not in excluded_files]

        if self.debug and raw_data:
            print(f"Validating {raw_data[0]}...")

        if "data/validated.csv" not in data:

            status, df = prerequisites.create_validated_csv(raw_data[0], self.debug)

            if status == os.EX_OK:
                prompt = (
                    f'Data was read successfully from {raw_data[0]}\n---'
                    'Here is a sample of the data:'
                    f'{df.head()}'
                )
                print(prompt)

            else:
                print("Error while validating data.")
        else:
            if self.debug:
                print("Validated data found. Skipping validation.")


if __name__ == "__main__":
    data_downloader = DataDownloader(debug=True)
    data_downloader.start()
