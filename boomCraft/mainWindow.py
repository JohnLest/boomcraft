import pygame
from pygame.locals import *
from widget import Button, MenuStrip, GroupBox
from window import Window


class MainWindow(Window):
    """ Class for main window """
    def __init__(self):
        self.main_win = Window.__init__(self, (1080, 720), "Boomcraft")
        self.__gbMenuButton()
        self.__gbResourceBanner()
        self.__gbGame()
        self.__gbAction()
        self.__menu_strip_api()

    def __gbMenuButton(self):
        """ GroupBox for Menu Button """
        self.gbMenuButton = GroupBox(
            (0, 0),
            (self.main_win.winXPercent * 10, self.main_win.winYPercent * 5),
            (0, 0, 0)
        )
        self.btnAPI = Button(self.main_win.window, "API", rect=self.gbMenuButton.data_rect)
        return self

    def __gbResourceBanner(self):
        """ GroupBox for banner resources """
        self.gbResourceBanner = GroupBox(
            (self.gbMenuButton.data_rect.topright[0], self.gbMenuButton.data_rect.topright[1]),
            (self.main_win.winXPercent * 90, self.main_win.winYPercent * 5),
            (0, 0, 0)
        )
        return self

    def __gbGame(self):
        """ GroupBox for the play board """
        self.gbGame = GroupBox(
            (self.gbMenuButton.data_rect.bottomleft[0], self.gbMenuButton.data_rect.bottomleft[1]),
            (self.main_win.winX, self.main_win.winYPercent * 75),
            (180, 250, 150)
        )
        self.gbGame.show_groupbox(self.main_win.window)
        return self

    def __gbAction(self):
        """ GroupBox for the action in game """
        self.gbAction = GroupBox(
            (self.gbGame.data_rect.bottomleft[0], self.gbGame.data_rect.bottomleft[1]),
            (self.main_win.winX, self.main_win.winYPercent * 20),
            (0, 0, 0)
        )
        return self

    def __menu_strip_api(self):
        self.menu_stripe_dict = {"twitch": "Twitch", "fcb": "Facebook", "discord": "Discord"}
        self.menu_sprite = MenuStrip(self.btnAPI.btn_rect, self.menu_stripe_dict)
