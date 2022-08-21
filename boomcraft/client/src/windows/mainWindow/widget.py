import pygame
from pygame.locals import *


class Button:
    def __init__(self, window, text, position=(0, 0), rect: pygame.Rect = None):
        self.window = window
        font = pygame.font.init()
        font = pygame.font.SysFont("Arial", 18)
        self.text_render = font.render(text, True, (0, 0, 0))
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


class MenuStripItem(pygame.sprite.Sprite):
    def __init__(self, size, text):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (100, 100, 100), self.rect)

        font = pygame.font.SysFont("Arial", 18)
        text_render = font.render(text, True, (0, 255, 0))
        rect_text = text_render.get_rect()
        rect_text.midleft = self.rect.midleft
        self.image.blit(text_render, (rect_text.x, rect_text.y))


class MenuStrip:
    def __init__(self, btn_attach: Rect, lst_choice: dict):
        self.max_width = self.__set_max_width(lst_choice)
        self.coord = btn_attach.bottomleft
        self.menu_strip_item = self.__draw_menu_strip_items(lst_choice, self.max_width, self.coord)
        self.tighten()

    def __set_max_width(self, lst_choice):
        max_width = 120
        for choice in lst_choice.values():
            font = pygame.font.SysFont("Arial", 18)
            text_render = font.render(choice, True, (0, 0, 0))
            if text_render.get_rect().w > max_width:
                max_width = text_render.get_rect().w
        return max_width

    def __draw_menu_strip_items(self, lst_choice, max_width, coord):
        self.menu_strip_item_dict = dict()
        menu_strip_item_group = pygame.sprite.Group()
        h = 30
        boucle = 0
        for clef, choice in lst_choice.items():
            menu_strip_item = MenuStripItem((max_width, h), choice)
            menu_strip_item.rect.topleft = (coord[0], coord[1] + (h*boucle))
            self.menu_strip_item_dict[clef] = menu_strip_item
            menu_strip_item_group.add(menu_strip_item)
            boucle += 1
        return menu_strip_item_group

    def tighten(self):
        for sprite in self.menu_strip_item.sprites():
            sprite.rect.update(0, 0, 0, 0)
        self.menu_strip_item = pygame.sprite.RenderUpdates(self.menu_strip_item)
        return

    def enlarge(self):
        boucle = 0
        for sprite in self.menu_strip_item.sprites():
            sprite.rect.update(self.coord[0], self.coord[1] + (30*boucle), self.max_width, 30)
            boucle += 1
        self.menu_strip_item = pygame.sprite.RenderUpdates(self.menu_strip_item)
        return


class GroupBox:
    def __init__(self, position, size, color):
        self.coord = position
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.data_rect = self.surface.get_rect()
        self.data_rect.topleft = self.coord

    def show_groupbox(self, window):
        window.blit(self.surface, self.data_rect.topleft)


class ImageAndText:
    def __init__(self, image, text, position_topleft:tuple = None, position_midleft:tuple = None):
        self.image = pygame.image.load(image)
        self.image_rect = self.image.get_rect()
        self.data_rect = self.image_rect.copy()
        if position_midleft is not None:
            self.data_rect.midleft = position_midleft
        elif position_topleft is not None:
            self.data_rect.topleft = position_topleft
        else :
            self.data_rect.topleft = (0, 0)
        self.image_rect.midleft = self.data_rect.midleft

        font = pygame.font.SysFont("Arial", 18)
        self.text_render = font.render(text, True, (255, 255, 255))
        self.rect_text = self.text_render.get_rect()
        self.data_rect.width = self.data_rect.width + self.rect_text.width

        self.rect_text.midleft = self.image_rect.midright
        self.rect_text.x = self.rect_text.x + 5

    def update_text(self, text):
        font = pygame.font.SysFont("Arial", 18)
        self.text_render = font.render(text, True, (255, 255, 255))

    def show_image_and_text(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.data_rect, 1)
        surface.blit(self.image, self.data_rect)
        surface.blit(self.text_render, (self.rect_text.x, self.rect_text.y))
        pygame.display.update()
