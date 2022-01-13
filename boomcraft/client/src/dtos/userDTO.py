class UserDTO:
    def __init__(self, id, pseudo, mail):
        self.id = id
        self.pseudo = pseudo
        self.mail = mail

    def get_id(self):
        return self.id

    def get_pseudo(self):
        return self.pseudo

    def get_mail(self):
        return self.mail

