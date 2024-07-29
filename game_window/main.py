from tkinter import *
import settings
import utils

# Window configuration
root = Tk()
root.title("MineSweeper")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.config(bg="black")

# Frame configuration
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

# Initial game title and labels
gameTitle = Label(
    topFrame,
    text="MineSweeper",
    bg="black",
    fg="white",
    font=('', 64),
)

gameTitle.place(x=utils.widthPrct(25), y=0)

# Difficulty option
def setDifficulty(difficulty):
    # Clear existing cells
    for widget in centerFrame.winfo_children():
        widget.destroy()
    # Modify difficulty and generate cells based on the new difficulty
    utils.modifyDifficulty(difficulty, centerFrame, leftFrame)


beginner_button = Button(
    topFrame,
    text="Beginner",
    bg="black",
    fg="white",
    font=('', 20),
    command=lambda: setDifficulty(0)
)
beginner_button.place(x=utils.widthPrct(25), y=utils.heightPrct(15))

intermediate_button = Button(
    topFrame,
    text="Intermediate",
    bg="black",
    fg="white",
    font=('', 20),
    command=lambda: setDifficulty(1)
)
intermediate_button.place(x=utils.widthPrct(36), y=utils.heightPrct(15))

expert_button = Button(
    topFrame,
    text="Expert",
    bg="black",
    fg="white",
    font=('', 20),
    command=lambda: setDifficulty(2)
)
expert_button.place(x=utils.widthPrct(50), y=utils.heightPrct(15))

root.mainloop()
