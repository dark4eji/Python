import os
from tkinter import Button, E, font, INSERT
from tkinter.filedialog import askopenfilename


class Image:
    def __init__(self, parent, textbox, root):
        self.parent = parent
        self.textbox = textbox
        self.segoe = font.Font(family='Segoe UI', size=8)
        self.insert_but = Button(parent, text='Insert Image', width=11, font=self.segoe)
        self.insert_inline = Button(parent, text='Insert Inline Image', width=16, font=self.segoe)
        self.insert_but.grid(column=5, row=1, sticky=E, padx=2)
        self.insert_but.bind("<ButtonRelease-1>", self.image_insert)
        root.bind("<Control-KeyPress-q>", self.image_insert)

        self.insert_inline.grid(column=6, row=1, sticky=E, padx=2)
        self.insert_inline.bind("<ButtonRelease-1>", self.image_insert_inline)
        root.bind("<Control-KeyPress-w>", self.image_insert_inline)


    def image_insert(self, event):
        self.image_path = askopenfilename(filetypes=[('*.png file', '*.png'), ('*.svg file', '*.svg')])
        self.cursor = self.textbox.index(INSERT)
        self.include = "include::img\\" + os.path.basename(os.path.normpath(self.image_path)) + "[align=center]\n"
        self.textbox.insert(self.cursor, self.include)

    def image_insert_inline(self, event):
        self.image_path_inline = askopenfilename(filetypes=[('*.png file', '*.png'), ('*.svg file', '*.svg')])
        self.cursor = self.textbox.index(INSERT)
        self.include = "include:img\\" + os.path.basename(os.path.normpath(self.image_path_inline)) + "[]"
        self.textbox.insert(self.cursor, self.include)

