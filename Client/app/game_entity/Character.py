from enum import Enum
from app.Tools import Tools
from app.game_entity.Entity import Entity
from app.game_entity.Environment import Environment, EnvironmentType
from app.game_entity.Mobile import Mobile
from app.game_entity.Ressource import RessourceType
from app.game_structure.Coord import Coord

class WeaponType(Enum):
    LANCE = 1
    SWORD = 2
    BOW = 3
    PITCHFORK = 4
    PICKAXE = 5



class CharacterType(Enum):
    WORKER = 1
    WARRIOR = 2
    ARCHER = 3
    HERO = 4

class Character(Mobile):

    def __init__(self,character_type : CharacterType, name : str, weapon : WeaponType, attack : int, coords : list[Coord], life : int, look_in_game : str, ressource_dropped : RessourceType):
        super().__init__(character_type, True, False, coords, 2, 2, life, look_in_game, ressource_dropped)

        self.__character_type=character_type
        self.__name=name
        self.__weapon=weapon
        self.__attack=attack


    def attack(self, entity : Entity):
        print(entity)


    def set_character_type(self,character_type):
        self.__character_type=character_type
    def get_character_type(self):
        return self.__character_type

    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

    def set_weapon(self,weapon):
        self.__weapon=weapon
    def get_weapon(self):
        return self.__weapon

    def set_attack(self,attack):
        self.__attack=attack
    def get_attack(self):
        return self.__attack













class Worker(Character):
    path_to_img = "ressources/worker_img.png"
    ''' 
    Path to the image of the Worker
    '''
    def __init__(self, name, weapon, coords):

        super().__init__(CharacterType.WORKER, name, weapon, Tools.give_random_int_between(1, 30), coords,  Tools.give_random_int_between(50, 80), Worker.path_to_img, RessourceType.WOOD)
    
    def harvest(self, envi : Environment):
        """ 
        get ressources from entity
        """
        switcher={
                   EnvironmentType.TREE: RessourceType.WOOD,
                    EnvironmentType.ROCK: RessourceType.STONE ,
                    EnvironmentType.WATER: RessourceType.FOOD,
                    EnvironmentType.CREVASSE: RessourceType.IRON,
                    EnvironmentType.RUIN :  RessourceType.STONE
        }
        return switcher.get(envi.get_env_type(),"Invalid environment type")
