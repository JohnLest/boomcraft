import pygame
from interfaces.mainWindow.mainWindow import MainWindow
from interfaces.mainWindow.mainWindowsEvent import MainWindowEvent


def main():
    pygame.init()
    main_win = MainWindow()
    MainWindowEvent(main_win)
    pygame.quit()
    return
    ''' 
    GameClient
    LoginMenu
    MainMenu
    '''

if __name__ == "__main__":
    main()
