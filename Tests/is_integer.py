#Just for tests

import tkinter as tk

class Main(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self,root)
        self.root = root

        self.var = tk.StringVar(value="")
        self.var.trace("w", lambda name, index, mode, var=self.var: self.entryCallback(var))

        tk.Label(self.root, text="input").pack(side=tk.LEFT, anchor=tk.W)
        self.entry = tk.Entry(self.root, width=4, textvariable=self.var)
        self.entry.pack(side=tk.LEFT)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack(side=tk.LEFT, anchor=tk.W)

    def entryCallback(self, var):
        print("updated Variable")
        print(var.get())


root = tk.Tk()

window = Main(root)
root.mainloop()



