from pygame.sprite import Sprite
import sys, pygame


CHARACTER_UP = './split/up/0.png'
CHARACTER_DOWN = './split/down/0.png'
CHARACTER_LEFT = './split/left/0.png'
CHARACTER_RIGHT = './split/right/0.png'

class WORKER(Sprite):
    

    def __init__(self, id : int, x : int , y : int, width : int = 16, height : int = 32) :
        Sprite.__init__(self)
        self.id = id
        self.x : int = 0
        self.y : int = 0
        self.width = 16
        self.height = 32

        self.img_up = pygame.image.load(CHARACTER_UP).convert_alpha()
        self.img_down = pygame.image.load(CHARACTER_DOWN).convert_alpha()
        self.img_left = pygame.image.load(CHARACTER_LEFT).convert_alpha()
        self.img_right = pygame.image.load(CHARACTER_RIGHT).convert_alpha()
        
        self.img = self.img_up
        self.destination : list[int] = []
        self.current_step : list[int]= []

        """ 
        The destination to arrive to

        self.x = 9
        self.y = 25

        example --> [15,25]
        or
        example --> [13,22]

        """
        self.road_to_destination = [[]]
        """ 
        The points on which mobile has to pass to arrive to the destination
        self.x = 9
        self.y = 25
        example --> [[10,25], [11,25], [12,25], [13,25], [14,25], [15,25]]
        or              X,Y
        example --> [[1,-1],[1,-1],[1,-1],[1,0]]

        """
        self.DEPLACEMENT = 1
