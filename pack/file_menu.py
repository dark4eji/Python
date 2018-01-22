from tkinter.filedialog import *
import os

class FileMenuBuilder:
    project_path = None

    def __init__(self, parent, name, root):
        self.root = root
        self.name = name
        self.parent = parent
        self.constructing_menu()

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_projpath)

    def session_label(self, root):
        if FileMenuBuilder.project_path is None or FileMenuBuilder.project_path in "":
            pass
        else:
            session = Label(root, text="Current project: " + os.path.basename(FileMenuBuilder.project_path).replace(".adoc", ""))
            session.grid(column=1, row=2)

    def get_projpath(self):
        """Used for specifying a path to the project file"""
        FileMenuBuilder.project_path = askopenfilename(filetype=[('Adoc file', '*.adoc')])
        self.session_label(self.root)
