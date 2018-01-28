from tkinter.filedialog import *

class OpenFile:
    def __init__(self, parent, text, name):
        self.text = text
        self.parent = parent
        self.name = name
        self.constructing_menu()

    def get_file(self):
        """Used for specifying a path to the project file"""
        self.filepath = askopenfilename(filetype=[('Adoc file', '*.adoc')])
        self.text.insert_text(self.filepath)

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_file)
