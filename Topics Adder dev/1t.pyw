from tkinter.filedialog import *
from tkinter import messagebox

pref = None
projpath = None
topicname = None
topicspath = None


def pathname(event):

    entry1.delete(0, END)
    entry1.insert(END, askopenfilename(filetype=[('Adoc files', '*.adoc'), ('Text files', '*.txt')]))

    global projpath
    projpath = str(entry1.get())

    get_prefix()

    global topicspath
    topicspath = os.path.dirname(projpath) + "/topics/"


def get_prefix():

    global pref
    if var.get() == 0:
        pref = "UI_"

    elif var.get() == 1:
        pref = "INS_"

def creating(event):

    global topicname
    topicname = entry2.get()

    if topicname in " " or topicname is None:
        messagebox.showinfo("No Topic Name", "Please, enter topic name")

    elif projpath in " " or projpath is None:
        messagebox.showinfo("No Project File", "Please, specify path to the project file")

    else:
        name = pref + topicname.replace(" ", "_") + ".adoc"
        print(name)
        include = "\n//" + str(topicname) + "\n:leveloffset: 0\ninclude::{t}\\" + name + "[]"

        q = topicspath + name
        with open(str(q), 'a') as f:
            f.write("== " + str(topicname))

        with open(str(projpath), 'a') as g:
            g.write(include)


root = Tk()

label1 = Label(root,
               text="Project file path:")

label2 = Label(root,
               text="Enter name of a topic:")

btn1 = Button(root,
              text="...",
              width=3,
              height=1)


btn2 = Button(root,
              text="Create",
              width=5,
              height=1)

entry1 = Entry(root,
               width=40,
               bd=3)

entry2 = Entry(root,
               width=40,
               bd=3)


var = IntVar()
var.set(0)

rad0 = Radiobutton(root,
                   text="Reference topic",
                   variable=var,
                   value=0,
                   command=get_prefix)

rad1 = Radiobutton(root,
                   text="Procedure topic",
                   variable=var,
                   value=1,
                   command=get_prefix)

label1.grid(column=1, row=1, pady = 25, padx = 10, sticky=W)
label2.grid(column=1, row=7, pady = 25, padx = 10, sticky=W)

entry1.grid(column=2, row=1)
entry2.grid(column=2, row=7)

btn1.grid(column=3, row=1, padx = 10)
btn2.grid(column=3, row=7, padx = 10)

rad0.grid(column=1, row=5, padx = 10, columnspan=2, sticky=W)
rad1.grid(column=1, row=6, padx = 10, columnspan=2, sticky=W)

btn1.bind("<ButtonRelease-1>", pathname)
btn2.bind("<ButtonRelease-1>", creating)

root.title('Topics Adder')
root.geometry('457x215')
root.resizable(width=False, height=False)
root.iconbitmap(r"D:\Workplace\Python\Topics Adder dev\dokumenty_poisk.ico")

root.mainloop()
