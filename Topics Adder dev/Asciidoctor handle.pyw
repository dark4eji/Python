from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import *
import fileinput
import os

pref = None
projpath = None
topicname = None
topicspath = None
varpath = "{t}\\"
leveloffset = None
delimiter = None
file_to_rename = None
newnewname = None

def pathname(event):
    global topicspath

    entry1.delete(0, END)

    entry1.insert(END, askopenfilename(filetype=[('Adoc file', '*.adoc'), ('Text file', '*.txt')]))

    global projpath
    projpath = str(entry1.get())
    get_prefix()

    if topicspath is None:
        topicspath = os.path.dirname(projpath) + "/topics/"
    else:
        return


def select_to_rename(event):

    if str(projpath) in "" or projpath is None:
        messagebox.showwarning("No Project File", "Specify path to the project folder")
        return

    entry4.delete(0, END)
    entry4.insert(END, askopenfilename(initialdir=topicspath, filetype=[('Adoc file', '*.adoc'), ('Text file', '*.txt')]))
    entry5.delete(0, END)
    entry5.insert(END, "(current)" + (os.path.basename(entry4.get())).replace(".adoc", ""))
    global file_to_rename
    file_to_rename = entry4.get()


def renamer(event):

    newname = entry5.get()

    if newname in "" or newname is None:
        messagebox.showwarning("New Name", "Enter new name of the topic")
        return

    if not os.path.exists(file_to_rename):
        messagebox.showwarning("No Project File", "File does not exist")
        return

    global newnewname

    if "UI_" in newname:
            newnewname = newname.replace("UI_", "")
    elif "INS_" in newname:
            newnewname = newname.replace("INS_", "")

    if "_" in newname:
            newnewname = newnewname.replace("_", " ")
    print(newnewname)
    # Replacing the first line in topic

    with open(str(file_to_rename)) as file:
        first_line = file.readline().strip()

    with fileinput.FileInput(str(file_to_rename), inplace=True) as file:

        for line in file:
            print(line.replace(str(first_line), "== " + str(newnewname)), end='')

    newnameop = topicspath + newname + ".adoc"

    os.rename(str(file_to_rename), newnameop)

    if newname + ".adoc" in os.listdir(str(topicspath)):
        messagebox.showinfo("Renaming File", "Topic renamed successfully!")

    changing1 = "include::" + varpath + os.path.basename(str(file_to_rename)) + "[]"
    changing2 = "include::" + varpath + newname + ".adoc[]"

    print(changing1)
    print(changing2)

    with fileinput.input(projpath, inplace=1) as x:
        for line in x:
            line = line.replace(changing1, changing2).strip()
            print(line)
    return
    # with fileinput.FileInput(str(projpath), inplace=True) as file:
    #     for line in file:
    #         print(line.replace(str(changing1), str(changing2), end=''))


def far_topicfolder(event):
    entry3.delete(0, END)
    entry3.insert(END, askdirectory())

    global topicspath
    topicspath = str(entry3.get()) + "/"

    global varpath
    varpath = topicspath

def get_prefix():

    global pref
    if var.get() == 0:
        pref = "UI "

    elif var.get() == 1:
        pref = "INS "

    elif var.get() == 2:
        pref = ""

def creating(event):

    global topicname
    topicname = entry2.get()

    global leveloffset
    leveloffset = dropvalue1.get()

    global delimiter
    delimiter = dropvalue2.get()

    global to_replace

    if delimiter in "Default":
        to_replace = "_"
    elif delimiter in "Space":
        to_replace = " "
    elif delimiter in "Dash":
        to_replace = "-"

    if str(topicname) in "" or topicname is None:
        messagebox.showwarning("No Topic Name", "Enter the topic name")

    elif str(projpath) in "" or projpath is None:
        messagebox.showwarning("No Project File", "Specify path to the project folder")

    else:
        name = pref.replace(" ", to_replace) + topicname.replace(" ", to_replace) + ".adoc"

        if name in os.listdir(str(topicspath)):
            messagebox.showwarning("Creating Topic", "Topic already exists!")
            return

        if leveloffset in "No leveloffset":
            include = "\n//" + str(topicname) + "\ninclude::" + varpath.replace("/", "\\") + name + "[]"
        else:
            include = "\n//" + str(topicname) + "\n:leveloffset: " + leveloffset + "\ninclude::" + varpath.replace(
                "/", "\\") + name + "[]"

        topicfile = topicspath + name

        with open(str(topicfile), 'a') as f:
            f.write("== " + str(topicname))

        with open(str(projpath), 'a') as g:
            g.write(include)

        if name in os.listdir(str(topicspath)):
            messagebox.showinfo("Creating Topic", "Topic created successfully!")

        else:
            messagebox.showerror("Error", "Creating is unsuccessful")



root = Tk()

p = PanedWindow(root, orient=VERTICAL)
p1 = PanedWindow(root, orient=VERTICAL)

f1 = LabelFrame(p, text='Creating Topics', width=500, height=100)
f2 = LabelFrame(p, text='Renaming Topics', width=100, height=100)
f3 = LabelFrame(p1, text='Specifying Path', width=100, height=100)

p.add(f1)
p.add(f2)
p1.add(f3)

#LABELS

label1 = Label(root,
               text="Project file path:")

label2 = Label(f1,
               text="Name of the topic:")

label3 = Label(root,
               text="Topic folder path (if not in project folder):")

label4 = Label(f1,
               text="Leveloffset:")

label5 = Label(f1,
               text="Name delimiter:")

label6 = Label(f2,
               text="Select topic file:")

label7 = Label(f2,
               text="New topic name:")
#BUTTONS

btn1 = Button(root,
              text="...",
              width=3,
              height=1)

btn2 = Button(f1,
              text="Create",
              width=5,
              height=1)

btn3 = Button(root,
              text="...",
              width=3,
              height=1)

btn4 = Button(f2,
              text="...",
              width=3,
              height=1)

btn5 = Button(f2,
              text="Rename",
              width=7,
              height=1)

exit_btn = Button(root,
              text="Exit",
              width=6,
              height=1,
              font="Arial 10",
              command=root.quit)

#ENTRIES

entry1 = Entry(root,
               width=40,
               bd=3)

entry2 = Entry(f1,
               width=40,
               bd=3)

entry3 = Entry(root,
               width=40,
               bd=3)

entry4 = Entry(f2,
               width=40,
               bd=3)

entry5 = Entry(f2,
               width=40,
               bd=3)
#RADIOBUTTONS

var = IntVar()
var.set(1)

rad0 = Radiobutton(f1,
                   text="Reference topic (UI)",
                   variable=var,
                   value=0,
                   command=get_prefix)

rad1 = Radiobutton(f1,
                   text="Procedure topic (INS)",
                   variable=var,
                   value=1,
                   command=get_prefix)

rad2 = Radiobutton(f1,
                   text="Custom topic",
                   variable=var,
                   value=2,
                   command=get_prefix)

#OPTIONLISTS

dropvalue1 = StringVar()
dropvalue1.set("No leveloffset")

val1 = ["No leveloffset", "+1", "+2", "+3", "-1", "-2", "-3", "0", "1", "2", "3", "4", "5"]

om1 = OptionMenu(f1, dropvalue1, *val1)


dropvalue2 = StringVar()
dropvalue2.set("Default")

val2 = ["Default", "Space", "Dash"]

om2 = OptionMenu(f1, dropvalue2, *val2)

#LABEL PLACING

label1.grid(column=1, row=1, pady=10, padx=10, sticky=W)
label3.grid(column=1, row=2, pady=10, padx=10, sticky=W)
label2.grid(column=1, row=7, pady=20, padx=10, sticky=NW)
label4.grid(column=1, row=6, pady=10, padx=10, sticky=NW)
label5.grid(column=2, row=6, sticky=E)
label6.grid(column=1, row=1, pady=10, padx=10, sticky=NW)
label7.grid(column=1, row=2, pady=10, padx=10, sticky=NW)

#ENTRY PLACING

entry1.grid(column=2, pady=10, row=1)
entry3.grid(column=2, pady=10, row=2, sticky=W)
entry2.grid(column=2, row=7)
entry4.grid(column=2, pady=10, row=1, sticky=W)
entry5.grid(column=2, pady=10, row=2, sticky=W)

#BUTTON PLACING

btn1.grid(column=3, row=1, padx=10, sticky=W)
btn3.grid(column=3, row=2, pady=10, padx=10, sticky=W)
btn2.grid(column=3, row=7, padx=10, sticky=W)
exit_btn.place(x=470, y=380)
btn4.grid(column=3, row=1, padx=10, sticky=W)
btn5.grid(column=3, row=2, padx=10, sticky=W)

#RADIOBUTTON PLACING

rad0.grid(column=1, row=5, padx=0, pady=5, sticky=W)
rad1.grid(column=2, row=5, padx=39, sticky=W)
rad2.place(x=350, y=5)

#OPTIONLIST PLACING

om1.place(x=90, y=41)
om2.grid(column=3, row=6, padx=8, sticky=E)

#BOXAREAS PLACING
p.place(x=10, y=100)

#BUTTON BINDINGS

btn1.bind("<ButtonRelease-1>", pathname)
btn2.bind("<ButtonRelease-1>", creating)
btn3.bind("<ButtonRelease-1>", far_topicfolder)
btn4.bind("<ButtonRelease-1>", select_to_rename)
btn5.bind("<ButtonRelease-1>", renamer)

#ROOT SETTINGS

root.title('Asciidoctor handle')
root.geometry('550x426')
root.resizable(width=False, height=False)

root.mainloop()