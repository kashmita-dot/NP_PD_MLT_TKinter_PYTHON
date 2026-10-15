from tkinter import *
#Label = an area widget that holds text and/or an image within a window
window = Tk()

photo = PhotoImage(file='label_logo.png')
label = Label(window,
                text="Hey, Do you breathe??",
                font=('Arial',40,'bold'),
                fg='black',
                bg='beige',
                relief=RAISED,
                bd=10,
                padx=20,
                pady=20,
                image=photo,
                compound='bottom')
label.pack()
# label.place(x=0,y=0)




window.mainloop()