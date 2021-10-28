import pygame
from mainWindow import MainWindow
from mainWindowsEvent import MainWindowEvent


def main():
    pygame.init()
    main_win = MainWindow()
    MainWindowEvent(main_win)
    pygame.quit()
    return


if __name__ == "__main__":
    main()
