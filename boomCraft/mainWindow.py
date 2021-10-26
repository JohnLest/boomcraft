import pygame
from pygame.locals import *
from widget import Widget


class MainWindow(Widget):
    """ Class for main window """
    def __init__(self):
        self.mainWindow = pygame.display.set_mode((1080, 720))#, pygame.FULLSCREEN) # Initialisation full screen
        pygame.display.set_caption("BoomCraft")
        self.mainWinX, self.mainWinY = self.mainWindow.get_size()
        self.mainWinXPercent = self.mainWinX / 100
        self.mainWinYPercent = self.mainWinY / 100
        self.gbMenuButton = Rect(0, 0, self.mainWinXPercent*10, self.mainWinYPercent*5)
        self.gbResourceBanner = Rect(self.gbMenuButton.topright[0], self.gbMenuButton.topright[1], self.mainWinXPercent*90, self.mainWinYPercent*5)
        self.gbGame = Rect(self.gbMenuButton.bottomleft[0], self.gbMenuButton.bottomleft[1], self.mainWinX, self.mainWinYPercent*75)
        self.gbAction = Rect(self.gbGame.bottomleft[0], self.gbGame.bottomleft[1], self.mainWinX, self.mainWinYPercent*20)
        self.__drawWindow()
        return
    
    def __drawWindow(self):
        pygame.draw.rect(self.mainWindow, (255, 0, 0), self.gbMenuButton, 4)
        pygame.draw.rect(self.mainWindow, (0, 255, 0), self.gbResourceBanner, 4)
        pygame.draw.rect(self.mainWindow, (255, 255, 255), self.gbGame, 4)
        pygame.draw.rect(self.mainWindow, (0, 0, 255), self.gbAction, 4)
        pygame.display.flip()
        return

    def button_(self):
        return Widget.button(self.mainWindow, "API", rect=self.gbMenuButton)