from app.game_structure.Coord import Coord

class Coord :
    ''' 
    Represents a coordinate in a table using line and col numbers
    '''
    def __init__(self, line : int, col : int):
        self.__line = line
        self.__col = col
    
    def equals(self,c : Coord):

        return (self.__line == c.get_line() & self.__col == c.get_col())

    def set_line(self,line):
        self.__line = line

    def get_line(self):
        return self.__line

    def set_col(self,col):
        self.__col = col

    def get_col(self):
        return self.__col