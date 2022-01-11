from tkinter import *


class ConnectWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title('BoomCraft - Menu')
        self.window.geometry("720x240")
        self.lbl_pseudo = Label(self.window,
                                text="Pseudo :")
        self.lbl_pseudo.place(x=50, y=20)
        self.txt_pseudo = Entry(self.window,
                                width=30)
        self.txt_pseudo.place(x=50, y=50)
        self.__set_buttons()

    def __set_buttons(self):
        self.btn_connect = Button(self.window,
                               text="Connection",
                               fg='blue',
                               width='30',
                               height='2',
                               font=("Helvetica", 12),
                               command=self.__btn_connect_click)
        self.btn_connect.place(x=50, y=100)

    def __btn_connect_click(self):
        self.window.quit()

    def connect(self):
        self.window.mainloop()
        pseudo = self.txt_pseudo.get()
        self.window.destroy()
        return pseudo
