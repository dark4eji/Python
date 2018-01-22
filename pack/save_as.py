from tkinter.filedialog import *


class SaveAs:

    def __init__(self, parent, name, text):
        self.name = name
        self.text = text
        self.parent = parent
        self.constructing_menu()

    def saving(self):
        self.path = asksaveasfilename(filetypes=[('*.Adoc file', '.adoc')])
        with open(self.path + ".adoc", 'w') as wri:
            wri.write(self.text)

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.saving)
