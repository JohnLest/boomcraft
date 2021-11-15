import pygame, random, sys


from app.game_entity.Ressource import RessourceType

class Entity :
    
    def __init__(self, active : bool, disappear : bool, coords : list, life : int, look_in_game : str, ressource_dropped : RessourceType):
        
        self.active = active

        self.disappear = disappear

        self.coords = coords

        self.life = life

        self.look_in_game = look_in_game

        self.ressource_dropped = ressource_dropped

        pygame.sprite.Sprite.__init__(self)




    """ 
     make entity appear inactive
    """
    def inactive_appeareance(self):
        print("active " + self.active)

    """
     define the path to follow to get the entity image
    """
    def define_look_in_game(self, path_to_entity_image):
        print("look_in_game " + self.look_in_game)


    """
     return the area of tile occupied by the entity
    """
    def give_area(self):
        area = self.coords[0] * self.coods[1]
        return area

    """
     return the width of the entity in a number of tile
    """
    def give_width(self):
        width = self.coords[0]
        return width

    """
     return the height of the entity in a number of tile
    """
    def give_height(self):
        height = self.coords[1]
        return height

    """
     give the amount of ressource in parameter to the ressource counter
    """
    def give_ressources(ressource, amount):
        dict_of_ressources[ressource] =+ amount  
        print(amount + " of " + ressource + " dropped")

    
    def set_active(self,active):
            self.active = active

    def get_active(self):
        return self.active



    def set_disappear(self,active):
        self.active = disappear

    def get_disappear(self):
        return self.disappear


        