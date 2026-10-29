import tkinter
from tkinter import *
o = Tk()
o.title("krupanidhi College")
o.geometry("500x500")
l1 = Label(o,text="Welcome to my home")
l1.pack()

l2 = Label(text="HI THERE")

def hello():
    print("hello")
    l2.pack()




b1 = Button(o,text="hit me",command=hello)
b1.pack()
b2= Button(o,text="quit",command=o.quit)
b2.pack()

b3=Button(o,text="destroy",command=o.destroy)
b3.pack()

b4=Button(o,text="exit",command=exit)
b4.pack()

mainloop()
