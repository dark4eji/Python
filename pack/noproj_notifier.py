from tkinter import messagebox
from tkinter.filedialog import *

def noproj_notifier(project_path, parent):
    if project_path is None:
        messagebox.showwarning("No Project File", "Specify path to the project "
                                                  "file in the File → Open Project menu")
        parent.destroy()
    else:
        pass
