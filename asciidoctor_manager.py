from tkinter import *
from pack import publisher_class as pub
from pack import menu_builder_class as a_m
from pack import creator_class as cr
from pack import renamer_class as rr
from pack import file_menu as fm
from pack import save_as as sa
import os
import pickle
root = Tk()

# scrollbar = Scrollbar(root)
# text_box = Text(root, yscrollcommand=scrollbar.set)
# scrollbar.config(command=text_box.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# text_box.pack(side=LEFT, fill=BOTH)

# -------------
# Menu bar
rootbar = Menu(root, tearoff=0)

actionmenu = Menu(rootbar, tearoff=0)
filemenu = Menu(rootbar, tearoff=0)

rootbar.add_cascade(label="File", menu=filemenu)
rootbar.add_cascade(label="Operations", menu=actionmenu)

publisher = pub.Publisher
creator = cr.Creator
renamer = rr.Renamer

saveas = sa.SaveAs
file_menu = fm.FileMenuBuilder


file_menu(filemenu, "Open Project", root)

operations_menu_interface = a_m.MenuBuilder

operations_menu_interface(actionmenu, publisher, "Publish")
operations_menu_interface(actionmenu, creator, "Create Topic")
operations_menu_interface(actionmenu, renamer, "Rename Topic")
# -------------

root.config(menu=rootbar)
root.title('Asciidoctor Manager')
root.geometry('550x426')
root.resizable(width=False, height=False)
root.attributes("-topmost", 0)
root.mainloop()
