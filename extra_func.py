import requests

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content
