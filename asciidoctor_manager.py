import os
from tkinter import Tk, Frame
from pack.menu_constructor_class import MenuConstructor as Mc
from pack.full_screen_class import FullScreenApp as FSA



class AM:
    def __init__(self, parent):
        self.parent = parent
        Mc(parent)
        self.newasas = Frame(parent, bd=10)
        self.newasas.grid(column=4, row=2, columnspan=2, rowspan=2)

if __name__ == "__main__":
    root = Tk()
    AM(root)
    FSA(root)
    if not os.path.exists(os.path.join('C:', 'ProgramData', 'config.ini')):
        root.title("Asciidoctor Manager")
    root.geometry('760x600')
    #root.resizable(width=False, height=False)
    root.attributes("-topmost", 0)
    root.mainloop()
