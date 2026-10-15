from tkinter import *
from PIL import Image, ImageTk

def load_icon(path, size=(20, 20)):
    img = Image.open(path)
    img = img.resize(size, Image.LANCZOS)   # high-quality resizing
    return ImageTk.PhotoImage(img)

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cutFile():
    print("You cut some text!")

def copyFile():
    print("You copied some text!")

def pasteFile():
    print("You pasted some text!")

window = Tk()

openImage = PhotoImage(file="open.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")
cutImage = PhotoImage(file="cut.png")
copyImage = PhotoImage(file="copy.png")
pasteImage = PhotoImage(file="paste.png")

openImage = load_icon("open.png")
saveImage = load_icon("save.png")
exitImage = load_icon("exit.png")
cutImage = load_icon("cut.png")
copyImage = load_icon("copy.png")
pasteImage = load_icon("paste.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=cutFile,image=cutImage,compound='left')
editMenu.add_command(label="copy",command=copyFile,image=copyImage,compound='left')
editMenu.add_command(label="paste",command=pasteFile,image=pasteImage,compound='left')

window.mainloop() 