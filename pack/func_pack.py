from tkinter import messagebox
from tkinter.filedialog import *


def no_project_notifier(project_path, parent):
    """Notifies a user that the project path is not specified and blocks access to the operations"""
    if project_path is None:
        messagebox.showwarning("No Project File", "Specify path to the project "
                                                  "file in the File → Open Project menu")
        parent.destroy()
    else:
        pass


def field_check(variable1, variable2):
    """Performs checking of the entry content and sips it through the conditions"""
    if variable1 in ".":
        return
    if variable1 not in ".":
        variable2.delete(0, END)
    variable2.insert(END, os.path.normpath(variable1))
