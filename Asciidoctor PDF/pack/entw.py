from tkinter import *


class EntryW:

    def __init__(self, parent):

        self.entry1 = Entry(parent,
                       width=40,
                       bd=3)

        self.entry2 = Entry(parent,
                       width=40,
                       bd=3)

        self.entry3 = Entry(parent,
                       width=40,
                       bd=3)

        self.entry4 = Entry(parent,
                       width=40,
                       bd=3)

        self.entry_placing()

    def get_path_field(self, arg):
        self.entry1.insert(END, arg)

    def entry_placing(self):

        self.entry1.grid(column=2, row=1, pady=20)
        self.entry2.grid(column=2, row=2)
        self.entry3.grid(column=2, row=3, pady=20, sticky=W)
        self.entry4.grid(column=2, row=4, sticky=W)