from tkinter import *
import random

root = Tk()
root.geometry('500x500')
root.title("Dice Simulator")
label = Label(root,text ='',font=('Helvetica',260))

def roll_dice():
	dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	label.configure(text=f'{random.choice(dice)}')
	label.pack()


button = Button(root,text='roll dice',foreground='green',bg='blue',command=roll_dice)
button.pack()
root.mainloop()
