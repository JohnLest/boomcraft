from tkinter import *


class NewGameWindow:
    def __init__(self, player_info, flappy_resources):
        self.player_info = player_info
        self.new_game = False
        self.window = Tk()
        self.__flappy_resources: dict = flappy_resources
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
        self.wood_bc = IntVar(self.window)
        self.stone_bc = IntVar(self.window)
        self.food_bc = IntVar(self.window)
        self.iron_bc = IntVar(self.window)
        self.gold_bc = IntVar(self.window)

        self.wood_flp = IntVar(self.window)
        self.stone_flp = IntVar(self.window)
        self.food_flp = IntVar(self.window)
        self.iron_flp = IntVar(self.window)
        self.gold_flp = IntVar(self.window)
        # endregion

        # region Header
        lbl_header_name = Label(self.window,
                                text="Name",
                                fg='black',
                                bg='#DDDBDB',
                                font=("Helvetica", 12),
                                width=20)
        lbl_header_name.place(x=50, y=420)
        lbl_header_bc = Label(self.window,
                               text="Resources boomcraft",
                               fg='black',
                               bg='#DDDBDB',
                               font=("Helvetica", 12),
                               width=20)
        lbl_header_bc.place(x=250, y=420)
        lbl_header_resources_bc = Label(self.window,
                                     text="Resources to import",
                                     fg='black',
                                     bg='#DDDBDB',
                                     font=("Helvetica", 12),
                                     width=21)
        lbl_header_resources_bc.place(x=450, y=420)
        lbl_header_flappy = Label(self.window,
                              text="Resources flappy",
                              fg='black',
                              bg='#DDDBDB',
                              font=("Helvetica", 12),
                              width=20)
        lbl_header_flappy.place(x=650, y=420)
        lbl_header_resources_flappy = Label(self.window,
                                     text="Resources to import",
                                     fg='black',
                                     bg='#DDDBDB',
                                     font=("Helvetica", 12),
                                     width=21)
        lbl_header_resources_flappy.place(x=850, y=420)
        lbl_header_all = Label(self.window,
                               text="Import all",
                               fg='black',
                               bg='#DDDBDB',
                               font=("Helvetica", 12),
                               width=9)
        lbl_header_all.place(x=1050, y=420)
        # endregion

        self.__create_table_resource("Wood", self.own_resources_dict.get("wood"), self.wood_bc, self.__flappy_resources.get("Wood", 0), self.wood_flp, 450)
        self.__create_table_resource("Stone", self.own_resources_dict.get("stone"), self.stone_bc, self.__flappy_resources.get("Stone", 0), self.stone_flp, 480)
        self.__create_table_resource("Food", self.own_resources_dict.get("food"), self.food_bc, self.__flappy_resources.get("Food", 0), self.food_flp, 510)
        self.__create_table_resource("Iron", self.own_resources_dict.get("iron"), self.iron_bc, self.__flappy_resources.get("Iron", 0), self.iron_flp, 540)
        self.__create_table_resource("Gold", self.own_resources_dict.get("gold"), self.gold_bc, self.__flappy_resources.get("Gold", 0), self.gold_flp, 570)

    def __create_table_resource(self, name_resource, resource_own, set_resource_bc, flappy_resource, set_resource_flappy, y):
        lbl_res = Label(self.window,
                         text=name_resource,
                         fg='black',
                         bg='white',
                         font=("Helvetica", 12),
                         width=20)
        lbl_res.place(x=50, y=y)
        lbl_res_bc = Label(self.window,
                             text=resource_own,
                             fg='black',
                             bg='white',
                             font=("Helvetica", 12),
                             width=20)
        lbl_res_bc.place(x=250, y=y)
        entry_res_bc = Entry(self.window,
                          textvariable=set_resource_bc,
                          width=21,
                          font=("Helvetica", 12))
        entry_res_bc.place(x=450, y=y)
        lbl_res_flappy = Label(self.window,
                             text=flappy_resource,
                             fg='black',
                             bg='white',
                             font=("Helvetica", 12),
                             width=20)
        lbl_res_flappy.place(x=650, y=y)
        entry_res_flappy = Entry(self.window,
                          textvariable=set_resource_flappy,
                          width=21,
                          font=("Helvetica", 12))
        entry_res_flappy.place(x=850, y=y)
        btn = Button(self.window,
                          text="All",
                          fg='blue',
                          width=8,
                          font=("Helvetica", 10),
                          command=lambda: self.__btn_click(resource_own, flappy_resource, set_resource_bc, set_resource_flappy)
                     )
        btn.place(x=1050, y=y-3)

    def __btn_click(self, resource_own, flappy_resource, set_resource_bc, set_resource_flappy):
        set_resource_bc.set(resource_own)
        set_resource_flappy.set(flappy_resource)

    def __btn_quit_click(self):
        self.window.quit()

    def __btn_start_click(self):
        self.game_resources_dict = {
            "wood": self.wood_bc.get(),
            "stone": self.stone_bc.get(),
            "food": self.food_bc.get(),
            "iron": self.iron_bc.get(),
            "gold": self.gold_bc.get(),
        }
        self.game_flappy_resources_dict = {
            "Wood": self.wood_flp.get(),
            "Stone": self.stone_flp.get(),
            "Food": self.food_flp.get(),
            "Iron": self.iron_flp.get(),
            "Gold": self.gold_flp.get(),
        }
        self.new_game = True
        self.window.quit()





