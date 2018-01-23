from tkinter import messagebox
from tkinter.filedialog import *
from pack.func_pack import no_project_notifier

class Creator:
    def __init__(self, parent, path):

        self.path = path
        self.name_of_the_topic_label = Label(parent, text="Name of the topic:")
        self.leveloffset_label = Label(parent, text="Leveloffset:")
        self.prefix_label = Label(parent, text="Prefix:")

        self.entry2 = Entry(parent, width=45, bd=3)
        self.entry3 = Entry(parent, width=17, bd=3)

        self.create_button = Button(parent, text="Create", width=5, height=1, command=self.creator)

        self.leveloffsetvar = StringVar()
        self.leveloffsetvar.set("No leveloffset")
        self.leveloffsetlistval = ["No leveloffset", "+1", "+2", "+3", "-1", "-2", "-3", "0", "1", "2", "3", "4", "5"]
        self.leveloffsetlist = OptionMenu(parent, self.leveloffsetvar, *self.leveloffsetlistval)
        self.elements_placing()
        no_project_notifier(self.path, parent)


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

    def creator(self):
        """Used for creating topics in topics folder, adding path with leveloffset \
         to the project file and a title to the topic file"""
        self.topic_name = self.entry2.get().replace(" ", "").lower() + ".adoc"

        if self.path is None:  # Checks if both entries are empty
            if self.entry2.get() in "":
                messagebox.showwarning("No Project File", "Specify path to the project "
                                                          "file in the File → Open Project menu")
                return

        if self.entry2.get() in "":  # Checks if proj entry is not empty but topic name is.
            if self.path is not None:
                messagebox.showwarning("No Topic Name", "Enter the topic name")
                return

        if self.topic_name in (str(os.listdir(os.path.join(os.path.dirname(self.path), "topics")))):
            # Checks if topic already exists
            messagebox.showwarning("Creating Topic", "Topic already exists!")
            return

        self.leveloffset()

        self.new_topic_parth = os.path.join(os.path.join(os.path.dirname(self.path), "topics"), (self.entry3.get() + self.topic_name))

        with open(self.new_topic_parth, 'a') as self.new_file:
            self.new_file.write("== " + self.entry2.get())

        with open(self.path, 'a') as self.project_file:
         self.project_file.write(self.path_to_topic_file)

        if self.entry3.get() + self.topic_name in os.listdir(os.path.join(os.path.dirname(self.path), "topics")):
            messagebox.showinfo("Creating Topic", "Topic created successfully!")
            return

        else:
            messagebox.showerror("Error", "Creating is unsuccessful")
            return

    def elements_placing(self):
        self.entry2.grid(column=2, row=3, pady=10, sticky=W)
        self.entry3.place(x=346, y=10)

        self.create_button.grid(column=3, row=3, pady=10, padx=10, sticky=W)

        self.name_of_the_topic_label.grid(column=1, row=3, pady=20, padx=10, sticky=NW)
        self.leveloffset_label.grid(column=1, row=1, pady=10, padx=10, sticky=W)
        self.prefix_label.place(x=300, y=10)

        self.leveloffsetlist.place(x=86, y=5)





