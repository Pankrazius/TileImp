import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, width=800, height=600)
frame.grid(row=0, column=0)

canvas = tk.Canvas(frame, bg="blue", width=800, height=600, scrollregion=(0,0,1280,800))

hbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM, fill=tk.X)
hbar.config(command=canvas.xview)

vbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT, fill=tk.Y)
vbar.config(command=canvas.yview)

canvas.config(width=800, height=600)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

root.mainloop()


