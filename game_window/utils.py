import settings
from cell import Cell, Label
from tkinter import Frame


def widthPrct(prct: float):
    return settings.WIDTH * prct / 100


def heightPrct(prct: float):
    return settings.HEIGHT * prct / 100


def modifyDifficulty(difficulty: int, cellFrame: Frame, labelFrame: Frame):
    if difficulty == 0:
        settings.GRID_SIZE = 9
    elif difficulty == 1:
        settings.GRID_SIZE = 16
    elif difficulty == 2:
        settings.GRID_SIZE = 24

    settings.MINE_COUNT = settings.GRID_SIZE ** 2 // 4
    settings.CELLS = settings.GRID_SIZE**2

    generateCells(cellFrame, settings.GRID_SIZE)
    displayRemainingsLabel(labelFrame, cells=settings.CELLS)


def generateCells(frame: Frame, gridSize: int):
    for x in range(gridSize):
        for y in range(gridSize):
            cell = Cell(x, y)
            cell.createButton(frame)
            cell.buttonObj.grid(row=x, column=y)

    Cell.randomizeMines()


def displayRemainingsLabel(frame: Frame, x: int = 0, y: int = 0, cells: int = settings.CELLS):
    lbl = Label(frame,
                bg="black",
                fg="white",
                height=4,
                font=("", 16),
                text=f"Remaining Cells: {cells}")

    lbl.place(x=x, y=y)
