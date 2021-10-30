




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


    def setcharacterType(self,characterType):
        
        self.characterType=characterType
    def setname(self,name):
        self.name=name
    def setweapon(self,weapon):
        self.weapon=weapon
    def setattack(self,attack):
        self.attack=attack


    def getcharacterType(self):
        return self.characterType
    def getname(self):
        return self.name
    def getweapon(self):
        return self.weapon
    def getattack(self):
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