import pygame


class Name(pygame.sprite.Sprite):
    def __init__(self, name, x, y, width=64, height=16):
        super().__init__()
        self.name = name
        self.x: int = x
        self.y: int = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((64, 16)).convert_alpha()
        self.image.fill([0, 0, 0, 0])
        self.rect = self.image.get_rect()
        self.text_type = pygame.font.SysFont("Arial", 14).render(self.name, True, (255, 0, 0))
        self.image.blit(self.text_type, self.text_type.get_rect(center=self.image.get_rect().center))


    def update(self) -> None:
        self.rect.bottomleft = [self.x, self.y]
        self.image.blit(self.text_type, self.text_type.get_rect(center=self.image.get_rect().center))

