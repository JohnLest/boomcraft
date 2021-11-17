from enum import Enum
from interface import implements
from app.Tools import Tools

from app.game_entity.Entity import Entity
from app.game_entity.Ressource import Ressource
from app.game_entity.Ressource import RessourceType
from app.game_entity.TrainerInterface import TrainerInterface
from app.game_entity.Character import Worker
from app.game_entity.Character import CharacterType
from app.game_structure.Coord import Coord

class BuildingType(Enum):
    FARM = 1
    PIT = 2
    MINE = 3
    FORUM = 4
    BARRACK = 5
    WALL = 6

class Building(Entity):
    
    def __init__(self, building_type : BuildingType, active : bool, disappear : bool, coords : list[Coord], life : int, look_in_game : str, ressource_dropped : RessourceType, ressource_to_create : list[RessourceType]):
        
        """
        Construct a new 'Building' object.

        :param building_type: The type of the building
        :param ressource_created: The ressource that is created by the building

        :return: returns nothing
        """
        super().__init__(active, disappear, coords, life, look_in_game, ressource_dropped)
        self.__building_type = building_type
        ''' 
        The type of the building
        '''
        self.__ressource_to_create = ressource_to_create
        ''' 
        The ressource that the building is able to create
        '''

    def set_building_type(self,building_type):
            self.__building_type = building_type

    def get_building_type(self):
        return self.__building_type

    def set_ressource_to_create(self,ressource_to_create):
            self.__ressource_to_create = ressource_to_create

    def get_ressource_to_create(self):
        return self.__ressource_to_create




class Forum(Building, implements(TrainerInterface)):
    
    path_to_img = "ressources/forum_img.png"
    ''' 
    Path to the image of the forum
    '''
    def __init__(self, coords : list[Coord]):
        super().__init__(BuildingType.FORUM, True, False, coords, Tools.give_random_int_between(200,500), Forum.path_to_img, RessourceType.WOOD, [CharacterType.WORKER,CharacterType.HERO])

    def train(self, character_type) :

        if character_type == CharacterType.WORKER:
            self.appear_next_to(CharacterType.WORKER)

        elif character_type == CharacterType.WARRIOR:
            return Warrior()

        elif character_type == CharacterType.ARCHER:
            return Archer()

        elif character_type == CharacterType.HERO:
            return Hero()


    def appear_next_to(self,character_type : CharacterType):
        self.__coords


 