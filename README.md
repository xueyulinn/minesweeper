# Minesweeper Game

A classic Minesweeper game implemented in Python using Tkinter for the graphical user interface.

## Table of Contents

- [Minesweeper Game](#minesweeper-game)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Gameplay](#gameplay)
  - [Difficulty Levels](#difficulty-levels)
  - [Contributing](#contributing)

## Features

- Classic Minesweeper gameplay with three difficulty levels: Beginner, Intermediate, and Expert.
- Graphical user interface built with Tkinter.
- Dynamic grid size and mine count based on selected difficulty level.
- Remaining cells counter to keep track of the game progress.
- Mines are placed randomly at the start of each game.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/xueyulinn/minesweeper
    cd minesweeper
    ```

2. Ensure you have Python installed (version 3.6 or higher).

## Usage

1. Run the `main.py` file to start the game:
    ```sh
    python main.py
    ```

2. Select the difficulty level by clicking the appropriate button (Beginner, Intermediate, Expert).

3. Enjoy the game!

## Gameplay

- **Objective**: Uncover all cells that are not mines without triggering any mines.
- **Controls**:
  - Left-click on a cell to uncover it.
  - Right-click on a cell to place a flag, marking it as a suspected mine.
- **Winning**: You win the game by uncovering all cells that are not mines.
- **Losing**: The game ends if you uncover a cell that contains a mine.

## Difficulty Levels

1. **Beginner**:
   - Grid size: 9x9
   - Mine count: 10

2. **Intermediate**:
   - Grid size: 16x16
   - Mine count: 40

3. **Expert**:
   - Grid size: 24x24
   - Mine count: 99

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear and descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request explaining your changes.


