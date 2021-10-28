import pygame
from pygame.locals import *


class Button(pygame.Rect):
    def __init__(self, window, text, position=(0, 0), rect: pygame.Rect = None):
        self.window = window
        font = pygame.font.SysFont("Arial", 18)
        self.text_render = font.render(text, 1, (0, 0, 0))
        self.rect_text = self.text_render.get_rect()
        if rect is not None:
            self.btn_rect = rect
            self.rect_text.center = rect.center
        else:
            self.btn_rect = self.rect_text
            self.rect_text.x, self.rect_text.y = self.btn_rect.x, self.btn_rect.y = position
        self.__draw_button()

    def __draw_button(self):
        pygame.draw.rect(self.window,
                         (100, 100, 100),
                         (self.btn_rect.x, self.btn_rect.y, self.btn_rect.w, self.btn_rect.h))
        pygame.draw.line(self.window,
                         (150, 150, 150),
                         (self.btn_rect.x, self.btn_rect.y+1),
                         (self.btn_rect.x + self.btn_rect.w, self.btn_rect.y+1),
                         3)  # Bord Haut
        pygame.draw.line(self.window,
                         (150, 150, 150),
                         (self.btn_rect.x+1, self.btn_rect.y),
                         (self.btn_rect.x+1, self.btn_rect.y + self.btn_rect.h),
                         3)  # Bord Gauche
        pygame.draw.line(self.window,
                         (50, 50, 50),
                         (self.btn_rect.x, self.btn_rect.y + self.btn_rect.h-1),
                         (self.btn_rect.x + self.btn_rect.w, self.btn_rect.y + self.btn_rect.h-1),
                         3)  # Bord Bas
        pygame.draw.line(self.window,
                         (50, 50, 50),
                         (self.btn_rect.x + self.btn_rect.w-1, self.btn_rect.y + self.btn_rect.h),
                         (self.btn_rect.x + self.btn_rect.w-1, self.btn_rect.y),
                         3)  # Bord Droit
        self.window.blit(self.text_render, (self.rect_text.x, self.rect_text.y))


class MenuStrip(pygame.sprite.Sprite):
    def __init__(self, window, btn_attach:Rect, lst_choice:dict):
        super().__init__()
        self.menu_strip_item = dict()
        self.max_width = 120
        self.coord = btn_attach.bottomleft
        h = 30

        #$surf = pygame.Surface((255, 255))
        #surf.fill(168, 255, 100)
        self.image = pygame.Surface((25, 75))

        pygame.draw.rect(self.image, (0, 255, 0), pygame.Rect(0, 0, 25, 75))
        self.rect = self.image.get_rect()

        #self.rect = self.s.get_rect()

    def test(self):
        self.image = pygame.transform.rotate(self.image, 90)


class GroupBox(pygame.Surface):
    def __init__(self, position, size, color):
        self.coord = position
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.data_rect = self.surface.get_rect()
        self.data_rect.topleft = self.coord

    def show_groupbox(self, window):
        window.blit(self.surface, self.coord)

class Widget:
    @staticmethod
    def menu_strip(window, btn_attach:Rect, lst_choice:dict):
        menu_strip_item = dict()
        max_width = 120
        x, y = btn_attach.bottomleft
        h = 30
        for choice in lst_choice.values():
            font = pygame.font.SysFont("Arial", 18)
            text_render = font.render(choice, 1, (0, 0, 0))
            if text_render.get_rect().w > max_width:
                max_width = text_render.get_rect().w
        boucle = 0
        for clef, choice in lst_choice.items():
            font = pygame.font.SysFont("Arial", 18)
            text_render = font.render(choice, 1, (0, 255, 0))
            rect_text = text_render.get_rect()
            case = Rect(x, y + (h*boucle), max_width, h)
            pygame.draw.rect(window, (100, 100, 100), case)
            rect_text.midleft = case.midleft
            window.blit(text_render, (rect_text.x, rect_text.y))
            menu_strip_item[clef] = case
            boucle += 1
        return menu_strip_item
