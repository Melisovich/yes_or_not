from tkinter import *
from tkinter import messagebox
import random


def no():
    messagebox.showinfo(' ', 'Правильно!')
    quit()


def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))


root = Tk()
root.geometry('600x600')
root.title('Внимание вопрос!')
root.resizable(width=False, height=False)
root['bg'] = 'white'


label = Label(root, text='Ты дурак?', font='Arial 40 bold', bg='white').pack()
btnYes = Button(root, text='Нет', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Да', font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()