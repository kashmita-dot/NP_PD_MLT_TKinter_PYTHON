from tkinter import *

#Widgets = GUI elements: buttons, textboxes, labels, images
#Windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Cashie first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="pink")
window.mainloop() #place window on computer screen, listen for events
