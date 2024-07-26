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

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell = Cell(x, y)
        cell.createButton(centerFrame)
        cell.buttonObj.grid(row=x, column=y)

Cell.randomizeMines()

Cell.createLabel(leftFrame)
Cell.labelObj.place(x=0, y=0)

gameTitle = Label(
    topFrame,
    text="MineSweeper",
    bg="black",
    fg="white",
    font=('', 64),
)

gameTitle.place(x=utils.widthPrct(25), y=0)


root.mainloop()
