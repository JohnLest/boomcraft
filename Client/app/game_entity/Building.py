from enum import Enum

class BuildingType(Enum):
    FARM = 1
    PIT = 2
    MINE = 3
    FORUM = 4
    BARRACK = 5
    WALL = 6

class Building :
    
    def __init__(self):
        
            self.building_type = "BuildingType"
            self.ressource_created = "RessourceType"

    def set_building_type(self,building_type):
            self.building_type = building_type

    def get_building_type(self):
        return self.building_type

    def set_ressource_created(self,ressource_created):
            self.ressource_created = ressource_created

    def get_ressource_created(self):
        return self.ressource_created




