import tkinter as tk
from tkinter import *

window = tk.Tk()
te = "hello world"
frame = tk.Frame(master=window, width=100, height=1)
frame.pack()

def get_text():
    s = text.get(1.0, END)
    text['text'] = s

yen = tk.Entry().pack(ipadx=50 ,ipady=20,)
#yk = yen.get
yen2 = tk.Entry().pack(ipadx= 50 ,ipady=20,)
Button(frame, text="save",
       command=get_text).pack(ipadx=100, ipady=20,side=LEFT)

be2 = tk.Button(text= "del").pack(ipadx=100, ipady=20)
#adg = tk.Entry.get()
text = Text(width=28, height=10)
text.pack(side=LEFT)
text.insert('1.0',te)

window.mainloop()

