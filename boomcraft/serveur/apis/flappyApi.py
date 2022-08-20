import requests


class FlappyApi:
    def __init__(self):
        self.uri = "https://api.flappybird2.games"
        self.header = {'Content-Type': 'application/json'}

    def login(self, body):
        req = requests.post(f"{self.uri}/AuthenticationCustom/login", headers=self.header, data=body)
        json = req.json()
        return req.status_code, json

    def get_player_exist(self, mail, token):
        self.header.update({"Authorization": f"Bearer {token}"})
        req = requests.get(f"{self.uri}/Player/PlayerExistOrNot/{mail}")
        json = req.json()
        return req.status_code, json

    def get_resources(self, id_player, token):
        self.header.update({"Authorization": f"Bearer {token}"})
        req = requests.get(f"{self.uri}/Ressource/GetRessources/{id_player}")
        json = req.json()
        return req.status_code, json

    def get_resource_list(self, token):
        self.header.update({"Authorization": f"Bearer {token}"})
        req = requests.get(f"{self.uri}/Ressource/all")
        json = req.json()
        return req.status_code, json

    def remove_resources(self, token, body):
        self.header.update({"Authorization": f"Bearer {token}"})
        req = requests.post(f"{self.uri}/Ressource/decreaseAmountRessource", headers=self.header, data=body)
        return req.status_code

