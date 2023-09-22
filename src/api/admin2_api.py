import requests


def main():
    url = "https://api-euw1.rms.com/li/geocode/latest/admin2?limit=100&offset=0"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)


if __name__ == "__main__":
    main()
