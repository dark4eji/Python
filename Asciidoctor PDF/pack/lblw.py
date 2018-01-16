from tkinter import *


class LabelW:
    def __init__(self, parent):
        self.parent = parent
        self.label1 = Label(self.parent,
                            text="Path to the project file:")
        self.label2 = Label(self.parent,
                            text="Path to the template file:")
        self.label3 = Label(self.parent,
                            text="Path to the fonts folder:")
        self.label4 = Label(self.parent,
                            text="Output folder:")

        self.label_placing()

    def label_placing(self):

        self.label1.grid(column=1, row=1, pady=5, padx=10, sticky=W)
        self.label2.grid(column=1, row=2, pady=5, padx=10, sticky=W)
        self.label3.grid(column=1, row=3, pady=5, padx=10, sticky=W)
        self.label4.grid(column=1, row=4, pady=5, padx=10, sticky=W)