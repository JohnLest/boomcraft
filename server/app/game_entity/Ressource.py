from enum import Enum


class RessourceType(Enum):
    MOBILE = 1
    CHARACTER = 2
    WORKER = 3
    GOLD = 4
    STONE = 5
    WOOD = 6
    IRON = 7
    FOOD = 8

class Ressource :
    
    def __init__(self, ressource_type : RessourceType):
        
        self.__ressource_type = ressource_type


    def set_ressource_type(self,ressource_type : RessourceType):
        self.__ressource_type = ressource_type

    def get_ressource_type(self) :
        return self.__ressource_type
