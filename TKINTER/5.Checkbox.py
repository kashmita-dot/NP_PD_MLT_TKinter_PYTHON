from tkinter import *
from PIL import Image, ImageTk

def display():
    if (x.get()==1) & (y.get()==0):
        print("I like you")
    elif (x.get()==0) & (y.get()==1):
        print("You like me")
    elif (x.get()==1) & (y.get()==1):
        print("You like both")
    else:
        print("I don't like either")

def load_image(path, size=(40, 40)):
    return ImageTk.PhotoImage(Image.open(path).resize(size))

window = Tk()   # must come before any image is created

photo = load_image('checkbox_pic.png')
photo2 = load_image('checkbox_pic2.png')

x = IntVar()
y = IntVar()

checkbox = Checkbutton(window, text='Hey You', variable=x, onvalue=1, offvalue=0, command=display)
checkbox.pack()
checkbox.config(font=('Arial', 20))
checkbox.config(fg='red')
checkbox.config(bg='beige')
checkbox.config(activeforeground='red')
checkbox.config(activebackground='beige')
checkbox.config(image=photo, compound='left')
checkbox.config(padx=25, pady=10, width=250, height=50)
checkbox.config(anchor='w')

checkbox2 = Checkbutton(window, text='Yes You', variable=y, onvalue=1, offvalue=0, command=display)
checkbox2.pack()
checkbox2.config(font=('Arial', 20))
checkbox2.config(fg='red')
checkbox2.config(bg='beige')
checkbox2.config(activeforeground='red')
checkbox2.config(activebackground='beige')

checkbox2.config(image=photo2, compound='left')
checkbox2.config(padx=25, pady=10, width=250, height=50)
checkbox2.config(anchor='w')

window.mainloop()