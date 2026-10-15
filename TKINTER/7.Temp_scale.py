from tkinter import *
from PIL import Image, ImageTk

def load_image(path, size):
    img = Image.open(path).resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

def submit():
    print("The temperature is: "+ str(scale.get())+ "°C")
window = Tk()

fireImage = load_image('fire.png', (100, 100))
fireLabel = Label(image=fireImage)
fireLabel.pack()

scale = Scale(window,
            from_=100,
            to= 0,
            length=400,
            orient=VERTICAL,
            font = ('Consolas', 20),
            tickinterval = 10,#adds numeric indicators for value
            # showvalue = 0 #hide current value
            resolution = 5, #increment of slider
            troughcolor = 'red',
            fg = "#ff005d",
            bg = 'beige'
            )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

snowflakeImage = load_image('snowflake.png',(100, 100))
snowflakeLabel = Label(image=snowflakeImage)
snowflakeLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()