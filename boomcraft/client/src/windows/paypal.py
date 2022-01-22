import json
from tkinter import *
import requests

class Paypal:
    def __init__(self):
        self.window = Tk()
        self.window.title('BoomCraft - Donate Paypal')
        self.window.geometry("650x320")
        self.rb_value = StringVar(self.window, 100.00)
        self.__radio_button()
        self.__entry()
        self.__button()

        self.window.mainloop()

    def __radio_button(self):
        frame = LabelFrame(self.window, text='Donate mount', padx=50)
        frame.pack()
        frame.place(x=50, y=0)
        donate = {1.00: "Donate 1€",
                  2.00: "Donate 2€",
                  5.00: "Donate 5€",
                  10.00: "Donate 10€",
                  20.00: "Donate 20€",
                  50.00: "Donate 50€",
                  100.00: "Donate 100€",
                  200.00: "Donate 200€",
                  250.00: "Donate 250€"}
        for (key, value) in donate.items():
            Radiobutton(frame,
                        text=value,
                        variable=self.rb_value,
                        value=key,
                        ).pack()

    def __button(self):
        self.btn_donate = Button(self.window,
                                 text="Donate",
                                 fg="blue",
                                 font=("Helvetica", 12),
                                 command=self.__btn_donate_click)
        self.btn_donate.place(x=300, y=220, height=30, width=300)
        self.btn_quit = Button(self.window,
                               text="Quit",
                               fg='red',
                               font=("Helvetica", 12),
                               command=self.__btn_quit_click)
        self.btn_quit.place(x=300, y=270, height=30, width=300)

    def __entry(self):
        lbl_name = Label(self.window,
                         text="Name : ")
        lbl_name.place(x=300, y=10)
        self.entry_name = Entry(self.window,
                           width=30)
        self.entry_name.place(x=300, y=40)
        lbl_msg = Label(self.window,
                         text="Message :")
        lbl_msg.place(x=300, y=70)
        self.entry_msg = Entry(self.window,
                          width=30)
        self.entry_msg.place(x=300, y=100)

    def __btn_donate_click(self):
        data: dict = {
            "transactions": [
                {
                    "item_list": {
                        "items": [
                            {
                                "name": self.entry_name.get(),
                                "sku": "item",
                                "price": self.rb_value.get(),
                                "currency": "EUR",
                                "quantity": 1
                            }
                        ]
                    },
                    "amount": {
                        "total": self.rb_value.get(),
                        "currency": "EUR"
                    },
                    "description": self.entry_msg.get()
                }
            ]
        }
        req = requests.post(f"http://localhost:8000/paypal/", json=json.dumps(data))
        print(req)



    def __btn_quit_click(self):
        self.window.quit()

