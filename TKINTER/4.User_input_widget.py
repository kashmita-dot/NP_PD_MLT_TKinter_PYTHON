# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hey "+username)

def delete():
    entry.delete(0,END) #delete the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character

window = Tk()

submit = Button(window,text="submit",command=submit)
submit.pack(side=RIGHT)

delete = Button(window,text="delete",command=delete)
delete.pack(side=RIGHT)

backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side=RIGHT)

entry = Entry()
entry.config(font=('Ink Free', 50))
entry.config(bg="white")
entry.config(fg="blue")
# entry.insert(0,"Heyaaa!!")
# entry.config(state=DISABLED)
entry.config(width=10)
# entry.config(show='*') #EX- hidden password
entry.pack()






window.mainloop()