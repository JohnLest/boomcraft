from tkinter import *
from src.windows.importWindow import ImportWindow

class NewGameWindow:
    def __init__(self, player_info):
        self.player_info = player_info
        self.new_game = False
        self.window = Tk()
        self.__set_labels()
        self.__set_buttons()
        self.__get_own_resource()
        self.__set_resources()

        self.window.title('BoomCraft - New Game')
        self.window.configure(bg='#26e6bd')
        self.window.geometry("1200x900+10+20")
        self.window.mainloop()

    def __set_labels(self):
        self.lbl_boomcraft = Label(self.window,
                                   text="BOOMCRAFT",
                                   fg='white',
                                   bg='#26e6bd',
                                   font=("Copperplate Gothic Bold", 44))
        self.lbl_boomcraft.place(x=600, y=100, anchor='center')

        self.lbl_title = Label(self.window,
                               text="Forum Defender",
                               fg='black', bg='white',
                               font=("Helvetica", 20), width=40)
        self.lbl_title.place(x=600, y=350, anchor='center')

        self.lbl_subtitle = Label(self.window,
                                  text="Import Resources",
                                  fg='black',
                                  bg='white',
                                  font=("Helvetica", 15),
                                  width=58)
        self.lbl_subtitle.place(x=600, y=400, anchor='center')

    def __set_buttons(self):
        self.btn_start = Button(self.window,
                                text="Start the game",
                                fg='blue', width='20',
                                height='2',
                                font=("Helvetica", 20),
                                command=self.__btn_start_click)
        self.btn_start.place(x=600, y=240, anchor='center')

        self.btn_import = Button(self.window,
                                text="Import",
                                fg='blue', width='10',
                                height='2',
                                font=("Helvetica", 20),
                                command=self.__btn_import_click)
        self.btn_import.place(x=900, y=240, anchor='center')

        self.btn_quit = Button(self.window,
                               text="Quit",
                               fg='red',
                               width='30',
                               height='2',
                               font=("Helvetica", 12),
                               command=self.__btn_quit_click)
        self.btn_quit.place(x=600, y=680, anchor='center')

    def __get_own_resource(self):
        self.own_resources_dict = {}
        for own_resource in self.player_info.own_resources:
            self.own_resources_dict.update({own_resource.resource: own_resource.quantity})

    def __set_resources(self):
        self.resources_total = {}
        self.resources_import = {}

        # region self variable
        self.wood = IntVar(self.window)
        self.stone = IntVar(self.window)
        self.food = IntVar(self.window)
        self.iron = IntVar(self.window)
        self.gold = IntVar(self.window)
        self.worker = IntVar(self.window)
        # endregion

        # region Header
        lbl_header_name = Label(self.window,
                                text="Name",
                                fg='black',
                                bg='#DDDBDB',
                                font=("Helvetica", 12),
                                width=20)
        lbl_header_name.place(x=278, y=420)
        lbl_header_own = Label(self.window,
                               text="Resources own",
                               fg='black',
                               bg='#DDDBDB',
                               font=("Helvetica", 12),
                               width=20)
        lbl_header_own.place(x=464, y=420)
        lbl_header_resources = Label(self.window,
                                     text="Resources to import",
                                     fg='black',
                                     bg='#DDDBDB',
                                     font=("Helvetica", 12),
                                     width=21)
        lbl_header_resources.place(x=650, y=420)
        lbl_header_all = Label(self.window,
                               text="Import all",
                               fg='black',
                               bg='#DDDBDB',
                               font=("Helvetica", 12),
                               width=9)
        lbl_header_all.place(x=836, y=420)
        # endregion

        self.__create_table_resource("Wood", self.own_resources_dict.get("wood"), self.wood, 450)
        self.__create_table_resource("Stone", self.own_resources_dict.get("stone"), self.stone, 480)
        self.__create_table_resource("Food", self.own_resources_dict.get("food"), self.food, 510)
        self.__create_table_resource("Iron", self.own_resources_dict.get("iron"), self.iron, 540)
        self.__create_table_resource("Gold", self.own_resources_dict.get("gold"), self.gold, 570)
        self.__create_table_resource("Worker", self.own_resources_dict.get("worker"), self.worker, 600)

    def __create_table_resource(self, name_resource, resource_own, resource, y):
        lbl_res = Label(self.window,
                         text=name_resource,
                         fg='black',
                         bg='white',
                         font=("Helvetica", 12),
                         width=20)
        lbl_res.place(x=278, y=y)
        lbl_res_own = Label(self.window,
                             text=resource_own,
                             fg='black',
                             bg='white',
                             font=("Helvetica", 12),
                             width=20)
        lbl_res_own.place(x=464, y=y)
        entry_res = Entry(self.window,
                          textvariable=resource,
                          width=21,
                          font=("Helvetica", 12))
        entry_res.place(x=651, y=y)
        btn = Button(self.window,
                          text="All",
                          fg='blue',
                          width=8,
                          font=("Helvetica", 10),
                          command=lambda: self.__btn_click(resource_own, resource))
        btn.place(x=849, y=y-3)

    def __btn_click(self, max_res, import_res):
        import_res.set(max_res)

    def __btn_import_click(self):
        _import = ImportWindow()
        tab_import = _import.value.split(" ")
        key = tab_import[0].lower()
        value = int(tab_import[1])
        if key == "wood":
            self.wood.set(value)
        elif key == "stone":
            self.stone.set(value)
        elif key == "iron":
            self.iron.set(value)
        elif key == "food":
            self.food.set(value)
        elif key == "gold":
            self.gold.set(value)
        _import.window.destroy()
        del _import

    def __btn_quit_click(self):
        self.window.quit()

    def __btn_start_click(self):
        self.game_resources_dict = {
            "wood": self.wood.get(),
            "stone": self.stone.get(),
            "food": self.food.get(),
            "iron": self.iron.get(),
            "gold": self.gold.get(),
            "worker": self.worker.get()
        }
        self.new_game = True
        self.window.quit()





