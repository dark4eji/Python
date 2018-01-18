from tkinter import *

class Panedwindow:

    def __init__(self, master):

        self.panedw1 = PanedWindow(master, orient=VERTICAL)

        self.frame1 = LabelFrame(self.panedw1, text='Creating Topics', width=500, height=100)
        self.frame2 = LabelFrame(self.panedw1, text='Renaming Topics', width=100, height=100)

        self.panedw1.add(self.frame1)
        self.panedw1.add(self.frame2)

        self.panedw1.place(x=10, y=100)

    def get_frame1(self):
        return self.frame1

    def get_frame2(self):
        return self.frame2
