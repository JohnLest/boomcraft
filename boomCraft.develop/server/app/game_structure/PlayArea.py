class PlayArea :
    
    def __init__(self):
        
        self.__play_area = [
            [ #line 0
                [0,0], #col 0
                [5,9], #col 1
                [0,1], #col 2
                [0,1]  #col 3
            ],
            [ #line 1
                [0,0], #col 0
                [0,1], #col 1
                [0,1], #col 2
                [0,1]  #col 3
            ]
        ]
        
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




        
