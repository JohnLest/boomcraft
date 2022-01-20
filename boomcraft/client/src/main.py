from windows.mainWindow import MainWindow
from connection import Connection
import webbrowser


# region main

def main():
    print(f"Hello Client")
    new_connection = Connection("192.168.0.100", 8080)
    MainWindow(new_connection)

# endregion


if __name__ == "__main__":
    main()
