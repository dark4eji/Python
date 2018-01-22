from tkinter import messagebox
from tkinter.filedialog import *
import fileinput
from pack.noproj_notifier import noproj_notifier


class Renamer:
    def __init__(self, parent, path):
        self.path = path
        self.label2 = Label(parent, text="Select topic file:")
        self.label3 = Label(parent, text="New topic name:")
        self.label4 = Label(parent, text="Prefix:")

        self.entry2 = Entry(parent, width=40, bd=3)
        self.entry3 = Entry(parent, width=40, bd=3)
        self.entry4 = Entry(parent, width=17, bd=3)

        self.btn2 = Button(parent, text="...", width=3, height=1, command=self.get_current_topic_name)
        self.btn3 = Button(parent, text="Rename", width=7, height=1, command=self.renamer)

        self.elements_placing()
        noproj_notifier(self.path, parent)

    def get_current_topic_name(self):
        self.entry2.delete(0, END)
        self.entry2.insert(END, askopenfilename(filetype=[('Adoc file', '*.adoc')]))

    def renamer(self):
        if self.entry2.get() in "":
            if self.entry3.get() in "":
                messagebox.showwarning("No Topic Selected", "Select topic to rename")
                return

        if self.entry2.get() not in "":  # Checks if proj entry is not empty but topic name is.
            if self.entry3.get() in "":
                messagebox.showwarning("No Topic Name", "Enter new topic name")
                return

        if self.entry2.get() in "":
            messagebox.showwarning("No Topic Selected", "Select topic to rename")
            return

        self.new_topic_name = self.entry4.get() + self.entry3.get().replace(" ", "").lower()
        self.topic_dir = os.path.join(os.path.dirname(self.path), "topics")

        if self.new_topic_name in self.topic_dir:
            messagebox.showwarning("Creating Topic", "Topic already exists!")
            return

        with open(self.entry2.get()) as file:
            self.first_line = file.readline().strip()

        with fileinput.FileInput(self.entry2.get(), inplace=True) as file:
            for line in file:
                print(line.replace(self.first_line, "== " + self.entry3.get()), end='')

        os.rename(self.entry2.get(), os.path.join(self.topic_dir, self.new_topic_name + ".adoc"))

        if self.new_topic_name + ".adoc" in os.listdir(self.topic_dir):
             messagebox.showinfo("Renaming File", "Topic renamed successfully!")

        self.to_change = "include::" + os.path.join("topics", os.path.basename(self.entry2.get())) + "[]"
        print(self.to_change)

        self.to_final = "include::" + os.path.join("topics", self.new_topic_name + ".adoc") + "[]"
        print(self.to_final)

        with fileinput.input(self.path, inplace=1) as x:
            for line in x:
                line = line.replace(self.to_change, self.to_final).strip()
                print(line)
        return


    def elements_placing(self):
        self.label2.grid(column=1, row=1, pady=10, padx=10, sticky=NW)
        self.label3.grid(column=1, row=3, pady=10, padx=10, sticky=NW)
        self.label4.grid(column=2, row=2, padx=10, sticky=EW)

        self.entry2.grid(column=2, row=1, pady=10, sticky=W)
        self.entry3.grid(column=2, row=3, pady=10, sticky=W)
        self.entry4.place(x=280, y=42)

        self.btn2.grid(column=3, row=1, padx=10, sticky=W)
        self.btn3.grid(column=3, row=3, padx=10, sticky=W)


 # def new(self):
    #     new_name = []
    #     true_false = []
    #     delimiters = [".", "/", "_", "-"]
    #
    #     new_name.append("en_ultra_megadrive33")
    #
    #     for new in delimiters:
    #         boolean_value = new in new_name[0]
    #         true_false.append(boolean_value)
    #
    #     get_index = true_false.index(True)
    #     get_delimiter = delimiters[get_index]
    #     spaced_name = new_name[0].replace(get_delimiter, " ")
    #     name_to_doc = spaced_name.split()[-1]
    #
    #     print(name_to_doc)