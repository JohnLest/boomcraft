from windows.mainWindow import MainWindow
from connection import Connection
import webbrowser


# region main

def main():
    print(f"Hello Client")
    url = "http://localhost:8000"
    new_connection = Connection("127.0.0.1", 8080)
    webbrowser.open(url)
    MainWindow(new_connection)

# endregion


if __name__ == "__main__":
    main()
