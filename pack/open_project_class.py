from tkinter.filedialog import *
import os


class OpenProject:
    project_path = None
    preserved_path = None

    def __init__(self, parent, root, name):
        self.root = root
        self.name = name
        self.parent = parent
        self.constructing_menu()
        self.check = None

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_projpath)

    def session_label(self, root):
        if OpenProject.project_path is None or OpenProject.project_path in ".":
            OpenProject.project_path = None
            return

        if self.check == 0:
            if OpenProject.project_path in ".":               
                return

        if self.check == 0:
            OpenProject.preserved_path = OpenProject.project_path
        else:
            OpenProject.preserved_path = OpenProject.project_path
            root.title('Asciidoctor Manager' + " [" + OpenProject.preserved_path + "]")

    def get_projpath(self):
        """Used for specifying a path to the project file"""
        OpenProject.project_path = os.path.normpath(askopenfilename(filetype=[('Adoc file', '*.adoc')]))
        self.session_label(self.root)
