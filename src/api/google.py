import requests


def get_url(raw_url):
    try:
        url = 'https://drive.google.com/uc?id=' + raw_url.split('/')[-2]
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        raise from e
