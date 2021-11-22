import pygame


class Window:
    def __init__(self, size, title):
        self.window = pygame.display.set_mode(size)
        self.surface = pygame.display.get_surface()
        pygame.display.set_caption(title)
        self.winX, self.winY = self.window.get_size()
        self.winXPercent = self.winX / 100
        self.winYPercent = self.winY / 100
        return self
