# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.pack()

Button(frame,text="↑",font=("Consolas",25),width=3).pack(side=TOP) #Up Arrow (↑): Alt + 24 (Windows NumPad) or 2191
Button(frame,text="←",font=("Consolas",25),width=3).pack(side=LEFT) #Left Arrow (←): Alt + 27 (Windows NumPad) or 2190
Button(frame,text="↓",font=("Consolas",25),width=3).pack(side=LEFT) #Down Arrow (↓): Alt + 25 (Windows NumPad) or 2193
Button(frame,text="→",font=("Consolas",25),width=3).pack(side=LEFT) #Right Arrow (→): Alt + 26 (Windows NumPad) or 2192

window.mainloop()