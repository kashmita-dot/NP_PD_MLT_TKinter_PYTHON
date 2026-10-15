from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is an info message box',message='You are a person')
    # messagebox.showerror(title='ERROR',message='something went wrong')
    

    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print('You did a thing!')
    # else:
    #     print('You canceled a thing! :(')


    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want to retry the thing?'):
    #     print('You retried a thing!')
    # else:
    #     print('You canceled a thing! :(')
    

    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #     print('I like cake too :)')
    # else:
    #     print('Why do you not like cake? :( ')


    # answer = messagebox.askquestion(title='ask question',message='Do you like coding?')
    # if(answer == 'yes'):
    #     print('I like coding too :) ')
    # else:
    #     print("Why the hell you don't like coding? :(")

    
    answer = messagebox.askyesnocancel(title=' Yes no cancel',message='do you like me?',icon='info') #error, warning, info
    if(answer == True):
        print("Dayumm you like me :) ")
    elif(answer == False):
        print("Then why do you hate me?")
    else:
        print("You are stupid!!")
    


    # messagebox.showwarning(title='WARNING!',message='You have a VIRUS!!!')
window = Tk()

button = Button(window,command=click,text='click me')
button.pack()




window.mainloop()