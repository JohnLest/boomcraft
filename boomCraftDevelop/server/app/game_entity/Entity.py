from typing import List, Set
import pygame, random, sys
import pytmx

from pygame.sprite import Group, Sprite
from pygame import Rect, Surface


from boomCraftDevelop.server.app.Tools import Tools
from boomCraftDevelop.server.app.game_structure.PygameClasses import SpriteSheet
from boomCraftDevelop.server.app.game_structure.Coord import Coord

class Entity (Sprite) :
    
    def __init__(self, coords : Set[Coord], width : int, height : int, life : int, look_in_game : str, ressource_dropped ):
        Sprite.__init__(self)
        from boomCraftDevelop.server.app.game_entity.Ressource import RessourceOffer, RessourceType
        from boomCraftDevelop.server.app.game_entity.Character import Worker
        from boomCraftDevelop.server.app.game_entity.Building import Building

        """
        Construct a new 'Entity' object.

        :param active: The state of activity of the entity
        :param disappear: The state of disappearness of the entity
        :param coords : The coordinates on which is the entity
        :param width : The width of the entity (equivalent to the number of (16x16) tiles in width)
        :param height : The height of the entity (equivalent to the number of (16x16) tiles in height)
        :param life : The life level of the entity (0 - 100)
        :param target : The target which the entity has to attack
        :param accessible : Coords included in the area attackable
        :param range : The range of the attack
        :param look_in_game : The path to the look of the entity in the game
        :param ressource_dropped : The ressource that the entity drops when destroyed


        :return: returns nothing
        """


        self.__active = True
        ''' 
        The state of activity of the entity
        '''
        self.__disappear = False
        ''' 
        The state of disappearness of the entity
        '''
        self.__coords = coords
        '''
        The coordinates on which is the entity
        '''
        self.__width = width
        '''
        The width of the entity (equivalent to the number of (16x16) tiles in width)
        '''
        self.__height = height
        ''' 
        The height of the entity (equivalent to the number of (16x16) tiles in height)
        '''
        self.__life = life
        '''
        The life level of the entity (0 - 100)
        '''
        self.__target = None
        ''' 
        The target which the entity has to attack
        '''
        self.__accessible : Set[Coord] = None
        '''
        Coords included in the area attackable
        '''
        self.__range : int = 1
        ''' 
        The range of the attack
        '''
        self.__look_in_game = look_in_game
        '''
        The path to the look of the entity in the game
        '''
        self.__ressource_dropped : RessourceType = ressource_dropped
        '''
        The ressource that the entity drops when destroyed
        '''

        self.sprites = SpriteSheet(self.__look_in_game)
        '''
        SpriteSheet containing sprites representing the entity
        '''
    

    def reduce_life(self, attack : int):
        """ 
        reduce life following entering attack
        """
        life_difference : int = self.get_life() - attack

        if life_difference <= 0 :
            self.set_active(False)           
            
        self.set_life(life_difference)




    def inactive_appeareance(self):
        """ 
        make entity appear inactive
        """
        print("active ", self.__disappear)
        self.__disappear=True

    
    def define_look_in_game(self, path_to_entity_image):
        """
        define the path to follow to get the entity image
        """
        print("look_in_game ", self.__look_in_game)


    
    def give_area(self):
        """
        return the area of tile occupied by the entity
        """
        area = self.__width * self.__height
        return area

    
    def give_ressources(self):
        """
        give an amount of ressources
        :return a ressource offer object
        """
        print(type(object))
        if(isinstance(self, Worker)) :
            return RessourceOffer(RessourceType.WOOD, Tools.give_random_int_between(1,10))

        elif(isinstance(self, Building)) :
            return RessourceOffer(RessourceType.STONE, Tools.give_random_int_between(10,50))


         

    ################################################################
    #  Getters and Setters
    ################################################################

    def set_active(self,active):
            self.__active = active

    def get_active(self):
        return self.__active



    def set_disappear(self,disappear):
        self.__disappear = disappear

    def get_disappear(self):
        return self.__disappear


    def set_coords(self,coords):
        self.__coords = coords

    def get_coords(self):
        return self.__coords

    def set_width(self,width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self,height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_life(self,life):
                self.__life = life

    def get_life(self):
        return self.__life


    def set_look_in_game(self,look_in_game):
                self.__look_in_game = look_in_game

    def get_look_in_game(self):
        return self.__look_in_game


    def set_ressource_dropped(self,ressource_dropped):
                self.__ressource_dropped = ressource_dropped

    def get_ressource_dropped(self):
        return self.__ressource_dropped



