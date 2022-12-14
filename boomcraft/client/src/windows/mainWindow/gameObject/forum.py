import pygame
from pygame.sprite import Sprite

FORUM_IMG = "../resources/mainWindows/struct/scifiStructure_07.png"


class Forum(Sprite):
    def __init__(self, id_forum, id_owner, x: int = 0, y: int = 0, width: int = 64, height: int = 64, life: int = 100):
        Sprite.__init__(self)
        self.id = id_forum
        self.id_owner = id_owner
        self.x : int = x
        self.y : int = y
        self.width = width
        self.height = height
        self.life = life
        self.hitbox_area_x = [0,0]
        self.hitbox_area_y = [0,0]

        self.image = pygame.image.load(FORUM_IMG).convert_alpha()
        self.rect = self.image.get_rect()
        self.absolute_rect = pygame.Rect(self.rect)
        self.rect.topleft = [self.x, self.y]
        self.absolute_rect.topleft = [self.x + 40, self.y + 45]
