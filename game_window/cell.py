from tkinter import Button


class Cell:
    def __init__(self, isMine=False):
        self.isMine = isMine
        self.buttonObj = None

    def createButton(self, location):
        btn = Button(
            location,
            text='text'
        )

        btn.bind('<Button-1>', self.leftClick)
        btn.bind('<Button-3>', self.rightClick)

        self.buttonObj = btn

    def leftClick(self, event):
        # the tkinter will automatically pass the 'event' paramater
        # which contains some metadata about the event
        # print(event)
        print("I'm left clicked!")

    def rightClick(self, event):
        print("I'm right clicked!")
