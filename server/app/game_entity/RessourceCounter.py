from typing import Dict

from app.game_entity.Ressource import RessourceType


class RessourceCounter :
    
    def __init__(self, dict_of_ressources : Dict[RessourceType,int]):
        
            self.__dict_of_ressources : Dict[RessourceType,int] = dict_of_ressources



    ################################################################
    #  Methods
    ################################################################

    def add_ressource_type_to_dict(self, ressourceType):
        """ 
        add a new type of ressources into dictOfRessources
        """
        print("before add " + self.__dict_of_ressources)
        self.__dict_of_ressources[ressourceType] = 0
        print("after add " + self.__dict_of_ressources)

    
    def add_ressource_amount(self, listAmountOfEachRessources):
        """ 
        add an amount of ressources into dictOfRessources
        """
        print("before add an amount" + self.__dict_of_ressources)

        for item in self.__dict_of_ressources: 
            self.__dict_of_ressources[item] += listAmountOfEachRessources[item]

        print("after add an amount" + self.__dict_of_ressources)



    ################################################################
    #  Getters and Setters
    ################################################################

    def set_dict_of_ressources(self,dict_of_ressources):
        self.__dict_of_ressources = dict_of_ressources

    def get_dict_of_ressources(self) :
        return self.__dict_of_ressources

    
    def set_quantity(self, amount : int, ressource_type: RessourceType):
        """ 
        set the quantity of a ressource
        """
        self.__dict_of_ressources[ressource_type] = amount

    def get_quantity(self, ressource_type: RessourceType) :
        """ 
        get the quantity of a ressource in the dict of ressources
        """
        return self.__dict_of_ressources[ressource_type]
