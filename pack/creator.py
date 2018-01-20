from tkinter import messagebox
from tkinter.filedialog import *


class Creator:
    def __init__(self, parent):

        self.label1 = Label(parent, text="Project file path:")
        self.label2 = Label(parent, text="Name of the topic:")
        self.label3 = Label(parent, text="Leveloffset:")
        self.label4 = Label(parent, text="Prefix:")

        self.entry1 = Entry(parent, width=45, bd=3)
        self.entry2 = Entry(parent, width=45, bd=3)
        self.entry3 = Entry(parent, width=17, bd=3)

        self.btn1 = Button(parent, text="...", width=3, height=1, command=self.get_projpath)
        self.btn2 = Button(parent, text="Create", width=5, height=1, command=self.creator)

        self.leveloffsetvar = StringVar()
        self.leveloffsetvar.set("No leveloffset")
        self.leveloffsetlistval = ["No leveloffset", "+1", "+2", "+3", "-1", "-2", "-3", "0", "1", "2", "3", "4", "5"]
        self.leveloffsetlist = OptionMenu(parent, self.leveloffsetvar, *self.leveloffsetlistval)

        self.elements_placing()

    def leveloffset(self):
        """Used to construct a text construction to write in a project file"""
        if self.leveloffsetvar.get() in "No leveloffset":
            self.path_to_topic_file = "\n//" + self.entry2.get().replace("_", " ") + "\ninclude::" + "topics\\" + self.entry3.get() + \
                                      self.topic_name + "[]"
            print(self.path_to_topic_file)
        else:
            self.path_to_topic_file = "\n//" + self.entry2.get() + "\n:leveloffset: " + self.leveloffsetvar.get() + \
                                      "\ninclude::" + "topics\\" + self.entry3.get() + \
                                      self.topic_name + "[]"
            print(self.path_to_topic_file)

    #  Creator functional parts begin
    def get_projpath(self):
        """Used for specifying a path to the project file"""
        self.entry1.delete(0, END)
        self.entry1.insert(END, askopenfilename(filetype=[('Adoc file', '*.adoc')]))

    def creator(self):
        """Used for creating topics in topics folder, adding path with leveloffset \
         to the project file and a title to the topic file"""
        self.topic_name = self.entry2.get().replace(" ", "").lower() + ".adoc"

        if self.entry1.get() in "":  # Checks if both entries are empty
            if self.entry2.get() in "":
                messagebox.showwarning("No Project File", "Specify path to the project folder")
                return

        if self.entry2.get() in "":  # Checks if proj entry is not empty but topic name is.
            if self.entry1.get() not in "":
                messagebox.showwarning("No Topic Name", "Enter the topic name")
                return

        if self.topic_name in (str(os.listdir(os.path.join(os.path.dirname(self.entry1.get()), "topics")))):
            # Checks if topic already exists
            messagebox.showwarning("Creating Topic", "Topic already exists!")
            return

        self.leveloffset()

        self.new_topic_parth = os.path.join(os.path.join(os.path.dirname(self.entry1.get()), "topics"), (self.entry3.get() + self.topic_name))

        with open(self.new_topic_parth, 'a') as self.new_file:
            self.new_file.write("== " + self.entry2.get())

        with open(self.entry1.get(), 'a') as self.project_file:
         self.project_file.write(self.path_to_topic_file)

        if self.entry3.get() + self.topic_name in os.listdir(os.path.join(os.path.dirname(self.entry1.get()), "topics")):
            messagebox.showinfo("Creating Topic", "Topic created successfully!")
            return

        else:
            messagebox.showerror("Error", "Creating is unsuccessful")
            return

    def elements_placing(self):
        self.entry1.grid(column=2, row=1, pady=10)
        self.entry2.grid(column=2, row=4, pady=10, sticky=W)
        self.entry3.place(x=330, y=53)

        self.btn1.grid(column=3, row=1, padx=10, sticky=W)
        self.btn2.grid(column=3, row=4, pady=10, padx=10, sticky=W)

        self.label1.grid(column=1, row=1, pady=10, padx=10, sticky=W)
        self.label2.grid(column=1, row=4, pady=20, padx=10, sticky=NW)
        self.label3.grid(column=1, row=2, pady=10, padx=10, sticky=W)
        self.label4.place(x=280, y=53)

        self.leveloffsetlist.place(x=90, y=49)





