import pygame
import logging

from windows.mainWindow.mainWindow import MainWindow
from windows.mainWindow.mainWindowsEvent import MainWindowEvent
from connection import Connection


# region main

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - class : %(name)s - %(message)s")
    logger = logging.getLogger(__name__)
    new_connection = Connection("192.168.0.100", 8080)
    pygame.init()
    main_win = MainWindow(new_connection)
    if main_win.menuWin.new_game:
        MainWindowEvent(main_win)
    pygame.quit()
# endregion


if __name__ == "__main__":
    main()
