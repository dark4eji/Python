from tkinter.filedialog import *


class FileMenuBuilder:
    project_path = None

    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.constructing_menu()

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_projpath)

    def get_projpath(self):
        """Used for specifying a path to the project file"""
        FileMenuBuilder.project_path = askopenfilename(filetype=[('Adoc file', '*.adoc')])
