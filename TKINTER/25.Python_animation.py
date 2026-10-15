from tkinter import *
from PIL import Image, ImageTk, ImageOps
import time


WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2


def load_image(path, size):
    img = Image.open(path).resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def load_background(path, size):
    img = Image.open(path)
    img = ImageOps.fit(img, size, Image.LANCZOS)   # scales and crops, no distortion
    return ImageTk.PhotoImage(img)

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = load_background('witchsky.png', (WIDTH, HEIGHT))
background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

photo_image = load_image('animewitch.png', (100, 100))            # resized witch
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()