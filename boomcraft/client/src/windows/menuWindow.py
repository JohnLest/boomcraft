from tkinter import *
from src.windows.connectWindow import ConnectWindow
from src.windows.newGameWindow import NewGameWindow
from src.windows.paypal import Paypal


class MenuWindow:
    def __init__(self, connection, main_win):
        self.connection = connection
        self.main_windows = main_win
        self.bck_img = "../resources/bg-img.png"
        self.logo_img = "../resources/logo_MM.png"
        self.new_game = False

        self.window = Tk()
        self.window.title('BoomCraft - Menu')
        self.window.geometry("1200x900+10+20")

        # add background
        self.background = PhotoImage(file=self.bck_img)
        self.lb_background = Label(self.window, image=self.background)
        self.lb_background.place(x=0, y=0)

        # add logo
        self.logo = PhotoImage(file=self.logo_img)
        self.lb_logo = Label(self.window, image=self.logo, bg='#26e6bd')
        self.lb_logo.place(x=450, y=50)

        self.__set_buttons()

        self.window.mainloop()

    def __set_buttons(self):
        #add buttons
        self.btn_connect = Button(self.window,
                                  text="Connection",
                                  fg='blue', width='30',
                                  height='2',
                                  font=("Helvetica", 12),
                                  command=self.__btn_connect_click)
        self.btn_connect.place(x=380, y=240)
        self.btn_new_game = Button(self.window,
                                   text="New Game",
                                   fg='blue', width='30',
                                   height='2',
                                   font=("Helvetica", 12),
                                   command=self.__btn_new_game_click)
        self.btn_new_game.place(x=380, y=300)
        self.btn_new_game["state"] = "disabled"
        self.btn_settings = Button(self.window,
                                   text="Settings",
                                   fg='blue',
                                   width='30',
                                   height='2',
                                   font=("Helvetica", 12),
                                   command=self.__btn_settings_click)
        self.btn_settings.place(x=380, y=360)
        self.btn_paypal = Button(self.window,
                                   text="Donate with paypal",
                                   fg='blue',
                                   width='30',
                                   height='2',
                                   font=("Helvetica", 12),
                                   command=self.__btn_paypal_click)
        self.btn_paypal.place(x=380, y=420)
        self.btn_quit = Button(self.window,
                               text="Quit",
                               fg='red',
                               width='30',
                               height='2',
                               font=("Helvetica", 12),
                               command=self.__btn_quit_click)
        self.btn_quit.place(x=380, y=480)

    def __btn_connect_click(self):
        conn_win = ConnectWindow(self.connection, self.main_windows)
        conn_win.window.destroy()
        del conn_win
        self.btn_connect["state"] = "disabled"
        pseudo = self.main_windows.user.user.pseudo
        self.btn_connect["text"] = f"hello {pseudo}"
        self.btn_new_game["state"] = "active"

    def __btn_new_game_click(self):
        new_game_win = NewGameWindow(self.main_windows.user)
        new_game_win.window.destroy()
        if new_game_win.new_game:
            self.new_game = True
            self.connection.write({3: new_game_win.game_resources_dict})
        del new_game_win
        self.window.quit()

    def __btn_settings_click(self):
        print(f"Settings")

    def __btn_paypal_click(self):
        paypal = Paypal()
        paypal.window.destroy()
        del paypal

    def __btn_quit_click(self):
        self.window.quit()



