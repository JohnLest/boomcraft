from app.game_entity.RessourceCounter import RessourceCounter


class PlayerInfo :

    def __init__(self, pseudo: str, own_ressources : RessourceCounter, game_ressources : RessourceCounter):
        
            self.__pseudo : str = pseudo

            self.__own_ressources : RessourceCounter= own_ressources

            self.__game_ressources : RessourceCounter = game_ressources
            #self.__achievements = "type par défaut"

    """ 
     get ressources amount from a ressource counter and add it to the own ressources variable
    """
    def update_own_ressources(self, ressourceCounter : RessourceCounter):
        print("before update_own_ressources " + self.__own_ressources)
        self.__own_ressources.add_ressource_amount(ressourceCounter)
        print("after update_own_ressources " + self.__own_ressources)

    """ 
     import amount of ressources from own ressources to game_ressources
    """
    def import_from_own_ressources(self):
        print("before import_from_own_ressources " + self.__own_ressources)

        self.__game_ressources.add_ressource_amount(self.__own_ressources)
        print("after import_from_own_ressources " + self.__own_ressources)




    def set_pseudo(self,pseudo : str):
        self.__pseudo = pseudo
    def get_pseudo(self) :
        return self.__pseudo

    def set_own_ressources(self,own_ressources : RessourceCounter):
        self.__own_ressources = own_ressources
    def get_own_ressources(self) :
        return self.__own_ressources
    
    def set_game_ressources(self,game_ressources : RessourceCounter):
        self.__game_ressources = game_ressources
    def get_game_ressources(self) :
        return self.__game_ressources

    #def set_achievements(self,achievements : str):
    #    self.__achievements = achievements
    #def get_achievements(self) :
    #    return self.__achievements
