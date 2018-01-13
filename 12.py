from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk


root = Tk()


p = PanedWindow(root, orient=VERTICAL)

f1 = LabelFrame(p, text='Adding Topics', width=500, height=100)
f2 = LabelFrame(p, text='Renaming Topics', width=100, height=100)
p.add(f1)
p.add(f2)




label1 = Label(root,
               text="Project file path:")

label2 = Label(f1,
               text="Enter name of a topic:")

btn1 = Button(root,
              text="...",
              width=3,
              height=1)


btn2 = Button(f1,
              text="Add",
              width=5,
              height=1)

entry1 = Entry(root,
               width=40,
               bd=3)

entry2 = Entry(f1,
               width=40,
               bd=3)


var = IntVar()
var.set(1)

rad0 = Radiobutton(f1,
                   text="Reference topic (UI)",
                   variable=var,
                   value=0)

rad1 = Radiobutton(f1,
                   text="Procedure topic (INS)",
                   variable=var,
                   value=1)

rad2 = Radiobutton(f1,
                   text="Custom topic",
                   variable=var,
                   value=2)

top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)

label1.grid(column=1, row=1, pady = 25, padx=10, sticky=W)
label2.grid(column=1, row=8, pady = 25, padx=10, sticky=NW)

entry1.grid(column=2, row=1)
entry2.grid(column=2, row=8)

btn1.grid(column=3, row=1, padx=10)
btn2.grid(column=4, row=8, padx=10, sticky=E)

rad0.grid(column=1, row=5, padx=10, sticky=W)
rad1.grid(column=2, row=5, sticky=W)
rad2.grid(column=2, row=5, columnspan=2, sticky=E)
p.place(x=10, y=80)
root.geometry('800x640')
root.mainloop()
