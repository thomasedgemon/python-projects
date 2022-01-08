from tkinter import *
import tkinter as tk

global expression
global equation

equation = StringVar()
expression = ""

def press(num):
    
    global expression
 
    expression = expression + str(num)

    equation.set(num)

def equalpress():
    global expression
    global equation
    total = str(eval(expression))
 
    equation.set(total)
 
    expression = ""

def clear():
    global expression

    expression = ""

    equation.set("")
   


#initialize GUI window
root = Tk()
title = Label(root, text="Calculator")
title.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
root.geometry('300x300')

result = ()
#initialize buttons
addition_button = Button(topFrame, text="add", command=lambda: press("+"))
subtraction_button = Button(topFrame, text="subtract", command=lambda: press("-"))
multiplication_button = Button(topFrame, text="multiply", command=lambda: press("x"))
division_button = Button(topFrame, text="divide", command=lambda: press("/"))
clear_button = Button(topFrame, text="clear", commmand=clear)
equal = Button(topFrame, text="enter", command=equalpress)
zero_button = Button(topFrame, text="0")
one_button = Button(topFrame, text="1")
two_button = Button(topFrame, text="2")
three_button = Button(topFrame, text="3")
four_button = Button(topFrame, text="4")
five_button = Button(topFrame, text="5")
six_button = Button(topFrame, text="6")
seven_button = Button(topFrame, text="7")
eight_button = Button(topFrame, text="8")
nine_button = Button(topFrame, text="9")
expression_field = Entry(topFrame, textvariable=result)

#place buttons on GUI
addition_button.grid(column=3)
subtraction_button.grid(column=3)
multiplication_button.grid(column=3)
division_button.grid(column=3)
#clear_button.grid(column=3)
equal.grid(column=3)
zero_button.grid(column=0, row=0)
one_button.grid(column=0, row=1)
two_button.grid(column=0, row=2)
three_button.grid(column=0, row=3)
four_button.grid(column=1, row=1)
five_button.grid(column=1, row=2)
six_button.grid(column=1, row=3)
seven_button.grid(column=2, row=1)
eight_button.grid(column=2, row=2)
nine_button.grid(column=2, row=3)


root.mainloop()