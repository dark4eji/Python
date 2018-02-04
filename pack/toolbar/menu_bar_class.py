from tkinter import Frame, NW
from pack.menu_bar.text_transformers import Bold, Italic, Regular


class MenuBar:
    def __init__(self, parent, textbox):
        self.parent = parent
        self.textbox = textbox
        self.formatting = Frame(self.parent, bd=3)        
        self.formatting.configure(background='#5fb3e1')
        self.formatting.grid(column=1, row=1, sticky=NW)
        
        Bold(self.formatting, textbox, parent)
        Italic(self.formatting, textbox, parent)
        Regular(self.formatting, textbox, parent)
    
