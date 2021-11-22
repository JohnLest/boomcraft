from app.game_structure.Coord import Coord

class Direction(Coord) :
    
    UP : Coord =  Coord(-1, 0);
    DOWN : Coord =  Coord (1, 0);
    LEFT : Coord =  Coord (0, -1);
    RIGHT : Coord =  Coord (0, 1);

    def __init__(self,l : int, c : int):
        super().__init__(l,c)