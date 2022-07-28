import requests

class OtherApi:
    def __init__(self, uri):
        self.uri = uri

    def get_request(self, request):
        req = requests.get(f"{self.uri}/{request}")
        json = req.json()
        return json