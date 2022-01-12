from interfaces.menuWindow import MenuWindow
from connection import Connection


def main():
    print(f"Hello Client")
    new_connection = Connection("127.0.0.1", 8080)
    MenuWindow(new_connection)


if __name__ == "__main__":
    main()
