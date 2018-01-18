from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import fileinput
import os
from pack import *
from pack import pdf_logic as ml

projpath = None
topicname = None
topicspath = None
varpath = "{t}\\"
file_to_rename = None
newnewname = None


def pathname(event):
    global topicspath

    entry1.delete(0, END)

    entry1.insert(END, askopenfilename(filetype=[('Adoc file', '*.adoc'), ('Text file', '*.txt')]))

    global projpath
    projpath = str(entry1.get())

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


def far_topicfolder(event):
    entry3.delete(0, END)
    entry3.insert(END, askdirectory())

    global topicspath
    topicspath = str(entry3.get()) + "/"

    global varpath
    varpath = topicspath


def creating(event):

    global topicname
    topicname = entry2.get()

    if str(topicname) in "" or topicname is None:
        messagebox.showwarning("No Topic Name", "Enter the topic name")

    elif str(projpath) in "" or projpath is None:
        messagebox.showwarning("No Project File", "Specify path to the project folder")

    else:
        name = radbutton.Radbuttons.prefix.replace(" ", optionlist.Optionlist.delim_replacer) + topicname.replace(" ", optionlist.Optionlist.delim_replacer) + ".adoc"

        if name in os.listdir(str(topicspath)):
            messagebox.showwarning("Creating Topic", "Topic already exists!")
            return

        if optionlist.Optionlist.leveloffset in "No leveloffset":
            include = "\n//" + str(topicname) + "\ninclude::" + varpath.replace("/", "\\") + name + "[]"
        else:
            include = "\n//" + str(topicname) + "\n:leveloffset: " + optionlist.Optionlist.leveloffset + "\ninclude::" + varpath.replace(
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


nb = ttk.Notebook(root, height=350)

fr1 = ttk.Frame(width=768, height=576)
fr2 = ttk.Frame(width=768, height=576)

nb.add(fr1, text="Publishing")
nb.add(fr2, text="Creating")

p = PanedWindow(fr2, orient=VERTICAL)

gpw1 = LabelFrame(p, text='Creating Topics', width=500, height=100)
gpw2 = LabelFrame(p, text='Renaming Topics', width=100, height=100)

p.add(gpw1)
p.add(gpw2)


# fm1 = Menu(root, tearoff=0)
# fm1.add.command(label="File", command=)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Open", command=hello)
# filemenu.add_command(label="Save", command=hello)
btn1 = Button(fr2,
              text="...",
              width=3,
              height=1)

btn2 = Button(gpw1,
              text="Create",
              width=5,
              height=1)

btn3 = Button(fr2,
              text="...",
              width=3,
              height=1)

btn4 = Button(gpw2,
              text="...",
              width=3,
              height=1)

btn5 = Button(gpw2,
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

entry1 = Entry(fr2,
               width=40,
               bd=3)

entry2 = Entry(gpw1,
               width=40,
               bd=3)

entry3 = Entry(fr2,
               width=40,
               bd=3)

entry4 = Entry(gpw2,
               width=40,
               bd=3)

entry5 = Entry(gpw2,
               width=40,
               bd=3)

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

# BUTTON BINDINGS

btn1.bind("<ButtonRelease-1>", pathname)
btn2.bind("<ButtonRelease-1>", creating)
btn3.bind("<ButtonRelease-1>", far_topicfolder)
btn4.bind("<ButtonRelease-1>", select_to_rename)
btn5.bind("<ButtonRelease-1>", renamer)

label.Labels(fr2, gpw1, gpw2)  # Labels placing

radbutton.Radbuttons(gpw1)  # Radio buttons code

optionlist.Optionlist(gpw1)  # Option list code

ml.Pdflogic(fr1)

p.place(x=10, y=100)

nb.grid(row=1, column=1)

root.title('Asciidoctor handle')
root.geometry('550x426')
root.resizable(width=False, height=False)

root.mainloop()
