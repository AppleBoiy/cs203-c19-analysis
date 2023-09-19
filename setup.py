from src.downloader import DataDownloader

if __name__ == "__main__":
    data_downloader = DataDownloader(debug=True, write=True)
    data_downloader.start()
