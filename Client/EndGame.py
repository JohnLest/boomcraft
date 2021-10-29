from tkinter import *

window=Tk()
victory = 0
# add widgets here

lbl=Label(window, text="Game over", fg='white', bg='#26e6bd', font=("Helvetica", 30))
lbl.place(x=600, y=100, anchor='center')
if victory == 1:
     lbl=Label(window, text="VICTORY !", fg='green', bg='white', font=("Helvetica", 20), width=40)
else:
     lbl=Label(window, text="DEFEAT !", fg='red', bg='white', font=("Helvetica", 20), width=40)
lbl.place(x=600, y=200, anchor='center')
btn=Button(window, text="Find a new game", fg='blue',width='20', height='2',font=("Helvetica", 17))
btn.place(x=600, y=300, anchor='center')
lbl=Label(window, text="Export Ressources", fg='black', bg='white', font=("Helvetica", 15), width=58)
lbl.place(x=600, y=400, anchor='center')

# Table of ressources
wood = 567864
stone = 68675
food = 5645
iron = 3548
warrior = 56
archer = 87
exportWood = IntVar(window)
exportStone = IntVar(window)
exportFood = IntVar(window)
exportIron = IntVar(window)
exportWarrior = IntVar(window)
exportArcher = IntVar(window)

lbl=Label(window, text="Name", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=420)
lbl=Label(window, text="Game Ressources", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=420)
lbl=Label(window, text="Ressources to export", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=21)
lbl.place(x=650, y=420)
lbl=Label(window, text="Export all", fg='black', bg='#DDDBDB', font=("Helvetica", 12), width=9)
lbl.place(x=836, y=420)

lbl=Label(window, text="Wood", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=449)
lbl=Label(window, text=wood, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=449)
entryBox = Entry(window, textvariable=exportWood, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=450)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=448)

lbl=Label(window, text="Stone", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=478)
lbl=Label(window, text=stone, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=478)
entryBox = Entry(window, textvariable=exportStone, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=479)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=477)

lbl=Label(window, text="Food", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=507)
lbl=Label(window, text=food, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=507)
entryBox = Entry(window, textvariable=exportFood, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=509)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=506)

lbl=Label(window, text="Iron", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=536)
lbl=Label(window, text=iron, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=536)
entryBox = Entry(window, textvariable=exportIron, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=537)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=535)

lbl=Label(window, text="Warrior", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=565)
lbl=Label(window, text=warrior, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=565)
entryBox = Entry(window, textvariable=exportWarrior, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=566)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=564)

lbl=Label(window, text="Archer", fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=278, y=594)
lbl=Label(window, text=archer, fg='black', bg='white', font=("Helvetica", 12), width=20)
lbl.place(x=464, y=594)
entryBox = Entry(window, textvariable=exportArcher, width=21, font=("Helvetica", 12))
entryBox.place(x=651, y=595)
btn=Button(window, text="All", fg='blue', width=8, font=("Helvetica", 10))
btn.place(x=849, y=593)

btn=Button(window, text="Quit", fg='red',width='30', height='2',font=("Helvetica", 12))
btn.place(x=600, y=650, anchor='center')

window.title('BoomCraft - End Game')
window.configure(bg='#26e6bd')
window.geometry("1200x900+10+20")
window.mainloop()