"""
The module is used for building text box in the root window
"""
from tkinter import Scrollbar, Text, RIGHT, Y, LEFT, BOTH, END, font

class TextBox:
    selected_text = None
    """The class build the text box"""
    def __init__(self, parent):
        self.Font = font.Font(family='Segoe UI', size=12)
        self.scrollbar = Scrollbar(parent)
        self.text_box = Text(parent, yscrollcommand=self.scrollbar.set, font=self.Font)
        self.scrollbar.config(command=self.text_box.yview)
        TextBox.selected_text = self.text_box
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text_box.pack(side=LEFT, fill=BOTH, expand=True)

    def get_text(self):
        return (self.text_box.get(1.0, END)).strip()

    def insert_text(self, file):
        with open(file, 'r') as file:
            self.text_box.delete(1.0, END)
            self.text_box.insert(1.0, file.read())
