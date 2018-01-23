from tkinter.filedialog import *
import os


class OpenProject:
    project_path = None

    def __init__(self, parent, root, name):
        self.root = root
        self.name = name
        self.parent = parent
        self.constructing_menu()

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_projpath)

    def session_label(self, root):
        if OpenProject.project_path is None or OpenProject.project_path in "":
            pass
        else:
            session = Label(root, text="Current project: " + os.path.basename(OpenProject.project_path).replace(".adoc", ""))
            session.grid(column=1, row=2)

    def get_projpath(self):
        """Used for specifying a path to the project file"""
        OpenProject.project_path = os.path.normpath(askopenfilename(filetype=[('Adoc file', '*.adoc')]))
        self.session_label(self.root)
