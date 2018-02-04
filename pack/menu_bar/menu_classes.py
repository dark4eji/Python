import os
import traceback
import logging
import subprocess
import fileinput
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from pack.func_pack import no_project_notifier, field_check, config_writer, config_retriever
from tkinter import Toplevel, messagebox, IntVar, StringVar, Radiobutton,\
    BooleanVar, Checkbutton, Button, Entry, Label, END, E, W, EW, NW, OptionMenu


class OpenFile:
    """Class builds the 'Open File' menu, allowing import file contents to
the Text Box"""
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


class OpenProject:
    """The class represents an Open Project menu that
determines what 'project file' should be published
"""
    project_path = None
    secured_project_path = None

    def __init__(self, parent, root, name):
        self.root = root
        self.name = name
        self.parent = parent
        self.check = None
        self.constructing_menu()

    def constructing_menu(self):
        """Adds menu with the given name"""
        self.parent.add_command(label=self.name, command=self.get_projpath)

    def get_projpath(self):
        """Used for specifying a path to the project file"""
        OpenProject.project_path = \
            os.path.normpath(askopenfilename(filetype=[('Adoc file', '*.adoc')]))
        if OpenProject.project_path in '.':
            OpenProject.project_path = None
            return
        OpenProject.secured_project_path = OpenProject.project_path
        config_writer('project_file', 'file_path', OpenProject.secured_project_path)
        self.root_title(OpenProject.secured_project_path)

    def root_title(self, path):
        """Constructs root title"""
        self.root.title('Asciidoctor Manager' + " [" + path + "]")


class OperationsMenu:
    """Generates Actions menu with cascades"""
    def __init__(self, parent, class_, subclass_,  name):
        self.class_ = class_
        self.subclass_ = subclass_
        self.name = name
        self.parent = parent
        self.filewin = None
        self.parent.add_command(label=self.name, command=self.invoking_pub)

    def creating_toplevel(self, menu, name):
        """Generates top-level windows"""
        self.filewin = Toplevel(menu)
        self.filewin.focus_force()
        self.filewin.grab_set()
        self.filewin.title(name)
        self.filewin.resizable(width=False, height=False)
        self.class_(self.filewin, self.subclass_.secured_project_path)

    def invoking_pub(self):
        """Translates class to the top-level window"""
        self.creating_toplevel(self.parent, self.name)


class Publisher:
    """The module contains logic of project publishing, file opening,
and logging"""
    def __init__(self, parent, path):
        self.pub_conf = os.path.join('C:\\', 'ProgramData', 'AMConf', 'data')
        self.path = path        
        self.temppath = None
        self.fontfolder = None
        self.rbvar = IntVar()
        self.rbvar.set(1)
        self.radiobut_plus = Radiobutton(parent, text="PLUS", variable=self.rbvar, value=1)
        self.radiobut_enter = Radiobutton(parent, text="Enterprise", variable=self.rbvar, value=2)
        self.var1 = BooleanVar()
        self.chbtn1 = Checkbutton(parent, text="Open file after publishing", variable=self.var1)

        self.var2 = BooleanVar()
        self.chbtn2 = Checkbutton(parent, text="Create log file", variable=self.var2)

        self.btn2 = Button(parent, text="...", width=3, height=1, command=self.get_template)
        self.btn4 = Button(parent, text="...", width=3, height=1, command=self.get_outfolder)
        self.btn5 = Button(parent, text="Publish", width=20, height=1, command=self.pubcheck)

        self.entry2 = Entry(parent, width=40, bd=3)
        self.entry4 = Entry(parent, width=40, bd=3)

        self.label2 = Label(parent, text="Template file path:")
        self.label3 = Label(parent, text="Fonts folder path:")
        self.label4 = Label(parent, text="Output folder:")

        self.elements_placing()
        no_project_notifier(self.path, parent)

        if os.path.exists(os.path.join('C:', 'ProgramData', 'config.ini')):
            
            self.outfolder = config_retriever('publisher', 'output')
            self.temppath = config_retriever('publisher', 'tempfile')
            self.fontfolder = os.path.join(os.path.dirname(self.temppath), "sptt_fonts")
                        
            self.entry4.insert(END, str(self.outfolder))        
            self.entry2.insert(END, str(self.temppath))

    def get_outfolder(self):
        """Gets a path to the output folder"""
        self.outfolder = os.path.normpath(str(askdirectory()))
        if self.outfolder in "D:\\":
            messagebox.showwarning("Wrong path", "Output folder should not be a root")
            del self.outfolder
            return
        field_check(self.outfolder, self.entry4)
        config_writer('publisher', 'output', self.outfolder)        
        
    def get_template(self):
        """Gets a path to the template folder"""
        self.temppath = os.path.normpath(askopenfilename(filetype=[('Template file', '*.yml')]))

        if self.temppath in '.':
            return

        self.fontfolder = os.path.join(os.path.dirname(self.temppath), "sptt_fonts")

        if os.path.exists(self.fontfolder):
            pass
        else:            
            messagebox.showwarning("No fonts", "No fonts found. Place the 'sptt_fonts' folder with fonts to the template folder. \nDefault template will be used.")
            self.temppath, self.fontfolder = '', ''
            return

        field_check(self.temppath, self.entry2)        
        config_writer('publisher', 'tempfile', self.temppath)
                       
    def publishing(self):
        self.get_pub_vars()
        self.get_build()
        self.outtext = "asciidoctor-pdf " + self.outputplace.replace("\\", "/") + self.fonts + self.template + self.build_name + self.projectplace
        print(self.outtext)
        try:
            subprocess.call(self.outtext, shell=True)
        except Exception as e:
            logging.error(traceback.format_exc())
            messagebox.showerror("Error", "Error occurred")
        self.openpdf()
        self.postpub()

    def get_build(self):
        if self.rbvar.get() == 1:
            self.build_name = " -a PLUS "
        else:
            self.build_name = " -a Enter "

    def get_pub_vars(self):
        self.projectplace = None
        self.template = None
        self.fonts = None        
        if self.temppath not in ".":
            self.template = " -a pdf-style=" + "\"" + self.temppath + "\"" + " "
            self.fonts = " -a pdf-fontsdir=" + "\"" + self.fontfolder + "\"" + " "
        else:
            self.template, self.fonts = "", ""

        self.projectplace = " \"" + self.path + "\""
        self.outputplace = "-D " + "\"" + os.path.normpath(self.outfolder) + "\""

    def postpub(self):
        if self.var1.get() is False:
            if os.path.exists(os.path.join(self.outfolder, self.pubbed_file)):
                messagebox.showinfo("Successful publishing", "Project published successfully")
            else:
                messagebox.showwarning("No File", "Project was not published")
                return

        if self.var2.get():
            self.logcheck = subprocess.check_output(self.outtext, stderr=subprocess.STDOUT, shell=True).decode('UTF-8')
            if self.logcheck in '':
                pass
            elif self.logcheck not in '':
                with open((os.path.join(os.path.abspath(self.outfolder), 'Log.txt')), 'w') as log:
                    log.write(self.logcheck)
                self.result = messagebox.askyesno("Issues", "Issues occurred while publishing. Show log file?")
                if self.result:
                    os.system("explorer.exe " + os.path.join(os.path.abspath(self.outfolder), 'Log.txt'))

    def openpdf(self):
        self.pubbed_file = os.path.basename(self.path).replace(".adoc", ".pdf")
        self.openfile = os.path.join(self.outfolder, self.pubbed_file)
        if self.var1.get():
            try:
                os.startfile("" + self.openfile + "", 'open')
            except FileNotFoundError:
                messagebox.showwarning("No File", "Project was not published")
                return

    def pubcheck(self):
        if self.path in '':
            messagebox.showwarning("No Project File", "Specify path to the project file")
            return

        if self.path not in '':
            if self.entry4.get() in '':
                messagebox.showwarning("No output folder", "Specify output folder")
                return

        if self.temppath is None:
            self.temppath = ''

        if self.fontfolder is None:
            self.fontfolder = ''
        self.publishing()

    def elements_placing(self):
        self.btn2.grid(column=3, row=4, padx=10, sticky=W)
        self.btn4.grid(column=3, row=2, padx=10, sticky=W)
        self.btn5.grid(column=2, row=6, padx=0, pady=10, sticky=W)

        self.radiobut_enter.grid(column=2, row=5, sticky=E)
        self.radiobut_plus.grid(column=2, row=5, sticky=EW)

        self.entry2.grid(column=2, row=4, sticky=W)
        self.entry4.grid(column=2, row=2, pady=10, sticky=W)

        self.chbtn1.grid(column=1, row=5, padx=10, pady=10)
        self.chbtn2.grid(column=1, row=6, padx=10, pady=10, sticky=W)

        self.label2.grid(column=1, row=4, pady=5, padx=10, sticky=W)
        self.label4.grid(column=1, row=2, pady=5, padx=10, sticky=W)


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
        no_project_notifier(self.path, parent)

    def get_current_topic_name(self):
        self.entry2.delete(0, END)
        self.entry2.insert(END, os.path.normpath(askopenfilename(filetype=[('Adoc file', '*.adoc')])))

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

        if os.path.join(self.topic_dir, (self.new_topic_name + ".adoc")):
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

"""
The class is used for creating new topics in the topics folder, head in the new file
itself, and entry in the project file
"""


class Creator:
    """Class contains variables and methods for creating the desired
    topics"""
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
        self.leveloffsetlistval = ["No leveloffset",
                                   "+1", "+2", "+3", "-1", "-2", "-3", "0", "1", "2", "3", "4", "5"]
        self.leveloffsetlist = OptionMenu(parent, self.leveloffsetvar, *self.leveloffsetlistval)
        self.elements_placing()
        no_project_notifier(self.path, parent)

    def leveloffset(self):
        """Used to construct a text construction to write in a project file"""
        if self.leveloffsetvar.get() in "No leveloffset":
            self.path_to_topic_file = "\n//" + self.entry2.get().replace("_", " ") +\
                                      "\ninclude::" + "topics\\" + self.entry3.get() + \
                                      self.topic_name + "[]"
            print(self.path_to_topic_file)
        else:
            self.path_to_topic_file = "\n//" + self.entry2.get() +\
                                      "\n:leveloffset: " + self.leveloffsetvar.get() + \
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

        if self.topic_name in str(os.listdir(os.path.join(os.path.dirname(self.path), "topics"))):
            # Checks if topic already exists
            messagebox.showwarning("Creating Topic", "Topic already exists!")
            return

        self.leveloffset()

        self.new_topic_parth = os.path.join(os.path.join(os.path.dirname(self.path), "topics"),
                                            (self.entry3.get() + self.topic_name))

        with open(self.new_topic_parth, 'a') as self.new_file:
            self.new_file.write("== " + self.entry2.get())

        with open(self.path, 'a') as self.project_file:
            self.project_file.write(self.path_to_topic_file)

        if self.entry3.get() + self.topic_name in \
                os.listdir(os.path.join(os.path.dirname(self.path), "topics")):
            messagebox.showinfo("Creating Topic", "Topic created successfully!")
            return

        messagebox.showerror("Error", "Creating is unsuccessful")
        return

    def elements_placing(self):
        """Places elements on the widget"""
        self.entry2.grid(column=2, row=3, pady=10, sticky=W)
        self.entry3.place(x=346, y=10)
        self.create_button.grid(column=3, row=3, pady=10, padx=10, sticky=W)
        self.name_of_the_topic_label.grid(column=1, row=3, pady=20, padx=10, sticky=NW)
        self.leveloffset_label.grid(column=1, row=1, pady=10, padx=10, sticky=W)
        self.prefix_label.place(x=300, y=10)
        self.leveloffsetlist.place(x=86, y=5)






