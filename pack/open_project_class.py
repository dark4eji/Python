"""
The class represents an Open Project menu that
determines what 'project file' should be published
"""

from tkinter.filedialog import *
from pack.func_pack import config_writer


class OpenProject:
    project_path = None
    secured_project_path = None

    def __init__(self, parent, root, name):
        self.root = root
        self.name = name
        self.parent = parent
        self.check = None
        self.constructing_menu()

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_projpath)

    def get_projpath(self):
        """Used for specifying a path to the project file"""
        OpenProject.project_path = os.path.normpath(askopenfilename(filetype=[('Adoc file', '*.adoc')]))
        if OpenProject.project_path in '.':
            OpenProject.project_path = None
            return
        OpenProject.secured_project_path = OpenProject.project_path
        config_writer('project_file', 'file_path', OpenProject.secured_project_path)
        self.root_title(OpenProject.secured_project_path)

    def root_title(self, path):
        """Constructs root title"""
        self.root.title('Asciidoctor Manager' + " [" + path + "]")
