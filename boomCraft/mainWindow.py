import pygame
from pygame.locals import *
from widget import Widget
from window import Window


class MainWindow(Window):
    """ Class for main window """
    def __init__(self):
        self.main_win = Window.__init__(self, (1080, 720), "Boomcraft")
        self.__gbMenuButton()
        self.__gbResourceBanner()
        self.__gbGame()
        self.__gbAction()

    def __gbMenuButton(self):
        """ GroupBox for Menu Button """
        self.gbMenuButton = Widget.groupbox(
            self.main_win.window,
            (0, 0),
            (self.main_win.winXPercent * 10, self.main_win.winYPercent * 5)
        )
        self.btn = Widget.button(self.main_win.window, "API", rect=self.gbMenuButton)
        return self

    def __gbResourceBanner(self):
        """ GroupBox for banner resources """
        self.gbResourceBanner = Widget.groupbox(
            self.main_win.window,
            (self.gbMenuButton.topright[0], self.gbMenuButton.topright[1]),
            (self.main_win.winXPercent * 90, self.main_win.winYPercent * 5)
        )
        return self

    def __gbGame(self):
        """ GroupBox for the play board """
        self.gbGame = Widget.groupbox(
            self.main_win.window,
            (self.gbMenuButton.bottomleft[0], self.gbMenuButton.bottomleft[1]),
            (self.main_win.winX, self.main_win.winYPercent * 75)
        )
        return self

    def __gbAction(self):
        """ GroupBox for the action in game """
        self.gbAction = Widget.groupbox(
            self.main_win.window,
            (self.gbGame.bottomleft[0], self.gbGame.bottomleft[1]),
            (self.main_win.winX, self.main_win.winYPercent * 20)
        )
        return self

    def button(self, text):
        return
