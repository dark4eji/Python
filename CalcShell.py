import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
pb = ttk.Progressbar(root, length=100)
pb.pack()
pb.start(100)
root.mainloop()
