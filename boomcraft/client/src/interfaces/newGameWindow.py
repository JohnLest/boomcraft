from tkinter import *


class NewGameWindow:
    def __init__(self):
        self.window = Tk()
        self.__set_labels()
        self.__set_buttons()
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
                                font=("Helvetica", 20))
        self.btn_start.place(x=600, y=240, anchor='center')

        self.btn_quit = Button(self.window,
                               text="Quit",
                               fg='red',
                               width='30',
                               height='2',
                               font=("Helvetica", 12))
        self.btn_quit.place(x=600, y=680, anchor='center')

    def __set_resources(self):
        self.resources_total = {}
        self.resources_import = {}

        # region self variable
        self.wood = IntVar()
        self.stone = IntVar()
        self.food = IntVar()
        self.iron = IntVar()
        self.gold = IntVar()
        self.worker = IntVar()
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

        # region Wood
        self.__create_table_resource("Wood", 0, self.wood, 450)
        btn_wood = Button(self.window,
                          text="All",
                          fg='blue',
                          width=8,
                          font=("Helvetica", 10))
        btn_wood.place(x=849, y=447)
        # endregion

        # region Stone
        self.__create_table_resource("Stone", 0, self.stone, 480)
        btn_stone = Button(self.window,
                           text="All",
                           fg='blue',
                           width=8,
                           font=("Helvetica", 10))
        btn_stone.place(x=849, y=477)
        # endregion

        # region Food
        self.__create_table_resource("Food", 0, self.food, 510)
        btn_food = Button(self.window,
                          text="All",
                          fg='blue',
                          width=8,
                          font=("Helvetica", 10))
        btn_food.place(x=849, y=507)
        # endregion

        # region Iron
        self.__create_table_resource("Iron", 0, self.iron, 540)
        btn_iron = Button(self.window,
                          text="All",
                          fg='blue',
                          width=8,
                          font=("Helvetica", 10))
        btn_iron.place(x=849, y=537)
        # endregion

        # region Gold
        self.__create_table_resource("Gold", 0, self.gold, 570)
        btn_gold = Button(self.window,
                          text="All",
                          fg='blue',
                          width=8,
                          font=("Helvetica", 10))
        btn_gold.place(x=849, y=567)
        # endregion

        # region Worker
        self.__create_table_resource("Worker", 0, self.worker, 600)
        btn_worker = Button(self.window,
                            text="All",
                            fg='blue',
                            width=8,
                            font=("Helvetica", 10))
        btn_worker.place(x=849, y=597)
        # endregion

    def __create_table_resource(self, name_resource, resource_own, resource_import, y):
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
                           textvariable=resource_import,
                           width=21,
                           font=("Helvetica", 12))
        entry_res.place(x=651, y=y)

