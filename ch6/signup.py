import tkinter
from tkinter import *
a = Tk()
a.title("signup form")
a.geometry("800x640")
a.config(bg="#445757")

FONT = "Elephant 20 bold"

l = Label(
    text="Sign up into your dreams..",
    font="Times 30 bold",
    fg="white",
    bg="#445757")
l.place(x=200,y=100)


l1 = Label(text="First Name",font=FONT)
l1.place(x=150,y=200)
e1 = Entry(font=FONT)
e1.place(x=230,y=200)

l2 = Label(text="email",font=FONT)
l2.place(x=150,y=230)
e2 = Entry(font=FONT)
e2.place(x=230,y=230)

l3 = Label(text="password",font=FONT)
l3.place(x=150,y=260)
e3 = Entry(font=FONT,show="`")
e3.place(x=230,y=260)

def submit():
    do()

submitButton = Button(text="Submit",font=FONT,command=submit)
submitButton.place(x=200,y=300)



def moveup():
    x_relative = l.winfo_x()
    y_relative = l.winfo_y()
 
    l.place(x=x_relative,y=y_relative-10)
def movedown():
    x_relative = l.winfo_x()
    y_relative = l.winfo_y()
 
    l.place(x=x_relative,y=y_relative+10)
    
def moveleft():
    x_relative = l.winfo_x()
    y_relative = l.winfo_y()
 
    l.place(x=x_relative-10,y=y_relative)


def moveright():
    x_relative = l.winfo_x()
    y_relative = l.winfo_y()
 
    l.place(x=x_relative+10,y=y_relative)

def do():
    for _ in range(1,10):
        movedown()




bup = Button(text="up",command=moveup)
bup.pack()
bdown = Button(text="down",command=movedown)
bdown.pack()
bleft = Button(text="left",command=moveleft)
bleft.pack()
bright = Button(text="right",command=moveright)
bright.pack()









mainloop()
