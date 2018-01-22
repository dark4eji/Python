from tkinter import *


class Editor:

    def __init__(self, parent):
        self.parent = parent
        self.scrollbar = Scrollbar(parent)
        self.text_box = Text(parent, yscrollcommand=self.scrollbar.set)
        self.elements_placing()
        self.scrollbar.config(command=self.text_box.yview)

    def get_text(self):
        return 1+1
        # print(self.text_box.get(END))
        # print("assasd")

    def elements_placing(self):
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text_box.pack(side=LEFT, fill=BOTH)

