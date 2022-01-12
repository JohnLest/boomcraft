class UserDTO:
    def __init__(self, pseudo):
        self.id = 0
        self.pseudo = pseudo
        self.mail = ""

    def get_pseudo(self):
        return self.pseudo
