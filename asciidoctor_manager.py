from tkinter import *
from pack.menu_constructor_class import MenuConstructor as Mc
from pack.full_screen_class import FullScreenApp as FSA


class AM:
    def __init__(self, parent):
        self.parent = parent
        Mc(parent)


if __name__ == "__main__":
    root = Tk()
    AM(root)
    FSA(root)
    root.geometry('620x780')
    #  root.resizable(width=False, height=False)
    root.attributes("-topmost", 0)
    root.mainloop()
