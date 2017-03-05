"""
Slice png-files into tilesets.

args: one png-file in subfolder source/game/tilesets

returns: xml-file containing tileset informations
"""

# this comment should show up on git, when pushing it.

import tkinter as tk
import tkinter.filedialog as tkfd
import xml.etree.ElementTree as et
from PIL import ImageTk
from config import Labels, Paths, Dims



class Application(tk.Frame):
    """ Main Window Layout """

    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.image = None
        self.tilewidth = tk.IntVar()
        self.tileheight = tk.IntVar()
        self.leftmargin = tk.IntVar()
        self.topmargin = tk.IntVar()
        self.tilewidth.trace("w", self.valueChanged)
        self.tileheight.trace("w", self.valueChanged)
        self.leftmargin.trace("w", self.valueChanged)
        self.topmargin.trace("w", self.valueChanged)
        self.canvas = tk.Canvas(self)
        self.window.title(Labels.TITLE_MAIN)
        self.window.wm_minsize(*Dims.WIN_MIN_SIZE)
        self.drawMenu()
        self.drawToolBar()
        self.canvas.pack()
                

    def drawMenu(self):
        menu = tk.Menu(self.window)
        file = tk.Menu(menu, tearoff=0)
        file.add_command(label=Labels.MENU_NEW)
        file.add_command(label=Labels.MENU_IMPORT, command=self.fileopen)
        file.add_command(label=Labels.MENU_EXPORT)
        file.add_command(label=Labels.MENU_QUIT, command=self.window.quit)
        menu.add_cascade(label=Labels.MENU_FILE, menu=file)
        self.window.config(menu=menu)

    def drawToolBar(self):
        labels = [
            (Labels.TOOL_WIDTH, self.tilewidth),
            (Labels.TOOL_HEIGHT, self.tileheight),
            (Labels.TOOL_LMARGIN, self.leftmargin),
            (Labels.TOOL_TMARGIN, self.topmargin)
        ]
        frame = tk.Frame(self)
        for label in labels:
            tk.Label(frame, text=label[0]).pack(side=tk.LEFT, anchor=tk.W)
            entry = tk.Entry(frame, width=Dims.TOOL_ENTRY_WIDTH, textvariable=label[1])
            entry.pack(side=tk.LEFT)
        frame.pack(fill=tk.X, expand=1)

    def valueChanged(self, name, empty, type):
        print(self.topmargin.get())



    def fileopen(self):
        options={"filetypes":[("PNG image", ".png"),("JPEG image", ".jpg")], "initialdir":"Images"}
        filename = tkfd.askopenfilename(**options)

        with open(filename, mode="rb") as file:
            print("I opened", filename)
            self.image = ImageTk.PhotoImage(file=file)
            #imagelabel = tk.Label(self, image=image)
            #imagelabel.image=image
            #imagelabel.pack()
            self.drawCanvas()

    def drawCanvas(self):
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0,0, image=self.image, anchor=tk.NW)





        
        


if __name__ == "__main__":

    window = tk.Tk()
    app = Application(window)
    app.pack(fill=tk.BOTH)
    window.geometry(Dims.WIN_GEOMETRY)
    window.mainloop()
    
        


    


