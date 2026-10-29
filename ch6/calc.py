import tkinter
from tkinter import *
a = Tk()
a.title("Calculator")
a.geometry("358x610")
BG="#445757"
a.config(bg=BG)

FONT = "Elephant 10 bold"

l = Label(text="Standard",font=FONT,fg="white",bg=BG).place(x=100,y=30)

l1 = Label(text="Enter first number",font=FONT,fg="white",bg=BG).place(x=30,y=150)
e1 = Entry(font=FONT,width=10)
e1.place(x=200,y=150)
l2 = Label(text="Enter second number",font=FONT,fg="white",bg=BG).place(x=30,y=200)
e2 = Entry(font=FONT,width=10)
e2.place(x=200,y=200)


def add():
    op1 =  float(e1.get())
    op2 =  float(e2.get())
    op.delete(1.0,END)
    res = op1+op2
    op.insert(END,f"\nAddition Result= {res}")

def subtract():
    op1 =  float(e1.get())
    op2 =  float(e2.get())
    op.delete(1.0,END)
    
    res = op1-op2
    op.insert(END,f"\nSubstraction Result= {res}")
def multiply():
    op1 =  float(e1.get())
    op2 =  float(e2.get())
    op.delete(1.0,END)
    res = op1*op2
    op.insert(END,f"\nMultiplication Result= {res}")
        
def divide():
    op1 =  float(e1.get())
    op2 =  float(e2.get())
    op.delete(1.0,END)

    try:
        res = op1/op2
        op.insert(END,f"\nDivision Result= {res}")
    except ZeroDivisionError as e:
        res="division by zero"
        op.insert(END,res)
    

BTNWIDTH = 2
addBtn = Button(text="+", font=FONT, width=BTNWIDTH , command=add,).place(x=50,y=250)
subBtn = Button(text="-", font=FONT, width=BTNWIDTH , command=subtract).place(x=100,y=250)
multiplyBtn = Button(text="x", font=FONT, width=BTNWIDTH , command=multiply).place(x=150,y=250)
divideBtn = Button(text="/", font=FONT, width=BTNWIDTH , command=divide).place(x=200,y=250)




op = Text(height=10,width=20,font=FONT,name="geeg")
op.place(x=50,y=300)

mainloop()
