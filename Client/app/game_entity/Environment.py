from enum import Enum


class EnvironmentType(Enum):
    TREE = 1
    ROCK = 2
    WATER = 3
    CREVASSE = 4
    RUIN = 5

class Environment :
    
    def __init__(self, env_type : EnvironmentType):
        
            self.__env_type = env_type



    def followSeason(self):
        """ 
        follow the season by putting a filter on the picture of the entity
        """
        print("active " + self.active)

    def set_env_type(self,env_type : EnvironmentType):
        self.__env_type = env_type

    def get_env_type(self) :
        return self.__env_type

class Tree(Environment) :

    def __init__(self):
        super().__init__(EnvironmentType.TREE)

class Rock(Environment) :
    
    def __init__(self):
        super().__init__(EnvironmentType.ROCK)

class Water(Environment) :
    
    def __init__(self):
        super().__init__(EnvironmentType.WATER)