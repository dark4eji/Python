from tkinter import *

class Opmenu:
    def __init__(self, parent, func):
        self.func = func
        self.parent = parent

        self.menubar = Menu(parent)
        self.opmenu = Menu(self.menubar, tearoff=0)
        self.constructing_menu()
        self.placing_elements()

    def constructing_menu(self):
        self.opmenu.add_command(label="Publish", command=self.invoking_pub)

        self.menubar.add_cascade(label="Actions", menu=self.opmenu)

    def placing_elements(self):
        self.parent.config(menu=self.menubar)

    def invoking_pub(self):
            self.filewin = Toplevel(self.parent)
            self.filewin.focus_force()
            self.filewin.title("Publisher")
            self.filewin.resizable(width=False, height=False)
            self.func(self.filewin)