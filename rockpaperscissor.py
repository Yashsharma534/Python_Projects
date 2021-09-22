from tkinter import *
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("Rock_Paper_Scissor")
root.configure(background='red')

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root,image = scissor_img,bg = "red")
comp_label = Label(root,image = scissor_img_comp,bg ="red")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerscore = Label(root,text=0,font=100,bg="blue",fg="yellow")
compscore = Label(root,text=0,font=100,bg="blue",fg="yellow")
playerscore.grid(row=1,column=3)
compscore.grid(row=1,column=1)

msg = Label(root,font=50,bg = 'blue',fg='yellow')
msg.grid(row=3,column=2)

def updateUserScore():
	score = int(playerscore["text"])
	score+=1
	playerscore["text"] = str(score)

def updatecompscore():
	score =int(compscore["text"])
	score+=1
	compscore["text"] =str(score)


def UpdateMessage(x):
	msg['text'] = x

def checkWin(player,computer):
	if player == computer:
		UpdateMessage("It's tie")
	elif player == "rock":
		if computer == "paper":
			UpdateMessage("You Loose")
			updatecompscore()
		else:
			UpdateMessage("You Win")
			updateUserScore()
	elif player == "paper":
		if computer == "scissor":
			UpdateMessage("You Loose")
			updatecompscore()
		else:
			UpdateMessage("You Win")
			updateUserScore()
	elif player == "scissor":
		if computer == "rock":
			UpdateMessage("You Loose")
			updatecompscore()
		else:
			UpdateMessage("You Win")
			updateUserScore()
	else:
		pass



choices = ["rock","paper","scissor"]
def UpdateChoice(x):
	comp_choice = choices[randint(0,2)]
	if comp_choice == "rock":
		comp_label.configure(image=rock_img_comp)
	elif comp_choice == "paper":
		comp_label.configure(image=paper_img_comp)
	else:
		comp_label.configure(image=scissor_img_comp)

	if x == "rock":
		user_label.configure(image=rock_img)
	elif x == "paper":
		user_label.configure(image=paper_img)
	else:
		user_label.configure(image=scissor_img)

	checkWin(x,comp_choice)

rock = Button(root,height=2,width=20,text="ROCK",bg="blue",fg="yellow",command=lambda:UpdateChoice("rock")).grid(row=2,column=1)
paper=Button(root,height=2,width=20,text="PAPER",bg="blue",fg="yellow",command=lambda:UpdateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,height=2,width=20,text="SCISSOR",bg="blue",fg="yellow",command=lambda:UpdateChoice("scissor")).grid(row=2,column=3)

root.mainloop()