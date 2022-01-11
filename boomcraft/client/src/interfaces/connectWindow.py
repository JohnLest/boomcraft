from tkinter import *


class ConnectWindow:
    def __init__(self):
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

    def __set_buttons(self):
        self.btn_connect = Button(self.window,
                               text="Connection",
                               fg='blue',
                               font=("Helvetica", 12),
                               command=self.__btn_connect_click)
        self.btn_connect.place(x=350, y=110, height=30, width=300)

        self.btn_create = Button(self.window,
                                 text="Create new user",
                                 fg='blue',
                                 font=("Helvetica", 12),
                                 command=self.__btn_create_click)
        self.btn_create.place(x=350, y=150, height=30, width=300)

        self.btn_quit = Button(self.window,
                                 text="Quit",
                                 fg='red',
                                 font=("Helvetica", 12),
                                 command=self.__btn_connect_click)
        self.btn_quit.place(x=350, y=190, height=30, width=300)

    def __btn_connect_click(self):
        self.head = 1
        self.window.quit()

    def __btn_create_click(self):
        self.head = 2
        self.window.quit()

    def connect(self):
        self.window.mainloop()
        user = {"pseudo": self.txt_pseudo.get(),
                "mail": self.txt_mail.get(),
                "password": self.txt_password.get()}
        msg = {self.head: user}
        return msg
