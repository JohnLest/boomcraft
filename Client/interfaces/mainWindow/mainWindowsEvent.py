import pygame
""" from widget import MenuStrip
from mainWindow import MainWindow """

from interfaces.mainWindow.widget import MenuStrip
from interfaces.mainWindow.mainWindow import MainWindow


class MainWindowEvent:
    def __init__(self, main_win: MainWindow):
        self.main_win = main_win
        self.__event()

    def __event(self):
        btn = self.main_win.btnAPI
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn.btn_rect.collidepoint(pygame.mouse.get_pos()):
                        self.main_win.menu_sprite.enlarge()
                        self.main_win.menu_sprite.menu_strip_item.draw(self.main_win.window)
                        self.__menu_strip_on_click()
            pygame.display.update()
        return

    def __menu_strip_on_click(self):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_win.menu_sprite.menu_strip_item_dict.get("twitch").rect.collidepoint(pygame.mouse.get_pos()):
                        print("Un")
                    elif self.main_win.menu_sprite.menu_strip_item_dict.get("fcb").rect.collidepoint(pygame.mouse.get_pos()):
                        print("Deux")
                    elif self.main_win.menu_sprite.menu_strip_item_dict.get("discord").rect.collidepoint(pygame.mouse.get_pos()):
                        print("Long")
                    else:
                        self.main_win.menu_sprite.tighten()
                        self.main_win.gbGame.show_groupbox(self.main_win.window)
                        return
