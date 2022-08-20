import pygame
from pygame.sprite import Sprite

BOSS = "../resources/mainWindows/boss.png"

class Boss(pygame.sprite.Sprite):
    def __init__(self, id_boss, name, x: int = 0, y: int = 0, width: int = 64, height: int = 64, life: int = 1000):
        super().__init__()
        self.id = id_boss
        self.name = name
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.life = life
        self.hitbox_area_x = [0, 0]
        self.hitbox_area_y = [0, 0]
        self.name_items = None

        self.image = pygame.image.load(BOSS).convert_alpha()
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255, 0, 0), self.rect, 2)

    def update(self):
        self.rect.topleft = [self.x, self.y]