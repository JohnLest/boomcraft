from typing import List
from app.game_entity.Entity import Entity
from app.game_entity.Ressource import Ressource, RessourceType
from app.game_structure.Coord import Coord

class Mobile(Ressource, Entity):
        ''' 
        Mobile class bringing 
        together all the entity 
        that can move and 
        that are considered as a ressource
        '''
        def __init__(self, ressource_Type : RessourceType, coords : list, width : int, height : int, life : int, look_in_game : str, ressource_dropped : RessourceType):
            """
            Construct a new 'Mobile' object.

            :param deplacement: The state of deplacement of the Mobile entity
            :param speed: The speed of the Mobile entity
        
            :return: returns nothing
            """
            super(Entity).__init__(coords, width, height, life, look_in_game, ressource_dropped)
            super(Ressource).__init__(ressource_Type)

            self.__deplacement : bool = False
            self.__speed : float = 1.00



        def move(coord : Coord) -> bool :
            ''' 
            Permits the mobile entity to move from one place to another
            '''
            return True
        
        def set_deplacement(self,deplacement):
            self.__deplacement=deplacement
        def get_deplacement(self):
            return self.__deplacement

        def set_speed(self,speed):
                self.__speed=speed
        def get_speed(self):
            return self.__speed