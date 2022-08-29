import tkinter as tk
import string
from tkinter import *
from tkinter import scrolledtext
import random


parent = tk.Tk()

#noc = tk.IntVar()
#code_len = tk.IntVar()
global noc
    
tiento = Label(parent, text="Tiền tố:").grid(row = 0, column = 0)
e1 = Entry(parent)
e1.grid(row = 0, column = 1)
sl = Label(parent, text = "Số lượng code:").grid(row = 1, column = 0)
e2 = Entry(parent)
e2.grid(row = 1, column = 1)

output = Text(parent,width=20,height=10)
output.grid(row=6, column = 1)

def code_gen():
    prefix = e1.get()
    noc = e2.get()

    chars = string.ascii_uppercase+string.digits

    for i in range(int(noc)):
        code = ''.join(prefix)

        for j in range(1, 15):
            code = code+random.choice(chars)
            
    output.insert('1.0', code)

gen = Button(parent, text = "Sinh code", command = code_gen).grid(row = 4, column = 1)

parent.mainloop()


    
