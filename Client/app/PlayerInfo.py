class PlayerInfo :

    def __init__(self):
        
            self.pseudo = "default"

            self.own_ressources = "type par défaut"

            self.game_ressources = "type par défaut"

            self.achievements = "type par défaut"

    """ 
     get ressources amount from a ressource counter and add it to the own ressources variable
    """
    def update_own_ressources(self, ressourceCounter):
        print("update_own_ressources " + self.own_ressources)
    """ 
     import amount of ressources from own ressources to game_ressources
    """
    def import_from_own_ressources(self, listAmountOfEachRessources):
        print("import_from_own_ressources " + self.own_ressources)