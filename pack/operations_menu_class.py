from tkinter import Toplevel
from pack import open_project_class

class OperationsMenu:
    """Generates Actions menu with cascades"""
    def __init__(self, parent, class_, name):
        self.class_ = class_
        self.name = name
        self.parent = parent
        self.constructing_menu()

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.invoking_pub)

    def creating_toplevel(self, menu, name):
        """Generates top-level windows"""
        self.filewin = Toplevel(menu)
        self.filewin.focus_force()
        self.filewin.grab_set()
        self.filewin.title(name)
        self.filewin.resizable(width=False, height=False)
        self.class_(self.filewin, open_project_class.OpenProject.secured_project_path)

    def invoking_pub(self):
        """Translates class to the top-level window"""
        self.creating_toplevel(self.parent, self.name)
