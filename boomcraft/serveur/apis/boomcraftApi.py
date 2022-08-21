import requests

class BoomcraftApi:
    def __init__(self):
        self.uri = "http://192.168.0.110:40000"

    def connect(self, mail, password):
        req = requests.get(f"{self.uri}/user/connect?mail_user={mail}&password={password}")
        print(req)
        json = req.json()
        return req.status_code, json

    def post_new_user(self, data):
        req = requests.post(f"{self.uri}/user/post_new_user", data=data)
        print(req)
        json = req.json()
        return req.status_code, json

    def get_resources_by_id(self, id_user):
        req = requests.get(f"{self.uri}/resource/get_resources_by_user?id_user={id_user}")
        print(req)
        json = req.json()
        return json

    def connect_with_facebook(self, data):
        req = requests.post(f"{self.uri}/user/facebook_authentication", data=data)
        json = req.json()
        return req.status_code, json

    def get_weight_resource(self):
        req = requests.get(f"{self.uri}/resource/get_weight_resource")
        json = req.json()
        return json

    def update_resource_by_id(self, id_res, new_quantity):
        req = requests.put(f"{self.uri}/resource/update_resource_by_id?id_res={id_res}&new_quantity={new_quantity}")
        json = req.json()
        return json

    def get_user_by_mail(self, mail):
        req = requests.get(f"{self.uri}/user/get_user?mail_user={mail}")
        json = req.json()
        return req.status_code, json

    def get_user_by_id(self, id):
        req = requests.get(f"{self.uri}/user/get_user?id_user={id}")
        json = req.json()
        return req.status_code, json
