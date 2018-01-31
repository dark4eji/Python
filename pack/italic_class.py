from tkinter import Button, W, E

class Italic:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.bold_but = Button(parent, text='Italic', command=name)
        self.bold_but.grid(column=2, row=1, sticky=E)