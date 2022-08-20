import requests


def get_request(uri, request):
    req = requests.get(f"{uri}/{request}")
    json = req.json()
    return json
