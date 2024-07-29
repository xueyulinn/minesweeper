from tkinter import Button, Label
import settings
import random
import ctypes


class Cell:
    all = []
    remainingCells = settings.CELLS
    mineCount = settings.MINE_COUNT
    labelObj = None

    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.buttonObj = None
        self.x = x
        self.y = y
        self.displayed = False
        Cell.all.append(self)

    def createButton(self, location):
        btn = Button(
            location,
            width=2,
            height=1
        )

        btn.bind('<Button-1>', self.leftClick)
        btn.bind('<Button-3>', self.rightClick)

        self.buttonObj = btn

    def leftClick(self, event):
        # the tkinter will automatically pass the 'event' paramater
        # which contains some metadata about the event
        # print(event)
        self.displayCell()

        self.buttonObj.unbind('<Button-1>')
        self.buttonObj.unbind('<Button-3>')

    def rightClick(self, event):
        if self.buttonObj["bg"] == "orange":
            self.buttonObj.configure(bg="SystemButtonFace", text='')

        else:
            self.buttonObj.configure(
                bg="orange",
                text='🚩'
            )

    def getCellByAxis(self, x, y):
        # O(n)
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def displayCell(self):
        if self.displayed:
            return

        self.displayed = True

        if self.isMine == True:
            self.displayMine()
        else:
            if self.countMines() == 0:
                for cell in self.getSurroundedCells():
                    cell.displayCell()  # Recursively reveal cells with no mines around
            self.displayNormalCell()

    def displayMine(self):
        self.buttonObj.configure(bg="red", text='💣')
        ctypes.windll.user32.MessageBoxW(
            0, 'You clicked on a mine', 'Game Over', 0)

    def getSurroundedCells(self):
        surroundedCells = [
            self.getCellByAxis(self.x-1, self.y-1),
            self.getCellByAxis(self.x-1, self.y),
            self.getCellByAxis(self.x-1, self.y+1),
            self.getCellByAxis(self.x, self.y-1),
            self.getCellByAxis(self.x, self.y+1),
            self.getCellByAxis(self.x+1, self.y-1),
            self.getCellByAxis(self.x+1, self.y),
            self.getCellByAxis(self.x+1, self.y+1),
        ]

        surroundedCells = [
            cell for cell in surroundedCells if cell is not None]

        return surroundedCells

    def countMines(self):
        cells = self.getSurroundedCells()

        mines = [cell for cell in cells if cell.isMine == True]

        return len(mines)

    def displayNormalCell(self):
        self.buttonObj.configure(text=f"{self.countMines()}")
        self.buttonObj.configure(bg="SystemButtonFace")
        Cell.remainingCells -= 1

        if Cell.labelObj:
            Cell.labelObj.configure(text=f"Remaining Cells: {
                Cell.remainingCells}")

        if Cell.remainingCells == Cell.mineCount:
            ctypes.windll.user32.MessageBoxW(
                0, 'Congrats! You won the game!', 'Game Over', 0)

    @staticmethod
    def displayRemainingsLabel(frame,  cells):
        lbl = Label(frame,
                    bg="black",
                    fg="white",
                    height=4,
                    font=("", 16),
                    text=f"Remaining Cells: {cells}")

        Cell.labelObj = lbl

        lbl.place(x=0, y=0)

    @staticmethod
    def randomizeMines():
        mines = random.sample(Cell.all, Cell.mineCount)
        for cell in mines:
            cell.isMine = True
