from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Student registration for TA IT Training ")
window.geometry('400x400')
window.configure(background = "grey");
a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Middle Name").grid(row = 1,column = 0)
c = Label(window ,text = "Last Name").grid(row = 2,column = 0)
d = Label(window ,text = "Email Id").grid(row = 3,column = 0)
e = Label(window ,text = "Contact Number").grid(row = 4,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=5,column=0)
window.mainloop()
