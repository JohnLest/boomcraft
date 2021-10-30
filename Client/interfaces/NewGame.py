from tkinter import *
#from  tkinter import ttk

window=Tk()
# add widgets here

lbl=Label(window, text="BOOMCRAFT", fg='white', bg='#26e6bd', font=("Copperplate Gothic Bold", 44))
lbl.place(x=600, y=100, anchor='center')
btn=Button(window, text="Start the game", fg='blue',width='20', height='2',font=("Helvetica", 20))
btn.place(x=600, y=240, anchor='center')
lbl=Label(window, text="Forum Defender", fg='black', bg='white', font=("Helvetica", 20), width=40)
lbl.place(x=600, y=350, anchor='center')
lbl=Label(window, text="Import Ressources", fg='black', bg='white', font=("Helvetica", 15), width=58)
lbl.place(x=600, y=400, anchor='center')

# Table of ressources
DBWood = 567864531
DBStone = 68675
DBFood = 5645
DBIron = 3548
DBWarrior = 56
DBArcher = 87
importWood = IntVar(window)
importStone = IntVar(window)
importFood = IntVar(window)
importIron = IntVar(window)
importWarrior = IntVar(window)
importArcher = IntVar(window)

lbl=Label(window, text="Name", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=420)
lbl=Label(window, text="Ressources own", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=420)
lbl=Label(window, text="Ressources to import", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=21)
lbl.place(x=650, y=420)
lbl=Label(window, text="Import all", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=9)
lbl.place(x=836, y=420)

lbl=Label(window, text="Wood", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=449)
lbl=Label(window, text=DBWood, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=449)
entryBox = Entry(window, textvariable=importWood, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=450)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=448)

lbl=Label(window, text="Stone", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=478)
lbl=Label(window, text=DBStone, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=478)
entryBox = Entry(window, textvariable=importStone, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=479)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=477)

lbl=Label(window, text="Food", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=507)
lbl=Label(window, text=DBFood, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=507)
entryBox = Entry(window, textvariable=importFood, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=509)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=506)

lbl=Label(window, text="Iron", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=536)
lbl=Label(window, text=DBIron, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=536)
entryBox = Entry(window, textvariable=importIron, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=537)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=535)

lbl=Label(window, text="Warrior", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=565)
lbl=Label(window, text=DBWarrior, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=565)
entryBox = Entry(window, textvariable=importWarrior, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=566)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=564)

lbl=Label(window, text="Archer", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=594)
lbl=Label(window, text=DBArcher, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=594)
entryBox = Entry(window, textvariable=importArcher, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=595)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=593)

btn=Button(window, text="Quit", fg='red',width='30', height='2',font=("Helvetica", 12))
btn.place(x=600, y=650, anchor='center')


#list = ttk.Treeview(window)
#list.place(x=600, y=600, anchor='center')

#list['columns']= ('Res','Amount')

#list.column("#0", width=0,  stretch=NO)
#list.column("Res",anchor=CENTER, width=150)
#list.column("Amount",anchor=CENTER, width=150)

#list.insert(parent='',index='end',iid=0,text='',
#values=('Wood','1000'))
#list.insert(parent='',index='end',iid=1,text='',
#values=('Stone','1000'))
#list.insert(parent='',index='end',iid=2,text='',
#values=('Food','1000'))
#list.insert(parent='',index='end',iid=3,text='',
#values=('Iron','1000'))
#list.insert(parent='',index='end',iid=4,text='',
#values=('Warrior','1000'))
#list.insert(parent='',index='end',iid=5,text='',
#values=('Archer','1000'))




window.title('BoomCraft - New Game')
window.configure(bg='#26e6bd')
window.geometry("1200x900+10+20")
window.mainloop()