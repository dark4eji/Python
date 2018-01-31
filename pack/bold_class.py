"""
The module contains class that is used to make the selected text bold
"""

from tkinter import Button, W, E


class Bold:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.bold_but = Button(parent, text='Bold', command=name)
        self.bold_but.grid(column=1, row=1, sticky=W)