from tkinter import *
from tkinter import ttk
sus = []

def get_text():
    s = text.get()
    sus.append(s)
    s = text2.get()
    sus.append(s)
    label.insert(sus)


def delete_text():
    sus.pop(-1)
    sus.pop(-2)
    label['text'] = sus


root = Tk()

text = ttk.Entry()
text.pack(anchor=NW, padx=6, pady=6)

text2 = ttk.Entry()
text2.pack(anchor=NW, padx=6, pady=6)

frame = Frame()
frame.pack()

Button(frame, text="save",
       command=get_text).pack(ipadx=100, ipady=20)
Button(frame, text="del",
       command=delete_text).pack(ipadx=100, ipady=20)

label = Text()
label.pack()

root.mainloop()

