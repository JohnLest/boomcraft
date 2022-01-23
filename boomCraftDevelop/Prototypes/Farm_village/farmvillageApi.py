import requests

class FarmVillageApi:
    def __init__(self):
        self.uri = "http://192.113.50.2:20000"

    def get_potions(self):
        req = requests.get(f"{self.uri}/public/users/Tigrou")
        print(req)
        json = req.json()
        return json