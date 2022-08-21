import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, id, x, y):
        super().__init__()
        self.id_to_target: str = id
        self.x: int = x
        self.y: int = y
        self.width = 16
        self.height = 13

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))

        pygame.draw.rect(self.image, (0, 0, 0), pygame.Rect(0, 0, self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.bottomleft = [self.x, self.y]