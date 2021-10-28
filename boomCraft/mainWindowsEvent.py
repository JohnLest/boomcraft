import pygame
from widget import MenuStrip
from mainWindow import MainWindow


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
                        menu_stripe_dico = {"twitch": "Twitch", "fcb": "Facebook", "discord": "Discord"}
                        print(menu_stripe_dico)
                        menu_sprite = MenuStrip(self.main_win.btnAPI.btn_rect, menu_stripe_dico)
                        menu_sprite.menu_strip_item.draw(self.main_win.window)

                        """
                        self.__menu_strip_on_click(
                            MenuStrip(self.main_win.btnAPI.btn_rect, menu_strip)
                        )
                        """
            pygame.display.update()
        return

    def __menu_strip_on_click(self, menu_strip):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_strip.get("twitch").collidepoint(pygame.mouse.get_pos()):
                        print("Un")
                        for elem in menu_strip.values():
                            elem.update(0, 0, 0, 0)
                            pygame.draw.rect(self.main_win.window, (0, 0, 0), elem)
                    elif menu_strip.get("fcb").collidepoint(pygame.mouse.get_pos()):
                        print("Deux")
                    elif menu_strip.get("discord").collidepoint(pygame.mouse.get_pos()):
                        print("Long")
                    else:
                        self.main_win.gbGame.show_groupbox(self.main_win.window)
                        return
