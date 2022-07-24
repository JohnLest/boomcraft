import requests

class BoomcraftApi:
    def __init__(self):
        self.uri = "http://192.168.0.101:8000"

    def connect(self, mail, password):
        req = requests.get(f"{self.uri}/user/connect?mail_user={mail}&password={password}")
        print(req)
        json = req.json()
        return json

    def post_new_user(self, data):
        req = requests.post(f"{self.uri}/user/post_new_user", data=data)
        print(req)
        json = req.json()
        return json

    def get_resources_by_id(self, id_user):
        req = requests.get(f"{self.uri}/resource/get_resources_by_user?id_user={id_user}")
        print(req)
        json = req.json()
        return json

    def connect_with_facebook(self, data):
        req = requests.post(f"{self.uri}/user/facebook_authentication", data=data)
        json = req.json()
        return json
