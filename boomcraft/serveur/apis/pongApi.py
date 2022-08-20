import requests


class PongApi:
    def __init__(self):
        self.uri = "https://pogogame.azurewebsites.net"

    def login(self, body):
        url = f"{self.uri}/User/Login"
        header = {'Content-Type': 'application/json'}
        req = requests.request("POST", url, headers=header, data=body)
        json = req.json()
        return req.status_code, json
