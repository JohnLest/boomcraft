from typing import Dict, List
from app.game_entity.Ressource import RessourceType
class RessourceCounter :
    
    def __init__(self): 
     
        self.__dict_of_ressources : dict[RessourceType, int] = {
                                RessourceType.WORKER : 5,
                                RessourceType.GOLD : 1,
                                RessourceType.STONE : 500,
                                RessourceType.WOOD : 650,
                                RessourceType.IRON : 100,
                                RessourceType.FOOD : 1000
                            }

    """ 
     add a new type of ressources into dictOfRessources
    """
    def add_ressource_type_to_dict(self, ressourceType : RessourceType):
        self.__dict_of_ressources[ressourceType]=0
        
    """ 
     add an amount of ressources into dictOfRessources
    """
    def add_ressource_amount(self, listAmountOfEachRessources : dict[RessourceType, int]):
        
        for x in self.__dict_of_ressources:
            if(x in listAmountOfEachRessources) :
                print("self.__dict_of_ressources["+str(x)+"] -->" + str(self.__dict_of_ressources[x]))
                print("listAmountOfEachRessources["+str(x)+"] -->" + str(listAmountOfEachRessources[x]))

                self.__dict_of_ressources[x] += listAmountOfEachRessources[x]  
                
                print("Results -->" + self.__dict_of_ressources[x])

        self.get_dict_of_ressources()



    def set_dict_of_ressources(self,dict_of_ressources):
        self.__dict_of_ressources = dict_of_ressources

    def get_dict_of_ressources(self) :
        for x in self.__dict_of_ressources:
            print(x + "--> "+str(self.__dict_of_ressources[x]))
        return self.__dict_of_ressources

    
    def set_quantity(self, ressourceType : RessourceType, amount : int):
        """ 
        set the quantity of a ressource type in the dictionnary of ressources
        """
        self.__dict_of_ressources[ressourceType] = amount

    def get_quantity(self, ressourceType : RessourceType) :
        """ 
        get the quantity of a ressource type in the dictionnary of ressources
        """
        return self.__dict_of_ressources[ressourceType]
