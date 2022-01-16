import requests

class BoomcraftApi:
    def __init__(self):
        self.uri = "http://192.113.50.7:8000"

    def connect(self, mail, password):
        req = requests.get(f"{self.uri}/user/connect?mail_user={mail}&password={password}")
        print(req)
        json = req.json()
        return json

    def post_new_user(self, json):
        req = requests.post(f"{self.uri}/user/post_new_user", data=json)
        print(req)
        json = req.json()
        return json

    def get_resources_by_id(self, id_user):
        req = requests.get(f"{self.uri}/resource/get_resources_by_user?id_user={id_user}")
        print(req)
        json = req.json()
        return json
