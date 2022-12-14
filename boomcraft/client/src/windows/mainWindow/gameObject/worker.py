import pygame
import threading
import time

CHARACTER_UP = "../resources/mainWindows/up/0.png"
CHARACTER_DOWN = "../resources/mainWindows/down/0.png"
CHARACTER_LEFT = "../resources/mainWindows/left/0.png"
CHARACTER_RIGHT = "../resources/mainWindows/right/0.png"

class Worker(pygame.sprite.Sprite):
    def __init__(self, id_worker, id_owner, x: int = 0, y: int = 0, width: int = 16, height: int = 32, life: int = 100):
        super().__init__()
        self.coord: list = [x, y]
        self.id = id_worker
        self.id_owner: int = id_owner
        self.life = life
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height
        self.destination: list[int] = []
        self.road_to_destination = [[]]
        self.current_step: list[int] = []

        self.img_up = pygame.image.load(CHARACTER_UP).convert_alpha()
        self.img_down = pygame.image.load(CHARACTER_DOWN).convert_alpha()
        self.img_left = pygame.image.load(CHARACTER_LEFT).convert_alpha()
        self.img_right = pygame.image.load(CHARACTER_RIGHT).convert_alpha()

        self.image = self.img_down  # pygame.Surface((16, 32))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255, 0, 0), self.rect, 2)
        self.absolute_rect = pygame.Rect(self.rect)

        # self.image.blit(self.img_down, (0, 0), (self.x, self.y, self.width, self.height))
        # self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = [self.x, self.y]
        self.absolute_rect.topleft = [self.x + 40, self.y + 45]
