from tkinter import Frame, NW
from pack.toolbar.text_transformers import Bold, Italic, Regular
from pack.toolbar.image_insert_class import Image


class Toolbar:
    def __init__(self, parent, textbox):
        self.parent = parent
        self.textbox = textbox
        self.formatting = Frame(self.parent, bd=3)        
        self.formatting.configure(background='#5fb3e1')
        self.formatting.place(x=5, y=4)

        self.image = Frame(self.parent, bd=3)
        self.image.configure(background='#5fb3e1')
        self.image.place(x=130, y=4)

        
        Bold(self.formatting, textbox, parent)
        Italic(self.formatting, textbox, parent)
        Regular(self.formatting, textbox, parent)

        Image(self.image, textbox, parent)
    
