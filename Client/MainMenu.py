from tkinter import *

window=Tk()

# add background
img = PhotoImage(file="../Ressources/bg-img.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)

# add logo
img2 = PhotoImage(file="../Ressources/logo_MM.png")
label2 = Label(
    window,
    image=img2, bg='#26e6bd'
)
label2.place(x=450, y=50)

#add buttons
btn=Button(window, text="New Game", fg='blue',width='30', height='2',font=("Helvetica", 12))
btn.place(x=380, y=240)
btn=Button(window, text="Settings", fg='blue',width='30', height='2', font=("Helvetica", 12))
btn.place(x=380, y=300)
btn=Button(window, text="Quit", fg='red',width='30', height='2',font=("Helvetica", 12))
btn.place(x=380, y=360)

window.title('BoomCraft - Main Menu')
window.geometry("1200x900+10+20")
window.mainloop()