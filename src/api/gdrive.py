import requests

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def get_url(raw_url):
    try:
        url = "https://drive.google.com/uc?id=" + raw_url.split("/")[-2]
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return url
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        raise e


def download(file_id, path):
    # TODO set credentials_file to the path of your credentials file (pylint: disable=w0511)
    credentials_file = "path_to_your_credentials.json"

    credentials = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=["https://www.googleapis.com/auth/drive.readonly"]
    )
    drive_service = build("drive", "v3", credentials=credentials)
    request = drive_service.files().get_media(fileId=file_id)  # pylint: disable=E1101

    with open(path, "wb") as file:
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%")

    print(f"Downloaded '{path.split('/')[-1]}' from Google Drive.")
