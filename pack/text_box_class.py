from tkinter import *
from tkinter import font


class TextBox:
    def __init__(self, parent):
        self.Font = font.Font(family='Segoe UI', size=12)
        self.scrollbar = Scrollbar(parent)
        self.text_box = Text(parent, yscrollcommand=self.scrollbar.set, font=self.Font)
        self.scrollbar.config(command=self.text_box.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text_box.pack(side=LEFT, fill=BOTH, expand=YES)

    def get_text(self):
       return self.text_box.get(1.0, END)

    def insert_text(self, file):
        with open(file, 'r') as f:
            self.text_box.insert(1.0, f.read())
