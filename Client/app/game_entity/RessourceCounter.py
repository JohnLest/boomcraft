class RessourceCounter :
    
    def __init__(self):
        
            self.__dict_of_ressources = "Dictionnary<RessourceType,Integer>"

    """ 
     add a new type of ressources into dictOfRessources
    """
    def add_ressource_type_to_dict(self, ressourceType):
        print("dictOfRessources " + self.__dict_of_ressources)
    """ 
     add an amount of ressources into dictOfRessources
    """
    def add_ressource_amount(self, listAmountOfEachRessources):
        print("dictOfRessources " + self.__dict_of_ressources)


    def set_dict_of_ressources(self,dict_of_ressources):
        self.__dict_of_ressources = dict_of_ressources

    def get_dict_of_ressources(self) :
        return self.__dict_of_ressources

    
    def set_quantity(self,dict_of_ressources):
        """ 
        to be made
        """
        self.__dict_of_ressources = dict_of_ressources

    def get_quantity(self) :
        """ 
        to be made
        """
        return self.__dict_of_ressources
