"""
The module consists of the one MenuConstructor class and
is used for constructing the whole menu bar of the root window.

For additional information see class and methods docstrings.
"""
import os
from tkinter import Menu, Frame, NW
from pack.operations_menu_class import OperationsMenu
from pack.open_project_class import OpenProject
from pack.publisher_class import Publisher
from pack.renamer_class import Renamer
from pack.creator_class import Creator
from pack.open_file_class import OpenFile
from pack.text_box_class import TextBox
from pack.save_as_class import SaveAs
from pack.func_pack import config_retriever
from pack.text_transformers import Bold, Italic, Regular


class MenuConstructor:
    #textbox_window = TextBox
    """Class that constructs menu bar"""
    def __init__(self, parent):
        self.parent = parent
        self.rootbar = Menu(parent, tearoff=0)  # builds the whole menu bar
        self.actionmenu = Menu(self.rootbar, tearoff=0)  # builds "Operations" menu
        self.filemenu = Menu(self.rootbar, tearoff=0)  # builds "File" menu
        self.parent.config(menu=self.rootbar)

        self.text_box_frame = Frame(parent, bd=10)
        self.formatting = Frame(parent, bd=3)

        self.text_box_frame.grid(column=1, row=2, columnspan=2, rowspan=2)
        self.formatting.grid(column=1, row=1, sticky=NW, columnspan=4)
        self.text = TextBox(self.text_box_frame)

        Bold(self.formatting, TextBox.selected_text, parent)
        Italic(self.formatting, TextBox.selected_text, parent)
        Regular(self.formatting, TextBox.selected_text, parent)

        self.cascade_adding()
        self.constructor()
        if os.path.exists(os.path.join('C:', 'ProgramData', 'config.ini')):
            OpenProject.secured_project_path = config_retriever('project_file', 'file_path')
            self.parent.title('Asciidoctor Manager' + " [" + OpenProject.secured_project_path + "]")

    def cascade_adding(self):
        """Used for adding menus to the menu bar.
        The title for a new menu pack should be added here"""
        self.rootbar.add_cascade(label="File", menu=self.filemenu)
        self.rootbar.add_cascade(label="Operations", menu=self.actionmenu)

    def constructor(self):
        """Menus constructor"""
        self.build_pub = OperationsMenu
        self.build_ren = OperationsMenu
        self.build_cr = OperationsMenu
        self.open_project = OpenProject
        self.open_file = OpenFile
        self.save_as_file = SaveAs

        self.build_pub(self.actionmenu, Publisher, "Publish")
        self.build_cr(self.actionmenu, Creator, "Create Topic")
        self.build_ren(self.actionmenu, Renamer, "Rename Topics")

        OpenProject(self.filemenu, self.parent, "Open Project")
        OpenFile(self.filemenu, self.text, "Open Topic File")
        SaveAs(self.filemenu, self.text, "Save As")
