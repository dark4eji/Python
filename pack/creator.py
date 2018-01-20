from tkinter import*

class Creator()
    def __init__(self, parent):








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

