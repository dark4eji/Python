from tkinter.filedialog import *
from tkinter import messagebox
import os
import subprocess
from pack.noproj_notifier import noproj_notifier


class Publisher:
    def __init__(self, parent, path):
        self.config_path = os.path.join('C:', 'ProgramData', 'pub_conf')
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
        self.btn3 = Button(parent, text="...", width=3, height=1, command=self.get_fontfolder)
        self.btn4 = Button(parent, text="...", width=3, height=1, command=self.get_outfolder)
        self.btn5 = Button(parent, text="Publish", width=20, height=1, command=self.pubcheck)

        self.entry2 = Entry(parent, width=40, bd=3)
        self.entry3 = Entry(parent, width=40, bd=3)
        self.entry4 = Entry(parent, width=40, bd=3)

        self.label2 = Label(parent, text="Template file path:")
        self.label3 = Label(parent, text="Fonts folder path:")
        self.label4 = Label(parent, text="Output folder:")

        self.elements_placing()
        noproj_notifier(self.path, parent)

    def get_template(self):
        self.entry2.delete(0, END)
        self.temppath = os.path.normpath(str(askopenfilename(filetype=[('Template file', '*.yml')])))
        self.entry2.insert(END, self.temppath)

    def get_fontfolder(self):
        self.entry3.delete(0, END)
        self.fontfolder = os.path.normpath(str(askdirectory()))
        self.entry3.insert(END, self.fontfolder)

    def get_outfolder(self):
        self.entry4.delete(0, END)
        self.outfolder = os.path.normpath(str(askdirectory()))
        self.entry4.insert(END, self.outfolder)
        if self.entry4.get() in "D:/" or self.entry4.get() in "C:/":
            messagebox.showwarning("Wrong path", "Output folder should not be a root")
            self.entry4.delete(0, END)
            return
        else:
            pass

    def publishing(self):
        self.get_pub_vars()
        self.get_build()
        self.outtext = "asciidoctor-pdf " + self.outputplace + self.fonts + self.template + self.build_name + self.projectplace
        subprocess.call(self.outtext, shell=True)
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

        if self.temppath not in "":
            self.template = " -a pdf-style=" + "\"" + self.temppath + "\"" + " "
        else:
            self.template = ""

        if self.fontfolder not in "":
            self.fonts = " -a pdf-fontsdir=" + "\"" + self.fontfolder + "\"" + " "
        else:
            self.fonts = ""

        self.projectplace = " \"" + self.path + "\""
        self.outputplace = " -D " + "\"" + os.path.normpath(self.outfolder) + "\""

    def postpub(self):
        self.pubbed_file = os.path.basename(self.path).replace(".adoc", ".pdf")
        if self.var2.get():
            self.logcheck = subprocess.check_output(self.outtext, stderr=subprocess.STDOUT, shell=True).decode('UTF-8')
            if self.logcheck in '':
                pass
            elif self.logcheck not in '':
                with open((os.path.join(os.path.abspath(self.outfolder), 'Log.txt')), 'w') as log:
                    if self.pubbed_file not in os.listdir(self.outfolder):
                        log.write(self.logcheck + self.pubbed_file + " Is not published")
                    else:
                        log.write(self.logcheck)
                self.result = messagebox.askyesno("Issues", "Issues occurred while publishing. Show log file?")
                if self.result:
                    os.system("explorer.exe " + os.path.join(os.path.abspath(self.outfolder), 'Log.txt'))
        self.openpdf()

    def openpdf(self):
        self.openfile = os.path.join(self.outfolder, self.pubbed_file)
        if self.var1.get():
            try:
                os.startfile("" + self.openfile + "", 'open')
            except NameError:
                self.error_pub = True

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
        self.btn2.grid(column=3, row=2, padx=10, sticky=W)
        self.btn3.grid(column=3, row=3, pady=10, padx=10, sticky=W)
        self.btn4.grid(column=3, row=4, padx=10, sticky=W)
        self.btn5.grid(column=2, row=6, padx=0, pady=10, sticky=W)

        self.radiobut_enter.grid(column=2, row=5, sticky=E)
        self.radiobut_plus.grid(column=2, row=5, sticky=EW)

        self.entry2.grid(column=2, row=2)
        self.entry3.grid(column=2, row=3, pady=20, sticky=W)
        self.entry4.grid(column=2, row=4, sticky=W)

        self.chbtn1.grid(column=1, row=5, padx=10, pady=10)
        self.chbtn2.grid(column=1, row=6, padx=10, pady=10, sticky=W)

        self.label2.grid(column=1, row=2, pady=5, padx=10, sticky=W)
        self.label3.grid(column=1, row=3, pady=5, padx=10, sticky=W)
        self.label4.grid(column=1, row=4, pady=5, padx=10, sticky=W)
