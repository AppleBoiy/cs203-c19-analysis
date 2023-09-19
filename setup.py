import os
import glob
import subprocess
import logging

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
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

        # Create console handler and set level based on a debug flag
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG if self.debug else logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Create file handler if debug mode is enabled
        if self.debug:
            file_handler = logging.FileHandler('app.log')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            return logger
        return logging

    def log(self, _type, message):
        """
        Log a message to the console.

        Args:
            _type (str): The type of message to log.
            message (str): The message to log.
        """

        if _type == "info":
            self.logger.info(message)
        elif _type == "error":
            self.logger.error(message)
        elif _type == "debug":
            self.logger.debug(message)
        else:
            self.logger.info(message)

    def download_data(self):
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
            self.logger.info("Downloaded data successfully.")
            self.logger.debug(output)
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error running the shell script: {e}")

    def start(self):
        """
        Start the data download and validation process.
        """
        prerequisites.install_libraries()
        data = get_data()

        if data is None:
            self.logger.info("Data not found. Downloading data...")

            self.download_data()
            data = get_data()

        excluded_files = ["data/validated.csv", "data/country_flips.csv"]
        raw_data = [file for file in data if file not in excluded_files]

        self.logger.info(f"Validating {raw_data[0]}...")

        if "data/validated.csv" not in data:
            status, df = prerequisites.create_validated_csv(raw_data[0], self.debug)

            if status == os.EX_OK and df is not None:
                prompt = (
                    f'Data was read successfully from {raw_data[0]}\n---'
                    'Here is a sample of the data:'
                    f'{df.head()}'
                )
                self.logger.info(prompt)

            else:
                self.logger.error("Error while validating data.")
        else:
            self.logger.info("Validated data found. Skipping validation.")


if __name__ == "__main__":
    # Set debug to True to enable logging, or False to disable it
    data_downloader = DataDownloader(debug=True)
    data_downloader.start()
