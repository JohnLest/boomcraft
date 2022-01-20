from typing import List, Set
from app.game_entity.Entity import Entity
from app.game_entity.Ressource import Ressource, RessourceType
from app.game_structure.Coord import Coord
from app.game_entity.LinkedList import LinkedList


class Mobile(Ressource, Entity):
        ''' 
        Mobile class bringing 
        together all the entity 
        that can move and 
        that are considered as a ressource
        '''
        def __init__(self, ressource_Type : RessourceType, coords : Set[Coord], width : int, height : int, life : int, look_in_game : str, ressource_dropped : RessourceType):
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
            self.__destination : Coord = None
            self.__path_to_follow : LinkedList[Coord] = None



        def move(coord : Coord) : 
            """
            Permits the mobile entity to move from one place to another
            :return a boolean 
            """
            return True
        
    ################################################################
    #  Getters and Setters
    ################################################################


        def set_deplacement(self,deplacement):
            self.__deplacement=deplacement
        def get_deplacement(self):
            return self.__deplacement

        def set_speed(self,speed):
                self.__speed=speed
        def get_speed(self):
            return self.__speed

        def set_destination(self,destination : Coord):
                self.__destination=destination
        def get_destination(self):
            return self.__destination
        
        def set_path_to_follow(self,path_to_follow : LinkedList[Coord]):
            self.__path_to_follow=path_to_follow
        def get_path_to_follow(self):
            return self.__path_to_follow


