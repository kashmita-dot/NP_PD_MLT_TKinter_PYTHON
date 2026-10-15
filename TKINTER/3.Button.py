from tkinter import *

count = 0

def click():
    global count
    count+=1
    label.config(text=count)
    label2.pack()
window = Tk()
button = Button(window,text='Click me!!!')
button.config(command=click) #performs call back of function
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='green')
button.config(fg='black')
button.config(activebackground="#00FF55")
button.config(activeforeground='grey')
image = PhotoImage(file='label_pointing.png')
button.config(image=image)
button.config(compound='bottom')
# button.config(state=ACTIVE) #DISABLED/ACTIVE
label = Label(window,text=count)
label.config(font=('Monospace',50))
label.pack()
button.pack()
label2= Label(window,image=image)

window.mainloop()