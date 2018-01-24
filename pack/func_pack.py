from tkinter import messagebox
from tkinter.filedialog import *

def no_project_notifier(project_path, parent):
    if project_path is None:
        messagebox.showwarning("No Project File", "Specify path to the project "
                                                  "file in the File → Open Project menu")
        parent.destroy()
    else:
        pass

def destroyer(obj):
    obj.destroy()