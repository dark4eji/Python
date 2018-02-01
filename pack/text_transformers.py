from tkinter import Button, W, E, SEL_FIRST, SEL_LAST, _tkinter


class Bold:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.bold_but = Button(parent, text='Bold')
        self.bold_but.grid(column=1, row=1, sticky=W)
        self.bold_but.bind("<Button-1>", self.transformer)
        root.bind("<Control-KeyPress-b>", self.transformer)

    def transformer(self, event):
        try:
            self.selected_text = self.textbox.get(SEL_FIRST, SEL_LAST)
        except(TypeError, _tkinter.TclError):
            return
        self.ind1, self.ind2 = self.textbox.index(SEL_FIRST), self.textbox.index(SEL_LAST)
        self.selected_text_bold = self.selected_text.replace("*", "").replace("_", "")
        self.selected_text_bold = "*" + self.selected_text_bold + "*"
        self.textbox.delete(self.ind1, self.ind2)
        self.textbox.insert(self.ind1, self.selected_text_bold)



class Italic:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.italic_but = Button(parent, text='Italic')
        self.italic_but.grid(column=2, row=1, sticky=E)
        self.italic_but.bind("<Button-1>", self.transformer)
        root.bind("<Control-KeyPress-n>", self.transformer)

    def transformer(self, event):
        try:
            self.selected_text = self.textbox.get(SEL_FIRST, SEL_LAST)
        except(TypeError, _tkinter.TclError):
            return
        self.ind1, self.ind2 = self.textbox.index(SEL_FIRST), self.textbox.index(SEL_LAST)
        self.selected_text_italic = self.selected_text.replace("_", "").replace("*", "")
        self.selected_text_italic = "_" + self.selected_text_italic + "_"
        self.textbox.delete(self.ind1, self.ind2)
        self.textbox.insert(self.ind1, self.selected_text_italic)


class Regular:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.regular_but = Button(parent, text='Regular')
        self.regular_but.grid(column=3, row=1, sticky=W)
        self.regular_but.bind("<Button-1>", self.transformer)
        root.bind("<Control-KeyPress-r>", self.transformer)

    def transformer(self, event):
        try:
            self.selected_text = self.textbox.get(SEL_FIRST, SEL_LAST)
        except(TypeError, _tkinter.TclError):
            return
        self.ind1, self.ind2 = self.textbox.index(SEL_FIRST), self.textbox.index(SEL_LAST)
        self.selected_text_italic = self.selected_text.replace("_", "").replace("*", "")
        self.textbox.delete(self.ind1, self.ind2)
        self.textbox.insert(self.ind1, self.selected_text_italic)