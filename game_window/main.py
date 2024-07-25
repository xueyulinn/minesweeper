from tkinter import *
import settings
import utils
from cell import Cell

# window configuration
root = Tk()
root.title("MineSweeper")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.config(bg="black")

# frame configuration
topFrame = Frame(root,
                 bg="black",
                 width=utils.widthPrct(100),
                 height=utils.heightPrct(25))


topFrame.place(x=utils.widthPrct(0), y=utils.heightPrct(0))


leftFrame = Frame(root,
                  bg="black",
                  width=utils.widthPrct(25),
                  height=utils.heightPrct(75))

leftFrame.place(x=utils.widthPrct(0), y=utils.heightPrct(25))


centerFrame = Frame(root,
                    bg="black",
                    width=utils.widthPrct(75),
                    height=utils.heightPrct(75))

centerFrame.place(x=utils.widthPrct(25), y=utils.heightPrct(25))

for y in range(settings.GRID_SIZE):
    for x in range(settings.GRID_SIZE):
        cell = Cell()
        cell.createButton(centerFrame)
        cell.buttonObj.grid(column=y, row=x)

root.mainloop()
