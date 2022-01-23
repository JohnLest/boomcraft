import requests

class VeggieCrushApi:
    def __init__(self):
        self.uri = "http://192.113.50.2:8505"

    def get_potions(self):
        req = requests.get(f"{self.uri}/potions")
        print(req)
        json = req.json()
        return json