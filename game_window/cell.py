from tkinter import Button
import settings
import random


class Cell:
    all = []

    def __init__(self,  x, y, isMine=False):
        self.isMine = isMine
        self.buttonObj = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def createButton(self, location):
        btn = Button(
            location,
            width=5,
            height=1
        )

        btn.bind('<Button-1>', self.leftClick)
        btn.bind('<Button-3>', self.rightClick)

        self.buttonObj = btn

    @staticmethod
    def randomizeMines():
        mines = random.sample(Cell.all, settings.MINE_COUNT)
        for cell in mines:
            cell.isMine = True

    def leftClick(self, event):
        # the tkinter will automatically pass the 'event' paramater
        # which contains some metadata about the event
        # print(event)
        self.displayCell()

    def rightClick(self, event):
        print("I'm right clicked!")

    def getCellByAxis(self, x, y):
        # O(n)
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def displayCell(self):
        if self.isMine == True:
            self.displayMine()
        else:
            if self.countMines() == 0:
                for cell in self.getSurroundedCells():
                    # Only display cells that have not been displayed
                    if not cell.buttonObj["text"]:
                        cell.displayNormalCell()
                        cell.displayCell()  # Recursively reveal cells with no mines around
            else:
                self.displayNormalCell()

    def displayMine(self):
        self.buttonObj.configure(bg="red")

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
