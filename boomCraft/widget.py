import pygame
from pygame.locals import *


class Widget:
    @staticmethod
    def button(window, text, position=(0, 0), rect: pygame.Rect = None):
        font = pygame.font.SysFont("Arial", 25)
        text_render = font.render(text, 1, (0, 0, 0))
        rectText = text_render.get_rect()
        if (rect is not None):
            x, y, w, h = btn = rect
            rectText.center = rect.center
        else:
            x, y, w, h = btn = rectText
            rectText.x, rectText.y = x, y = position

        pygame.draw.line(window, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(window, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(window, (100, 100, 100), (x, y, w, h))
        window.blit(text_render, (rectText.x, rectText.y))
        return btn

    @staticmethod
    def groupbox(window, position, size):
        x, y = position
        w, h = size
        gb = Rect(x, y, w, h)
        pygame.draw.rect(window, (250, 250, 250), gb, 1)
        pygame.display.flip()
        return gb
