"""
The module build the 'Open File' menu, allowing import file contents to
the Text Box
"""
from tkinter.filedialog import askopenfilename


class OpenFile:
    """Class is used for getting contents of the file"""
    def __init__(self, parent, text, name):
        self.text = text
        self.parent = parent
        self.name = name
        self.parent.add_command(label=self.name, command=self.get_file)
        self.filepath = None

    def get_file(self):
        """Used for specifying a path to the project file"""
        self.filepath = askopenfilename(filetype=[('Adoc file', '*.adoc')])
        self.text.insert_text(self.filepath)
