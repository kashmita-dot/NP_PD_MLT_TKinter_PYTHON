from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)
# or
# def click():
#     window.config(bg=colorchooser.askcolor()[1]) #change background color

window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()