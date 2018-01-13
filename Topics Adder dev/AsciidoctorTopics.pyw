from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import *

pref = None
projpath = None
topicname = None
topicspath = None
varpath = "{t}\\"
leveloffset = None

def pathname(event):

    entry1.delete(0, END)
    entry1.insert(END, askopenfilename(filetype=[('Adoc file', '*.adoc'), ('Text file', '*.txt')]))

    global projpath
    projpath = str(entry1.get())
    get_prefix()

    global topicspath
    if topicspath is None:
        topicspath = os.path.dirname(projpath) + "/topics/"
    else:
        return

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
        pref = "UI_"

    elif var.get() == 1:
        pref = "INS_"

    elif var.get() == 2:
        pref = ""


def creating(event):

    global topicname
    topicname = entry2.get()

    global leveloffset
    leveloffset = dropvalue.get()

    if str(topicname) in "" or topicname is None:
        messagebox.showwarning("No Topic Name", "Enter the topic name")
        print(projpath)

    elif str(projpath) in "" or projpath is None:
        messagebox.showwarning("No Project File", "Specify path to the project folder")
        print(projpath)

    else:
        name = pref + topicname.replace(" ", "_") + ".adoc"

        if name in os.listdir(str(topicspath)):
            messagebox.showwarning("Adding Topic", "Topic already exists!")
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
            messagebox.showinfo("Adding Topic", "Topic added successfully!")

        else:
            messagebox.showerror("Error", "Topic adding is unsuccessful")


root = Tk()

p = PanedWindow(root, orient=VERTICAL)
p1 = PanedWindow(root, orient=VERTICAL)

f1 = LabelFrame(p, text='Adding Topics', width=500, height=100)
f2 = LabelFrame(p, text='Renaming Topics', width=100, height=100)
f3 = LabelFrame(p1, text='Specifying Path', width=100, height=100)

p.add(f1)
p.add(f2)
p1.add(f3)

label1 = Label(root,
               text="Project file path:")

label2 = Label(f1,
               text="Name of the topic:")

label3 = Label(root,
               text="Topic folder path (if not in project folder):")

label4 = Label(f1,
               text="Leveloffset: ")

btn1 = Button(root,
              text="...",
              width=3,
              height=1)

btn2 = Button(f1,
              text="Add",
              width=5,
              height=1)

btn3 = Button(root,
              text="...",
              width=3,
              height=1)

entry1 = Entry(root,
               width=40,
               bd=3)

entry2 = Entry(f1,
               width=40,
               bd=3)

entry3 = Entry(root,
               width=40,
               bd=3)

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

dropvalue = StringVar()
dropvalue.set("No leveloffset")

val = ["No leveloffset", "+1", "+2", "+3", "-1", "-2", "-3", "0", "1", "2", "3", "4", "5"]

om1 = OptionMenu(f1, dropvalue, *val)

top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)

label1.grid(column=1, row=1, pady=10, padx=10, sticky=W)
label3.grid(column=1, row=2, pady=10, padx=10, sticky=W)
label2.grid(column=1, row=7, pady=20, padx=10, sticky=NW)
label4.grid(column=1, row=6, pady=10, padx=10, sticky=NW)

entry1.grid(column=2, pady=10, row=1)
entry3.grid(column=2, pady=10, row=2, sticky=W)
entry2.grid(column=2, row=7)

btn1.grid(column=3, row=1, padx=10, sticky=W)
btn3.grid(column=3, row=2, pady=10, padx=10, sticky=W)
btn2.grid(column=4, row=7, padx=10, sticky=E)


rad0.grid(column=1, row=5, padx=0, pady=5, sticky=W)
rad1.grid(column=2, row=5, sticky=W)
rad2.grid(column=2, row=5, columnspan=2, sticky=E)

om1.grid(column=2, row=6, sticky=W)

p.place(x=10, y=100)

btn1.bind("<ButtonRelease-1>", pathname)
btn2.bind("<ButtonRelease-1>", creating)
btn3.bind("<ButtonRelease-1>", far_topicfolder)

root.title('Topics Adder')
root.geometry('550x600')
root.resizable(width=False, height=False)

root.mainloop()
