from tkinter import Button, W, E, SEL_FIRST, SEL_LAST,\
    _tkinter, EW, font, INSERT


class Bold:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.segoe_bold = font.Font(family='Verdana', size=8, weight='bold')
        self.bold_but = Button(parent, text='B',width=2, font=self.segoe_bold)
        self.bold_but.grid(column=3, row=1, sticky=W, padx=2)
        self.bold_but.bind("<Button-1>", self.transformer)
        root.bind("<Control-KeyPress-b>", self.transformer)

    def transformer(self, event):
        try:
            self.selected_text = self.textbox.get(SEL_FIRST, SEL_LAST)
            self.ind1, self.ind2 = self.textbox.index(SEL_FIRST), self.textbox.index(SEL_LAST)
            self.selected_text_bold = self.selected_text.replace("*", "").replace("_", "")
            self.selected_text_bold = "*" + self.selected_text_bold + "*"
            self.textbox.delete(self.ind1, self.ind2)
            self.textbox.insert(self.ind1, self.selected_text_bold)
        except(TypeError, _tkinter.TclError):
            self.cursor = self.textbox.index(INSERT)
            self.textbox.insert(self.cursor, "**")


class Italic:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.segoe_italic = font.Font(family='Verdana', size=8, weight='bold', slant='italic')
        self.italic_but = Button(parent, text='I', width=2, font=self.segoe_italic)
        self.italic_but.grid(column=4, row=1, sticky=EW)
        self.italic_but.bind("<Button-1>", self.transformer)
        root.bind("<Control-KeyPress-n>", self.transformer)

    def transformer(self, event):
        try:
            self.selected_text = self.textbox.get(SEL_FIRST, SEL_LAST)
            self.ind1, self.ind2 = self.textbox.index(SEL_FIRST), self.textbox.index(SEL_LAST)
            self.selected_text_italic = self.selected_text.replace("_", "").replace("*", "")
            self.selected_text_italic = "_" + self.selected_text_italic + "_"
            self.textbox.delete(self.ind1, self.ind2)
            self.textbox.insert(self.ind1, self.selected_text_italic)
        except(TypeError, _tkinter.TclError):
            self.cursor = self.textbox.index(INSERT)
            self.textbox.insert(self.cursor, "__")


class Regular:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.segoe_regular = font.Font(family='Verdana', size=8)
        self.regular_but = Button(parent, text='R', width=2, font=self.segoe_regular)
        self.regular_but.grid(column=5, row=1, sticky=E, padx=2)
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
