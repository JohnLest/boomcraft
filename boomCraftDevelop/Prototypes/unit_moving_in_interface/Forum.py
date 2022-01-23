from enum import Enum
import pygame
from pygame.sprite import Sprite



FORUM_IMG = "scifiStructure_07.png"


class Forum(Sprite):
    
    ''' 
    Path to the image of the forum
    '''
    def __init__(self, id : int = 0, x : int =0 , y : int =0, width : int = 64, height : int = 64, life : int = 100) :
        Sprite.__init__(self)
        from GameEngine import GameEngine

        self.id = id
        self.x : int = x
        self.y : int = y
        self.width = 64
        self.height = 64

        #self.hitbox_area = [[0,0]] * 2
        self.hitbox_area_x = [0,0]
        self.hitbox_area_y = [0,0]

        ''' 
        contains :
        min x [0][0] and max x [0][1]
        min y [1][0] and max y [1][1]
        '''
        self.life = life

        self.img = pygame.image.load(FORUM_IMG).convert_alpha()





 