import os
from tkinter import messagebox
from tkinter import END
from configparser import ConfigParser


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


def config_writer(section, key, variable):
    """Creates config.ini and writes the data"""
    config = ConfigParser()
    config.read(os.path.join('C:', 'ProgramData', 'config.ini'))
    if os.path.exists(os.path.join('C:', 'ProgramData', 'config.ini')):
       with open(os.path.join('C:', 'ProgramData', 'config.ini'), 'r') as f:
           if "[" + section + "]\n" in f:
               config.set(section, key, variable)
           else:
               config.add_section(section)
               config.set(section, key, variable)
    else:
        config.add_section(section)
        config.set(section, key, variable)

    with open(os.path.join('C:', 'ProgramData', 'config.ini'), 'w') as f:
        return config.write(f)


def config_retriever(section, key):
    """Retrieves the data from the config.ini"""
    config = ConfigParser()
    config.read(os.path.join('C:', 'ProgramData', 'config.ini'))
    with open(os.path.join('C:', 'ProgramData', 'config.ini'), 'r') as f:
        if "[" + section + "]\n" not in f:
            return ''
    return config.get(section, key)
