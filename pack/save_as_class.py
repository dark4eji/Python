from tkinter.filedialog import asksaveasfilename


class SaveAs:
    def __init__(self, parent, text, name):
        self.text = text
        self.parent = parent
        self.name = name
        self.constructing_menu()

    def save_as(self):
        self.filepath = asksaveasfilename(filetypes=[('*.Adoc file', '*.adoc')])
        if self.filepath in '.':
            return

        with open((self.filepath + ".adoc").replace(".adoc.adoc", ".adoc"), 'w') as f:
            f.write(self.text.get_text())

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.save_as)

