from tkinter import *
from pack import main_logic as b
from pack import lblw as lb

root = Tk()

lb.LabelW(root)
b.Mlogic(root)

root.title('Asciidoctor PDF')
root.geometry('490x300')
root.resizable(width=False, height=False)
root.mainloop()
