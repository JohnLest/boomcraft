from enum import Enum
from interface import implements

from app.game_entity.Entity import Entity
from app.game_entity.Ressource import Ressource
from app.game_entity.Ressource import RessourceType
from app.game_entity.TrainerInterface import TrainerInterface
from app.game_entity.Character import Worker

class BuildingType(Enum):
    FARM = 1
    PIT = 2
    MINE = 3
    FORUM = 4
    BARRACK = 5
    WALL = 6

class Building(Entity):
    
    def __init__(self, building_type : BuildingType, active : bool, disappear : bool, coords : list, life : int, look_in_game : str, ressource_dropped : RessourceType):
        super().__init__(active, disappear, coords, life, look_in_game, ressource_dropped)
        self.building_type = building_type
        self.ressource_created = "need to call a method that return the ressourceType linked to the building type"

    """ 
     make entity appear inactive
    """
    def call_ressource_to_create_in_the_building(self, ressourceType : RessourceType):
        print("active " + self.active)
        return Ressource(self.ressource_created)


    def set_building_type(self,building_type):
            self.building_type = building_type

    def get_building_type(self):
        return self.building_type

    def set_ressource_created(self,ressource_created):
            self.ressource_created = ressource_created

    def get_ressource_created(self):
        return self.ressource_created




class Forum(Building, implements(TrainerInterface)):
    
    def __init__(self, building_type : BuildingType, active : bool, disappear : bool, coords : list, life : int, look_in_game : str, ressource_dropped : RessourceType):
        super().__init__(building_type, active, disappear, coords, life, look_in_game, ressource_dropped)

    def train(self, character_type) :

        if character_type == WORKER:
            return Worker()

        elif character_type == WARRIOR:
            return Warrior()

        elif character_type == ARCHER:
            return Archer()

        elif character_type == HERO:
            return Hero()

        
        

    
    def appear_next_to(self):
        pass


 