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
    ''' 
    Represents a ressource in the game
    '''
    def __init__(self, ressource_type : RessourceType):
        
        self.__ressource_type = ressource_type


    def set_ressource_type(self,ressource_type : RessourceType):
        self.__ressource_type = ressource_type

    def get_ressource_type(self) :
        return self.__ressource_type




class RessourceOffer :
    ''' 
    Represents a ressource offer in the game
    '''
    def __init__(self, ressource_type : RessourceType, quantity : int):
        
        self.__ressource_type = ressource_type
        self.__quantity= quantity


    def set_ressource_type(self,ressource_type : RessourceType):
        self.__ressource_type = ressource_type

    def get_ressource_type(self) :
        return self.__ressource_type

    def set_quantity(self,quantity : int):
        self.__quantity = quantity

    def get_quantity(self) :
        return self.__quantity
