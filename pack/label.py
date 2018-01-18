from tkinter import *


class Labels:

    def __init__(self, main, frame1, frame2):

        self.main = main
        self.frame1 = frame1
        self.frame2 = frame2

        self.label1 = Label(self.main,
                       text="Project file path:")

        self.label2 = Label(self.main,
                          text="Topic folder path (if not in project folder):")

        self.label3 = Label(self.frame1,
                       text="Name of the topic:")

        self.label4 = Label(self.frame1,
                       text="Leveloffset:")

        self.label5 = Label(self.frame1,
                       text="Name delimiter:")

        self.label6 = Label(self.frame2,
                       text="Select topic file:")

        self.label7 = Label(self.frame2,
                       text="New topic name:")

        self.label_placing()

    def label_placing(self):
        """Places labels on root"""
        self.label1.grid(column=1, row=1, pady=10, padx=10, sticky=W)
        self.label2.grid(column=1, row=2, pady=20, padx=10, sticky=NW)

        self.label3.grid(column=1, row=7, pady=10, padx=10, sticky=W)
        self.label4.grid(column=1, row=6, pady=10, padx=10, sticky=NW)

        self.label5.grid(column=2, row=6, sticky=E)
        self.label6.grid(column=1, row=1, pady=10, padx=10, sticky=NW)

        self.label7.grid(column=1, row=2, pady=10, padx=10, sticky=NW)