from typing import Dict,List
from app.Settings import MAX_HEIGTH_SIZE, MAX_WIDTH_SIZE


class PlayArea :
    
    def __init__(self, width: int, height: int):
        

        self.__play_area : List[List[Dict[int, str]*MAX_WIDTH_SIZE]*MAX_HEIGTH_SIZE] = None
        """ 
        Play area containing each pixel (per default 540 x 840)
        Each element has a Dict with the key(int) of the team (0 or 1 when 2 teams) 
        and the value is the id of the entities
        """


        self.chunksize=16


    def get_chunks_from_cord(self, x, y):
        """
        Returns the chunk or chunks for the given location on the map, based on the tilesize of the map.
        Being in between chunks leads to multiple chunks being returned.

        (float or int) -> [tuple(int, int)]
        (20, 58)    ->  [[16, 68]]
        """

        """
        Adds the cords separate rounded to 16 to tilesize coordinates to the blocked list.
        """

        decimal_16 = [x % self.chunksize, y % self.chunksize]
        blocked = [[], []]  # [[x values], [y values]]
        for cnt, cord in enumerate((x, y)):
            if decimal_16[cnt] >= self.chunksize_05:
                blocked[cnt].append(cord + self.chunksize - decimal_16[cnt])
            else:
                blocked[cnt].append(cord - decimal_16[cnt])


        result = []
        for array in blocked[0]:
            for var in blocked[1]:
                result.append((round(array), round(var)))

        return result



    def initialize_playarea(self):    
        """ 
        Initialises a new PlayArea
        """

            
    def initialize_playarea(self): 
        """ 
        
        """




    def to_string() :
    
        result : str = "";

        #for lines in range(board) :    
            
        #    lines

    def set__id(self, id : str):
        self.__id = id

    def get__id(self) :
        return self.__id

