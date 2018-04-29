import os
from tkinter import Tk, Frame
from pack.menu_bar.menu_constructor_class import MenuConstructor as Mc
from pack.full_screen_class import FullScreenApp as FSA
from pack.toolbar.toolbar_class import Toolbar
from pack.text_box_class import TextBox
from tkinter.ttk import Notebook

class AM:
    def __init__(self, parent):
        self.parent = parent
        self.nb = Notebook(parent)
        self.text_box_frame = Frame(self.nb, bd=7)
        self.text_box_frame.configure(background='#5fb3e1')
        self.text_box_frame.place(y=30, relwidth=1, relheight=0.95)

        self.new = TextBox(self.text_box_frame)
        Mc(parent, self.new, self.nb)
        Toolbar(parent, TextBox.selected_text)

        self.nb.add(self.text_box_frame, text="Editor")
        self.nb.place(y=35, relwidth=1, relheight=0.95)

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
