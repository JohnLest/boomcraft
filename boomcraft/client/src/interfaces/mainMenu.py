from tkinter import *
import os


class MainMenu:
    def __init__(self):
        directory_path = os.getcwd()
        print("My current directory is : " + directory_path)
        folder_name = os.path.basename(directory_path)
        print("My directory name is : " + folder_name)

        self.bck_img = "../resources/bg-img.png"
        self.logo_img = "../resources/logo_MM.png"
        self.window = Tk()

        # add background
        self.background = PhotoImage(file=self.bck_img)
        self.lb_background = Label(self.window, image=self.background)
        self.lb_background.place(x=0, y=0)

        # add logo
        self.logo = PhotoImage(file=self.logo_img)
        self.lb_logo = Label(self.window, image=self.logo, bg='#26e6bd')
        self.lb_logo.place(x=450, y=50)

        self.__set_button()
        self.__show_window()

    def __set_button(self):
        #add buttons
        self.btn_new_game = Button(self.window,
                                   text="New Game",
                                   fg='blue', width='30',
                                   height='2',
                                   font=("Helvetica", 12),
                                   command=self.__btn_new_game_click)
        self.btn_new_game.place(x=380, y=240)
        self.btn_settings = Button(self.window,
                                   text="Settings",
                                   fg='blue',
                                   width='30',
                                   height='2',
                                   font=("Helvetica", 12),
                                   command=self.__btn_settings_click)
        self.btn_settings.place(x=380, y=300)
        self.btn_quit = Button(self.window,
                               text="Quit",
                               fg='red',
                               width='30',
                               height='2',
                               font=("Helvetica", 12),
                               command=self.__btn_quit_click)
        self.btn_quit.place(x=380, y=360)

    def __show_window(self):
        self.window.title('BoomCraft - Main Menu')
        self.window.geometry("1200x900+10+20")
        self.window.mainloop()

    def __btn_new_game_click(self):
        print(f"New game")

    def __btn_settings_click(self):
        print(f"Settings")

    def __btn_quit_click(self):
        print(f"Quit")


