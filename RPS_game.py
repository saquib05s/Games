import random
from tkinter import *
from tkinter import messagebox
root=Tk()

game_list=['Rock','Paper','Scissors']
c=0; p=0; result=""
e=Entry(root, width=50)
e.grid(row=0, column=0, columnspan=4)
ScoreLabel=Label(root,text="")
ScoreLabel.grid(row=1,column=0, columnspan=4)
def score(p,c):
    ScoreLabel.config(text="Computer="+str(c)+"   "+e.get()+"="+str(p))

def popup():
    messagebox.showwarning("","Enter name first")
    e.focus()

def fun(user):
    if(e.get()==""):
        popup()
    else:
        computer_choice=random.choice(game_list)
        global p,c, result
        if user == computer_choice:
            result="Tie"
            ResultLabel.config(text=result)
        elif user=="Rock":
            if computer_choice=="Scissors":
                result=e.get()+" won"
                p+=1
                score(p,c)
                ResultLabel.config(text=result)
            else:
                result="Computer Won"
                c+=1
                score(p,c)
                ResultLabel.config(text=result)
        elif user=="Paper":
            if computer_choice=="Rock":
                result=e.get()+" won"
                p+=1
                score(p,c)
                ResultLabel.config(text=result)
            else:
                result="Computer Won"
                c+=1
                score(p,c)
                ResultLabel.config(text=result)
        elif user=="Scissors":
            if computer_choice=="Paper":
                result=e.get()+" won"
                p+=1
                score(p,c)
                ResultLabel.config(text=result)
            else:
                result="Computer Won"
                c+=1
                score(p,c)
                ResultLabel.config(text=result)
    if user=="Reset":
        c=0; p=0
        score(p,c)
        ResultLabel.config(text="")
        ScoreLabel.config(text="")
        e.delete(0,END)

def Reset():
    ResultLabel.config(text="")
    fun("Reset")

Rock=Button(root, text="Rock", padx=20, pady=20, bg="#ff0000", command= lambda: fun("Rock"))
Paper=Button(root, text="Paper", padx=20, pady=20, bg="#ffff00", command= lambda: fun("Paper"))
Scissors=Button(root, text="Scissors", padx=20, pady=20, bg="#ff00ff", command= lambda: fun("Scissors"))
Reset=Button(root, text="Reset", padx=5, pady=5, bg="#00ff00", command=Reset)
Rock.grid(row=2, column=0, padx=10, pady=10)
Paper.grid(row=2, column=1, padx=10, pady=10)
Scissors.grid(row=2, column=2, padx=10, pady=10)
Reset.grid(row=2, column=3, padx=10, pady=10, ipadx=15, ipady=15)
ResultLabel=Label(root,text="")
ResultLabel.grid(row=3, column=0, columnspan=4)
root.mainloop()
