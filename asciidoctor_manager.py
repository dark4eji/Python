import os
from tkinter import Tk, Frame
from pack.menu_constructor_class import MenuConstructor as Mc
from pack.full_screen_class import FullScreenApp as FSA
from pack.menu_bar.menu_bar_class import MenuBar
from pack.text_box_class import TextBox


class AM:
    def __init__(self, parent):
        self.parent = parent
        Mc(parent, TextBox)
        MenuBar(parent, TextBox.selected_text)

if __name__ == "__main__":
    root = Tk()
    AM(root)
    FSA(root)
    if not os.path.exists(os.path.join('C:', 'ProgramData', 'config.ini')):
        root.title("Asciidoctor Manager")
    root.geometry('665x700')    
    #root.attributes("-topmost", 0)
    root.configure(background='#5fb3e1')
    root.mainloop()
