def get_url(raw_url):
    return 'https://drive.google.com/uc?id=' + raw_url.split('/')[-2]
