from tkinter import *
from pack import publisher as pub
from pack import project_menu as a_m
from pack import creator as cr
from pack import renamer as rr

root = Tk()

# -------------
# Menu bar
rootbar = Menu(root, tearoff=0)
actionmenu = Menu(rootbar, tearoff=0)
rootbar.add_cascade(label="Project", menu=actionmenu)

publisher = pub.Publisher
creator = cr.Creator
renamer = rr.Renamer

project_menu_interface = a_m.ProjectMenu

project_menu_interface(actionmenu, publisher, "Publish Project")
project_menu_interface(actionmenu, creator, "Create Topic")
project_menu_interface(actionmenu, renamer, "Rename Topic")
# -------------

root.config(menu=rootbar)
root.title('Asciidoctor Manager')
root.geometry('550x426')
root.resizable(width=False, height=False)
root.attributes("-topmost", 0)
root.mainloop()
