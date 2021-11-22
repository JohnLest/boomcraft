from app.game_structure.Direction import Direction

class Direction :
    
    UP : Direction =  Direction(-1, 0);
    DOWN : Direction =  Direction (1, 0);
    LEFT : Direction =  Direction (0, -1);
    RIGHT : Direction =  Direction (0, 1);

    def __init__(self,l : int, c : int):
        super().__init__(l,c)