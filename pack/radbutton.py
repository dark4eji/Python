from tkinter import *


class Radbuttons:
    """Class is used for constructing radio buttons in main file"""
    prefix = "INS "
    def __init__(self, frame1):

            self.var = IntVar()
            self.var.set(1)
            self.rad1 = Radiobutton(frame1,
                               text="Reference topic (UI)",
                               variable=self.var,
                               value=0,
                               command=self.get_prefix)

            self.rad2 = Radiobutton(frame1,
                               text="Procedure topic (INS)",
                               variable=self.var,
                               value=1,
                               command=self.get_prefix)

            self.rad3 = Radiobutton(frame1,
                               text="Custom topic",
                               variable=self.var,
                               value=2,
                               command=self.get_prefix)

            self.radbutton_placing()

    def get_prefix(self):
        """Forms prefix for topics type"""
        if self.var.get() == 0:
            print(self.var.get())
            Radbuttons.prefix = "UI "

        elif self.var.get() == 1:
            Radbuttons.prefix = "INS "

        elif self.var.get() == 2:
            Radbuttons.prefix = ""

    def radbutton_placing(self):
        """Places radio buttons on root"""
        self.rad1.grid(column=1, row=5, padx=10, pady=5, sticky=W)
        self.rad2.grid(column=2, row=5, padx=10, sticky=W)
        self.rad3.place(x=350, y=5)