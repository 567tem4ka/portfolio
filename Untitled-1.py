from tkinter import *

sus = []

def get_text():
    s = text.get(1.0, END)
    sus.append(s)
    label['text'] = sus
    s = text2.get(1.0, END)
    sus.append(s)
    label['text'] = sus
    sus.append(" ")

def delete_text():
    sus.pop(-1)
    sus.pop(-2)
    label['text'] = sus


root = Tk()

text = Text(width=30, height=4)
text.pack()

text2 = Text(width=30, height=4)
text2.pack()

frame = Frame()
frame.pack()

Button(frame, text="save",
       command=get_text).pack(ipadx=100, ipady=20)
Button(frame, text="del",
       command=delete_text).pack(ipadx=100, ipady=20)

label = Label()
label.pack()

root.mainloop()

