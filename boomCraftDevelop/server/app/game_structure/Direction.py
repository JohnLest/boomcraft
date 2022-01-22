class Direction :
    
    UP = (-1, 0);
    DOWN = (1, 0);
    LEFT = (0, -1);
    RIGHT = (0, 1);

    def __init__(self,l : int, c : int):
        super().__init__(l,c)