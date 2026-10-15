from tkinter import *
from PIL import Image, ImageTk
import os

# Radio button = similar to checkbox, but you can only select one from a group.

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered hamburger!")
    elif x.get() == 2:
        print("You ordered hotdog!")
    else:
        print("Huh?")

def load_image(path, size=(60, 60)):
    return ImageTk.PhotoImage(Image.open(path).resize(size))

window = Tk()

# Look for the images in the same folder as this script
folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pizzaImage = load_image(os.path.join(folder, 'pizza.png'))
hamburgerImage = load_image(os.path.join(folder, 'hamburger.png'))
hotdogImage = load_image(os.path.join(folder, 'hotdog.png'))
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                            text=food[index],
                            variable=x,
                            value=index,
                            padx=25,
                            font=("Impact", 50),
                            image=foodImages[index],
                            compound='left',
                            indicatoron=0,
                            width=375,
                            command=order)
    radiobutton.pack(anchor=W)

window.mainloop()