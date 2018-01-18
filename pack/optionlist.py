from tkinter import *


class Optionlist:
    """Class is used for constructing option lists in main file"""
    leveloffset = "No leveloffset"
    delim_replacer = "_"

    def __init__(self, frame1):

            self.lvloffsetvar = StringVar()
            self.delimvar = StringVar()

            self.lvloffsetvar.set("No leveloffset")
            self.delimvar.set("Default")

            self.lvloffsetlistval = ["No leveloffset", "+1", "+2", "+3", "-1", "-2", "-3", "0", "1", "2", "3", "4", "5"]
            self.delimlistval = ["Default", "Space", "Dash"]

            self.lvloffsetlist = OptionMenu(frame1,
                                            self.lvloffsetvar,
                                            *self.lvloffsetlistval,
                                            command=self.get_leveloffset)

            self.delimlist = OptionMenu(frame1,
                                        self.delimvar,
                                        *self.delimlistval,
                                        command=self.get_delim_to_replace)

            self.optionlist_placing()

    def get_leveloffset(self, event):
        Optionlist.leveloffset = self.lvloffsetvar.get()

    def get_delim_to_replace(self, event):

        if self.delimvar.get() in "Default":
            Optionlist.delim_replacer = "_"

        elif self.delimvar.get() in "Space":
            Optionlist.delim_replacer = " "

        elif self.delimvar.get() in "Dash":
            Optionlist.delim_replacer = "-"

    def optionlist_placing(self):

        self.lvloffsetlist.place(x=90, y=41)
        self.delimlist.grid(column=3, row=6, padx=8, sticky=E)