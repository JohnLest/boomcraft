from enum import Enum

class WeaponType(Enum):
    LANCE = 1
    SWORD = 2
    BOW = 3

class CharacterType(Enum):
    WORKER = 1
    WARRIOR = 2
    ARCHER = 3
    HERO = 4

class Character():

    def __init__(self,character_type : CharacterType, name : str, weapon : WeaponType, attack : int):
        self.character_type=character_type
        self.name=name
        self.weapon=weapon
        self.attack=attack


    def attack(self,entity):
        print(entity)


    def set_character_type(self,character_type):
        self.characterType=character_type
    def get_character_type(self):
        return self.character_type

    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

    def set_weapon(self,weapon):
        self.weapon=weapon
    def get_weapon(self):
        return self.weapon

    def set_attack(self,attack):
        self.attack=attack
    def get_attack(self):
        return self.attack













class Worker(Character):
    
    def __init__(self, character_type, name, weapon, attack):
        super().__init__(character_type,name,weapon,attack)

    def Character(self,characterType,name,weapon,attack,annee):
        self.characterType=characterType
        self.name=name
        self.weapon=weapon
        self.attack=attack

    def attack(self,entity):
        print(entity)