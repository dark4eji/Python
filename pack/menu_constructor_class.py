from tkinter.filedialog import *
from pack.operations_menu_class import OperationsMenu as Om
from pack.open_project_class import OpenProject as Op
from pack.publisher_class import Publisher
from pack.renamer_class import Renamer
from pack.creator_class import Creator


class MenuConstructor():
    """Class that constructs menu bar"""
    def __init__(self, parent):
        self.parent = parent
        self.rootbar = Menu(parent, tearoff=0)
        self.actionmenu = Menu(self.rootbar, tearoff=0)
        self.filemenu = Menu(self.rootbar, tearoff=0)
        self.parent.config(menu=self.rootbar)

        self.cascade_adding()
        self.constructor()

    def cascade_adding(self):
        """Used for adding menus to the menu bar. The title for a new menu pack should be added here"""
        self.rootbar.add_cascade(label="File", menu=self.filemenu)
        self.rootbar.add_cascade(label="Operations", menu=self.actionmenu)

    def constructor(self):
        """Menus constructor"""
        self.renamer = Renamer
        self.publisher = Publisher
        self.creator = Creator

        self.build_pub = Om
        self.build_ren = Om
        self.build_cr = Om
        self.open_project = Op

        self.build_pub(self.actionmenu, self.publisher, "Publish")
        self.build_cr(self.actionmenu, self.creator, "Create Topic")
        self.build_ren(self.actionmenu, self.renamer, "Rename Topics")
        self.open_project(self.filemenu, self.parent, "Open Project")
