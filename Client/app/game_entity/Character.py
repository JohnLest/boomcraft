




class Character():
    
    def __init__(self):
        self.characterType=""
        self.name=""
        self.weapon=""
        self.attack=0

    def Character(self,characterType,name,weapon,attack,annee):
        self.characterType=characterType
        self.name=name
        self.weapon=weapon
        self.attack=attack


    def attack(self,entity):
        print(entity)


    def set_characterType(self,characterType):
        self.characterType=characterType
    def set_name(self,name):
        self.name=name
    def set_weapon(self,weapon):
        self.weapon=weapon
    def set_attack(self,attack):
        self.attack=attack


    def get_characterType(self):
        return self.characterType
    def get_name(self):
        return self.name
    def get_weapon(self):
        return self.weapon
    def get_attack(self):
        return self.attack




class Worker(Character):
    
    def __init__(self):
        self.characterType=""
        self.name=""
        self.weapon=""
        self.attack=0

    def Character(self,characterType,name,weapon,attack,annee):
        self.characterType=characterType
        self.name=name
        self.weapon=weapon
        self.attack=attack

    def attack(self,entity):
        print(entity)