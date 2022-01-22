import pygame
from windows.mainWindow.mainWindow import MainWindow
from windows.mainWindow.mainWindowsEvent import MainWindowEvent
from connection import Connection


# region main

def main():
    print(f"Hello Client")
    new_connection = Connection("192.168.0.100", 8080)
    pygame.init()
    main_win = MainWindow(new_connection)
    MainWindowEvent(main_win)
    pygame.quit()
# endregion


if __name__ == "__main__":
    main()
