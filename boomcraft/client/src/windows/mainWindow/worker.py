import pygame

CHARACTER_UP = "../resources/mainWindows/up/0.png"
CHARACTER_DOWN = "../resources/mainWindows/down/0.png"
CHARACTER_LEFT = "../resources/mainWindows/left/0.png"
CHARACTER_RIGHT = "../resources/mainWindows/right/0.png"

class Worker(pygame.sprite.Sprite):
    def __init__(self, x: int = 0, y: int = 0, width: int = 16, height: int = 32):
        super().__init__()
        self.coord: list = [x, y]
        self.width = width
        self.height = height

        self.img_up = pygame.image.load(CHARACTER_UP).convert_alpha()
        self.img_down = pygame.image.load(CHARACTER_DOWN).convert_alpha()
        self.img_left = pygame.image.load(CHARACTER_LEFT).convert_alpha()
        self.img_right = pygame.image.load(CHARACTER_RIGHT).convert_alpha()

        self.image = self.img_down  # pygame.Surface((16, 32))
        self.rect = self.image.get_rect()
        # self.image.blit(self.img_down, (0, 0), (self.x, self.y, self.width, self.height))
        # self.rect = self.image.get_rect()

    def move_right(self):
        self.coord[0] += 3

    def update(self):
        self.rect.topleft = self.coord

