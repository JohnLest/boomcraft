import time
from tkinter import *
import webbrowser
import uuid


class ConnectWindow:
    def __init__(self, connection, main_win):
        self.connection = connection
        self.main_windows = main_win
        self.head = 0
        self.window = Tk()
        self.window.title('BoomCraft - Menu')
        self.window.geometry("720x240")
        self.lbl_pseudo = Label(self.window,
                                text="Pseudo :")
        self.lbl_pseudo.place(x=50, y=20)
        self.txt_pseudo = Entry(self.window,
                                width=30)
        self.txt_pseudo.place(x=50, y=50)

        self.lbl_mail = Label(self.window,
                              text="Mail :")
        self.lbl_mail.place(x=350, y=20)
        self.txt_mail = Entry(self.window,
                              width=30)
        self.txt_mail.place(x=350, y=50)

        self.lbl_password = Label(self.window,
                                  text="Pseudo :")
        self.lbl_password.place(x=50, y=100)
        self.txt_password = Entry(self.window,
                                  show='*',
                                  width=30)
        self.txt_password.place(x=50, y=130)

        self.__set_buttons()
        self.window.mainloop()

    def __set_buttons(self):
        self.btn_connect = Button(self.window,
                               text="Connection",
                               fg='blue',
                               font=("Helvetica", 12),
                               command=self.__btn_connect_click)
        self.btn_connect.place(x=350, y=110, height=30, width=300)

        self.btn_facebook = Button(self.window,
                                 text="Connect with Facebook",
                                 fg='blue',
                                 font=("Helvetica", 12),
                                 command=self.__btn_facebook_click)
        self.btn_facebook.place(x=350, y=150, height=30, width=300)

        self.btn_create = Button(self.window,
                                 text="Create new user",
                                 fg='blue',
                                 font=("Helvetica", 12),
                                 command=self.__btn_create_click)
        self.btn_create.place(x=350, y=190, height=30, width=300)

        self.btn_quit = Button(self.window,
                                 text="Quit",
                                 fg='red',
                                 font=("Helvetica", 12),
                                 command=self.__btn_quit_click)
        self.btn_quit.place(x=50, y=190, height=30, width=300)

    def __btn_connect_click(self):
        self.head = 1
        self.__connect()
        self.window.quit()

    def __btn_create_click(self):
        self.head = 2
        self.__connect()
        self.window.quit()

    def __btn_facebook_click(self):
        _uuid = uuid.uuid4()
        self.connection.write({100: {"uuid": str(_uuid)}})
        url = f"https://localhost:8000/facebook/{_uuid}"
        webbrowser.open(url)
        while True:
            if self.main_windows.user is not None:
                break
            time.sleep(0.5)
        self.window.quit()

    def __btn_quit_click(self):
        self.window.quit()

    def __connect(self):
        user = {"pseudo": self.txt_pseudo.get(),
                "mail": self.txt_mail.get(),
                "password": self.txt_password.get()}
        self.connection.write({self.head: user})
        while True:
            if self.main_windows.user is not None:
                break
