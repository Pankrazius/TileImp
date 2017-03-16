import tkinter as tk
import tkinter.filedialog as tkfd
from PIL import ImageTk, Image
from config import Labels, Paths, Dims
from copy import copy
import xml.etree.ElementTree as et


class g:
    """basic variables"""

    gridw = 0
    gridh = 0
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
        self.setupTsCanvas()
        #self.setupButtons
        #self.setupSomething
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def setupTsCanvas(self):
        """setup tileset-image-canvas"""
        tscanvas = tk.Canvas(self)
        tscanvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.widgets.update({"ts_canvas" : tscanvas})
        vbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=tscanvas.yview)
        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=tscanvas.xview)
        vbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        hbar.grid(row=1, column=0, sticky=tk.E+tk.W)
        tscanvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

    def loadImage(self):
        options = {"filetypes": [("PNG image", ".png"), ("JPEG image", ".jpg")], "initialdir": Paths.DEFAULT_LOAD}
        filename = tkfd.askopenfilename(**options)

        with open(filename, mode="rb") as file:
            g.ts_image = ImageTk.PhotoImage(file=file)
            self.widgets["ts_canvas"].create_image(0,0, image=g.ts_image, anchor=tk.NW)
            self.widgets["ts_canvas"].config(scrollregion=(0,0, g.ts_image.width(), g.ts_image.height()))

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
    edit.add_command(label=Labels.MENU_PREFERENCES)
    menu.add_cascade(label=Labels.MENU_EDIT, menu=edit)

    root.config(menu=menu)




if __name__=="__main__":

    root = tk.Tk(className="Tileset Manager")
    root.wm_attributes("-zoomed", "1")
    app = TilesetWindow(root)
    app.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    drawMenu(root)



    root.mainloop()

