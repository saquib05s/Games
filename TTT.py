import tkinter as tk
import random
root=tk.Tk()
root.geometry("200x200")
tcount=0
xcount=1
ocount=0
tiecount=0

def fun():
    global tiecount
    if tiecount==0:
        if R1C1Label.cget("text")=="X" and R2C1Label.cget("text")=="X" and R3C1Label.cget("text")=="X" or \
        R1C2Label.cget("text")=="X" and R2C2Label.cget("text")=="X" and R3C2Label.cget("text")=="X" or \
        R1C3Label.cget("text")=="X" and R2C3Label.cget("text")=="X" and R3C3Label.cget("text")=="X" or \
        R1C1Label.cget("text")=="X" and R1C2Label.cget("text")=="X" and R1C3Label.cget("text")=="X" or \
        R2C1Label.cget("text")=="X" and R2C2Label.cget("text")=="X" and R2C3Label.cget("text")=="X" or \
        R3C1Label.cget("text")=="X" and R3C2Label.cget("text")=="X" and R3C3Label.cget("text")=="X" or \
        R1C1Label.cget("text")=="X" and R2C2Label.cget("text")=="X" and R3C3Label.cget("text")=="X" or \
        R1C3Label.cget("text")=="X" and R2C2Label.cget("text")=="X" and R3C1Label.cget("text")=="X":
            ResultLabel.config(text="Player X Won")
            tiecount=1
        
        elif R1C1Label.cget("text")=="O" and R2C1Label.cget("text")=="O" and R3C1Label.cget("text")=="O" or \
        R1C2Label.cget("text")=="O" and R2C2Label.cget("text")=="O" and R3C2Label.cget("text")=="O" or \
        R1C3Label.cget("text")=="O" and R2C3Label.cget("text")=="O" and R3C3Label.cget("text")=="O" or \
        R1C1Label.cget("text")=="O" and R1C2Label.cget("text")=="O" and R1C3Label.cget("text")=="O" or \
        R2C1Label.cget("text")=="O" and R2C2Label.cget("text")=="O" and R2C3Label.cget("text")=="O" or \
        R3C1Label.cget("text")=="O" and R3C2Label.cget("text")=="O" and R3C3Label.cget("text")=="O" or \
        R1C1Label.cget("text")=="O" and R2C2Label.cget("text")=="O" and R3C3Label.cget("text")=="O" or \
        R1C3Label.cget("text")=="O" and R2C2Label.cget("text")=="O" and R3C1Label.cget("text")=="O":
            ResultLabel.config(text="Player O Won")
            tiecount=1
        
        else:
            if tcount>=8:
                ResultLabel.config(text="Tie")
                tiecount=1

def reset():
    global tiecount, tcount, xcount, ocount, lis
    lis=[R1C1Button, R1C2Button, R1C3Button, R2C1Button, R2C2Button, R2C3Button, R3C1Button, R3C2Button, R3C3Button]
    tcount=0
    xcount=1
    ocount=0
    tiecount=0
    R1C1Button['state']=tk.NORMAL
    R1C2Button['state']=tk.NORMAL
    R1C3Button['state']=tk.NORMAL
    R2C1Button['state']=tk.NORMAL
    R2C2Button['state']=tk.NORMAL
    R2C3Button['state']=tk.NORMAL
    R3C1Button['state']=tk.NORMAL
    R3C2Button['state']=tk.NORMAL
    R3C3Button['state']=tk.NORMAL
    R1C1Label.config(text="")
    R1C2Label.config(text="")
    R1C3Label.config(text="")
    R2C1Label.config(text="")
    R2C2Label.config(text="")
    R2C3Label.config(text="")
    R3C1Label.config(text="")
    R3C2Label.config(text="")
    R3C3Label.config(text="")
    ResultLabel.config(text="")
    R1C1Label.grid_forget()
    R1C2Label.grid_forget()
    R1C3Label.grid_forget()
    R2C1Label.grid_forget()
    R2C2Label.grid_forget()
    R2C3Label.grid_forget()
    R3C1Label.grid_forget()
    R3C2Label.grid_forget()
    R3C3Label.grid_forget()

def disableR1C1():
    global xcount, ocount, tcount, lis
    if R1C1Button in lis:
        lis.remove(R1C1Button)
    R1C1Button['state']=tk.DISABLED
    if xcount>ocount:
        R1C1Label.config(text="O")
        ocount+=1
    else:
        R1C1Label.config(text="X")
        xcount+=1
    R1C1Label.grid(row=0, column=0, padx=(10,0), pady=(10,0))
    tcount+=1
    fun()
    
def disableR1C2():
    global xcount, ocount, tcount, lis
    if R1C2Button in lis:
        lis.remove(R1C2Button)
    R1C2Button['state']=tk.DISABLED
    if xcount>ocount:
        R1C2Label.config(text="O")
        ocount+=1
    else:
        R1C2Label.config(text="X")
        xcount+=1
    R1C2Label.grid(row=0, column=1, pady=(10,0))
    tcount+=1
    fun()
    
def disableR1C3():
    global xcount, ocount, tcount, lis
    if R1C3Button in lis:
        lis.remove(R1C3Button)
    R1C3Button['state']=tk.DISABLED
    if xcount>ocount:
        R1C3Label.config(text="O")
        ocount+=1
    else:
        R1C3Label.config(text="X")
        xcount+=1
    R1C3Label.grid(row=0, column=2, pady=(10,0))
    tcount+=1
    fun()
    
def disableR2C1():
    global xcount, ocount, tcount, lis
    if R2C1Button in lis:
        lis.remove(R2C1Button)
    R2C1Button['state']=tk.DISABLED
    if xcount>ocount:
        R2C1Label.config(text="O")
        ocount+=1
    else:
        R2C1Label.config(text="X")
        xcount+=1
    R2C1Label.grid(row=1, column=0, padx=(10,0))
    tcount+=1
    fun()
    
def disableR2C2():
    global xcount, ocount, tcount, lis
    if R2C2Button in lis:
        lis.remove(R2C2Button)
    R2C2Button['state']=tk.DISABLED
    if xcount>ocount:
        R2C2Label.config(text="O")
        ocount+=1
    else:
        R2C2Label.config(text="X")
        xcount+=1
    R2C2Label.grid(row=1, column=1)
    tcount+=1
    fun()
    
def disableR2C3():
    global xcount, ocount, tcount, lis
    if R2C3Button in lis:
        lis.remove(R2C3Button)
    R2C3Button['state']=tk.DISABLED
    if xcount>ocount:
        R2C3Label.config(text="O")
        ocount+=1
    else:
        R2C3Label.config(text="X")
        xcount+=1
    R2C3Label.grid(row=1, column=2)
    tcount+=1
    fun()
    
def disableR3C1():
    global xcount, ocount, tcount, lis
    if R3C1Button in lis:
        lis.remove(R3C1Button)
    R3C1Button['state']=tk.DISABLED
    if xcount>ocount:
        R3C1Label.config(text="O")
        ocount+=1
    else:
        R3C1Label.config(text="X")
        xcount+=1
    R3C1Label.grid(row=2, column=0, padx=(10,0))
    tcount+=1
    fun()
    
def disableR3C2():
    global xcount, ocount, tcount, lis
    if R3C2Button in lis:
        lis.remove(R3C2Button)
    R3C2Button['state']=tk.DISABLED
    if xcount>ocount:
        R3C2Label.config(text="O")
        ocount+=1
    else:
        R3C2Label.config(text="X")
        xcount+=1
    R3C2Label.grid(row=2, column=1)
    tcount+=1
    fun()
    
def disableR3C3():
    global xcount, ocount, tcount, lis
    if R3C3Button in lis:
        lis.remove(R3C3Button)
    R3C3Button['state']=tk.DISABLED
    if xcount>ocount:
        R3C3Label.config(text="O")
        ocount+=1
    else:
        R3C3Label.config(text="X")
        xcount+=1
    R3C3Label.grid(row=2, column=2)
    tcount+=1
    fun()
    
R1C1Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR1C1)
R1C1Button.grid(row=0, column=0, padx=(10,0), pady=(10,0))
R1C1Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R1C2Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR1C2)
R1C2Button.grid(row=0, column=1, pady=(10,0))
R1C2Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R1C3Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR1C3)
R1C3Button.grid(row=0, column=2, pady=(10,0))
R1C3Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R2C1Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR2C1)
R2C1Button.grid(row=1, column=0, padx=(10,0))
R2C1Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R2C2Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR2C2)
R2C2Button.grid(row=1, column=1)
R2C2Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R2C3Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR2C3)
R2C3Button.grid(row=1, column=2)
R2C3Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R3C1Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR3C1)
R3C1Button.grid(row=2, column=0, padx=(10,0))
R3C1Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R3C2Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR3C2)
R3C2Button.grid(row=2, column=1)
R3C2Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

R3C3Button=tk.Button(root, text="", bg="#ff0000", padx=25, pady=10, bd=1, relief="solid", command=disableR3C3)
R3C3Button.grid(row=2, column=2)
R3C3Label=tk.Label(root, text="", bg="#00ff00", font=("Arial", 15, "bold"), padx=18, pady=6)

ResetButton=tk.Button(root, text="Reset", command=reset)
ResetButton.grid(row=3, column=0, columnspan=3, pady=10)

ResultLabel=tk.Label(root, text="")
ResultLabel.grid(row=4, column=0, columnspan=3)

lis=[R1C1Button, R1C2Button, R1C3Button, R2C1Button, R2C2Button, R2C3Button, R3C1Button, R3C2Button, R3C3Button]

def clickR1C1(event):
    global xcount, ocount, tcount, lis
    if R1C1Button['state']==tk.NORMAL:
        if R1C1Button in lis:
            lis.remove(R1C1Button)
        if xcount>ocount:
            R1C1Label.config(text="O")
            ocount+=1
        else:
            R1C1Label.config(text="X")
            xcount+=1
        R1C1Label.grid(row=0, column=0, padx=(10,0), pady=(10,0))
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R1C1Button['state']=tk.DISABLED

def clickR1C2(event):
    global xcount, ocount, tcount, lis
    if R1C2Button['state']==tk.NORMAL:
        if R1C2Button in lis:
            lis.remove(R1C2Button)
        if xcount>ocount:
            R1C2Label.config(text="O")
            ocount+=1
        else:
            R1C2Label.config(text="X")
            xcount+=1
        R1C2Label.grid(row=0, column=1, pady=(10,0))
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R1C2Button['state']=tk.DISABLED

def clickR1C3(event):
    global xcount, ocount, tcount, lis
    if R1C3Button['state']==tk.NORMAL:
        if R1C3Button in lis:
            lis.remove(R1C3Button)
        if xcount>ocount:
            R1C3Label.config(text="O")
            ocount+=1
        else:
            R1C3Label.config(text="X")
            xcount+=1
        R1C3Label.grid(row=0, column=2, pady=(10,0))
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R1C3Button['state']=tk.DISABLED

def clickR2C1(event):
    global xcount, ocount, tcount, lis
    if R2C1Button['state']==tk.NORMAL:
        if R2C1Button in lis:
            lis.remove(R2C1Button)
        if xcount>ocount:
            R2C1Label.config(text="O")
            ocount+=1
        else:
            R2C1Label.config(text="X")
            xcount+=1
        R2C1Label.grid(row=1, column=0, padx=(10,0))
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R2C1Button['state']=tk.DISABLED

def clickR2C2(event):
    global xcount, ocount, tcount, lis
    if R2C2Button['state']==tk.NORMAL:
        if R2C2Button in lis:
            lis.remove(R2C2Button)
        if xcount>ocount:
            R2C2Label.config(text="O")
            ocount+=1
        else:
            R2C2Label.config(text="X")
            xcount+=1
        R2C2Label.grid(row=1, column=1)
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R2C2Button['state']=tk.DISABLED

def clickR2C3(event):
    global xcount, ocount, tcount, lis
    if R2C3Button['state']==tk.NORMAL:
        if R2C3Button in lis:
            lis.remove(R2C3Button)
        if xcount>ocount:
            R2C3Label.config(text="O")
            ocount+=1
        else:
            R2C3Label.config(text="X")
            xcount+=1
        R2C3Label.grid(row=1, column=2)
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R2C3Button['state']=tk.DISABLED

def clickR3C1(event):
    global xcount, ocount, tcount, lis
    if R3C1Button['state']==tk.NORMAL:
        if R3C1Button in lis:
            lis.remove(R3C1Button)
        if xcount>ocount:
            R3C1Label.config(text="O")
            ocount+=1
        else:
            R3C1Label.config(text="X")
            xcount+=1
        R3C1Label.grid(row=2, column=0, padx=(10,0))
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C2Button: disableR3C2()
            elif a==R3C3Button: disableR3C3()
    R3C1Button['state']=tk.DISABLED

def clickR3C2(event):
    global xcount, ocount, tcount, lis
    if R3C2Button['state']==tk.NORMAL:
        if R3C2Button in lis:
            lis.remove(R3C2Button)
        if xcount>ocount:
            R3C2Label.config(text="O")
            ocount+=1
        else:
            R3C2Label.config(text="X")
            xcount+=1
        R3C2Label.grid(row=2, column=1)
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C3Button: disableR3C3()
    R3C2Button['state']=tk.DISABLED

def clickR3C3(event):
    global xcount, ocount, tcount, lis
    if R3C3Button['state']==tk.NORMAL:
        if R3C3Button in lis:
            lis.remove(R3C3Button)
        if xcount>ocount:
            R3C3Label.config(text="O")
            ocount+=1
        else:
            R3C3Label.config(text="X")
            xcount+=1
        R3C3Label.grid(row=2, column=2)
        tcount+=1
        fun()
        if len(lis)!=0:
            a=random.choice(lis)
            if a==R1C1Button: disableR1C1()
            elif a==R1C2Button: disableR1C2()
            elif a==R1C3Button: disableR1C3()
            elif a==R2C1Button: disableR2C1()
            elif a==R2C2Button: disableR2C2()
            elif a==R2C3Button: disableR2C3()
            elif a==R3C1Button: disableR3C1()
            elif a==R3C2Button: disableR3C2()
    R3C3Button['state']=tk.DISABLED

R1C1Button.bind('<Button-1>', clickR1C1)
R1C2Button.bind('<Button-1>', clickR1C2)
R1C3Button.bind('<Button-1>', clickR1C3)
R2C1Button.bind('<Button-1>', clickR2C1)
R2C2Button.bind('<Button-1>', clickR2C2)
R2C3Button.bind('<Button-1>', clickR2C3)
R3C1Button.bind('<Button-1>', clickR3C1)
R3C2Button.bind('<Button-1>', clickR3C2)
R3C3Button.bind('<Button-1>', clickR3C3)

root.mainloop()