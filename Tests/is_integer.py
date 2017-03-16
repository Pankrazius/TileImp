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


#root = tk.Tk()

#window = Main(root)
#root.mainloop()

rightlist1=[(0,0), (0,1), (0,2)]
rightlist2=[(1,1), (1,2), (2,1), (2,2)]
falselist1=[(0,0),(0,1),(0,2),(1,2)]
falselist2=[(0,0),(0,1),(0,2),(1,1)]

print(min(rightlist1)[0])
print(max(rightlist1))
print(min(rightlist2))
print(min(falselist1))

def validateTile(list):
    if len(list) == 1:
        return True
    minx = min(list, key=lambda x: x[0])[0]
    maxx = max(list, key=lambda x: x[0])[0]
    miny = min(list, key=lambda y: y[1])[1]
    maxy = max(list, key=lambda y: y[1])[1]
    size = (maxx - minx + 1) * (maxy - miny + 1)
    if len(list) == size:
        return True
    else:
        return False


class MainWindow(tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.root = root



class Subwindow(tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.root = root








if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)

    root.mainloop()






