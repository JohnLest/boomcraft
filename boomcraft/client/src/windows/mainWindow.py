from src.windows.menuWindow import MenuWindow



class MainWindow:
    def __init__(self, connection):
        print(f"mainWindow")
        self.connection = connection
        self.connection.service()
        self.menuWin = MenuWindow(self.connection)
        if self.menuWin.new_game:
            print("Start Game")
            print(self.connection.user.dict())
        self.menuWin.window.destroy()





