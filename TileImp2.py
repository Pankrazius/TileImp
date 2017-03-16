import tkinter as tk
import tkinter.filedialog as tkfd
from tkinter import ttk
from PIL import ImageTk, Image
from config import Labels, Paths, Dims
from copy import copy
import xml.etree.ElementTree as et


class g:
    """basic variables"""

    gridw = 16
    gridh = 16
    lmargin = 0
    tmargin = 0

    s_gridw = ""
    s_gridh = ""
    s_lmargin = ""
    s_tmargin = ""

    ts_image = None

class TilesetWindow(tk.Frame):
    """Main Window Layout"""

    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.root = root
        self.widgets = {}
        self.nb = ttk.Notebook(self)
        self.setupTsCanvas()
        #self.setupButtons
        #self.setupSomething
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.nb.grid(row=0, column=0, sticky=tk.N+tk.W+tk.S+tk.E)
        self.nb.grid_columnconfigure(0, weight=1)
        self.nb.grid_rowconfigure(0,weight=1)
        self.nb.bind("")

    def setupTsCanvas(self):
        """setup tileset-image-canvas"""
        page = ttk.Frame(self.nb)
        page.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        self.nb.add(page, text=Labels.TILESET_NB_NEW)
        page.grid_columnconfigure(0, weight=1)
        page.grid_rowconfigure(0, weight=1)
        tscanvas = tk.Canvas(page)
        tscanvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        tscanvas.grid_columnconfigure(0, weight=1)
        tscanvas.grid_rowconfigure(0, weight=1)
        self.widgets.update({page.winfo_name(): [page,tscanvas]})
        vbar = tk.Scrollbar(page, orient=tk.VERTICAL, command=tscanvas.yview)
        hbar = tk.Scrollbar(page, orient=tk.HORIZONTAL, command=tscanvas.xview)
        vbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        hbar.grid(row=1, column=0, sticky=tk.E+tk.W)
        tscanvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

    def loadImage(self):
        options = {"filetypes": [("PNG image", ".png"), ("JPEG image", ".jpg")], "initialdir": Paths.DEFAULT_LOAD}
        filename = tkfd.askopenfilename(**options)
        if filename:
            name = getName(self.nb.select())
            tab_id = self.nb.children[name]
            if self.nb.tab(tab_id, "text") == Labels.TILESET_NB_NEW:
                with open(filename, mode="rb") as file:
                    f = (file.name.split("/")[-1])
                    g.ts_image = ImageTk.PhotoImage(file=file)
                    self.nb.tab(tab_id, text=f)
                    canvas = self.widgets[self.nb.select().split(".")[-1]][1]
                    canvas.create_image(0,0, image=g.ts_image, anchor=tk.NW)
                    canvas.config(scrollregion=(0,0, g.ts_image.width(), g.ts_image.height()))
                    self.setupTsCanvas()
            else:
                print("Tab already in use, use new tab.")
        else:
            pass


    def getCell(self):
        print("getting Cell")

def drawMenu(root):
    menu = tk.Menu(root)
    file = tk.Menu(menu, tearoff=0)
    file.add_command(label=Labels.MENU_NEW)
    file.add_command(label=Labels.MENU_IMPORT, command=app.loadImage)
    file.add_command(label=Labels.MENU_EXPORT)
    file.add_command(label=Labels.MENU_QUIT, command=root.quit)
    menu.add_cascade(label=Labels.MENU_FILE, menu=file)
    edit = tk.Menu(menu, tearoff=0)
    edit.add_command(label=Labels.MENU_SET_GRID)
    edit.add_command(label=Labels.MENU_SHOW_GRID)
    edit.add_command(label=Labels.MENU_HIDE_GRID)
    edit.add_command(label=Labels.MENU_PREFERENCES)
    menu.add_cascade(label=Labels.MENU_EDIT, menu=edit)
    help = tk.Menu(menu, tearoff=0)
    help.add_command(label=Labels.MENU_HELP)
    help.add_command(label=Labels.MENU_VERSION)
    menu.add_cascade(label=Labels.MENU_HELP, menu=help)
    root.config(menu=menu)

## TODO: Make this a methode of TilesetWindow; 'getTabID'
def getName(name):
    return name.split(".")[-1]



if __name__=="__main__":

    root = tk.Tk(className="Tileset Manager")
    #root.wm_attributes("-zoomed", "1")
    app = TilesetWindow(root)
    app.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    drawMenu(root)

    root.mainloop()

