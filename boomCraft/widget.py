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

        pygame.draw.rect(window, (100, 100, 100), (x, y, w, h))
        pygame.draw.line(window, (150, 150, 150), (x, y+1), (x + w, y+1), 3)  # Bord Haut
        pygame.draw.line(window, (150, 150, 150), (x+1, y), (x+1, y + h), 3)  # Bord Gauche
        pygame.draw.line(window, (50, 50, 50), (x, y + h-1), (x + w, y + h-1), 3)  # Bord Bas
        pygame.draw.line(window, (50, 50, 50), (x + w-1, y + h), [x + w-1, y], 3)  # Bord Droit
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

    @staticmethod
    def menuStrip(windoww):

        return None
