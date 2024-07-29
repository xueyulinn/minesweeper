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
        settings.MINE_COUNT = 10  # Typical for Beginner
    elif difficulty == 1:
        settings.GRID_SIZE = 16
        settings.MINE_COUNT = 40  # Typical for Intermediate
    elif difficulty == 2:
        settings.GRID_SIZE = 24
        settings.MINE_COUNT = 99  # Typical for Expert

    settings.CELLS = settings.GRID_SIZE ** 2

    Cell.all = []
    Cell.remainingCells = settings.CELLS  # Correctly set remaining cells
    generateCells(cellFrame, settings.GRID_SIZE)
    Cell.mineCount = settings.MINE_COUNT
    Cell.randomizeMines()
    Cell.displayRemainingsLabel(labelFrame, Cell.remainingCells)  # Pass remaining cells




def generateCells(frame: Frame, gridSize: int):
    for x in range(gridSize):
        for y in range(gridSize):
            cell = Cell(x, y)
            cell.createButton(frame)
            cell.buttonObj.grid(row=x, column=y)

    Cell.randomizeMines()
