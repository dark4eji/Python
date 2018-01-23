from tkinter import *
from pack.menu_constructor_class import MenuConstructor as Mc

import os
import pickle
# scrollbar = Scrollbar(root)
# text_box = Text(root, yscrollcommand=scrollbar.set)
# scrollbar.config(command=text_box.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# text_box.pack(side=LEFT, fill=BOTH)

# -------------
class AM():
    def __init__(self, parent):
        self.parent = parent
        Mc(parent)


if __name__ == "__main__":
    root = Tk()
    AM(root)
    root.title('Asciidoctor Manager')
    root.geometry('550x426')
    root.resizable(width=False, height=False)
    root.attributes("-topmost", 0)
    root.mainloop()