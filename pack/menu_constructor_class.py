from tkinter.filedialog import *
from pack.operations_menu_class import OperationsMenu as Om
from pack.open_project_class import OpenProject as Op
from pack.publisher_class import Publisher
from pack.renamer_class import Renamer
from pack.creator_class import Creator
from pack.open_file_class import OpenFile
from pack.text_box_class import TextBox
from pack.save_as_class import SaveAs
from pack.func_pack import config_writer, config_retriever

class MenuConstructor():
    """Class that constructs menu bar"""
    def __init__(self, parent):
        self.Tb = TextBox(parent)
        self.parent = parent
        self.rootbar = Menu(parent, tearoff=0)
        self.actionmenu = Menu(self.rootbar, tearoff=0)
        self.filemenu = Menu(self.rootbar, tearoff=0)
        self.parent.config(menu=self.rootbar)

        self.cascade_adding()
        self.constructor()
        Op.project_path = config_retriever('project_file', 'file_path')
        self.parent.title('Asciidoctor Manager' + " [" + Op.project_path + "]")

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
        self.open_file = OpenFile
        self.save_as_file = SaveAs

        self.build_pub(self.actionmenu, self.publisher, "Publish")
        self.build_cr(self.actionmenu, self.creator, "Create Topic")
        self.build_ren(self.actionmenu, self.renamer, "Rename Topics")
        self.open_project(self.filemenu, self.parent, "Open Project")
        self.open_file(self.filemenu, self.Tb, "Open Topic File")
        self.save_as_file(self.filemenu, self.Tb, "Save As")

