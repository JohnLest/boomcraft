import json
from tkinter import *

class ImportWindow:
    def __init__(self, potions):

        self.window = Tk()
        self.window.title('BoomCraft - Import from Farm Village')
        self.window.geometry("650x320")
        self.rb_value = StringVar(self.window, 100.00)
        self.potions = potions 


        self.__construct_import_window()

        self.__button_import()

        self.window.mainloop()

    def __construct_import_window(self):
        frame = LabelFrame(self.window, text='Import resources from Farm Village', padx=50)
        frame.pack()
        frame.place(x=50, y=0)

        for i in self.potions["player"]["inventory"]:

            print ("i",i)
            Radiobutton(frame,
                        text=i["label"]+" : "+str(i["quantity"]),
                        variable=self.rb_value,
                        value=[i["label"],i["quantity"]],
                        ).pack() 


    def __button_import(self):
        self.btn_donate = Button(self.window,
                                 text="Import",
                                 fg="blue",
                                 font=("Helvetica", 12),
                                 command=self.__btn_import_resource)
        self.btn_donate.place(x=300, y=220, height=30, width=300)
        self.btn_quit = Button(self.window,
                               text="Quit",
                               fg='red',
                               font=("Helvetica", 12),
                               command=self.__btn_quit_click)
        self.btn_quit.place(x=300, y=270, height=30, width=300)


    def __btn_import_resource(self):
        print(self.rb_value.get())

        self.window.quit()


    def __btn_quit_click(self):
        self.window.quit()