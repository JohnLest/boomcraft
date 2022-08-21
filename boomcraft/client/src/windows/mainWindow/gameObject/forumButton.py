import pygame
import uuid

CHARACTER_DOWN = "../resources/mainWindows/down/0.png"


class ForumButton(pygame.sprite.Sprite):
    def __init__(self, x, y, width=64, height=64):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.image.load(CHARACTER_DOWN).convert_alpha()
        self.rect = self.image.get_rect()
        self.absolute_rect = pygame.Rect(self.rect)

    def update(self) -> None:
        self.rect.midleft = [self.x, self.y]
        self.absolute_rect.midleft = [self.x + 40, self.y + 765]

