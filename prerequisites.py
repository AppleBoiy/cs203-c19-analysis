from directories import Path
from src.downloader import DataDownloader
from src.validator import validator, clean_data

if __name__ == "__main__":
    data_downloader = DataDownloader(debug=True)
    data_downloader.start()

    file = f'{Path.DATA.value}/validated.csv'
    data = validator(data=file)
    clean_data(data)
    data.to_csv(f'{Path.DATA.value}/data.csv', index=False)
