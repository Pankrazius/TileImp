"""
Slice png-files into tilesets.

args: one png-file in subfolder source/game/tilesets

returns: xml-file containing tileset informations
"""


import tkinter as tk
import tkinter.filedialog as tkfd
import xml.etree.ElementTree as et
from PIL import ImageTk, Image
from config import Labels, Paths, Dims
from copy import copy



class Application(tk.Frame):
    """ Main Window Layout """

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.image = None
        self.tilewidth = 0
        self.tileheight = 0
        self.leftmargin = 0
        self.topmargin = 0
        self.str_tilewidth = tk.StringVar(value="")
        self.str_tileheight = tk.StringVar(value="")
        self.str_leftmargin = tk.StringVar(value="")
        self.str_topmargin = tk.StringVar(value="")

        self.canvas = tk.Canvas(self)
        self.root.title(Labels.TITLE_MAIN)
        self.root.wm_minsize(*Dims.WIN_MIN_SIZE)
        self.drawMenu()
        self.drawToolBar()
        self.drawScrollbars()
        self.canvas.pack()
        self.str_tilewidth.trace("w", lambda name, index, mode, var=self.str_tilewidth: self.entryCallback(var))
        self.str_tileheight.trace("w", lambda name, index, mode, var=self.str_tileheight: self.entryCallback(var))
        self.str_leftmargin.trace("w", lambda name, index, mode, var=self.str_leftmargin: self.entryCallback(var))
        self.str_topmargin.trace("w", lambda name, index, mode, var=self.str_topmargin: self.entryCallback(var))

                
    def drawMenu(self):
        menu = tk.Menu(self.root)
        file = tk.Menu(menu, tearoff=0)
        file.add_command(label=Labels.MENU_NEW)
        file.add_command(label=Labels.MENU_IMPORT, command=self.fileopen)
        file.add_command(label=Labels.MENU_EXPORT)
        file.add_command(label=Labels.MENU_QUIT, command=self.root.quit)
        menu.add_cascade(label=Labels.MENU_FILE, menu=file)
        self.root.config(menu=menu)

    def drawToolBar(self):
        labels = [
            (Labels.TOOL_WIDTH, self.str_tilewidth),
            (Labels.TOOL_HEIGHT, self.str_tileheight),
            (Labels.TOOL_LMARGIN, self.str_leftmargin),
            (Labels.TOOL_TMARGIN, self.str_topmargin)
        ]
        frame = tk.Frame(self)
        for label in labels:
            tk.Label(frame, text=label[0]).pack(side=tk.LEFT, anchor=tk.W)
            entry = tk.Entry(frame, width=Dims.TOOL_ENTRY_WIDTH, textvariable=label[1])
            entry.insert(0, str(label[1].get()))
            entry.pack(side=tk.LEFT)


        frame.pack(fill=tk.X, expand=1)
        apply_button=tk.Button(frame, text=Labels.BUTTON_APPLY, command=self.setGrid)
        apply_button.pack(side=tk.LEFT, anchor=tk.W)
        #print(self.str_tilewidth, self.str_tileheight, self.str_leftmargin, self.str_topmargin)

    def drawCanvas(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0,0, image=self.image, anchor=tk.NW)
        if self.image:
            self.canvas.config(scrollregion=(0,0, self.image.width(), self.image.height()))
        else:
            pass

    def drawScrollbars(self):
        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        vbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

    def fileopen(self):
        options={"filetypes":[("PNG image", ".png"),("JPEG image", ".jpg")], "initialdir":Paths.DEFAULT_LOAD}
        filename = tkfd.askopenfilename(**options)

        with open(filename, mode="rb") as file:
            print("I opened", filename)
            self.image = ImageTk.PhotoImage(file=file)
            print("Size is", self.image.width(), "x", self.image.height())
            self.drawCanvas()

    def entryCallback(self, var):
        print("Value changed")
        print(var, var.get())

    def setGrid(self):
        """ validates entries and draws tilegrid """

        # Validate
        print("validate entries")
        list = [(self.str_tilewidth, self.tilewidth),
                (self.str_tileheight, self.tileheight),
                (self.str_leftmargin, self.leftmargin),
                (self.str_topmargin, self.topmargin)]
        for entry in list:
            try:
                int(entry[0].get())
            except:
                print(entry[0], "(",entry[0].get(),") is no integer")
                print(self.tilewidth, self.tileheight, self.leftmargin, self.topmargin)
                return False
        # Set variables
        self.tilewidth = copy(int(self.str_tilewidth.get()))
        self.tileheight = copy(int(self.str_tileheight.get()))
        self.leftmargin = copy(int(self.str_leftmargin.get()))
        self.topmargin = copy(int(self.str_topmargin.get()))
        print("TW, TH, LM, TM", self.tilewidth, self.tileheight, self.leftmargin, self.topmargin)
        # Update grid
        if self.image:
            for i in range(self.leftmargin, self.image.width(), self.tilewidth):
                self.canvas.create_line(i, 0, i, self.image.height())
                print("i",i)
            for j in range(self.topmargin, self.image.height(), self.tileheight):
                self.canvas.create_line(0, j, self.image.width(),j)
                print("j",j)
        else:
            print("no image selected")


if __name__ == "__main__":

    root = tk.Tk()
    app = Application(root)
    app.pack(fill=tk.BOTH)
    root.geometry(Dims.WIN_GEOMETRY)
    root.mainloop()

    
        


    


